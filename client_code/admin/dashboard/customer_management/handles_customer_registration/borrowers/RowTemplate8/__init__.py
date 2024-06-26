from ._anvil_designer import RowTemplate8Template
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate8(RowTemplate8Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    selected_row = self.item
    value_to_display = selected_row['customer_id']  # Replace 'some_key' with the appropriate key
    open_form('admin.dashboard.lenders.view_profile_copy', value_to_display=value_to_display)
