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
    self.selected_row = selected_row

    # Any code you write here will run before the form opens.
    self.borrower_full_name.text = selected_row.get('borrower_full_name', 'N/A')
    self.borrower_email.text = selected_row.get('borrower_email_id', 'N/A')
    self.name.text = selected_row.get('lender_full_name', 'N/A')
    self.lender_email.text = selected_row.get('lender_email_id', 'N/A')
    self.interest.text = selected_row.get('interest_rate', 'N/A')
    self.loan_amount.text = selected_row.get('loan_amount', 'N/A')
    self.status.text = selected_row.get('loan_updated_status', 'N/A')
    self.repay_amount.text = selected_row.get('total_repayment_amount', 'N/A')
    self.membership.text = selected_row.get('membership_type', 'N/A')
    self.emi.text = selected_row.get('emi_payment_type', 'N/A')
    self.product_name.text = selected_row.get('product_name', 'N/A')
