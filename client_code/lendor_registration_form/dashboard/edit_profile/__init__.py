from ._anvil_designer import edit_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ....bank_users.main_form import main_form_module
class edit_profile(edit_profileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.email=main_form_module.email
    user_profile=app_tables.fin_user_profile.get(email_user=self.email)
    if user_profile:
      self.text_box_1.text=user_profile['full_name']
      self.text_box_2.text=user_profile['email_user']
      self.text_box_3.text=user_profile['mobile']
      
      options = app_tables.fin_gender.search()
      options_string = [str(option['gender']) for option in options]
      self.drop_down_1.items = options_string
      
      self.label_9.text=user_profile['date_of_birth']
      self.ad_number.text=user_profile['aadhaar_no']
      self.pan_number.text=user_profile['pan_number']
      
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard")

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    user_profile=app_tables.fin_user_profile.get(email_user=self.email)
    if user_profile: 
     user_profile['full_name']=self.text_box_1.text
     user_profile['email_user']=self.text_box_2.text
     user_profile['mobile']=self.text_box_3.text
     user_profile['date_of_birth']=self.label_9.text
     # user_profile['city']=self.city_text.text
     user_profile['pan_number']=self.pan_number.text
     user_profile['gender']=self.drop_down_1.selected_value
     user_profile['aadhaar_no']=self.ad_number.text
     user_profile.update()
    alert('saved sucessfully')
    open_form('lendor_registration_form.dashboard')

  