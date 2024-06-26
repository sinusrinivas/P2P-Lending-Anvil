from ._anvil_designer import kyc_verificationTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class kyc_verification(kyc_verificationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.load_kyc_data()

  def load_kyc_data(self):
    
     # Fetch data from the server
    combined_data = anvil.server.call('get_combined_user_and_guarantor_data_2')

    # Debug: Print the fetched data
    print("Fetched user profiles:", combined_data)
    
    # Bind the data to the DataGrid
    self.repeating_panel_1.items = combined_data
    #combined_data

  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.customer_management')
