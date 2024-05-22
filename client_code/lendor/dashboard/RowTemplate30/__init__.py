from ._anvil_designer import RowTemplate30Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# from .. import main_form_module

class RowTemplate30(RowTemplate30Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.user_id = main_form_module.userId

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    selcted_row=self.item
    open_form('lendor.dashboard.view_details_1_copy',selected_row=selcted_row)

  def link_2_click(self, **event_args):
      selcted_row=self.item
      open_form("lendor.dashboard.view_borrower_loan_request.Borr_loan_request", selected_row=selcted_row)
    