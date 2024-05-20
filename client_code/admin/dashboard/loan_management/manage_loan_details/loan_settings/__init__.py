from ._anvil_designer import loan_settingsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class loan_settings(loan_settingsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.current_entry_id = None

    # Display the latest loan settings when the form opens.
    self.display_latest_settings()
    # Any code you write here will run before the form opens.

  def save_button(self, **event_args):
    """This method is called when the button is clicked"""
    value1 = self.text_box_1.text
    value2 = self.text_box_2.text

    if self.current_entry_id:
      # Update the existing entry
      entry = app_tables.fin_loan_settings.get(self.current_entry_id)
      entry.update(
        minimum_days=value1,
        maximum_days=value2
      )
    else:
      # Insert new values into the fin_loan_settings table
      entry = app_tables.fin_loan_settings.add_row(
        minimum_days=value1,
        maximum_days=value2,
        loans="lapsed fee"
      )
      self.current_entry_id = entry.get_id()

    # Display the latest settings and make the text boxes non-editable
    self.display_latest_settings()

    # Optionally, display a success message
    alert("Loan settings saved successfully!")


  def display_latest_settings(self):
    """Fetch and display the latest loan settings based on 'lapsed fee'"""
    # Fetch the entry with loans set to 'lapsed fee' from the fin_loan_settings table
    latest_entry = app_tables.fin_loan_settings.get(loans="lapsed fee")
    if latest_entry:
      self.current_entry_id = latest_entry.get_id()
      self.text_box_1.text = latest_entry['minimum_days']
      self.text_box_2.text = latest_entry['maximum_days']
      self.text_box_1.enabled = False
      self.text_box_2.enabled = False
    else:
      self.current_entry_id = None
      self.text_box_1.text = ""
      self.text_box_2.text = ""
      self.text_box_1.enabled = True
      self.text_box_2.enabled = True

  def edit_button(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_1.enabled = True
    self.text_box_2.enabled = True
