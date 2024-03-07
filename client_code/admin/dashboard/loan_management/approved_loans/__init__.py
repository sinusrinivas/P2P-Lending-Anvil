from ._anvil_designer import approved_loansTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class approved_loans(approved_loansTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Retrieve loan details from the database
        loan_details = app_tables.fin_loan_details.search()

        # Initialize lists to store loan details
        self.loan_ids = []
        self.borrower_customer_ids = []
        self.borrower_full_names = []
        self.loan_statuses = []
        self.lender_full_names = []
        self.lender_customer_ids = []
        self.interest_rates = []
        self.tenures = []
        self.loan_amounts = []
        self.lender_accepted_timestamps = []

        # Iterate through the loan details
        for loan in loan_details:
            # Append loan details to respective lists
            self.loan_ids.append(loan['loan_id'])
            self.borrower_customer_ids.append(loan['borrower_customer_id'])
            self.loan_statuses.append(loan['loan_updated_status'])
            self.interest_rates.append(loan['interest_rate'])
            self.tenures.append(loan['tenure'])
            self.loan_amounts.append(loan['loan_amount'])
            self.lender_accepted_timestamps.append(loan['lender_accepted_timestamp'])

            # Retrieve user profile of borrower from user profile table
            borrower_profile = app_tables.fin_user_profile.get(customer_id=loan['borrower_customer_id'])
            if borrower_profile:
                self.borrower_full_names.append(borrower_profile['full_name'])
            else:
                self.borrower_full_names.append("N/A")

            # Retrieve user profile of lender from user profile table
            lender_profile = app_tables.fin_user_profile.get(customer_id=loan['lender_customer_id'])
            if lender_profile:
                self.lender_full_names.append(lender_profile['full_name'])
            else:
                self.lender_full_names.append("N/A")

        # Create a list of dictionaries containing loan details
        self.loan_data = [{'loan_id': self.loan_ids[i], 
                           'borrower_customer_id': self.borrower_customer_ids[i], 
                           'borrower_full_name': self.borrower_full_names[i], 
                           'loan_status': self.loan_statuses[i], 
                           'lender_full_name': self.lender_full_names[i], 
                           'lender_customer_id': self.lender_customer_ids[i], 
                           'interest_rate': self.interest_rates[i], 
                           'tenure': self.tenures[i], 
                           'loan_amount': self.loan_amounts[i], 
                           'lender_accepted_timestamp': self.lender_accepted_timestamps[i]} 
                          for i in range(len(self.loan_ids))]

        # Display approved loans in the repeating panel
        self.repeating_panel_2.items = [loan for loan in self.loan_data if loan['loan_status'].lower() == 'approved']

    def link_2_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('admin.dashboard.performance_tracker')

    def button_1_copy_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('admin.dashboard.loan_management')