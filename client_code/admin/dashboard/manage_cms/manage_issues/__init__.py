from ._anvil_designer import manage_issuesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class manage_issues(manage_issuesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    #items = [row for row in app_tables.fin_reported_problems.search() if row['email']]
    #self.repeating_panel_1.items = items
        
    #if not items:
        #self.label_no_issues.visible = True
    #else:
        #self.label_no_issues.visible = False
    self.repeating_panel_1.items = app_tables.fin_reported_problems.search()

  def button_1_click(self, **event_args):
    open_form('admin.dashboard.manage_cms')
