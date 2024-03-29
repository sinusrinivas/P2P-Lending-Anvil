import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



def final_points_update_bessem_table(user_id):
    user_points = get_user_points(user_id)
    group_points = get_group_points(user_id)

    print(f"Debug: user_points={user_points}, group_points={group_points}")

    if user_points is not None and group_points is not None and group_points != 0:
        points = (user_points / group_points) * 100

        final_points = '{:.2f}'.format(points)

        return final_points
    return None

def get_user_points(id):
    users = app_tables.fin_user_profile.search(customer_id=id)
    if users:
        user = users[0]
        email = user['email_user']
        gender = user['gender'].lower() 
        qualification = user['qualification'].lower()  
        marital_status = user['marital_status'].lower()  
        profession = user['profession'].lower()
        user_age = user['user_age']
        organization_type = user['organization_type'].lower()
        present_address = user['present_address'].lower()
        duration_at_address = str(user['duration_at_address']).lower()
        # self_employment = user['self_employment'].lower()
        self_employment = user['self_employment']
        if self_employment is not None:
          self_employment = self_employment.lower()
        age_of_business = user['business_age']
        salary_type = user['salary_type'].lower()
        home_loan = user['home_loan'].lower()
        other_loan = user['other_loan'].lower()
        credit_card_loan = user['credit_card_loans'].lower()
        vehicle_loan = user['vehicle_loan'].lower()
        
        user_points = 0

        # Find the age range for the user_age
        user_age_range = None
        if 18 <= user_age <= 24:
            user_age_range = '18-24'
        elif 25 <= user_age <= 30:
            user_age_range = '25-30'
        elif 31 <= user_age <= 36:
            user_age_range = '31-36'
        elif 37 <= user_age <= 40:
            user_age_range = '37-40'
        elif 41 <= user_age <= 50:
            user_age_range = '41-50'
        else:
            user_age_range = '51'      
      
        gender_search = app_tables.fin_admin_beseem_categories.search(group_name='gender', sub_category=gender.lower())
        if gender_search:
            gender_points = gender_search[0]['min_points']
            print("Gender Points:", gender_points)
            user_points += gender_points

        present_address_search = app_tables.fin_admin_beseem_categories.search(group_name='present_address', sub_category=present_address.lower())
        if present_address_search:
            present_address_points = present_address_search[0]['min_points']
            print("Present address Points:", present_address_points)
            user_points += present_address_points

        duration_at_address_search = app_tables.fin_admin_beseem_categories.search(group_name='duration_at_address', sub_category=duration_at_address.lower())
        if duration_at_address_search:
            duration_at_address_points = duration_at_address_search[0]['min_points']
            print("Duration at address Points:", duration_at_address_points)
            user_points += duration_at_address_points

        qualification_search = app_tables.fin_admin_beseem_categories.search(group_name='qualification', sub_category=qualification.lower())
        if qualification_search:
           qualification_points = qualification_search[0]['min_points']
           print("Qualification Points:", qualification_points)
           user_points += qualification_points
        else:
           print("Qualification not found in categories.")

        profession_search = app_tables.fin_admin_beseem_categories.search(group_name='profession', sub_category=profession.lower())
        if profession_search:
           profession_points = profession_search[0]['min_points']
           print("Profession Points:", profession_points)
           user_points += profession_points
        else:
            print("No matching profession found in the database")

            if profession == 'self employment':
                self_employment_search = app_tables.fin_admin_beseem_categories.search(group_name='profession', sub_category=self_employment.lower())
                if self_employment_search:
                    self_employment_points = self_employment_search[0]['min_points']
                    print("self employment Points:", self_employment_points)
                    user_points += self_employment_points
                
            elif profession == 'employee':
                organization_type_search = app_tables.fin_admin_beseem_categories.search(group_name='organization_type', sub_category=organization_type.lower())
                if organization_type_search:
                    organization_type_points = organization_type_search[0]['min_points']
                    print("Organization type Points:", organization_type_points)
                    user_points += organization_type_points
                salary_type_search = app_tables.fin_admin_beseem_categories.search(group_name='salary_type', sub_category=salary_type.lower())
                if salary_type_search:
                    salary_type_points = salary_type_search[0]['min_points']
                    print("Salary type Points:", salary_type_points)

            elif profession == 'business':
                business_age_search = app_tables.fin_admin_beseem_categories.search(group_name='age_of_business', sub_category=age_of_business.lower())
                if business_age_search:
                    business_age_points = business_age_search[0]['min_points']
                    print("Business Age Points:", business_age_points)
                    user_points += business_age_points
                  
        marital_status_search = app_tables.fin_admin_beseem_categories.search(group_name='marital_status', sub_category=marital_status.lower(), age=user_age_range)
        if marital_status_search:
            marital_status_points = marital_status_search[0]['min_points']
            print("Marital status Points:", marital_status_points)
            user_points += marital_status_points
    
            data = app_tables.fin_guarantor_details.search(customer_id=id)
            if data:
                for item in data:
                    another_person = item['another_person'].lower()
                    spouse_profession = item['guarantor_profession'].lower()

                    if marital_status == 'married' and another_person == 'spouse':
                        spouse_profession_search = app_tables.fin_admin_beseem_categories.search(group_name='spouse_profession', sub_category=spouse_profession.lower())
                        if spouse_profession_search:
                            spouse_profession_points = spouse_profession_search[0]['min_points']
                            print("Spouse profession:", spouse_profession_points)
                            user_points += spouse_profession_points        

        home_loan_search = app_tables.fin_admin_beseem_categories.search(group_name='home_loan', sub_category=home_loan.lower())
        if home_loan_search:
            home_loan_points = home_loan_search[0]['min_points']
            print("Home loan Points:", home_loan_points)
            user_points += home_loan_points

        other_loan_search = app_tables.fin_admin_beseem_categories.search(group_name='other_loan', sub_category=other_loan.lower())
        if other_loan_search:
            other_loan_points = other_loan_search[0]['min_points']
            print("Other loan Points:", other_loan_points)
            user_points += other_loan_points
          
        credit_card_loan_search = app_tables.fin_admin_beseem_categories.search(group_name='credit_card_loan', sub_category=credit_card_loan.lower())
        if credit_card_loan_search:
            credit_card_loan_points = credit_card_loan_search[0]['min_points']
            print("Credit card loan Points:", credit_card_loan_points)
            user_points += credit_card_loan_points

        vehicle_loan_search = app_tables.fin_admin_beseem_categories.search(group_name='vehicle_loan', sub_category=vehicle_loan.lower())
        if vehicle_loan_search:
            vehicle_loan_points = vehicle_loan_search[0]['min_points']
            print("Vehicle Points:", vehicle_loan_points)
            user_points += vehicle_loan_points                     

        return user_points
    else:
        return None

