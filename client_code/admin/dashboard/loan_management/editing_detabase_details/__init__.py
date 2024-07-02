from ._anvil_designer import editing_detabase_detailsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class editing_detabase_details(editing_detabase_detailsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.data_grid_1.role = self.scroll_into_view()
    self.repeating_panel_1.items = app_tables.fin_loan_details.search()
    self.repeating_panel_2.items = app_tables.fin_emi_table.search()
    self.repeating_panel_3.items = app_tables.fin_foreclosure.search()
    self.repeating_panel_4.items = app_tables.fin_extends_loan.search()
  
  def button_1_copy_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management')
    