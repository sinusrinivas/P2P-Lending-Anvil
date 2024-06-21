from ._anvil_designer import emi_detailsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class emi_details(emi_detailsTemplate):
  def __init__(self,selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

   
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
      
      # Collect EMI details and borrower/lender information
      filtered_emis.append({
        'borrower_name' : borrower_profile['full_name'] if borrower_profile else None,
        'lender_name' : lender_profile['full_name'] if lender_profile else None,
        'amount_paid': f"{emi['amount_paid']:.2f}" if emi else None,
        'loan_id': emi['loan_id'],
        'payment_date': emi['scheduled_payment_made'],
        'next_payment_date': emi['next_payment'],
        'total_remaining_amount': f"{emi['total_remaining_amount']:.2f}" if emi else None,        
        'payment_type': "Online",
        'loan_amount': f"{loan_details['loan_amount']:.2f}" if loan_details else None,
        'total_repayment_amount': f"{loan_details['total_repayment_amount']:.2f}" if loan_details else None
      })
    
    # Display the filtered EMIs in a repeating panel or similar component
    self.repeating_panel_1.items = filtered_emis

