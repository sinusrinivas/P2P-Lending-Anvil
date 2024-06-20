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
  def __init__(self,selected_row, **properties):
    self.init_components(**properties)

    self.selected_row = selected_row
    self.id = selected_row['customer_id']

    user_profile=app_tables.fin_user_profile.get(customer_id=self.id)
    self.image_1.source = user_profile['user_photo']
    self.label_6.text=user_profile['present_address']
    customer_details=app_tables.fin_reported_problems.get(customer_id=self.id)
    self.label_2.text=customer_details['name']
    self.label_4.text=customer_details['mobile_number']
    self.label_8.text=customer_details['category']
    self.label_10.text=customer_details['subcategory']
    self.label_13.text=customer_details['']
    
    
    
   
    

  def button_1_click(self, **event_args):
    open_form('admin.dashboard.manage_cms.manage_issues')

