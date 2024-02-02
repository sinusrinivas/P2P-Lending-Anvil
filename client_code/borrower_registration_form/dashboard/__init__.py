from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...bank_users.main_form import main_form_module
from ...bank_users.user_form import user_module

class dashboard(dashboardTemplate):
    def __init__(self, **properties):
        email = main_form_module.email
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self.email = main_form_module.email

        # Fetch the user profile based on the current user's email
        user = anvil.users.get_user()
        # Check if a user is logged in
        if user:
            # Fetch the user profile record based on the current user's email
            user_profile = app_tables.fin_user_profile.get(email_user=user['email'])
            # Check if the user profile record is found
            if user_profile:
                # Access the user ID from the user profile record
                user_id = user_profile['customer_id']
                # Filter loan_details table based on the current user's ID
                try:
                    customer_loans = app_tables.fin_loan_details.search(borrower_customer_id=user_id)
                    print(len(customer_loans))
                except anvil.tables.NoSuchRow:
                    customer_loans = []  # Handle the case when no row is found
                    alert("No data found")

                # Check if the user has at least 3 loans
                if len(customer_loans) > 3:
                    self.extended_loans.visible = True
                else:
                    self.extended_loans.visible = False


    def home_main_form_link_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form("borrower_registration_form.dashboard")

    def login_signup_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        alert("Logged out successfully")
        anvil.users.logout()
        open_form('bank_users.main_form')

    def button_3_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower_registration_form.dashboard.borrower_profile')

    def button_4_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower_registration_form.dashboard.new_loan_request')

    def button_6_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower_registration_form.dashboard.view_loans')

    def outlined_button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower_registration_form.dashboard.today_dues')

    def outlined_button_3_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower_registration_form.dashboard.application_tracker')

    def outlined_button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower_registration_form.dashboard.foreclosure_request')

    def outlined_button_6_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower_registration_form.dashboard.discount_coupons')

    def outlined_button_7_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower.view_portfolio')

    def about_main_form_link_click(self, **event_args):
        """This method is called when the link is clicked"""
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

    def extended_loans_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('borrower_registration_form.dashboard.extension_loan_request')

