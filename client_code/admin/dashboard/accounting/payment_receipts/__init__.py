from ._anvil_designer import payment_receiptsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class payment_receipts(payment_receiptsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.fetch_and_display_data()

  def fetch_and_display_data(self):
    # Fetch all EMI records from the database
    emi_records = app_tables.fin_emi_table.search()
    
    filtered_emis = []
    
    # Iterate through each EMI record
    for emi in emi_records:
      # Fetch borrower profile based on EMI's customer_id
      borrower_profile = app_tables.fin_user_profile.get(customer_id=emi['borrower_customer_id'])
      
      # Fetch loan details associated with this EMI
      loan_details = app_tables.fin_loan_details.get(loan_id=emi['loan_id'])
      
      if loan_details:
        # Fetch lender profile based on loan's lender_customer_id
        lender_profile = app_tables.fin_user_profile.get(customer_id=loan_details['lender_customer_id'])
      else:
        lender_profile = None
      
      # Append the EMI details to the filtered EMIs list
      filtered_emis.append({
        'borrower_photo': borrower_profile['user_photo'] if borrower_profile else None,
        'borrower_full_name': borrower_profile['full_name'] if borrower_profile else None,
        'borrower_email_id': borrower_profile['email_id'] if borrower_profile else None,
        'borrower_mobile': borrower_profile['mobile'] if borrower_profile else None,
        'borrower_address': borrower_profile['present_address'] if borrower_profile else None,
        'lender_photo': lender_profile['user_photo'] if lender_profile else None,
        'lender_full_name': lender_profile['full_name'] if lender_profile else None,
        'lender_email_id': lender_profile['email_id'] if lender_profile else None,
        'lender_mobile': lender_profile['mobile'] if lender_profile else None,
        'lender_address': lender_profile['present_address'] if lender_profile else None,
        'emi_amount': emi['emi_amount'],
        'interest_amount': emi['interest_amount'],
        'emi_due_date': emi['emi_due_date'],
        'loan_id': emi['loan_id'],
        'payment_date': emi['scheduled_payment_made'],
        'next_payment_date': emi['next_payment'],
        'total_remaining_amount': emi['total_remaining_amount'],
        
        'payment_type': emi['payment_type'],
        # 'loan_amount': loan_details['loan_amount'] if loan_details else None,
        # 'loan_updated_status': loan_details['loan_updated_status'] if loan_details else None,
        # 'membership_type': borrower_profile['membership'] if borrower_profile else None,
        # 'lending_type': lender_profile['lending_type'] if lender_profile else None
      })
    
    # Display the filtered EMIs in a repeating panel or similar component
    self.repeating_panel_1.items = filtered_emis

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.accounting')