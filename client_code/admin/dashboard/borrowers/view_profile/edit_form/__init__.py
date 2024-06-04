from ._anvil_designer import edit_formTemplate
from anvil import *
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
    self.account_type = tables.app_tables.fin_borrower_account_type.search()
    self.salary_type = tables.app_tables.fin_borrower_salary_type.search()
  

    self.id_list = []
    self.name_list = []
    self.status_list = []
    self.gender_list = []
    self.age_list = []
    self.dob_list = []
    self.aadhar_list = []
    self.pan_list = []
    self.city_list = []
    self.email_user_list = []
    self.last_confirm_list = []
    self.mobile_check_list = []
    self.mother_tongue_list = []
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
    self.ifsc_code = []
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

    self.drop_down_1.items=[(g['gender'],g['gender']) for g in self.genders]
    self.drop_down_2.items = [(ms['borrower_marrital_status'], ms['borrower_marrital_status']) for ms in self.marital_statuses]
    self.drop_down_3.items = [(q['borrower_qualification'], q['borrower_qualification']) for q in self.qualification]
    self.drop_down_8.items = [(lt['land_type'], lt['land_type']) for lt in self.address_type]
    self.drop_down_4.items = [(ot['borrower_organization_type'], ot['borrower_organization_type']) for ot in self.organization_type]
    self.drop_down_5.items = [(et['borrower_employee_type'], et['borrower_employee_type']) for et in self.employment_type]
    self.drop_down_6.items = [(at['borrower_account_type'], at['borrower_account_type']) for at in self.account_type]
    self.drop_down_7.items = [(st['borrower_salary_type'], st['borrower_salary_type']) for st in self.salary_type]
    
    a = -1
    for i in self.data:
      a+=1
      self.id_list.append(i['customer_id'])
      self.name_list.append(i['full_name'])
      self.status_list.append(i['profile_status'])
      self.gender_list.append(i['gender'])
      self.age_list.append(i['user_age'])
      self.dob_list.append(i['date_of_birth'])
      self.aadhar_list.append(i['aadhaar_no'])
      self.pan_list.append(i['pan_number'])
      self.city_list.append(i['city'])
      self.email_user_list.append(i['email_user'])
      self.last_confirm_list.append(i['last_confirm'])
      self.mobile_check_list.append(i['mobile_check'])
      self.mother_status_list.append(i['marital_status'])
      self.mother_tongue_list.append(i['mouther_tounge'])
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
      # self.ifsc_code.append(i['ifsc_code'])
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
      # self.running_loan.append('running_Home_Loan')

    print(self.company_adress_list)
    if get_customer_id_value in self.id_list:
      c = self.id_list.index(get_customer_id_value)

      self.set_textbox_visibility(self.text_box_2,self.label_2,self.name_list[c])
      self.set_textbox_visibility(self.text_box_3,self.label_4, str(self.status_list[c]))
      self.drop_down_1.selected_value=self.gender_list[c]
      self.set_textbox_visibility(self.text_box_5,self.label_6, self.age_list[c])
      self.set_textbox_visibility(self.text_box,self.label_7, self.dob_list[c])
      self.set_textbox_visibility(self.text_box_7,self.label_10, self.mobile_list[c])
      self.set_textbox_visibility(self.text_box_8,self.label_11, self.aadhar_list[c])
      self.set_textbox_visibility(self.text_box_9,self.label_12, self.pan_list[c])
      self.set_textbox_visibility(self.text_box_10,self.label_13, self.city_list[c])
      self.set_textbox_visibility(self.text_box_12,self.label_15, str(self.last_confirm_list[c]))
      self.set_textbox_visibility(self.text_box_13,self.label_16, str(self.mobile_check_list[c]))
      self.set_textbox_visibility(self.text_box_14,self.label_17, self.mother_tongue_list[c])
      self.drop_down_2.selected_value = self.mother_status_list[c]
      self.set_textbox_visibility(self.text_box_17,self.label_20, self.space_name_list[c])
      self.set_textbox_visibility(self.text_box_24,self.label_27, self.about_list[c])
      self.set_textbox_visibility(self.text_box_26,self.label_29, str(self.alets_list[c]))
      self.set_textbox_visibility(self.text_box_35,self.label_38, str(self.terms_list[c]))
      self.drop_down_3.selected_value = self.qualification_list[c]
      self.drop_down_4.selected_value = self.address_type_list[c]
      self.set_textbox_visibility(self.text_box_34,self.label_37, self.street_list[c])
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
      self.set_textbox_visibility(self.text_box_36,self.label_33, self.company_landmark[c])
      self.set_textbox_visibility(self.text_box_37,self.label_39, self.company_address[c])
      self.set_textbox_visibility(self.text_box_38,self.label_40, self.annual_salary[c])
      self.set_textbox_visibility(self.text_box_39,self.label_41, self.designation[c])
      self.set_textbox_visibility(self.text_box_40,self.label_44, self.account_name[c])
      self.drop_down_6.selected_value = self.account_type_list[c]
      self.set_textbox_visibility(self.text_box_42,self.label_46, self.account_number[c])
      self.set_textbox_visibility(self.text_box_43,self.label_47, self.account_bank_branch[c])
      self.drop_down_7.selected_value = self.salary_type_list[c]
      self.set_textbox_visibility(self.text_box_48,self.label_52, self.father_name[c])
      self.set_textbox_visibility(self.text_box_49,self.label_53, self.father_age[c])
      self.set_textbox_visibility(self.text_box_50,self.label_54, self.mother_name[c])
      self.set_textbox_visibility(self.text_box_51,self.label_55, self.mother_age[c])
      self.set_textbox_visibility(self.text_box_52,self.label_56, self.college_name[c])
      self.set_textbox_visibility(self.text_box_53,self.label_57, self.college_id[c])
      self.set_textbox_visibility(self.text_box_54,self.label_58,self.college_address[c])
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
      # self.text_box_14.text = self.mother_tongue_list[c]
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
      # self.text_box_40.text = self.account_name[c]
      # self.text_box_41.text = self.account_type[c]
      # self.text_box_42.text = self.account_number[c]
      # self.text_box_43.text = self.account_bank_branch[c]
      # # self.text_box_44.text = self.ifsc_code[c]
      # self.text_box_45.text = self.salary_type[c]
      # # self.text_box_46.text = self.select_bank[c]
      # # self.text_box_47.text = self.net_bank[c]
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
    Notification("You cannot edit the user age.").show()
    data = tables.app_tables.fin_user_profile.search()
    # data = tables.app_tables.fin_borrower.search()
    # data = tables.app_tables.fin_wallet.search()
    # data = tables.app_tables.fin_wallet_bank_account_table.search()

    id_list = [i['customer_id'] for i in data]

    if self.get in id_list:
        a = id_list.index(self.get)
        user_data = data[a]
    

        # Update user profile data with values from the text boxes
        user_data['full_name'] = self.text_box_2.text
        user_data['profile_status'] = bool(self.text_box_3.text)
        user_data['gender'] = self.drop_down_1.selected_value
        user_data['user_age'] = int(self.text_box_5.text) 
        dob = self.calculate_dob_from_age(int(self.text_box_5.text))
        if dob > date.today():
          Notification("Date of Birth cannot be in the future.").show()
          return
        
        user_data['date_of_birth'] = dob.strftime('%Y-%m-%d')
        # user_data['date_of_birth'] = self.date_picker_1
        user_data['mobile'] = self.text_box_7.text
        user_data['aadhaar_no'] = self.text_box_8.text
        user_data['pan_number'] = self.text_box_9.text
        user_data['city'] = self.text_box_10.text
        user_data['last_confirm'] = bool(self.text_box_12.text)
        user_data['mobile_check'] = bool(self.text_box_13.text)
        user_data['mouther_tounge'] = self.text_box_14.text
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
        user_data['designation'] = self.text_box_39.text
        user_data['account_name'] = self.text_box_40.text
        user_data['account_type'] = self.drop_down_6.selected_value
        user_data['account_number'] = self.text_box_42.text
        user_data['account_bank_branch'] = self.text_box_43.text
        # user_data['ifsc_code'] = self.text_box_44.text
        user_data['salary_type'] = self.drop_down_7.selected_value
        # user_data['select_bank'] = self.text_box_46.text
        # user_data['net_bank'] = self.text_box_47.text
        user_data['father_name'] = self.text_box_48.text
        user_data['father_age'] = self.text_box_49.text
        user_data['mother_name'] = self.text_box_50.text
        user_data['mother_age'] = self.text_box_51.text
        user_data['college_name'] = self.text_box_52.text
        user_data['college_id'] = self.text_box_53.text
        user_data['college_address'] = self.text_box_54.text
        # Calculate ascend score and update
        ascend_value = anvil.server.call('final_points_update_ascend_table', self.get)
        if ascend_value is not None:
    # Convert ascend_value to float before assigning it to ascend_score
         user_data['ascend_value'] = float(ascend_value)
         # Fetch the borrower data
         borrower = app_tables.fin_borrower.get(customer_id=self.get)
         if borrower:
            borrower['user_name'] = self.text_box_2.text
         # Update the wallet data
         wallet = app_tables.fin_wallet.get(customer_id=self.get)
         if wallet:
            wallet['user_name'] = self.text_box_2.text  
  
              # Assign the converted value to ascend_score
            borrower['ascend_score'] = float(ascend_value)
        # data.update()
        print(f"Updated user profile, borrower and wallet table for customer_id: {self.get}")
        open_form('admin.dashboard.borrowers.view_profile', self.get)
  def calculate_dob_from_age(self, age):
      """Calculate date of birth from age"""
      today = date.today()
      year_of_birth = today.year - age
      dob = date(year_of_birth, today.month, today.day)
      # Adjust if the birthdate is not valid (e.g., leap year)
      while True:
        try:
          dob = dob.replace(year=year_of_birth)
          break
        except ValueError:
          year_of_birth -= 1
      return dob    

  # def button_2_click(self, **event_args):
  #   """This method is called when the button is clicked"""
  #   data = tables.app_tables.fin_user_profile.search()

  #   id_list = []
  #   for i in self.data:
  #     id_list.append(i['customer_id'])

  #   if self.get in id_list:
  #     a = id_list.index(self.get)
  #     data[a]['full_name'] = self.text_box_2.text
  #     data[a]['profile_status'] = bool(self.text_box_3.text)
  #     data[a]['gender'] = self.text_box_4.text
  #     data[a]['user_age'] = int(self.text_box_5.text)
  #     # data[a]['date_of_birth'] = self.date_picker_1.date
  #     data[a]['mobile'] = self.text_box_7.text
  #     data[a]['aadhaar_no'] = self.text_box_8.text
  #     data[a]['pan_number'] = self.text_box_9.text
  #     data[a]['city'] = self.text_box_10.text
  #     data[a]['last_confirm'] = bool(self.text_box_12.text)
  #     data[a]['mobile_check'] = bool(self.text_box_13.text)
  #     data[a]['mouther_tounge'] = self.text_box_14.text
  #     data[a]['marital_status'] = self.text_box_15.text
  #     # data[a]['Date_mariage'] = self.date_picker_2.date
  #     data[a]['spouse_name'] = self.text_box_17.text
  #     data[a]['spouse_mobile'] = self.text_box_18.text
  #     data[a]['spouse_company_name'] = self.text_box_19.text
  #     data[a]['spouse_company_address'] = self.text_box_20.text
  #     data[a]['spouse_profession'] = self.text_box_21.text
  #     data[a]['usertype'] = self.text_box_22.text
  #     data[a]['registration_approve'] = bool(self.text_box_23.text)
  #     data[a]['about'] = self.text_box_24.text
  #     data[a]['address_type'] = self.text_box_25.text
  #     data[a]['alerts'] = bool(self.text_box_26.text)
  #     data[a]['building_name'] = self.text_box_27.text
  #     data[a]['house_landmark'] = self.text_box_28.text
  #     data[a]['house_no'] = self.text_box_29.text
  #     data[a]['pincode'] = self.text_box_30.text
  #     data[a]['business_no'] = self.text_box_31.text
  #     data[a]['qualification'] = self.text_box_32.text
  #     data[a]['state'] = self.text_box_33.text
  #     data[a]['street'] = self.text_box_34.text
  #     data[a]['terms'] = bool(self.text_box_35.text)
  #     data[a]['another_email'] = self.text_box_1.text
  #     data[a]['company_name'] = self.text_box_6.text
  #     data[a]['organization_type'] = self.text_box_11.text
  #     data[a]['employment_type'] = self.text_box_16.text
  #     data[a]['company_landmark'] = self.text_box_36.text
  #     data[a]['company_address'] = self.text_box_37.text
  #     data[a]['annual_salary'] = self.text_box_38.text
  #     data[a]['designation'] = self.text_box_39.text
  #     data[a]['account_name'] = self.text_box_40.text
  #     data[a]['account_type'] = self.text_box_41.text
  #     data[a]['account_number'] = self.text_box_42.text
  #     data[a]['account_bank_branch'] = self.text_box_43.text
  #     # data[a]['ifsc_code'] = self.text_box_44.text
  #     data[a]['salary_type'] = self.text_box_45.text
  #     # data[a]['select_bank'] = self.text_box_46.text
  #     # data[a]['net_bank'] = self.text_box_47.text
  #     data[a]['father_name'] = self.text_box_48.text
  #     data[a]['father_age'] = self.text_box_49.text
  #     data[a]['mother_name'] = self.text_box_50.text
  #     data[a]['mother_age'] = self.text_box_51.text
  #     data[a]['college_name'] = self.text_box_52.text
  #     data[a]['college_id'] = self.text_box_53.text
  #     data[a]['college_address'] = self.text_box_54.text
  #     # data[a]['running_Home_Loan'] = self.text_box_55.text
  #     print(a)
  #     open_form('admin.dashboard.borrowers.view_profile', self.get)

  def button_1_copy_click(self, **event_args):
    open_form('admin.dashboard.borrowers.view_profile', self.get)