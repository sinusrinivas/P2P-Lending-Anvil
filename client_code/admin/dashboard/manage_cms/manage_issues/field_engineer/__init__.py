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
    self.data = app_tables.fin_reported_problems.search()
    self.address = app_tables.fin_urser_profile.search
   
    for i in self.data:
      if selected_row in self.data(i['email']):
        self.label_2.text = self.data(i['name'])
        self.label_4.text = self.data(i['mobile_number'])
        self.label_6.text = self.data(i['issue_description'])
        self.label_8.text = 

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('admin.dashboard.manage_cms.manage_issues')

