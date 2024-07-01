from ._anvil_designer import RowTemplate66Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate66(RowTemplate66Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.editing = False

    # Any code you write here will run before the form opens.
    self.refresh_data_bindings()

  # def edit_button_click(self, **event_args):
  #   """This method is called when the edit button is clicked"""
  #   self.editing = True
  #   self.refresh_data_bindings()

  def save_button_click(self, **event_args):
    """This method is called when the save button is clicked"""
    # Save changes to the database here if necessary
    app_tables.fin_loan_details.update(self.item)
    # self.editing = False
    self.refresh_data_bindings()

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called before the data bindings are refreshed"""
    # Custom logic to handle the editable state
    if self.editing:
      self.date_picker_1.enabled = True
      # self.date_picker_2.enabled = True
    else:
      self.date_picker_1.enabled = False
      # self.date_picker_2.enabled = False