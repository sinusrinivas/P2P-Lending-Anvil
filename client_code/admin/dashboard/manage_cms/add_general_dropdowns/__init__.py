from ._anvil_designer import add_general_dropdownsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class add_general_dropdowns(add_general_dropdownsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def gender_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_data = self.text_box_01.text
    new_row = app_tables.fin_gender.add_row(gender=entered_data)
    self.text_box_01.text = ' '
    self.refresh()
