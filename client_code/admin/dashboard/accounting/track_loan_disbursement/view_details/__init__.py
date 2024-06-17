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

    # Any code you write here will run before the form opens.
    self.borrower_full_name.text = selected_row['borrower_full_name'] if 'borrower_full_name' in selected_row else 'N/A'
    self.borrower_email.text = selected_row['borrower_email_id'] if 'borrower_email_id' in selected_row else 'N/A'
    self.name.text = selected_row['lender_full_name'] if 'lender_full_name' in selected_row else 'N/A'
    self.lender_email.text = selected_row['lender_email_id'] if 'lender_email_id' in selected_row else 'N/A'
    self.interest.text = selected_row['interest_rate'] if 'interest_rate' in selected_row else 'N/A'
    self.loan_amount.text = selected_row['loan_amount'] if 'loan_amount' in selected_row else 'N/A'
    self.status.text = selected_row['loan_updated_status'] if 'loan_updated_status' in selected_row else 'N/A'
    self.repay_amount.text = selected_row['total_repayment_amount'] if 'total_repayment_amount' in selected_row else 'N/A'
    self.membership.text = selected_row['membership_type'] if 'membership_type' in selected_row else 'N/A'
    self.emi.text = selected_row['emi_payment_type'] if 'emi_payment_type' in selected_row else 'N/A'
    self.product_name.text = selected_row['product_name'] if 'product_name' in selected_row else 'N/A'
