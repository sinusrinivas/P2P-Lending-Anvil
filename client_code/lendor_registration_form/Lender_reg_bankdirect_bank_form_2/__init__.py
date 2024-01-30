from ._anvil_designer import Lender_reg_bankdirect_bank_form_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_bankdirect_bank_form_2(Lender_reg_bankdirect_bank_form_2Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_data = anvil.server.call('get_user_data', user_id)
    if user_data:
            self.ifsc = user_data.get('ifsc_code', '')
            self.salary_type = user_data.get('salary_type', '')
            self.branch_name = user_data.get('branch_name', '')
            
            
            
    else:
        self.ifsc = ''
        self.salary_type = ''
        self.branch_name = ''

       #Restore previously entered data if available
    if self.ifsc:
            self.text_box_1.text= self.ifsc
    if self.salary_type:
            self.drop_down_1.selected_value = self.salary_type
    if self.branch_name:
          self.text_box_2.text = self.branch_name

    options = app_tables.fin_lendor_manage_dropdown.search()
    options_string =[str(option['salary_type']) for option in options]
    self.drop_down_1.items = options_string

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    user_id = self.userId
    ifsc = self.text_box_1.text
    salary_type = self.drop_down_1.selected_value
    branch_name = self.text_box_2.text
    user_id = self.userId
    if not ifsc or not salary_type or not branch_name:
      Notification("please fill all required fields").show()
    else:
      anvil.server.call('add_lendor_bank_details_form_2', ifsc,salary_type,branch_name, user_id)
      open_form('lendor_registration_form.dashboard')

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_bothdirect_bank_form_1',user_id=self.userId)

  def button_3_click(self, **event_args):
    open_form("bank_users.user_form")
    
  def link_1_copy_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert('Agreements, Privacy Policy and Applicant should accept following:Please note that any information concealed (as what we ask for), would be construed as illegitimate action on your part and an intentional attempt to hide material information which if found in future, would attract necessary action (s) at your sole cost. Hence, request to be truthful to your best knowledge while sharing your details)')

  def check_box_1_copy_3_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    self.accepted_terms = self.check_box_1_copy_3.checked
    self.button_2.enabled = self.accepted_terms
