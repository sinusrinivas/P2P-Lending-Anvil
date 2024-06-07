from ._anvil_designer import lender_revenue_shareTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import open_form



class lender_revenue_share(lender_revenue_shareTemplate):
  def __init__(self, selected_row, **properties):
    self.selected_row = selected_row
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
