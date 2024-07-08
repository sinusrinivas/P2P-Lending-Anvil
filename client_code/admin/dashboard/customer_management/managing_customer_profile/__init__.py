from ._anvil_designer import managing_customer_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class managing_customer_profile(managing_customer_profileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

        # Load the customer data from the data tables
    self.load_customer_data()

  def load_customer_data(self):
    # Fetch the customer data from the data tables
    # user_profile = app_tables.fin_user_profile.search()
     combined_data = anvil.server.call('get_combined_user_and_guarantor_data')
     # user_profile = anvil.server.call('get_filtered_user_profiles')
     self.repeating_panel_1.items = combined_data
    # gurantor = app_tables.fin_guarantor_details.search()
    # Set the items property of the repeating panel to the fetched data

  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.customer_management')


