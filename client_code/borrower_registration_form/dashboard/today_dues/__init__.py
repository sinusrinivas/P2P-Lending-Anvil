from ._anvil_designer import today_duesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timezone
from .. import main_form_module as main_form_module

class today_dues(today_duesTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.user_id=main_form_module.userId

        self.init_components(**properties)
        today_date = datetime.now(timezone.utc).date()

        # Fetch all loan details from fin_emi_table where scheduled_payment matches today's date
        all_loans = app_tables.fin_emi_table.search(
            next_payment=q.greater_than_or_equal_to(today_date)
        )

        # Create a list to store loan details
        loan_details = []
        
        # Populate loan details with loan amounts from fin_loan_details table
        for loan in all_loans:
            loan_id = loan['loan_id']
            loan_amount = app_tables.fin_loan_details.get(loan_id=loan_id)['loan_amount']
            next_payment = loan['next_payment']

            days_left = (next_payment - today_date).days
            emi_number = loan['emi_number']
            account_number = loan['account_number']
            scheduled_payment = loan['scheduled_payment']
          
            loan_details_row = app_tables.fin_loan_details.get(loan_id=loan_id)
            if loan_details_row is not None:
                tenure = loan_details_row['tenure']
                interest_rate = loan_details_row['interest_rate']
                borrower_loan_created_timestamp = loan_details_row['borrower_loan_created_timestamp']
                loan_updated_status = loan_details_row['loan_updated_status']
                loan_disbursed_timestamp = loan_details_row['loan_disbursed_timestamp']
            else:
                # Set default values if loan details are not found
                tenure = 'N/A'
                interest_rate = 'N/A'
                borrower_loan_created_timestamp = 'N/A'
                loan_updated_status = 'N/A'
                loan_disbursed_timestamp = 'N/A'
                
            days_left = (next_payment - today_date).days
          
            loan_details.append({
                'loan_id': loan_id,
                'loan_amount': loan_amount,
                'scheduled_payment': scheduled_payment,
                'days_left': days_left,
                'tenure': tenure,
                'interest_rate': interest_rate,
                'borrower_loan_created_timestamp': borrower_loan_created_timestamp,
                'emi_number': emi_number,
                'account_number': account_number,
                'loan_updated_status': loan_updated_status,
                'loan_disbursed_timestamp': loan_disbursed_timestamp,
                'next_payment': next_payment
            })
        self.repeating_panel_1.items = loan_details
      
    def home_borrower_registration_form_copy_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower_registration_form.dashboard')