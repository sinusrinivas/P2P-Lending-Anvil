from ._anvil_designer import edit_formTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
from anvil.tables import app_tables
from datetime import datetime, timedelta
from datetime import date



class edit_form(edit_formTemplate):
  def __init__(self, get_customer_id_value, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.fin_user_profile.search()
    self.genders=tables.app_tables.fin_gender.search()
    self.marital_statuses = tables.app_tables.fin_borrower_marrital_status.search()
    self.qualification = tables.app_tables.fin_borrower_qualification.search()
    self.address_type = tables.app_tables.fin_borrower_land_type.search()
    self.organization_type = tables.app_tables.fin_borrower_organization_type.search()
    self.employment_type = tables.app_tables.fin_borrower_employee_type.search()
    self.profession_type=tables.app_tables.fin_borrower_profession.search()
    self.how_long = tables.app_tables.fin_duration_at_address.search()
    self.salary_type = tables.app_tables.fin_borrower_salary_type.search()    
  

    self.id_list = []
    self.name_list = []
    self.status_list = []
    self.gender_list = []
    self.age_list = []
    self.dob_list = []
    self.address_list = []
    self.address2_list = []
    self.profession_type_list = []
    self.country_list = []
    self.aadhar_list = []
    self.pan_list = []
    self.city_list = []
    self.email_user_list = []
    self.last_confirm_list = []
    self.mobile_check_list = []
    self.mother_status_list = []
    self.date_marrige_list = []
    self.space_name_list = []
    self.about_list = []
    self.alets_list = []
    self.terms_list = []
    self.mail_id_list = []
    self.qualification_list = []
    self.address_type_list = []
    self.how_long_list = []
    self.build_name_list = []
    self.house_no_list = []
    self.landmark_list = []
    self.pincode_list = []
    self.state_list = []
    self.spouse_number_list = []
    self.company_name_list = []
    self.company_adress_list = []
    self.proffic_list = []
    self.user_type_list = []
    self.approve_list = []
    self.mobile_list = []
    self.another_email = []
    self.company_name = []
    self.organization_type_list = []
    self.employment_type_list = []
    self.business_no = []
    self.company_landmark = []
    self.company_address = []
    self.annual_salary = []
    self.salary_type_list = []
    self.designation = []
    self.street_list = []
    self.father_name = []
    self.father_age = []
    self.mother_name = []
    self.mother_age = []
    self.college_name = []
    self.college_id = []
    self.college_address = []
    self.running_home_loan = []
    self.other_loan = []
    self.personal_loan = []
    self.vehicle_loan = []

    self.drop_down_1.items=[(g['gender'],g['gender']) for g in self.genders]
    self.drop_down_2.items = [(ms['borrower_marrital_status'], ms['borrower_marrital_status']) for ms in self.marital_statuses]
    self.drop_down_3.items = [(q['borrower_qualification'], q['borrower_qualification']) for q in self.qualification]
    self.drop_down_4.items = [(ot['borrower_organization_type'], ot['borrower_organization_type']) for ot in self.organization_type]
    self.drop_down_5.items = [(et['borrower_employee_type'], et['borrower_employee_type']) for et in self.employment_type]
    self.drop_down_6.items = [(st['borrower_salary_type'], st['borrower_salary_type']) for st in self.salary_type ]
    self.drop_down_8.items = [(lt['land_type'], lt['land_type']) for lt in self.address_type]
    self.drop_down_10.items = [(dt['duration_at_address'], dt['duration_at_address']) for dt in self.how_long]
    self.drop_down_9.items = [(pt['borrower_profession'], pt['borrower_profession']) for pt in self.profession_type]
    
    a = -1
    for i in self.data:
      a+=1
      self.id_list.append(i['customer_id'])
      self.name_list.append(i['full_name'])
      self.status_list.append(i['profile_status'])
      self.gender_list.append(i['gender'])
      self.age_list.append(i['user_age'])
      self.dob_list.append(i['date_of_birth'])
      self.address_list.append(i['street_adress_1'])
      self.address2_list.append(i['street_address_2'])
      self.country_list.append(i['country'])
      self.profession_type_list.append(i['profession'])
      self.street_list.append(i['street'])
      self.aadhar_list.append(i['aadhaar_no'])
      self.pan_list.append(i['pan_number'])
      self.city_list.append(i['city'])
      self.email_user_list.append(i['email_user'])
      self.last_confirm_list.append(i['last_confirm'])
      self.mobile_check_list.append(i['mobile_check'])
      self.mother_status_list.append(i['marital_status'])
      # self.date_marrige_list.append(i['Date_mariage'])
      self.space_name_list.append(i['spouse_name'])
      self.about_list.append(i['about'])
      self.alets_list.append(i['alerts'])
      self.terms_list.append(i['terms'])
      self.mail_id_list.append(i['mail_id'])
      self.qualification_list.append(i['qualification'])
      self.address_type_list.append(i['address_type'])
      self.how_long_list.append(i['duration_at_address'])
      self.street_list.append(i['street'])
      self.build_name_list.append(i['building_name'])
      self.house_no_list.append(i['house_no'])
      self.landmark_list.append(i['house_landmark'])
      self.pincode_list.append(i['pincode'])
      self.state_list.append(i['state'])
      self.spouse_number_list.append(i['spouse_mobile'])
      self.company_name_list.append(i['spouse_company_name'])
      self.company_adress_list.append(i['spouse_company_address'])
      self.proffic_list.append(i['spouse_profession'])
      self.user_type_list.append(i['usertype'])
      self.approve_list.append(i['registration_approve'])
      self.mobile_list.append(i['mobile'])
      self.another_email.append(i['another_email'])
      self.company_name.append(i['company_name'])
      self.organization_type_list.append(i['organization_type'])
      self.employment_type_list.append(i['employment_type'])
      self.business_no.append(i['business_no'])
      self.company_landmark.append(i['company_landmark'])
      self.company_address.append(i['company_address'])
      self.annual_salary.append(i['annual_salary'])
      self.salary_type_list.append(i['salary_type'])
      self.designation.append(i['designation'])
      self.father_name.append(i['father_name'])
      self.father_age.append(i['father_age'])
      self.mother_name.append(i['mother_name'])
      self.mother_age.append(i['mother_age'])
      self.college_name.append(i['college_name'])
      self.college_id.append(i['college_id'])
      self.college_address.append(i['college_address'])
      self.running_home_loan.append(i['home_loan'])
      self.other_loan.append(i['other_loan'])
      self.personal_loan.append(i['credit_card_loans'])
      self.vehicle_loan.append(i['vehicle_loan'])
      

    print(self.company_adress_list)
    if get_customer_id_value in self.id_list:
      c = self.id_list.index(get_customer_id_value)

      self.set_textbox_visibility(self.text_box_2,self.label_2,self.name_list[c])
      self.set_textbox_visibility(self.text_box_3,self.label_4, str(self.status_list[c]))
      self.drop_down_1.selected_value=self.gender_list[c]
      self.set_textbox_visibility(self.text_box_5,self.label_6, self.age_list[c])
      self.set_textbox_visibility(self.text_box_25,self.label_7, self.dob_list[c])
      self.set_textbox_visibility(self.text_box_32,self.label_60,self.email_user_list[c])
      self.set_textbox_visibility(self.text_box_11,self.label_61,self.address_list[c])
      self.set_textbox_visibility(self.text_box_4,self.label_43, self.address2_list[c])
      self.set_textbox_visibility(self.text_box_15,self.label_63,self.country_list[c])
      self.drop_down_9.selected_value=self.profession_type_list[c]
      self.set_textbox_visibility(self.text_box_7,self.label_10, self.mobile_list[c])
      self.set_textbox_visibility(self.text_box_40,self.label_11, self.aadhar_list[c])
      self.set_textbox_visibility(self.text_box_41,self.label_12, self.pan_list[c])
      self.set_textbox_visibility(self.text_box_10,self.label_13, self.city_list[c])
      self.set_textbox_visibility(self.text_box_12,self.label_15, str(self.last_confirm_list[c]))
      self.set_textbox_visibility(self.text_box_13,self.label_16, str(self.mobile_check_list[c]))
      self.drop_down_2.selected_value = self.mother_status_list[c]
      self.set_textbox_visibility(self.text_box_17,self.label_20, self.space_name_list[c])
      self.set_textbox_visibility(self.text_box_24,self.label_27, self.about_list[c])
      self.set_textbox_visibility(self.text_box_26,self.label_29, str(self.alets_list[c]))
      self.set_textbox_visibility(self.text_box_34,self.label_37,self.street_list[c])
      self.set_textbox_visibility(self.text_box_35,self.label_38, str(self.terms_list[c]))
      self.drop_down_3.selected_value = self.qualification_list[c]
      self.drop_down_4.selected_value = self.address_type_list[c]
      self.drop_down_10.selected_value = self.how_long_list[c]
      self.set_textbox_visibility(self.text_box_27,self.label_30, self.build_name_list[c])
      self.set_textbox_visibility(self.text_box_29,self.label_32, self.house_no_list[c])
      self.set_textbox_visibility(self.text_box_28,self.label_31, self.landmark_list[c])
      self.set_textbox_visibility(self.text_box_30, self.label_34,self.pincode_list[c])
      self.set_textbox_visibility(self.text_box_33,self.label_36, self.state_list[c])
      self.set_textbox_visibility(self.text_box_18,self.label_21, self.spouse_number_list[c])
      self.set_textbox_visibility(self.text_box_19,self.label_22, self.company_name_list[c])
      self.set_textbox_visibility(self.text_box_20,self.label_23, self.company_adress_list[c])
      self.set_textbox_visibility(self.text_box_21, self.label_24,self.proffic_list[c])
      self.set_textbox_visibility(self.text_box_22,self.label_25, self.user_type_list[c])
      self.set_textbox_visibility(self.text_box_23,self.label_26, str(self.approve_list[c]))
      self.set_textbox_visibility(self.text_box_1,self.label_1, self.another_email[c])
      self.set_textbox_visibility(self.text_box_6,self.label_3, self.company_name[c])
      self.drop_down_4.selected_value=self.organization_type_list[c]
      self.drop_down_5.selected_value = self.employment_type_list[c]
      self.set_textbox_visibility(self.text_box_31, self.label_14,self.business_no[c])
      # self.set_textbox_visibility(self.text_box_44,self.label_48,self.bank_id[c])
      self.set_textbox_visibility(self.text_box_36,self.label_33, self.company_landmark[c])
      self.set_textbox_visibility(self.text_box_37,self.label_39, self.company_address[c])
      self.set_textbox_visibility(self.text_box_38,self.label_40, self.annual_salary[c])
      self.drop_down_6.selected_value = self.salary_type_list[c]
      self.set_textbox_visibility(self.text_box_39,self.label_41, self.designation[c])
      self.set_textbox_visibility(self.text_box_48,self.label_52, self.father_name[c])
      self.set_textbox_visibility(self.text_box_49,self.label_53, self.father_age[c])
      self.set_textbox_visibility(self.text_box_50,self.label_54, self.mother_name[c])
      self.set_textbox_visibility(self.text_box_51,self.label_55, self.mother_age[c])
      self.set_textbox_visibility(self.text_box_52,self.label_56, self.college_name[c])
      self.set_textbox_visibility(self.text_box_53,self.label_57, self.college_id[c])
      self.set_textbox_visibility(self.text_box_54,self.label_58,self.college_address[c])
      self.set_textbox_visibility(self.text_box_8,self.label_17, self.running_home_loan[c])
      self.set_textbox_visibility(self.text_box_9,self.label_44,self.other_loan[c])
      self.set_textbox_visibility(self.text_box_14,self.label_46,self.personal_loan[c])
      self.set_textbox_visibility(self.text_box_16,self.label_45,self.vehicle_loan[c])
      
      # Add more textbox visibility settings here

    self.get = get_customer_id_value


  def set_textbox_visibility(self, textbox, label, data):
    if data:
        textbox.text = data
        textbox.visible = True
        label.visible = True
    else:
        textbox.visible = False
        label.visible = False
      # self.text_box_2.text = self.name_list[c]
      # self.text_box_3.text = bool(self.status_list[c])
      # self.text_box_4.text= self.gender_list[c]
      # self.text_box_5.text = self.age_list[c]
      # self.date_picker_1.text = self.dob_list[c]
      # self.text_box_7.text = self.mobile_list[c]
      # self.text_box_8.text = self.aadhar_list[c]
      # self.text_box_9.text = self.pan_list[c]
      # self.text_box_10.text = self.city_list[c]
      # self.text_box_12.text = bool(self.last_confirm_list[c])
      # self.text_box_13.text = bool(self.mobile_check_list[c])
      # self.text_box_15.text = self.mother_status_list[c]
      # # self.date_picker_2.text = self.date_marrige_list[c]
      # self.text_box_17.text = self.space_name_list[c]
      # self.text_box_24.text = self.about_list[c]
      # self.text_box_26.text = bool(self.alets_list[c])
      # self.text_box_35.text = bool(self.terms_list[c])
      # self.text_box_32.text = self.qualification_list[c]
      # self.text_box_25.text = self.address_type_list[c]
      # self.text_box_34.text = self.street_list[c]
      # self.text_box_27.text = self.build_name_list[c]
      # self.text_box_29.text = self.house_no_list[c]
      # self.text_box_28.text = self.landmark_list[c]
      # self.text_box_30.text = self.pincode_list[c]
      # self.text_box_33.text = self.state_list[c]
      # self.text_box_18.text = self.spouse_number_list[c]
      # self.text_box_19.text = self.company_name_list[c]
      # self.text_box_20.text = self.company_adress_list[c]
      # self.text_box_21.text =  self.proffic_list[c]
      # self.text_box_22.text = self.user_type_list[c]
      # self.text_box_23.text = bool(self.approve_list[c])
      # self.text_box_1.text = self.another_email[c]
      # self.text_box_6.text = self.company_name[c]
      # self.text_box_11.text = self.organization_type[c]
      # self.text_box_16.text = self.employment_type[c]
      # self.text_box_31.text = self.business_no[c]
      # self.text_box_36.text = self.company_landmark[c]
      # self.text_box_37.text = self.company_address[c]
      # self.text_box_38.text = self.annual_salary[c]
      # self.text_box_39.text = self.designation[c]
      # self.text_box_48.text = self.father_name[c]
      # self.text_box_49.text = self.father_age[c]
      # self.text_box_50.text = self.mother_name[c]
      # self.text_box_51.text = self.mother_age[c]
      # self.text_box_52.text = self.college_name[c]
      # self.text_box_53.text = self.college_id[c]
      # self.text_box_54.text = self.college_address[c]
      # # self.text_box_55.text = self.running_loan[c]
    

    # self.get = get_customer_id_value

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    # # Calculate the age based on the entered date of birth
    # Notification("You cannot edit the user age.").show()

    data = tables.app_tables.fin_user_profile.search()

    id_list = [i['customer_id'] for i in data]

    if self.get in id_list:
        a = id_list.index(self.get)
        user_data = data[a]
    

        # Update user profile data with values from the text boxes
        user_data['full_name'] = self.text_box_2.text
        user_data['profile_status'] = bool(self.text_box_3.text)
        user_data['gender'] = self.drop_down_1.selected_value
        user_data['user_age'] = int(self.text_box_5.text) 
        user_data['date_of_birth'] = self.text_box_25.text
        user_data['email_user'] = self.text_box_32.text
        user_data['street_adress_1'] = self.text_box_11.text
        user_data['street_address_2'] = self.text_box_4.text
        user_data['country'] = self.text_box_15.text
        user_data['profession'] = self.drop_down_9.selected_value
        user_data['mobile'] = self.text_box_7.text
        user_data['aadhaar_no'] = self.text_box_40.text
        user_data['pan_number'] = self.text_box_41.text
        user_data['city'] = self.text_box_10.text
        user_data['last_confirm'] = bool(self.text_box_12.text)
        user_data['mobile_check'] = bool(self.text_box_13.text)
        user_data['marital_status'] = self.drop_down_2.selected_value
        # user_data['Date_mariage'] = self.date_picker_2.date
        user_data['spouse_name'] = self.text_box_17.text
        user_data['spouse_mobile'] = self.text_box_18.text
        user_data['spouse_company_name'] = self.text_box_19.text
        user_data['spouse_company_address'] = self.text_box_20.text
        user_data['spouse_profession'] = self.text_box_21.text
        user_data['usertype'] = self.text_box_22.text
        user_data['registration_approve'] = bool(self.text_box_23.text)
        user_data['about'] = self.text_box_24.text
        user_data['address_type'] = self.drop_down_8.selected_value
        user_data['duration_at_address'] = self.drop_down_10.selected_value
        user_data['alerts'] = bool(self.text_box_26.text)
        user_data['building_name'] = self.text_box_27.text
        user_data['house_landmark'] = self.text_box_28.text
        user_data['house_no'] = self.text_box_29.text
        user_data['pincode'] = self.text_box_30.text
        user_data['business_no'] = self.text_box_31.text
        user_data['qualification'] = self.drop_down_3.selected_value
        user_data['state'] = self.text_box_33.text
        user_data['street'] = self.text_box_34.text
        user_data['terms'] = bool(self.text_box_35.text)
        user_data['another_email'] = self.text_box_1.text
        user_data['company_name'] = self.text_box_6.text
        user_data['organization_type'] = self.drop_down_4.selected_value
        user_data['employment_type'] = self.drop_down_5.selected_value
        user_data['company_landmark'] = self.text_box_36.text
        user_data['company_address'] = self.text_box_37.text
        user_data['annual_salary'] = self.text_box_38.text
        user_data['salary_type'] = self.drop_down_6.selected_value
        user_data['designation'] = self.text_box_39.text
        user_data['father_name'] = self.text_box_48.text
        user_data['father_age'] = self.text_box_49.text
        user_data['mother_name'] = self.text_box_50.text
        user_data['mother_age'] = self.text_box_51.text
        user_data['college_name'] = self.text_box_52.text
        user_data['college_id'] = self.text_box_53.text
        user_data['college_address'] = self.text_box_54.text
        user_data['home_loan'] = self.text_box_8.text
        user_data['other_loan'] = self.text_box_9.text
        user_data['credit_card_loans'] = self.text_box_14.text
        user_data['vehicle_loan'] = self.text_box_16.text
      

      # Calculate age based on the entered date of birth
        dob_text = self.text_box_25.text
        dob = datetime.strptime(dob_text, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        # Update user_age with calculated age
        user_data['user_age'] = age
        # Calculate ascend score and update
        ascend_value = anvil.server.call('final_points_update_ascend_table', self.get)
        if ascend_value is not None:
    # Convert ascend_value to float before assigning it to ascend_score
         user_data['ascend_value'] = float(ascend_value)
         # Fetch the borrower data
         borrower = app_tables.fin_borrower.get(customer_id=self.get)
         if borrower:
            borrower['user_name'] = self.text_box_2.text
            borrower.update()
         # Update the wallet data
         wallet = app_tables.fin_wallet.get(customer_id=self.get)
         if wallet:
            wallet['user_name'] = self.text_box_2.text
            wallet['user_type'] = self.text_box_22.text
            wallet.update()
         # update the foreclosure
         foreclosure = app_tables.fin_foreclosure.get(borrower_customer_id=self.get)
         if foreclosure:
            foreclosure['borrower_name']=self.text_box_2.text
            foreclosure.update()
         # update the extends
         extends_loan = app_tables.fin_extends_loan.get(borrower_customer_id=self.get)
         if extends_loan:
            extends_loan['borrower_full_name']=self.text_box_2.text 
            extends_loan.update()
         # update the loan_details 
         loan_details = app_tables.fin_loan_details.get(borrower_customer_id=self.get)
         if loan_details:
            loan_details['borrower_full_name']=self.text_box_2.text 
            loan_details.update()
 
              # Assign the converted value to ascend_score
            borrower['ascend_score'] = float(ascend_value)
        # Update the user profile
        user_data.update()
        alert("Date of birth and age updated successfully.", title="Success")
        alert("form saved successfully.", title="Success")
        print(f"Updated user profile, borrower, foreclosure, extends-loan, loan_details and wallet table for customer_id: {self.get}")
        open_form('admin.dashboard.customer_management.handles_customer_registration.borrowers.view_profile', self.get)
    else:
        alert("Customer user d not found. ", title="Error")
      
  def button_1_copy_click(self, **event_args):
    open_form('admin.dashboard.customer_management.handles_customer_registration.borrowers.view_profile', self.get)