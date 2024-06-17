from ._anvil_designer import view_detailsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class view_details(view_detailsTemplate):
  def __init__(self, selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Store the selected row
    self.selected_row = selected_row
    print(self.selected_row)

    # Retrieve the loan details from the database
    loan = app_tables.fin_loan_details.get(loan_id=self.selected_row)
    print(l)

    if loan:
        # Any code you write here will run before the form opens.
        self.borrower_full_name.text = loan['borrower_full_name'] if 'borrower_full_name' in loan else 'N/A'
        self.borrower_email.text = loan['borrower_email_id'] if 'borrower_email_id' in loan else 'N/A'
        self.name.text = loan['lender_full_name'] if 'lender_full_name' in loan else 'N/A'
        self.lender_email.text = loan['lender_email_id'] if 'lender_email_id' in loan else 'N/A'
        self.interest.text = str(loan['interest_rate']) if 'interest_rate' in loan else 'N/A'
        self.loan_amount.text = str(loan['loan_amount']) if 'loan_amount' in loan else 'N/A'
        self.status.text = loan['loan_updated_status'] if 'loan_updated_status' in loan else 'N/A'
        self.repay_amount.text = str(loan['total_repayment_amount']) if 'total_repayment_amount' in loan else 'N/A'
        self.membership.text = loan['membership_type'] if 'membership_type' in loan else 'N/A'
        self.emi.text = loan['emi_payment_type'] if 'emi_payment_type' in loan else 'N/A'
        self.product_name.text = loan['product_name'] if 'product_name' in loan else 'N/A'
