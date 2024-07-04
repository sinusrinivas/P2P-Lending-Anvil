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
    self.loan_details = loan_details

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
      self.remaining_amount.text = loan_details['remaining_amount']
      self.loan_amount.text = loan_details['loan_amount']
      self.product_name.text = loan_details['product_name']
      self.membership_type.text = loan_details['membership_type']
      self.interest_rate.text = loan_details['interest_rate']
      self.tenure.text = loan_details['tenure']
      self.leneder_id.text = loan_details['lender_customer_id']
      self.lender_returnss.text = loan_details['lender_returns']
      self.lender_email.text = loan_details['lender_email_id']
      self.disbursed_date_picker_2.date = loan_details['loan_disbursed_timestamp']
      self.emi_payment_type.text = loan_details['emi_payment_type']
      self.first_date_picker_1.date = loan_details['first_emi_payment_due_date']
      self.total_amount.text = loan_details['total_amount_paid']


    
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

  def loan_details_click(self, **event_args):
    """This method is called when the button is clicked"""
    loan = app_tables.fin_loan_details.get(loan_id=self.loan_details['loan_id'])
    if loan:
      loan['first_emi_payment_due_date'] = self.first_date_picker_1.date
      loan['loan_disbursed_timestamp'] = self.disbursed_date_picker_2.date
      loan.update()