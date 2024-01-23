from ._anvil_designer import add_borrower_dropdown_detailsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class add_borrower_dropdown_details(add_borrower_dropdown_detailsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh()

    # Any code you write here will run before the form opens.

  def gender_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # self.text_box_1.text = ""
    value1 = self.text_box_1.text
    anvil.server.call('add_to_database',value1,None)
    self.text_box_1.text = ''
    self.refresh()
    
  def marital_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    value2 = self.text_box_2.text
    anvil.server.call('add_to_database',None,value2)
    self.text_box_2.text = ' '
    self.refresh()
    
  def refresh(self):
        """Refresh repeating panels with the latest data"""
        self.repeating_panel_1.items = app_tables.fin_borrower_manage_dropdown.search()
        self.repeating_panel_2.items = app_tables.fin_borrower_manage_dropdown.search()