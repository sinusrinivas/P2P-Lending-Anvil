from ._anvil_designer import ots_dashboardTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ots_dashboard(ots_dashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_main_form_link_click(self, **event_args):
    open_form("borrower_registration_form.dashboard")

  def about_main_form_link_click(self, **event_args):
    open_form('borrower_registration_form.dashboard.dashboard_about')

  def contact_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("borrower_registration_form.dashboard.dashboard_contact")

  def notification_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('lender_registration_form.dashboard.notification')

  def wallet_dashboard_link_click(self, **event_args):
        user_profiles = server.call('fetch_user_profiles')
        
        for profile in user_profiles:
            result = server.call(
                'create_wallet_entry',
                profile['email_user'],
                profile['customer_id'],
                profile['full_name'],
                profile['usertype']
            )
            
            print(result)
        
        open_form('wallet.wallet')
        
        customer_id = 1000
        email = self.email
        anvil.server.call('fetch_profile_data_and_insert', email, customer_id)

  def button_4_click(self, **event_args):
    open_form('borrower_registration_form.ots_dashboard.my_loans')

