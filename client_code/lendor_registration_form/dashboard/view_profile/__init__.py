from ._anvil_designer import view_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ....bank_users.main_form import main_form_module
class view_profile(view_profileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.email=main_form_module.email
    user_profile=app_tables.fin_user_profile.get(email_user=self.email)
    if user_profile:
      self.full_name.text=user_profile['full_name']
      self.email_id.text=user_profile['email_user']
      self.mobile.text=user_profile['mobile']
      self.gender.text=user_profile['gender']
      self.date_of_birth.text=user_profile['date_of_birth']
      self.ad_number.text=user_profile['aadhaar_no']
      self.pan_number.text=user_profile['pan_number']
   
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard")



