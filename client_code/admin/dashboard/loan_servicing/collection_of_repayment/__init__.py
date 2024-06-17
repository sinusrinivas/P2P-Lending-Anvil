from ._anvil_designer import collection_of_repaymentTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class collection_of_repayment(collection_of_repaymentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.repeating_panel_1.items = self.fetch_repayment_data()

  def fetch_repayment_data(self):
    emi_rows = app_tables.fin_emi_table.search()
    data = []

    for emi_row in emi_rows:
      loan_row = app_tables.fin_loan_details.get(loan_id=emi_row['loan_id'])
      if loan_row:
        user_profile_row = app_tables.fin_user_profile.get(customer_id=loan_row['borrower_customer_id'])
        borrower_image = user_profile_row['user_photo'] if user_profile_row else None
        
        data.append({
          'loan_id': loan_row['loan_id'],
          'borrower_full_name': loan_row['borrower_full_name'],
          'product_name': loan_row['product_name'],
          'borrower_email_id': loan_row['borrower_email_id'],
          'emi_number': emi_row['emi_number'],
          'amount_paid': emi_row['amount_paid'],
          # 'lapsed_fee': emi_row['lapsed_fee'],
          # 'default_fee': emi_row['default_fee'],
          # 'npa_fee': emi_row['npa_fee'],
          # 'total_fees': emi_row['lapsed_fee'] + emi_row['default_fee'] + emi_row['npa_fee'],
          'image': borrower_image  # Include the image
        })
    return data

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.Tracking')
