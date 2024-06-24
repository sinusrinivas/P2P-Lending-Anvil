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
  def __init__(self, selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Store the selected loan_id
    self.selected_loan_id = selected_row['loan_id']
    
    # Fetch and display data for the selected loan_id
    self.fetch_and_display_data()
    self.button_1.text = "On"
    
  def fetch_and_display_data(self):
    # Fetch all EMI records for the selected loan_id from the database
    emi_records = app_tables.fin_emi_table.search(loan_id=self.selected_loan_id)
    
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
        'borrower_name': borrower_profile['full_name'] if borrower_profile else None,
        'lender_name': lender_profile['full_name'] if lender_profile else None,
        'amount_paid': f"{emi['amount_paid']:.2f}" if emi['amount_paid'] is not None else None,
        'loan_id': emi['loan_id'],
        'emi_number': emi['emi_number'],
        'payment_date': emi['scheduled_payment_made'],
        'next_payment_date': emi['next_payment'],
        'total_remaining_amount': f"{emi['total_remaining_amount']:.2f}" if emi['total_remaining_amount'] is not None else None,
        'remaining_tenure': emi['remaining_tenure'],
        'loan_amount': f"{loan_details['loan_amount']:.2f}" if loan_details and loan_details['loan_amount'] is not None else None,
        'total_repayment_amount': f"{loan_details['total_repayment_amount']:.2f}" if loan_details and loan_details['total_repayment_amount'] is not None else None
      })
    
    # Display the filtered EMIs in a repeating panel or similar component
    self.repeating_panel_1.items = filtered_emis

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.button_1.text == "On":
        self.button_1.text = "Off"
        self.data_grid_1.visible=True
        self.content.visible = False
    else:
        self.button_1.text = "On"
        self.content.visible = True
        self.data_grid_1.visible=False
