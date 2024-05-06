from ._anvil_designer import view_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class view_profile(view_profileTemplate):
  def __init__(self, value_to_display, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.fin_user_profile.search()
    
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
    self.organization_type = []
    self.employment_type = []
    self.business_no = []
    self.company_landmark = []
    self.company_address = []
    self.annual_salary = []
    self.designation = []
    self.account_name = []
    self.account_type = []
    self.account_number = []
    self.account_bank_branch = []
    self.ifsc_code = []
    self.salary_type = []
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
    self.profile = []
    self.aadhaar_photo = []
    self.pan_photo = []
    self.emp_id_proof = []
    self.last_six_month_bank_proof = []
    self.college_proof = []

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
      #self.date_marrige_list.append(i['Date_mariage'])
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
      self.organization_type.append(i['organization_type'])
      self.employment_type.append(i['employment_type'])
      self.business_no.append(i['business_no'])
      self.company_landmark.append(i['company_landmark'])
      self.company_address.append(i['company_address'])
      self.annual_salary.append(i['annual_salary'])
      self.designation.append(i['designation'])
      self.account_name.append(i['account_name'])
      self.account_type.append(i['account_type'])
      self.account_number.append(i['account_number'])
      self.account_bank_branch.append(i['account_bank_branch'])
      #self.ifsc_code.append(i['ifsc_code'])
      self.salary_type.append(i['salary_type'])
      #self.select_bank.append(i['select_bank'])
      # self.net_bank.append(i['net_bank'])
      self.father_name.append(i['father_name'])
      self.father_age.append(i['father_age'])
      self.mother_name.append(i['mother_name'])
      self.mother_age.append(i['mother_age'])
      self.college_name.append(i['college_name'])
      self.college_id.append(i['college_id'])
      self.college_address.append(i['college_address'])
      # self.running_loan.append('running_Home_Loan')
      self.profile.append(i['user_photo'])
      self.aadhaar_photo.append(i['aadhaar_photo'])
      self.pan_photo.append(i['pan_photo'])
      self.emp_id_proof.append(i['emp_id_proof'])
      self.last_six_month_bank_proof.append(i['last_six_month_bank_proof'])
      self.college_proof.append(i['college_proof'])

    print(self.company_adress_list)
    if a == -1:
      alert("No Data Available Here!!")
    else:
      if value_to_display in self.id_list:
        b = self.id_list.index(value_to_display)
        self.label_3.text = value_to_display

        self.set_label_visibility(self.label_8,self.label_2, self.name_list[b])
        self.set_label_visibility(self.label_9,self.label_4, bool(self.status_list[b]))
        self.set_label_visibility(self.label_39,self.label_5, self.gender_list[b])
        self.set_label_visibility(self.label_40, self.label_6,str(self.age_list[b]) if self.age_list[b] else '')
        self.set_label_visibility(self.label_41,self.label_7, self.dob_list[b])
        self.set_label_visibility(self.label_44,self.label_10, self.mobile_list[b])
        self.set_label_visibility(self.label_45,self.label_11, self.aadhar_list[b])
        self.set_label_visibility(self.label_46,self.label_12, self.pan_list[b])
        self.set_label_visibility(self.label_47,self.label_13, self.city_list[b])
        self.set_label_visibility(self.label_48,self.label_14, self.email_user_list[b])
        self.set_label_visibility(self.label_49, self.label_15,bool(self.last_confirm_list[b]))
        self.set_label_visibility(self.label_50,self.label_16, self.mobile_check_list[b])
        self.set_label_visibility(self.label_51,self.label_17, self.mother_tongue_list[b])
        self.set_label_visibility(self.label_52,self.label_18, self.mother_status_list[b])
        self.set_label_visibility(self.label_54,self.label_20, self.space_name_list[b])
        self.set_label_visibility(self.label_61,self.label_27, self.about_list[b])
        self.set_label_visibility(self.label_63,self.label_29, bool(self.alets_list[b]))
        self.set_label_visibility(self.label_72,self.label_38, bool(self.terms_list[b]))
        self.set_label_visibility(self.label_69,self.label_35, self.qualification_list[b])
        self.set_label_visibility(self.label_62,self.label_28, self.address_type_list[b])
        self.set_label_visibility(self.label_71,self.label_37, self.street_list[b])
        self.set_label_visibility(self.label_64,self.label_30, self.build_name_list[b])
        self.set_label_visibility(self.label_66,self.label_32, self.house_no_list[b])
        self.set_label_visibility(self.label_65,self.label_31, self.landmark_list[b])
        self.set_label_visibility(self.label_68,self.label_34, self.pincode_list[b])
        self.set_label_visibility(self.label_70,self.label_36, self.state_list[b])
        self.set_label_visibility(self.label_55,self.label_21, self.spouse_number_list[b])
        self.set_label_visibility(self.label_56,self.label_22, self.company_name_list[b])
        self.set_label_visibility(self.label_57, self.label_4,self.company_adress_list[b])
        self.set_label_visibility(self.label_58,self.label_4, self.proffic_list[b])
        self.set_label_visibility(self.label_59,self.label_4, self.user_type_list[b])
        self.set_label_visibility(self.label_60,self.label_4, bool(self.approve_list[b]))
        self.set_label_visibility(self.label_74,self.label_4, self.another_email[b])
        self.set_label_visibility(self.label_76,self.label_4, self.company_name[b])
        self.set_label_visibility(self.label_77,self.label_4, self.organization_type[b])
        self.set_label_visibility(self.label_79,self.label_4, self.employment_type[b])
        self.set_label_visibility(self.label_81,self.label_4, self.business_no[b])
        self.set_label_visibility(self.label_83,self.label_4, self.company_landmark[b])
        self.set_label_visibility(self.label_85,self.label_4, self.company_address[b])
        self.set_label_visibility(self.label_87,self.label_4, self.annual_salary[b])
        self.set_label_visibility(self.label_89,self.label_4, self.designation[b])
        self.set_label_visibility(self.label_91,self.label_4, self.account_name[b])
        self.set_label_visibility(self.label_93,self.label_4, self.account_type[b])
        self.set_label_visibility(self.label_95,self.label_4, self.account_number[b])
        self.set_label_visibility(self.label_97,self.label_4, self.account_bank_branch[b])
        self.set_label_visibility(self.label_101,self.label_4, self.salary_type[b])
        self.set_label_visibility(self.label_107, self.label_4,self.father_name[b])
        self.set_label_visibility(self.label_109,self.label_4, self.father_age[b])
        self.set_label_visibility(self.label_111,self.label_4, self.mother_name[b])
        self.set_label_visibility(self.label_113,self.label_4, self.mother_age[b])
        self.set_label_visibility(self.label_115,self.label_4, self.college_name[b])
        self.set_label_visibility(self.label_117,self.label_4, self.college_id[b])
        self.set_label_visibility(self.label_119,self.label_4, self.college_address[b])

        # Set image sources
        self.image_2.source = self.profile[b]
        self.image_3.source = self.aadhaar_photo[b]
        self.image_4.source = self.pan_photo[b]
        self.image_5.source = self.emp_id_proof[b]
        self.image_6.source = self.last_six_month_bank_proof[b]
        self.image_7.source = self.college_proof[b]

  def set_label_visibility(self, label,label_1, data ):
    if data:
        label.text = data
        label.visible = True
        label_1.visible = True
    else:
        label.visible = False
        label_1.visible = False
        
        # if self.name_list[b]:
        #   self.label_8.text = self.name_list[b]
        #   self.label_8.visible = True
        #   self.label_2.visible = True
        # else:
        #   self.label_8.visible =  False
        #   self.label_2.visible = False
          
        # self.label_9.text = bool(self.status_list[b])
        # self.label_39.text= self.gender_list[b]
        # self.label_40.text = (self.age_list[b])
        # self.label_41.text = self.dob_list[b]
        # self.label_44.text = self.mobile_list[b]
        # self.label_45.text = self.aadhar_list[b]
        # self.label_46.text = self.pan_list[b]
        # self.label_47.text = self.city_list[b]
        # self.label_48.text = self.email_user_list[b]
        # self.label_49.text = bool(self.last_confirm_list[b])
        # self.label_50.text = self.mobile_check_list[b]
        # self.label_51.text = self.mother_tongue_list[b]
        # self.label_52.text = self.mother_status_list[b]
        # #self.label_53.text = self.date_marrige_list[b]
        # self.label_54.text = self.space_name_list[b]

        # if self.space_name_list[b]:
        #   self.label_54.text = self.space_name_list[b]
        #   self.label_54.visible = True
        #   self.label_20.visible = True
        # else:
        #   self.label_54.visible =  False
        #   self.label_20.visible = False
        # self.label_61.text = self.about_list[b]
        # self.label_63.text = bool(self.alets_list[b])
        # self.label_72.text = bool(self.terms_list[b])
        # self.label_69.text = self.qualification_list[b]
        # self.label_62.text = self.address_type_list[b]
        # self.label_71.text = self.street_list[b]
        # self.label_64.text = self.build_name_list[b]
        # self.label_66.text = self.house_no_list[b]
        # self.label_65.text = self.landmark_list[b]
        # self.label_68.text = self.pincode_list[b]
        # self.label_70.text = self.state_list[b]
        # self.label_55.text = self.spouse_number_list[b]
        # self.label_56.text = self.company_name_list[b]
        # self.label_57.text = self.company_adress_list[b]
        # self.label_58.text =  self.proffic_list[b]
        # self.label_59.text = self.user_type_list[b]
        # self.label_60.text = bool(self.approve_list [b])
        # self.label_74.text = self.another_email[b]
        # self.label_76.text = self.company_name[b]
        # self.label_77.text = self.organization_type[b]
        # self.label_79.text = self.employment_type[b]
        # self.label_81.text = self.business_no[b]
        # self.label_83.text = self.company_landmark[b]
        # self.label_85.text = self.company_address[b]
        # self.label_87.text = self.annual_salary[b]
        # self.label_89.text = self.designation[b]
        # self.label_91.text = self.account_name[b]
        # self.label_93.text = self.account_type[b]
        # self.label_95.text = self.account_number[b]
        # self.label_97.text = self.account_bank_branch[b]
        # #self.label_99.text = self.ifsc_code[b]
        # self.label_101.text = self.salary_type[b]
        # #self.label_103.text = self.select_bank[b]
        # # self.label_105.text = self.net_bank[b]
        # self.label_107.text = self.father_name[b]
        # self.label_109.text = self.father_age[b]
        # self.label_111.text = self.mother_name[b]
        # self.label_113.text = self.mother_age[b]
        # self.label_115.text = self.college_name[b]
        # self.label_117.text = self.college_id[b]
        # self.label_119.text = self.college_address[b]
        # # self.label_121.text = self.running_loan[b]
        # self.image_2.source = self.profile[b]
        # self.image_3.source = self.aadhaar_photo[b]
        # self.image_4.source = self.pan_photo[b]
        # self.image_5.source = self.emp_id_proof[b]
        # self.image_6.source = self.last_six_month_bank_proof[b]
        # self.image_7.source = self.college_proof[b]

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    customer_id_value = self.label_3.text
    open_form('admin.dashboard.borrowers.view_profile.edit_form', customer_id_value)

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    customer_id_value = self.label_3.text
    open_form('admin.dashboard.borrowers.view_profile.update_form', customer_id_value)

  # def button_1_click(self, **event_args):
  #   """This method is called when the button is clicked"""
  #   open_form('admin.dashboard.borrowers')

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.borrowers')