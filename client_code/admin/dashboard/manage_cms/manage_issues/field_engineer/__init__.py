from ._anvil_designer import field_engineerTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class field_engineer(field_engineerTemplate):
  def __init__(self,main_form_module, **properties):

    self.user_id=main_form_module.userId 
    self.init_components(**properties)

    user_profile=app_tables.fin_user_profile.get(customer_id=self.user_id)
    if user_profile: 
      self.label_2.text=user_profile['full_name']
      self.label_4.text=user_profile['mobile']
      self.label_6.text=user_profile['present_address']
      self.label_8.text=user_profile['date_of_birth']
      self.city.text=user_profile['city']
   
    

  def button_1_click(self, **event_args):
    open_form('admin.dashboard.manage_cms.manage_issues')

