from ._anvil_designer import editTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class edit(editTemplate):
  def __init__(self,loan_details,emi_details,extension_details,foreclosure_details, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    if loan_details:
      self.loan_details_column_panel_1.visible = True

      self.processing_fee.text = loan_details['total_processing_fee_amount']
      self.loan_id_label.text = loan_details['loan_id']
      self.borrower_id.text = loan_details['borrower_customer_id']
      self.borrower_email.text = loan_details['borrower_email_id']
      self.borrower_name.text = loan_details['borrower_full_name']
      self.product_id.text = loan_details['product_id']
      self.updated_status.text = loan_details['loan_updated_status']
      self.interest_amount.text = loan_details['total_interest_amount']
      self.total_repayment_amount.text = loan_details['total_repayment_amount']
      self.remaining_amount = loan_details['remaining_amount']
      self.loan_amount = loan_details['loan_amount']
      self.product_name = loan_details['product_name']
      self.membership_type = loan_details['membership_type']
      tenure = loan_details['interest_rate']
      interest_rate = loan_details['tenure']
      emi_payment_type = loan_details['lender_customer_id']
      total_interest_amount = loan_details['lender_full_name']
      total_processing_fee_amount = loan_details['lender_returns']
      total_processing_fee_amount = loan_details['lender_email_id']
      loan_amount = loan_details['loan_disbursed_timestamp']
      tenure = loan_details['emi_payment_type']
      interest_rate = loan_details['first_emi_payment_due_date']
      emi_payment_type = loan_details['total_amount_paid']
      total_interest_amount = loan_details['lender_accepted_timestamp']


    
    elif emi_details:
      self.emi_panel.visible = True
    elif extension_details:
      self.extension_panel.visible = True
    elif foreclosure_details:
      self.forelosure_panel.visible = True
    # Any code you write here will run before the form opens.

  def button_1_copy_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.editing_detabase_details')
