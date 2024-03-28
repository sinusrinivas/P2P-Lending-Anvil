from ._anvil_designer import star_1_borrower_registration_form_3_marital_marriedTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re
from datetime import datetime, timedelta

class star_1_borrower_registration_form_3_marital_married(star_1_borrower_registration_form_3_marital_marriedTemplate):
    selected_radio_button = None
    def __init__(self, user_id, marital_status, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.userId = user_id

         #self.userId = user_id
        self.marital_status = marital_status

        # Set the visibility of the spouse controls based on the marital status
        if marital_status == 'Married':
            self.show_spouse_controls()
            self.button_1.visible = True
        else:
            self.hide_spouse_controls()
            self.button_1_3.visible = False
            self.button_1.visible = True

        options = app_tables.fin_spouse_profession.search()
        option_strings = [str(option['spouse_profession']) for option in options]
        self.drop_down_1.items = option_strings

    def show_spouse_controls(self):
        # Show the spouse radio button and related panels
        self.grid_panel_1.visible = False
        self.grid_panel_2.visible = False
        self.grid_panel_3.visible = False
        self.grid_panel_4.visible = False
        self.button_submit.visible = False
        self.button_submit_copy.visible = False
        self.button_submit_copy_2.visible = False
        self.button_submit_copy_3.visible = False
        self.prev_1.visible = False
        self.prev_2.visible = False
        self.prev_3.visible = False
        self.prev_4.visible = False
        self.button_1.visible = False

    def hide_spouse_controls(self):
        # Hide the spouse radio button and related panels
        self.grid_panel_1.visible = False
        self.grid_panel_2.visible = False
        self.grid_panel_3.visible = False
        self.grid_panel_4.visible = False
        self.button_submit.visible = False
        self.button_submit_copy.visible = False
        self.button_submit_copy_2.visible = False
        self.button_submit_copy_3.visible = False
        self.prev_1.visible = False
        self.prev_2.visible = False
        self.prev_3.visible = False
        self.prev_4.visible = False
        self.button_1.visible = False
    def is_married(self):
        # Check the marital status in the user profile table
        user_profile = app_tables.fin_user_profile.get(customer_id=self.userId)
        return user_profile['marital_status'] == 'Married'
  
    def button_1_click(self, **event_args):
        open_form('borrower_registration_form.star_1_borrower_registration_form_3_marital', user_id=self.userId)

    def button_1_1_click(self, **event_args):
        """This method is called when this radio button is selected"""
        self.button_1_1.background = '#0a2346'
        self.button_1_2.background = '#939191'
        self.button_1_3.background = '#939191'
        self.button_1_4.background = '#939191'
        self.grid_panel_1.visible = True
        self.grid_panel_2.visible = False
        self.grid_panel_3.visible = False
        self.grid_panel_4.visible = False
        self.button_submit.visible = True
        self.button_submit_copy.visible = False
        self.button_submit_copy_2.visible = False
        self.button_submit_copy_3.visible = False
        self.selected_radio_button = "father"
        self.prev_1.visible = True
        self.prev_2.visible = False
        self.prev_3.visible = False
        self.prev_4.visible = False
        self.button_1.visible = False

    def button_1_2_click(self, **event_args):
        """This method is called when this radio button is selected"""
        self.button_1_1.background = '#939191'
        self.button_1_2.background = '#0a2346'
        self.button_1_3.background = '#939191'
        self.button_1_4.background = '#939191'
        self.grid_panel_1.visible = False
        self.grid_panel_2.visible = True
        self.grid_panel_3.visible = False
        self.grid_panel_4.visible = False
        self.button_submit.visible = False
        self.button_submit_copy.visible = True
        self.button_submit_copy_2.visible = False
        self.button_submit_copy_3.visible = False
        self.selected_radio_button = "Mother"
        self.prev_1.visible = False
        self.prev_2.visible = True
        self.prev_3.visible = False
        self.prev_4.visible = False
        self.button_1.visible = False
      
    def button_1_3_click(self, **event_args):
        self.button_1_1.background = '#939191'
        self.button_1_2.background = '#939191'
        self.button_1_3.background = '#0a2346'
        self.button_1_4.background = '#939191'
        self.grid_panel_1.visible = False
        self.grid_panel_2.visible = False
        self.grid_panel_3.visible = True
        self.grid_panel_4.visible = False
        self.button_submit.visible = False
        self.button_submit_copy.visible = False
        self.button_submit_copy_2.visible = True
        self.button_submit_copy_3.visible = False
        self.selected_radio_button = "spouse"
        self.prev_1.visible = False
        self.prev_2.visible = False
        self.prev_3.visible = True
        self.prev_4.visible = False
        self.button_1.visible = False
    
    def button_1_4_click(self, **event_args):
        """This method is called when this radio button is selected"""
        self.button_1_1.background = '#939191'
        self.button_1_2.background = '#939191'
        self.button_1_3.background = '#939191'
        self.button_1_4.background = '#0a2346'
        self.grid_panel_1.visible = False
        self.grid_panel_2.visible = False
        self.grid_panel_3.visible = False
        self.grid_panel_4.visible = True
        self.button_submit.visible = False
        self.button_submit_copy.visible = False
        self.button_submit_copy_2.visible = False
        self.button_submit_copy_3.visible = True
        self.selected_radio_button = "others"
        self.prev_1.visible = False
        self.prev_2.visible = False
        self.prev_3.visible = False
        self.prev_4.visible = True
        self.button_1.visible = False

    def collect_details(self):
        # Collect details from the form
        father_name = self.father_name_text.text
        father_dob = self.date_picker_1.date
        father_mbl_no_text = self.father_mbl_no_text.text
        father_mbl_no = int(father_mbl_no_text) if father_mbl_no_text.strip().isdigit() else None
        father_profession = self.father_profession_text.text
        father_address = self.father_address_text.text

        # Mother details
        mother_name = self.mother_name_text_copy.text
        mother_dob = self.date_picker_2.date
        mother_mbl_no_text = self.mother_mbl_no_text.text
        mother_mbl_no = int(mother_mbl_no_text) if mother_mbl_no_text.strip().isdigit() else None
        mother_profession = self.mother_profession_text.text
        mother_address = self.mother_address_text.text

        # Spouse details
        spouse_name = self.spouse_name_text.text
        spouse_dob = self.date_picker_3.date
        spouse_mbl_no_text = self.spouse_mbl_no_text.text
        spouse_mbl_no = int(spouse_mbl_no_text) if spouse_mbl_no_text.strip().isdigit() else None
        spouse_profession = self.drop_down_1.selected_value
        spouse_company = self.spouse_companyname_text.text
        anual_earning = self.annual_earning_text.text

        # Related person details
        person_relation = self.related_person_text.text
        related_dob = self.date_picker_3_copy.date
        related_name = self.name_text_copy.text
        related_mob_text = self.mbl_no_text_copy.text
        related_mob = int(related_mob_text) if related_mob_text.strip().isdigit() else None
        related_profession = self.profession_text_copy.text

        # Return the collected details as a dictionary
        return {
            'father_name': father_name,
            'father_dob': father_dob,
            'father_mbl_no': father_mbl_no,
            'father_profession': father_profession,
            'father_address': father_address,

            'mother_name': mother_name,
            'mother_dob': mother_dob,
            'mother_mbl_no': mother_mbl_no,
            'mother_profession': mother_profession,
            'mother_address': mother_address,

            'spouse_name': spouse_name,
            'spouse_dob': spouse_dob,
            'spouse_mbl_no': spouse_mbl_no,
            'spouse_profession': spouse_profession,
            'spouse_company': spouse_company,
            'annual_earning': anual_earning,

            'related_person_relation': person_relation,
            'related_person_dob': related_dob,
            'related_person_name': related_name,
            'related_person_mob': related_mob,
            'related_person_profession': related_profession,
            'another_person': self.selected_radio_button 
        }

    def button_submit_click(self, guarantor_type, **event_args):
      """ This method is called when the button is clicked to submit guarantor details.

      Args:
      guarantor_type (str): The type of guarantor (e.g., "father", "mother", "spouse", "related_person")
      """
      details = self.collect_details()

      if not self.validate_guarantor_details(details):
        return

      # Update existing guarantor details based on guarantor_type
      existing_rows = app_tables.fin_guarantor_details.filter(customer_id=self.userId, guarantor_type=guarantor_type)
      if existing_rows:
         existing_row = existing_rows[0]
         # Update specific fields based on guarantor_type
         self.update_guarantor_fields(existing_row, details, guarantor_type)
         existing_row.update()
      else:
        details["guarantor_type"] = guarantor_type
        app_tables.fin_guarantor_details.add_row(**details)

      open_form('borrower_registration_form.star_1_borrower_registration_form_4_loan', user_id=self.userId)

    def validate_guarantor_details(self, details):
      errors = []
      if not re.match(r'^[A-Za-z\s]+$', details['father_name']):
        errors.append("Enter a valid full name!")
      if not details['father_dob'] or details['father_dob'] > datetime.now().date():
        errors.append("Enter a valid date of birth!")
      elif datetime.now().date() - details['father_dob'] < timedelta(days=365 * 18):
        errors.append("You must be at least 18 years old!")
      if not re.match(r'^\d{10}$', str(details['father_mbl_no'])):
        errors.append("Enter a valid mobile number (10 digits)!")
      if not all(details[key] for key in ['father_name', 'father_dob', 'father_mbl_no', 'father_profession', 'father_address']):
        errors.append("Please fill all the required fields")

      if errors:
        self.show_notification("\n".join(errors))  # Combine errors into a single message
        return False  # Indicate validation failure
      return True  # Indicate validation success

    def update_guarantor_fields(self, guarantor_row, details, guarantor_type):
      """ Updates specific guarantor fields based on the guarantor type.

      Args:
      guarantor_row (object): The existing guarantor row object.
      details (dict): The guarantor details dictionary.
      guarantor_type (str): The type of guarantor.
  """
  mapping = {
      "father": ["guarantor_name", "guarantor_date_of_birth", "guarantor_mobile_no",
                 "guarantor_profession", "guarantor_address"],
      "mother": ["guarantor_name", "guarantor_date_of_birth", "guarantor_mobile_no",
                 "guarantor_profession", "guarantor_address"],
      "spouse": ["guarantor_name", "guarantor_date_of_birth", "guarantor_mobile_no",
                 "guarantor_profession", "guarantor_company_name", "guarantor_annual_earning"],
      "related_person": ["guarantor_name", "guarantor_date_of_birth", "guarantor_mobile_no",
                          "guarantor_profession", "guarantor_person_relation"],
  }
  # Update relevant fields based on the mapping
  for field in mapping[guarantor_type]:
    setattr(guarantor_row, field, details[field])

    # def button_submit_click(self, **event_args):
    #    details = self.collect_details()

    #    existing_rows = app_tables.fin_guarantor_details.get(customer_id=self.userId)

    #    if existing_rows:
    #      existing_row = existing_rows[0]
    #      existing_row.guarantor_name = details['father_name']
    #      existing_row.guarantor_date_of_birth = details['father_dob']
    #      existing_row.guarantor_mobile_no = details['father_mbl_no']
    #      existing_row.guarantor_profession = details['father_profession']
    #      existing_row.guarantor_address = details['father_address']
    #      existing_row.another_person = details['another_person']
    #      existing_row.update()
    #    else:
    #       app_tables.fin_guarantor_details.add_row(
    #         customer_id=self.userId,
    #         guarantor_name=details['father_name'],
    #         guarantor_date_of_birth=details['father_dob'],
    #         guarantor_mobile_no=details['father_mbl_no'],
    #         guarantor_profession=details['father_profession'],
    #         guarantor_address=details['father_address'],
    #         another_person=details['another_person']
    #       )

    #    if not re.match(r'^[A-Za-z\s]+$', details['father_name']):
    #       Notification("Enter a valid full name!").show()
    #    elif not details['father_dob'] or details['father_dob'] > datetime.now().date():
    #       Notification("Enter a valid date of birth!").show()
    #    elif datetime.now().date() - details['father_dob'] < timedelta(days=365 * 18):
    #       Notification("You must be at least 18 years old!").show()
    #    elif not re.match(r'^\d{10}$', str(details['father_mbl_no'])):
    #       self.mbl_label_1.text = 'Enter valid mobile no'

    #    if not all(details[key] for key in ['father_name', 'father_dob', 'father_mbl_no', 'father_profession', 'father_address']):
    #       Notification("Please fill all the required fields").show()
    #    else:
    #       open_form('borrower_registration_form.star_1_borrower_registration_form_4_loan', user_id=self.userId)

    # def button_submit_copy_click(self, **event_args):
    #   """This method is called when the button is clicked"""
    #   details = self.collect_details()
  
    #   existing_rows = app_tables.fin_guarantor_details.get(customer_id=self.userId)
    
    #   if existing_rows:
    #      existing_row = existing_rows[0]
    #      existing_row.guarantor_name = details['mother_name']
    #      existing_row.guarantor_date_of_birth = details['mother_dob']
    #      existing_row.guarantor_mobile_no = details['mother_mbl_no']
    #      existing_row.guarantor_profession = details['mother_profession']
    #      existing_row.guarantor_address = details['mother_address']
    #      existing_row.another_person = details['another_person']
    #      existing_row.update()
    #   else:
    #      app_tables.fin_guarantor_details.add_row(
    #         customer_id=self.userId,
    #         guarantor_name=details['mother_name'],
    #         guarantor_date_of_birth=details['mother_dob'],
    #         guarantor_mobile_no=details['mother_mbl_no'],
    #         guarantor_profession=details['mother_profession'],
    #         guarantor_address=details['mother_address'],
    #         another_person=details['another_person']
    #      )
        
    #   if not re.match(r'^[A-Za-z\s]+$', details['mother_name']):
    #     Notification("Enter a valid full name!").show()
    #   elif not details['mother_dob'] or details['mother_dob'] > datetime.now().date():
    #     Notification("Enter a valid date of birth!").show()
    #   elif datetime.now().date() - details['mother_dob'] < timedelta(days=365 * 18):
    #     Notification("You must be at least 18 years old!")
    #   elif not re.match(r'^\d{10}$', str(details['mother_mbl_no'])):
    #     self.mbl_label_1.text = 'Enter valid mobile no'

    #   if not all(details[key] for key in ['mother_name', 'mother_dob', 'mother_mbl_no', 'mother_profession', 'mother_address']):
    #     Notification("Please fill all the required fields").show()
    #   else:
    #     open_form('borrower_registration_form.star_1_borrower_registration_form_4_loan', user_id=self.userId)

    # def button_submit_copy_2_click(self, **event_args):
    #     """This method is called when the button is clicked"""
    #     details = self.collect_details()

    #     existing_rows = app_tables.fin_guarantor_details.get(customer_id=self.userId)

    #     if existing_rows:
    #       existing_row = existing_rows[0]
    #       existing_row.guarantor_name = details['spouse_name']
    #       existing_row.guarantor_date_of_birth = details['spouse_dob']
    #       existing_row.guarantor_mobile_no = details['spouse_mbl_no']
    #       existing_row.guarantor_profession = details['spouse_profession']
    #       existing_row.guarantor_company_name = details['spouse_company']
    #       existing_row.guarantor_annual_earning = details['annual_earning']
    #       existing_row.another_person = details['another_person']
    #       existing_row.update()
    #     else:
    #        app_tables.fin_guarantor_details.add_row(
    #          customer_id=self.userId,
    #          guarantor_name=details['spouse_name'],
    #          guarantor_date_of_birth=details['spouse_dob'],
    #          guarantor_mobile_no=details['spouse_mbl_no'],
    #          guarantor_profession=details['spouse_profession'],
    #          guarantor_company_name=details['spouse_company'],
    #          guarantor_annual_earning=details['annual_earning'],
    #          another_person=details['another_person']
    #        )
          
    #     if not re.match(r'^[A-Za-z\s]+$', details['spouse_name']):
    #         alert("Enter a valid full name!", title="Error")
    #         return
    #     elif not details['spouse_dob'] or details['spouse_dob'] > datetime.now().date():
    #         alert("Enter a valid date of birth!", title="Error")
    #         return
    #     elif datetime.now().date() - details['spouse_dob'] < timedelta(days=365 * 18):
    #         alert("You must be at least 18 years old!", title="Error")
    #         return
    #     elif not re.match(r'^\d{10}$', str(details['spouse_mbl_no'])):
    #         self.mbl_label_1.text = 'Enter valid mobile no'

    #     if not all(details[key] for key in ['spouse_name', 'spouse_dob', 'spouse_mbl_no', 'spouse_profession']):
    #       Notification("Please fill all the required fields").show()
    #     else:
    #       open_form('borrower_registration_form.star_1_borrower_registration_form_4_loan',user_id=self.userId)

    # def button_submit_copy_3_click(self, **event_args):
    #     """This method is called when the button is clicked"""
    #     details = self.collect_details()
    #     existing_rows = app_tables.fin_guarantor_details.get(customer_id=self.userId)
    #     if existing_rows:
    #       existing_row = existing_rows[0]
    #       existing_row.guarantor_name = details['mother_name']
    #       existing_row.guarantor_date_of_birth = details['mother_dob']
    #       existing_row.guarantor_mobile_no = details['mother_mbl_no']
    #       existing_row.guarantor_profession = details['mother_profession']
    #       existing_row.guarantor_address = details['mother_address']
    #       existing_row.another_person = details['another_person']
    #       existing_row.update()
    #     else:
    #       app_tables.fin_guarantor_details.add_row(
    #         customer_id=self.userId,
    #         guarantor_name=details['related_person_name'],
    #         guarantor_date_of_birth=details['related_person_dob'],
    #         guarantor_mobile_no=details['related_person_mob'],
    #         guarantor_profession=details['related_person_profession'],
    #         guarantor_person_relation= details['related_person_relation'],
    #         another_person=details['another_person']
    #       )        

    #     if not re.match(r'^[A-Za-z\s]+$', details['related_person_name']):
    #         alert("Enter a valid full name!", title="Error")
    #         return
    #     elif not details['related_person_dob'] or details['related_person_dob'] > datetime.now().date():
    #         alert("Enter a valid date of birth!", title="Error")
    #         return
    #     elif datetime.now().date() - details['related_person_dob'] < timedelta(days=365 * 18):
    #         alert("You must be at least 18 years old!", title="Error")
    #         return
    #     elif not re.match(r'^\d{10}$', str(details['related_person_mob'])):
    #         self.mbl_label_1.text = 'Enter valid mobile no'

    #     if not all(details[key] for key in ['related_person_name', 'related_person_dob', 'related_person_mob', 'related_person_profession', 'related_person_relation']):
    #       Notification("Please fill all the required fields").show()
    #     else:
    #         open_form('borrower_registration_form.star_1_borrower_registration_form_4_loan',user_id=self.userId)

    def prev_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('borrower_registration_form.star_1_borrower_registration_form_3_marital', user_id=self.userId)

    def prev_2_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('borrower_registration_form.star_1_borrower_registration_form_3_marital', user_id=self.userId)

    def prev_3_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('borrower_registration_form.star_1_borrower_registration_form_3_marital', user_id=self.userId)

    def prev_4_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('borrower_registration_form.star_1_borrower_registration_form_3_marital', user_id=self.userId)