def get_group_points(customer_id):
    # Fetch user details
    user = app_tables.fin_user_profile.get(customer_id=customer_id)
    if user:
        profession = user['profession'].lower()
        marital_status = user['marital_status'].lower()
        
        loans_data = app_tables.fin_guarantor_details.search(customer_id=customer_id)
        another_person = ''
        spouse_profession = ''
        if loans_data:
            for item in loans_data:
                another_person = item['another_person'].lower()
                spouse_profession = item['guarantor_profession'].lower()

        groups = app_tables.fin_admin_beseem_groups.search()
        if groups:
            group_points = 0
            for group_row in groups:
                group_name = group_row['group_name'].lower()
                max_points = group_row['max_points']
                
                # Add points based on group criteria
                if group_name == 'gender':
                    group_points += max_points
                elif group_name == 'present_address':
                    group_points += max_points
                elif group_name == 'duration_at_address':
                    group_points += max_points
                elif group_name == 'qualification':
                    group_points += max_points
                elif group_name == 'home_loan':
                    group_points += max_points
                elif group_name == 'other_loan':
                    group_points += max_points
                elif group_name == 'credit_card_loan':
                    group_points += max_points
                elif group_name == 'vehicle_loan':
                    group_points += max_points
                elif group_name == 'profession':
                    group_points += max_points
                elif group_name == 'organization_type' and profession == 'employee':
                    group_points += max_points
                elif group_name == 'salary_type' and profession == 'employee':
                    group_points += max_points
                elif group_name == 'age_of_business' and profession == 'business':
                    group_points += max_points
                elif group_name == 'marital_status':
                    group_points += max_points
                elif group_name == 'spouse_profession' and marital_status == 'married' and another_person == 'spouse':
                    group_points += max_points

            return group_points

    return None


# # this function is force push to total points in bessem table
# def final_points_update_bessem_table(user_id):
  
#     user_points = get_user_points(user_id)
#     group_points = get_group_points()

#     if user_points is not None and group_points is not None and group_points != 0:
#         # Calculate final_points as a percentage
#         final_points = (user_points / group_points) * 100
#         return final_points

#     return None

# def get_user_points(id):
#     users = app_tables.fin_user_profile.search(customer_id=id)

#     if users:
#         user = users[0]
#         gender = user['gender']
#         qualification = user['qualification']
#         marrital_status = user['marital_status']

#         def search_category(group_name, sub_category):
#             return app_tables.fin_admin_beseem_categories.search(
#                 group_name=group_name, sub_category=sub_category
#             )

#         # Initialize user_points to 0
#         user_points = 0

#         gender_category_rows = search_category('gender', gender)
#         if gender_category_rows:
#             user_points += gender_category_rows[0]['min_points']

#         qualification_category_rows = search_category('qualification', qualification)
#         if qualification_category_rows:
#             user_points += qualification_category_rows[0]['min_points']

#         marital_status_category_rows = search_category('marrital_status', marrital_status)
#         if marital_status_category_rows:
#             user_points += marital_status_category_rows[0]['min_points']

#         # Return the total user_points
#         return user_points

#     # Handle the case where no user with the specified id is found or no matching row is found
#     return None
        
# def get_group_points():
#     groups = app_tables.fin_admin_beseem_groups.search()

#     if groups:
#         group_points = 0

#         for group_row in groups:
#             group_points += group_row['max_points']

#         return group_points
#     return None
