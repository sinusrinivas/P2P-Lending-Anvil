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
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.selected_row = selected_row
    print(self.selected_row)
    #cust_id = app_tables.fin_user_profile.search()

  #if selected_row in cust
    

  def button_1_click(self, **event_args):
    open_form('admin.dashboard.manage_cms.manage_issues')

