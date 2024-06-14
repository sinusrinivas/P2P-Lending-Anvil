from ._anvil_designer import edit_form_copyTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
from datetime import date, datetime, timedelta
from anvil import open_form



class edit_form_copy(edit_form_copyTemplate):
    def __init__(self, get_customer_id_value, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
      
        # Any code you write here will run before the form opens.
        self.data = tables.app_tables.fin_user_profile.search()
        self.genders = tables.app_tables.fin_gender.search()
        self.marital_statuses = tables.app_tables.fin_lendor_marrital_status.search()
        self.account_types = tables.app_tables.fin_lendor_account_type.search()
        self.organization_types = tables.app_tables.fin_lendor_organization_type.search()
        self.employment_types = tables.app_tables.fin_lendor_employee_type.search()
        self.salary_types = tables.app_tables.fin_lendor_salary_type.search()
        self.address_types = tables.app_tables.fin_present_address.search()
        self.qualification_types = tables.app_tables.fin_lendor_qualification.search()
        self.lending_types = tables.app_tables.fin_lendor_lending_type.search()

        # Initialize lists for user profile details
        self.id_list = []
        self.name_list = []
        self.status_list = []
        self.gender_list = []
        self.age_list = []
        self.dob_list = []
        self.address_list = []
        self.lending_type_list = []
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
        self.street_list = []
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
        self.designation = []
        self.account_name = []
        self.account_type_list = []
        self.account_number = []
        self.account_bank_branch = []
        self.bank_id = []
        self.salary_type_list = []
        self.select_bank = []
        self.net_bank = []
        self.father_name = []
        self.father_age = []
        self.mother_name = []
        self.mother_age = []
        self.college_name = []
        self.college_id = []
        self.college_address = []
        self.running_loan = []

        self.drop_down_1.items = [(g['gender'], g['gender']) for g in self.genders]
        self.drop_down_2.items = [(ms['lendor_marrital_status'], ms['lendor_marrital_status']) for ms in self.marital_statuses]
        self.drop_down_3.items = [(at['lendor_account_type'], at['lendor_account_type']) for at in self.account_types]
        self.drop_down_4.items = [(ot['lendor_organization_type'], ot['lendor_organization_type']) for ot in self.organization_types]
        self.drop_down_5.items = [(et['lendor_employee_type'], et['lendor_employee_type']) for et in self.employment_types]
        self.drop_down_6.items = [(sa['lendor_salary_type'], sa['lendor_salary_type']) for sa in self.salary_types]
        self.drop_down_7.items = [(at['present_address'], at['present_address']) for at in self.address_types]
        self.drop_down_8.items = [(qa['lendor_qualification'], qa['lendor_qualification']) for qa in self.qualification_types]
        self.drop_down_9.items = [(lt['lendor_lending_type'], lt['lendor_lending_type']) for lt in self.lending_types]

        # Fill in user profile details
        # Populate lists with data
        a = -1
        for i in self.data:
            a += 1
            self.id_list.append(i['customer_id'])
            self.name_list.append(i['full_name'])
            self.status_list.append(i['profile_status'])
            self.gender_list.append(i['gender'])
            self.age_list.append(i['user_age'])
            self.dob_list.append(i['date_of_birth'])
            self.address_list.append(i['street_adress_1'])
            self.country_list.append(i['country'])
            self.lending_type_list.append(i['lendor_lending_type'])
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
            self.designation.append(i['designation'])
            self.account_name.append(i['account_name'])
            self.account_type_list.append(i['account_type'])
            self.account_number.append(i['account_number'])
            self.account_bank_branch.append(i['account_bank_branch'])
            # self.ifsc_code.append(i['bak_id'])
            self.salary_type_list.append(i['salary_type'])
            # self.select_bank.append(i['select_bank'])
            # self.net_bank.append(i['net_bank'])
            self.father_name.append(i['father_name'])
            self.father_age.append(i['father_age'])
            self.mother_name.append(i['mother_name'])
            self.mother_age.append(i['mother_age'])
            self.college_name.append(i['college_name'])
            self.college_id.append(i['college_id'])
            self.college_address.append(i['college_address'])
            self.running_loan.append('running_Home_Loan')

        print(self.company_adress_list)
        # If the customer ID exists, populate the form
        if get_customer_id_value in self.id_list:
            c = self.id_list.index(get_customer_id_value)
            self.populate_form(c)

        self.get = get_customer_id_value
      
    def populate_form(self, c):
        self.set_textbox_visibility(self.text_box_2, self.label_2, self.name_list[c])
        self.set_textbox_visibility(self.text_box_3, self.label_4, str(self.status_list[c]))      
        self.drop_down_1.selected_value =self.gender_list[c]
        # self.set_dropdown_visibility(self.drop_down_1,self.label_5,str(self.gender_list[c]))
        self.set_textbox_visibility(self.text_box_5, self.label_6, self.age_list[c])
        self.set_textbox_visibility(self.text_box, self.label_7, self.dob_list[c])
        self.set_textbox_visibility(self.text_box_4,self.label_60,self.email_user_list[c])
        self.set_textbox_visibility(self.text_box_11,self.label_61,self.address_list[c])
        self.set_textbox_visibility(self.text_box_15,self.label_62,self.country_list[c])
        self.set_textbox_visibility(self.text_box_7, self.label_10, self.mobile_list[c])
        self.set_textbox_visibility(self.text_box_8, self.label_11, self.aadhar_list[c])
        self.set_textbox_visibility(self.text_box_9, self.label_12, self.pan_list[c])
        self.set_textbox_visibility(self.text_box_10, self.label_13, self.city_list[c])
        self.set_textbox_visibility(self.text_box_12, self.label_15, str(self.last_confirm_list[c]))
        self.set_textbox_visibility(self.text_box_13, self.label_16, str(self.mobile_check_list[c]))
        # self.set_textbox_visibility(self.text_box_14, self.label_17, self.mother_tongue_list[c])
        # self.set_textbox_visibility(self.text_box_15, self.label_18, self.mother_status_list[c])
        self.drop_down_2.selected_value = self.mother_status_list[c]
        self.set_textbox_visibility(self.text_box_17, self.label_20, self.space_name_list[c])
        self.set_textbox_visibility(self.text_box_24, self.label_27, self.about_list[c])
        self.set_textbox_visibility(self.text_box_26, self.label_29, str(self.alets_list[c]))
        self.set_textbox_visibility(self.text_box_34,self.label_37,self.street_list[c])
        self.set_textbox_visibility(self.text_box_35, self.label_38, str(self.terms_list[c]))
        # self.set_textbox_visibility(self.text_box_32, self.label_35, self.qualification_list[c])
        self.drop_down_8.selected_value = self.qualification_list[c]
        self.drop_down_9.selected_value = self.lending_type_list[c]
        # self.set_textbox_visibility(self.text_box_25, self.label_28, self.address_type_list[c])
        self.drop_down_7.selected_value = self.address_type_list[c]
        self.set_textbox_visibility(self.text_box_34, self.label_37, self.street_list[c])
        self.set_textbox_visibility(self.text_box_27, self.label_30, self.build_name_list[c])
        self.set_textbox_visibility(self.text_box_29, self.label_32, self.house_no_list[c])
        self.set_textbox_visibility(self.text_box_28, self.label_31, self.landmark_list[c])
        self.set_textbox_visibility(self.text_box_30, self.label_34, self.pincode_list[c])
        self.set_textbox_visibility(self.text_box_33, self.label_36, self.state_list[c])
        self.set_textbox_visibility(self.text_box_18, self.label_21, self.spouse_number_list[c])
        self.set_textbox_visibility(self.text_box_19, self.label_22, self.company_name_list[c])
        self.set_textbox_visibility(self.text_box_20, self.label_23, self.company_adress_list[c])
        self.set_textbox_visibility(self.text_box_21, self.label_24, self.proffic_list[c])
        self.set_textbox_visibility(self.text_box_22, self.label_25, self.user_type_list[c])
        self.set_textbox_visibility(self.text_box_23, self.label_26, str(self.approve_list[c]))
        self.set_textbox_visibility(self.text_box_1, self.label_1, self.another_email[c])
        self.set_textbox_visibility(self.text_box_6, self.label_3, self.company_name[c])
        # self.set_textbox_visibility(self.text_box_11, self.label_9, self.organization_type[c])
        self.drop_down_4.selected_value = self.organization_type_list[c]
        # self.set_textbox_visibility(self.text_box_16, self.label_8, self.employment_type[c])
        self.drop_down_5.selected_value = self.employment_type_list[c]
        self.set_textbox_visibility(self.text_box_31, self.label_14, self.business_no[c])
        self.set_textbox_visibility(self.text_box_36, self.label_33, self.company_landmark[c])
        self.set_textbox_visibility(self.text_box_37, self.label_39, self.company_address[c])
        self.set_textbox_visibility(self.text_box_38, self.label_40, self.annual_salary[c])
        self.set_textbox_visibility(self.text_box_39, self.label_41, self.designation[c])
        self.set_textbox_visibility(self.text_box_40, self.label_44, self.account_name[c])
        # self.set_textbox_visibility(self.text_box_41, self.label_45, self.account_type[c])
        self.drop_down_3.selected_value = self.account_type_list[c]
        self.set_textbox_visibility(self.text_box_42, self.label_46, self.account_number[c])
        self.set_textbox_visibility(self.text_box_43, self.label_47, self.account_bank_branch[c])
        # self.ifsc_code.append(i['bank_id'])
        # self.set_textbox_visibility(self.text_box_45, self.label_49, self.salary_type[c])
        self.drop_down_6.selected_value = self.salary_type_list[c]
        # self.select_bank.append(i['select_bank'])
        # self.net_bank.append(i['net_bank'])
        self.set_textbox_visibility(self.text_box_48, self.label_52, self.father_name[c])
        self.set_textbox_visibility(self.text_box_49, self.label_53, self.father_age[c])
        self.set_textbox_visibility(self.text_box_50, self.label_54, self.mother_name[c])
        self.set_textbox_visibility(self.text_box_51, self.label_55, self.mother_age[c])
        self.set_textbox_visibility(self.text_box_52, self.label_56, self.college_name[c])
        self.set_textbox_visibility(self.text_box_53, self.label_57, self.college_id[c])
        self.set_textbox_visibility(self.text_box_54, self.label_58, self.college_address[c])

        # self.calculate_and_validate_age(c)

 

    def set_textbox_visibility(self, textbox, label, data):
      if data :
            textbox.text = data
            textbox.visible = True
            label.visible = True
      
      else:
            textbox.visible = False
            label.visible = False

    def validate_age(self, date_of_birth, age):
        if not date_of_birth or not age:
            return False

        try:
            dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        except ValueError:
            return False

        today = date.today()
        calculated_age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return calculated_age == int(age)
   

    # def button_2_click(self, **event_args):
        # """This method is called when the button is clicked"""
        # Notification("You cannot edit the user age.").show()
        # data = tables.app_tables.fin_user_profile.search()


        # id_list = []
        # for i in self.data:
        #     id_list.append(i['customer_id'])

        # if self.get in id_list:
        #     a = id_list.index(self.get)
        #     data[a]['full_name'] = self.text_box_2.text
        #     data[a]['profile_status'] = bool(self.text_box_3.text)
        #     data[a]['gender'] = self.drop_down_1.selected_value
        #     data[a]['user_age'] = int(self.text_box_5.text)
        #     # data[a]['date_of_birth'] = self.date_picker_1.date
        #     data[a]['mobile'] = self.text_box_7.text
        #     data[a]['aadhaar_no'] = self.text_box_8.text
        #     data[a]['pan_number'] = self.text_box_9.text
        #     data[a]['city'] = self.text_box_10.text
        #     data[a]['last_confirm'] = bool(self.text_box_12.text)
        #     data[a]['mobile_check'] = bool(self.text_box_13.text)
        #     data[a]['marital_status'] = self.drop_down_2.selected_value
        #     #data[a]['Date_mariage'] = self.date_picker_2.date
        #     data[a]['spouse_name'] = self.text_box_17.text
        #     data[a]['spouse_mobile'] = self.text_box_18.text
        #     data[a]['spouse_company_name'] = self.text_box_19.text
        #     data[a]['spouse_company_address'] = self.text_box_20.text
        #     data[a]['spouse_profession'] = self.text_box_21.text
        #     data[a]['usertype'] = self.text_box_22.text
        #     data[a]['registration_approve'] = bool(self.text_box_23.text)
        #     data[a]['address_type'] = self.drop_down_7.selected_value
        #     data[a]['qualification'] = self.drop_down_8.selected_value
        #     data[a]['another_email'] = self.text_box_1.text
        #     data[a]['company_name'] = self.text_box_6.text
        #     data[a]['organization_type'] = self.drop_down_4.selected_value
        #     data[a]['employment_type'] = self.drop_down_5.selected_value
        #     data[a]['business_no'] = self.text_box_31.text
        #     data[a]['company_landmark'] = self.text_box_36.text
        #     data[a]['company_address'] = self.text_box_37.text
        #     data[a]['annual_salary'] = self.text_box_38.text
        #     data[a]['designation'] = self.text_box_39.text
        #     data[a]['account_name'] = self.text_box_40.text
        #     data[a]['account_type'] = self.drop_down_3.selected_value
        #     data[a]['account_number'] = self.text_box_42.text
        #     data[a]['account_bank_branch'] = self.text_box_43.text
        #     # data[a]['ifsc_code'] = self.text_box_44.text
        #     data[a]['salary_type'] = self.drop_down_6.selected_value
        #     # data[a]['select_bank'] = self.text_box_46.text
        #     # data[a]['net_bank'] = self.text_box_47.text
        #     data[a]['father_name'] = self.text_box_48.text
        #     data[a]['father_age'] = self.text_box_49.text
        #     data[a]['mother_name'] = self.text_box_50.text
        #     data[a]['mother_age'] = self.text_box_51.text
        #     data[a]['college_name'] = self.text_box_52.text
        #     data[a]['college_id'] = self.text_box_53.text
        #     data[a]['college_address'] = self.text_box_54.text
    def button_2_click(self, **event_args):
            date_of_birth = self.text_box.text
    
              # Calculate age based on the new date of birth
            try:
                dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
            except ValueError:
                alert("Invalid date format. Please enter the date in YYYY-MM-DD format.", title="Validation Error")
                return

        # Calculate age based on the new date of birth
            today = date.today()
            calculated_age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
      
            # Update the age textbox with the calculated age
            self.text_box_5.text = str(calculated_age)
           
             # Retrieve the record using a search query
            record = app_tables.fin_user_profile.get(customer_id=self.get)
    
            if record:
                record.update(
                    full_name=self.text_box_2.text,
                    profile_status=bool(self.text_box_3.text),
                    gender=self.drop_down_1.selected_value,
                    date_of_birth=date_of_birth, #new
                    user_age = calculated_age, #new
                    email_user=self.text_box_35.text,
                    street_adress_1= self.text_box_11.text,
                    country = self.text_box_15.text,
                    lendor_lending_type = self.drop_down_9.selected_value,
                    mobile=self.text_box_7.text,
                    aadhaar_no=self.text_box_8.text,
                    pan_number=self.text_box_9.text,
                    city=self.text_box_10.text,
                    last_confirm=bool(self.text_box_12.text),
                    mobile_check=bool(self.text_box_13.text),
                    marital_status=self.drop_down_2.selected_value,
                    spouse_name=self.text_box_17.text,
                    spouse_mobile=self.text_box_18.text,
                    spouse_company_name=self.text_box_19.text,
                    spouse_company_address=self.text_box_20.text,
                    spouse_profession=self.text_box_21.text,
                    usertype=self.text_box_22.text,
                    registration_approve=bool(self.text_box_23.text),
                    about=self.text_box_24.text,
                    address_type=self.drop_down_7.selected_value,
                    alerts=bool(self.text_box_26.text),
                    building_name=self.text_box_27.text,
                    house_landmark=self.text_box_28.text,
                    house_no=self.text_box_29.text,
                    pincode=self.text_box_30.text,
                    business_no=self.text_box_31.text,
                    qualification=self.drop_down_8.selected_value,
                    state=self.text_box_33.text,
                    street=self.text_box_34.text,
                    mail_id=self.text_box_21.text,
                    terms=bool(self.text_box_35.text),
                    another_email=self.text_box_1.text,
                    company_name=self.text_box_6.text,
                    organization_type=self.drop_down_4.selected_value,
                    employment_type=self.drop_down_5.selected_value,
                    company_landmark=self.text_box_36.text,
                    company_address=self.text_box_37.text,
                    annual_salary=self.text_box_38.text,
                    designation=self.text_box_39.text,
                    account_name=self.text_box_40.text,
                    account_type=self.drop_down_3.selected_value,
                    account_number=self.text_box_42.text,
                    account_bank_branch=self.text_box_43.text,
                    # bank_id=self.text_box_44.text,
                    salary_type=self.drop_down_6.selected_value,
                    # select_bank=self.text_box_46.text,
                    # net_bank=self.text_box_47.text,
                    father_name=self.text_box_48.text,
                    father_age=self.text_box_49.text,
                    mother_name=self.text_box_50.text,
                    mother_age=self.text_box_51.text,
                    college_name=self.text_box_52.text,
                    college_id=self.text_box_53.text,
                    college_address=self.text_box_54.text,
                )
            else:
                alert("Date of birth and age updated successfully.", title="Success") #new
                alert("Form saved successfully.", title="Success")
                self.raise_event('x-close-alert')

            lender = app_tables.fin_lender.get(customer_id=self.get)
            if lender:
                lender['user_name'] = self.text_box_2.text
                lender.update()
            # Update the wallet data
            wallet = app_tables.fin_wallet.get(customer_id = self.get)
            if wallet:
                wallet['user_name'] = self.text_box_2.text
                wallet['user_type'] = self.text_box_22.text
                wallet.update()

            #loan details table
            loan_details = app_tables.fin_loan_details.get(lender_customer_id = self.get)
            if loan_details:
                loan_details['lender_full_name'] = self.text_box_2.text
                loan_details.update()

            #extends_loa
            extends_loan = app_tables.fin_extends_loan.get(lender_customer_id = self.get)
            if extends_loan:
                extends_loan['lender_full_name'] = self.text_box_2.text
                extends_loan.update()

            forclosure = app_tables.fin_foreclosure.get(lender_customer_id=self.get)
            if forclosure:
                forclosure['lender_full_name'] = self.text_box_2.text
                forclosure.update()

            wallet_bank_accont_table = app_tables.fin_wallet_bank_account_table.get(customer_id=self.get)
            if wallet_bank_accont_table:
                wallet_bank_accont_table['account_name']=self.text_box_40.text
                wallet_bank_accont_table.update()
              
            print(f"Updates user profile, lender, wallet, forclosure, loan_details and extends_loan table for customer_id: {self.get}")
            open_form('admin.dashboard.customer_management.handles_customer_registration.lenders.view_profile_copy', self.get)


    def button_1_click(self, **event_args):
          """This method is called when the button is clicked"""
          open_form('admin.dashboard.customer_management.handles_customer_registration.lenders.view_profile_copy', self.get)
      
    def button_1_copy_click(self, **event_args):
          """This method is called when the button is clicked"""
          open_form('admin.dashboard.customer_management.handles_customer_registration.lenders.view_profile_copy', self.get)

   
