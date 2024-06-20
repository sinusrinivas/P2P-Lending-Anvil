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

      
      self.label_7.text = borrower_profile['full_name']       
      self.label_8.text = borrower_profile['mobile'] if borrower_profile else None
      self.label_19.text= borrower_profile['street_adress_1'] if borrower_profile else None
      self.label_13.text = lender_profile['full_name'] if lender_profile else None
      self.label_14.text= lender_profile['mobile'] if lender_profile else None
      self.label_21.text= lender_profile['street_adress_1'] if lender_profile else None
      self.label_27.text =  emi['scheduled_payment_made'] if emi else None
      self.label_29.text = "Online"
      self.label_30.text = emi['amount_paid'] if emi else None
      # # Append the EMI details to the filtered EMIs list
      filtered_emis.append({
       
        'amount_paid': emi['amount_paid'],
        'loan_id': emi['loan_id'],
        'payment_date': emi['scheduled_payment_made'],
        'next_payment_date': emi['next_payment'],
        'total_remaining_amount': emi['total_remaining_amount'],        
        'payment_type': "Online",
        'loan_amount': loan_details['loan_amount'] if loan_details else None,
        'total_repayment_amount': loan_details['total_repayment_amount'] if loan_details else None
      })
    
    # Display the filtered EMIs in a repeating panel or similar component
    self.repeating_panel_1.items = filtered_emis

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.accounting.payment_receipts')