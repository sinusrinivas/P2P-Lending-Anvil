from ._anvil_designer import star_1_borrower_registration_form_3_maritalTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re
from datetime import datetime, timedelta

class star_1_borrower_registration_form_3_marital(star_1_borrower_registration_form_3_maritalTemplate):
  def __init__(self,user_id, **properties):
    # Set Form properties and Data Bindings.
    self.userId = user_id
    user_data=app_tables.fin_user_profile.get(customer_id=user_id)
    if user_data:
      self.marital_status_borrower_registration_dropdown.selected_value=user_data['marital_status']
      user_data.update()

    options = app_tables.fin_borrower_marrital_status.search()
    options_string = [str(option['borrower_marrital_status']) for option in options]
    self.marital_status_borrower_registration_dropdown.items = options_string

    # user_data=app_tables.fin_guarantor_details.get(customer_id=user_id)
    # if user_data:
    #   self.drop_down_1.selected_value = user_data['another_person']

    # self.drop_down_1.items = ['Father','Mother','Spouse','Others']
    self.init_components(**properties)

    # options = app_tables.fin_spouse_profession.search()
    # option_strings = [str(option['spouse_profession']) for option in options]
    # self.drop_down_1_copy.items = option_strings

    user_data=app_tables.fin_guarantor_details.get(customer_id=user_id)
    if user_data:
           self.drop_down_1.selected_value = user_data['another_person']
           self.father_name_text.text=user_data['guarantor_name']
           self.date_picker_1.date =user_data['guarantor_date_of_birth']
           self.father_mbl_no_text.text=user_data['guarantor_mobile_no']
           self.father_profession_text.text = user_data['guarantor_profession']
           self.father_address_text.text = user_data['guarantor_address']

           # self.drop_down_1.selected_value = user_data['another_person']
           self.spouse_name_text.text=user_data['guarantor_name']
           self.date_picker_3.date =user_data['guarantor_marriage_date']
           self.spouse_mbl_no_text.text=user_data['guarantor_mobile_no']
           self.drop_down_1_copy.selected_value = user_data['guarantor_profession']
           self.spouse_companyname_text.text = user_data['guarantor_company_name']
           self.annual_earning_text.text = user_data['guarantor_annual_earning']

    options = app_tables.fin_spouse_profession.search()
    option_strings = [str(option['spouse_profession']) for option in options]
    self.drop_down_1_copy.items = option_strings
    
    self.drop_down_1.items = ['Father','Mother','Spouse','Others']

    self.father_name_text.add_event_handler("change", self.validate_father_name)
    self.date_picker_1.add_event_handler("change", self.validate_father_dob)
    self.father_mbl_no_text.add_event_handler("change", self.validate_father_mbl_no)
    self.father_profession_text.add_event_handler("change", self.validate_father_profession)
    self.father_address_text.add_event_handler("change", self.validate_father_address)

    self.spouse_name_text.add_event_handler("change", self.validate_spouse_name)
    self.date_picker_3.add_event_handler("change", self.validate_spouse_dob)
    self.spouse_mbl_no_text.add_event_handler("change", self.validate_spouse_mbl_no)
    self.drop_down_1_copy.add_event_handler("change", self.validate_spouse_profession)
    # self.spouse_companyname_text.add_event_handler("change", self.validate_spouse_company)
    # self.annual_earning_text.add_event_handler("change", self.validate_annual_earning)

  def collect_details(self):
        # Collect details from the form
        father_name = self.father_name_text.text
        father_dob = self.date_picker_1.date
        father_mbl_no_text = self.father_mbl_no_text.text
        father_mbl_no = int(father_mbl_no_text) if father_mbl_no_text.strip().isdigit() else None
        father_profession = self.father_profession_text.text
        father_address = self.father_address_text.text

        # Spouse details
        spouse_name = self.spouse_name_text.text
        spouse_mob = self.date_picker_3.date
        spouse_mbl_no_text = self.spouse_mbl_no_text.text
        spouse_mbl_no = int(spouse_mbl_no_text) if spouse_mbl_no_text.strip().isdigit() else None
        spouse_profession = self.drop_down_1_copy.selected_value
        spouse_company = self.spouse_companyname_text.text
        anual_earning = self.annual_earning_text.text

        return {
            'father_name': father_name,
            'father_dob': father_dob,
            'father_mbl_no': father_mbl_no,
            'father_profession': father_profession,
            'father_address': father_address,
            'another_person' : self.drop_down_1.selected_value,
            'spouse_name': spouse_name,
            'spouse_mob': spouse_mob,
            'spouse_mbl_no': spouse_mbl_no,
            'spouse_profession': spouse_profession,
            'spouse_company': spouse_company,
            'annual_earning': anual_earning,

        }

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    open_form('bank_users.user_form')

  def button_next_click(self, **event_args):
      marital_status = self.marital_status_borrower_registration_dropdown.selected_value
      user_id = self.userId

      if not marital_status or marital_status not in ['Not Married', 'Married', 'Other']:
        Notification("Please select a valid marital status").show()
        return

      selected_value = self.drop_down_1.selected_value
    
      if selected_value in ['Father', 'Mother', 'Others']:
          details = self.collect_details()
          if details:
              # Extracting details from the form
              father_name = details.get('father_name', '')
              father_dob = details.get('father_dob', '')
              father_mbl_no = details.get('father_mbl_no', '')
              father_profession = details.get('father_profession', '')
              father_address = details.get('father_address', '')
              another_person = details.get('another_person', '')
      
              # Checking if the user already has data in the table
              existing_row = app_tables.fin_guarantor_details.get(customer_id=self.userId)
      
              try:
                  # If there's no existing data, add a new row
                  if existing_row is None:
                      new_row = app_tables.fin_guarantor_details.add_row(
                          customer_id=self.userId,
                          guarantor_name=father_name,
                          guarantor_date_of_birth=father_dob,
                          guarantor_mobile_no=father_mbl_no,
                          guarantor_profession=father_profession,
                          guarantor_address=father_address,
                          another_person=another_person
                      )
                  else:
                      # If there's existing data, update it
                      existing_row.update(
                          guarantor_name=father_name,
                          guarantor_date_of_birth=father_dob,
                          guarantor_mobile_no=father_mbl_no,
                          guarantor_profession=father_profession,
                          guarantor_address=father_address,
                          another_person=another_person
                      )
              except Exception as e:
                  Notification(f"Failed to submit form: {e}").show()
                  return
      
              # Validations...
              errors = []
              if not father_name:
                errors.append("Enter a valid full name!")
                self.father_name_text.focus()
              elif not re.match(r'^[A-Za-z\s]+$', father_name):
                errors.append("Enter a valid full name!")
                self.father_name_text.focus()
              elif not father_dob or father_dob > datetime.now().date():
                errors.append("Enter a valid date of birth!")
                self.date_picker_1.focus()
              elif (datetime.now().date() - father_dob).days < 365 * 18:
                errors.append("You must be at least 18 years old!")
                self.date_picker_1.focus()
              elif not father_mbl_no:
                errors.append("Enter a valid mobile no!")
                self.father_mbl_no_text.focus()
              elif not re.match(r'^\d{10}$', str(father_mbl_no)):
                errors.append("Enter a valid mobile no!")
                self.father_mbl_no_text.focus()
              elif not father_profession:
                errors.append("Enter a valid profession!")
                self.father_profession_text.focus()
              elif not father_address:
                errors.append("Enter a valid address!")
                self.father_address_text.focus()
      
              if errors:
                Notification("\n".join(errors)).show()
              else:
                  anvil.server.call('add_borrower_step3', marital_status, user_id)
                  anvil.server.call('add_lendor_father_details', 
                                    another_person, father_name, father_dob, 
                                    father_mbl_no, father_profession, 
                                    father_address, self.userId)
                  open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_4_loan', 
                            user_id=self.userId)
          else:
            Notification("Please fill all the required fields").show()

      elif selected_value == 'Spouse':
        details = self.collect_details()
        if details:
          spouse_name = details.get('spouse_name', '')
          spouse_mob = details.get('spouse_mob', '')
          spouse_mbl_no = details.get('spouse_mbl_no', '')
          spouse_profession = details.get('spouse_profession', '')
          spouse_company = details.get('spouse_company', '')
          annual_earning = details.get('annual_earning', '')
          another_person = details.get('another_person', '')
    
          # Validations
          errors = []
          if not spouse_name:
            errors.append("Enter a valid full name!")
            self.spouse_name_text.focus()
          elif not re.match(r'^[A-Za-z\s]+$', spouse_name):
            errors.append("Enter a valid full name!")
            self.spouse_name_text.focus()
          elif not spouse_mob or spouse_mob > datetime.now().date():
            errors.append("Enter a valid date of marriage!")
            self.date_picker_3.focus()
          elif not spouse_mbl_no:
            errors.append("Enter a valid mobile no!")
            self.spouse_mbl_no_text.focus()
          elif not re.match(r'^\d{10}$', str(spouse_mbl_no)):
            errors.append("Enter a valid mobile no!")
            self.spouse_mbl_no_text.focus()
          elif not spouse_profession:
            errors.append("Select a valid profession!")
            self.drop_down_1_copy.focus()
          # elif not spouse_company:
          #   errors.append("Enter a valid company name!")
          #   self.spouse_companyname_text.focus()
          # elif not annual_earning:
          #   errors.append("Enter a valid annual earning!")
          #   self.annual_earning_text.focus()
    
          if errors:
            Notification("\n".join(errors)).show()
            return
    
          existing_row = app_tables.fin_guarantor_details.get(customer_id=self.userId)
          
          try:
            if existing_row is None:
              new_row = app_tables.fin_guarantor_details.add_row(
                customer_id=self.userId,
                guarantor_name=spouse_name,
                guarantor_marriage_date=spouse_mob,
                guarantor_mobile_no=spouse_mbl_no,
                guarantor_profession=spouse_profession,
                guarantor_company_name=spouse_company,
                guarantor_annual_earning=annual_earning,
                another_person=another_person
              )
            else:
              existing_row.update(
                guarantor_name=spouse_name,
                guarantor_marriage_date=spouse_mob,
                guarantor_mobile_no=spouse_mbl_no,
                guarantor_profession=spouse_profession,
                guarantor_company_name=spouse_company,
                guarantor_annual_earning=annual_earning,
                another_person=another_person
              )
          except Exception as e:
            Notification(f"Failed to submit form: {e}").show()
            return
    
          anvil.server.call('add_borrower_step3', marital_status, self.userId)
          anvil.server.call('add_lendor_spouse_details',
                            another_person, spouse_name, spouse_mob,
                            spouse_mbl_no, spouse_profession,
                            spouse_company, annual_earning, self.userId)
          open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_4_loan', user_id=self.userId)
        else:
          Notification("Please fill all the required fields").show()
      else:
        alert('Please select a specific preference')
      
  
  def button_1_click(self, **event_args): 
    open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment',user_id=self.userId)

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    selected_value = self.drop_down_1.selected_value
    
    # Hide all panels initially
    self.column_panel_1.visible = False
    self.column_panel_2.visible = False

    # Set the visibility of grid panels based on the selected value
    if selected_value in ['Father', 'Mother', 'Others']:
        self.column_panel_1.visible = True
    elif selected_value == 'Spouse':
        self.column_panel_2.visible = True


    
    
  def validate_father_name(self, **event_args):
    father_name = self.father_name_text.text
    if not father_name or not re.match(r'^[A-Za-z\s]+$', father_name):
        self.father_name_text.background = 'red'
    else:
        self.father_name_text.background = 'white'

  def validate_father_dob(self, **event_args):
    father_dob = self.date_picker_1.date
    if not father_dob or father_dob > datetime.now().date() or (datetime.now().date() - father_dob).days < 365 * 18:
        self.date_picker_1.background = 'red'
    else:
        self.date_picker_1.background = 'white'

  def validate_father_mbl_no(self, **event_args):
    father_mbl_no = self.father_mbl_no_text.text
    if not father_mbl_no or not re.match(r'^\d{10}$', str(father_mbl_no)):
        self.father_mbl_no_text.background = 'red'
    else:
        self.father_mbl_no_text.background = 'white'

  def validate_father_profession(self, **event_args):
    father_profession = self.father_profession_text.text
    if not father_profession:
        self.father_profession_text.background = 'red'
    else:
        self.father_profession_text.background = 'white'

  def validate_father_address(self, **event_args):
    father_address = self.father_address_text.text
    if not father_address:
        self.father_address_text.background = 'red'
    else:
        self.father_address_text.background = 'white'
    

  def validate_spouse_name(self, **event_args):
    spouse_name = self.spouse_name_text.text
    if not spouse_name or not re.match(r'^[A-Za-z\s]+$', spouse_name):
        self.spouse_name_text.background = 'red'
    else:
        self.spouse_name_text.background = 'white'

  def validate_spouse_dob(self, **event_args):
    spouse_mob = self.date_picker_3.date
    if not spouse_mob or spouse_mob > datetime.now().date():
        self.date_picker_3.background = 'red'
    else:
        self.date_picker_3.background = 'white'

  def validate_spouse_mbl_no(self, **event_args):
    spouse_mbl_no = self.spouse_mbl_no_text.text
    if not spouse_mbl_no or not re.match(r'^\d{10}$', str(spouse_mbl_no)):
        self.spouse_mbl_no_text.background = 'red'
    else:
        self.spouse_mbl_no_text.background = 'white'

  def validate_spouse_profession(self, **event_args):
    spouse_profession = self.drop_down_1_copy.selected_value
    if not spouse_profession:
        self.drop_down_1_copy.background = 'red'
    else:
        self.drop_down_1_copy.background = 'white'

  # def validate_spouse_company(self, **event_args):
  #   spouse_company = self.spouse_companyname_text.text
  #   if not spouse_company:
  #       self.spouse_companyname_text.background = 'red'
  #   else:
  #       self.spouse_companyname_text.background = 'white'
        
  # def validate_annual_earning(self, **event_args):
  #   annual_earning = self.annual_earning_text.text
  #   if not annual_earning:
  #       self.annual_earning_text.background = 'red'
  #   else:
  #       self.annual_earning_text.background = 'white'