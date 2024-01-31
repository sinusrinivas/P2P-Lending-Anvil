from ._anvil_designer import check_outTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import main_form_module as main_form_module

class check_out(check_outTemplate):
    def __init__(self, selected_row, **properties):
        self.selected_row = selected_row
        # Set Form properties and Data Bindings.
        self.user_id = main_form_module.userId
        self.init_components(**properties)

        # Extract loan details from the selected row
        loan_amount = selected_row['loan_amount']
        tenure = selected_row['tenure']
        interest_rate = selected_row['interest_rate']

        # Calculate EMI amount
        monthly_interest_rate = interest_rate / 12 / 100  # Convert annual interest rate to monthly and percentage to decimal
        total_payments = tenure * 12  # Convert tenure from years to months
        emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)

        # Update labels with loan details
        self.loan_id_label.text = str(selected_row['loan_id'])
        self.loan_amount_label.text = str(loan_amount)
        self.interest_label.text = str(interest_rate)
        self.tenure_label.text = str(tenure)
        self.date_of_apply_label.text = str(selected_row['borrower_loan_created_timestamp'])
        self.emi_no_label.text = str(selected_row['emi_number'])
        self.account_no_label.text = str(selected_row['account_number'])
        
        # Display calculated EMI amount
        self.emi_amount_label.text = "{:.2f}".format(emi)  # Format EMI to display only two decimal places

    def button_1_copy_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower_registration_form.dashboard.today_dues')

    def button_1_copy_3_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('borrower_registration_form.dashboard.view_loans.payment_details_b',selected_row=self.selected_row, entered_values=None)
