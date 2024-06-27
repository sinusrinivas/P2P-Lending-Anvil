from ._anvil_designer import RowTemplate16Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate16(RowTemplate16Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    selcted_row=self.label_1.text
    value_to_display = self.label_1.text
    open_form('admin.dashboard.lenders.view_profile_copy',selected_row=selcted_row,value_to_display = value_to_display)
