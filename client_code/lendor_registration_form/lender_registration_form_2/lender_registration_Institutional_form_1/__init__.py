from ._anvil_designer import lender_registration_Institutional_form_1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class lender_registration_Institutional_form_1(lender_registration_Institutional_form_1Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_data = anvil.server.call('get_user_data', user_id)
        
    if user_data:
            self.business_name = user_data.get('business_name', '')
            self.business_add = user_data.get('business_add', '')
            
            
    else:
        self.business_name = ''
        self.business_add = ''
            
    if self.business_name:
            self.text_box_1.text= self.business_name
    if self.business_add:
            self.text_box_2.text= self.business_add

  def button_2_click(self, **event_args):
    business_name = self.text_box_1.text
    business_add = self.text_box_2.text
    user_id = self.userId
    if not business_name or not business_add:
      Notification("Please fill all the fields").show()
    else:
      anvil.server.call('add_lendor_institutional_form_1',business_name,business_add,user_id)
      open_form('lendor_registration_form.lender_registration_form_2.lender_registration_Institutional_form_2',user_id=self.userId)

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.lender_registration_form_2',user_id=self.userId)
    """This method is called when the button is clicked"""

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")
    
