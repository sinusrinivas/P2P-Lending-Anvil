from ._anvil_designer import ItemTemplate82Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate82(ItemTemplate82Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        item = self.item  # Get the item associated with the button
        
        if item is not None:
            # Update the status column to indicate the problem is solved
            item['status'] = True  # Replace 'status' with the actual column name
            alert('Problem solved.')
            open_form('admin.dashboard.manage_issues')
        else:
            alert('Please select a problem to mark as solved.')