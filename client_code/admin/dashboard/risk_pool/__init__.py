from ._anvil_designer import risk_poolTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class risk_pool(risk_poolTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = []

  def button_low_risk_click(self, **event_args):
    """This method is called when the button is clicked"""
    lapsed_settings = app_tables.fin_loan_settings.get(loans="lapsed fee")
    min_days = lapsed_settings['minimum_days']
    max_days = lapsed_settings['maximum_days']

    # Fetch rows from EMI table where days left is within the range
    emi_rows = app_tables.fin_emi_table.search()
    filtered_rows = [row for row in emi_rows if min_days <= row['days_left'] <= max_days]

    # Set the filtered rows to the repeating panel
    result = []
    for row in filtered_rows:
      loan_details = app_tables.fin_loan_details.get(loan_id=row['loan_id'])
      if loan_details:
        combined_data = {
          'emi_number': row['emi_number'],
          'borrower_customer_id': row['borrower_customer_id'],
          'product_name': loan_details['product_name'],
          'borrower_full_name': loan_details['borrower_full_name']
        }
        result.append(combined_data)
    
    # Set the combined data to the repeating panel
    self.repeating_panel_1.items = result

  def button_medium_risk_click(self, **event_args):
      """This method is called when the button is clicked"""
      lapsed_settings = app_tables.fin_loan_settings.get(loans="default fee")
      min_days = lapsed_settings['minimum_days']
      max_days = lapsed_settings['maximum_days']
  
      # Fetch rows from EMI table where days left is within the range
      emi_rows = app_tables.fin_emi_table.search()
      filtered_rows = [row for row in emi_rows if min_days <= row['days_left'] <= max_days]
  
      # Fetch additional details from the loan details table
      result = []
      for row in filtered_rows:
        loan_details = app_tables.fin_loan_details.get(loan_id=row['loan_id'])
        if loan_details:
          combined_data = {
            'emi_number': row['emi_number'],
            'borrower_customer_id': row['borrower_customer_id'],
            'product_name': loan_details['product_name'],
            'borrower_full_name': loan_details['borrower_full_name']
          }
          result.append(combined_data)
      
      # Set the combined data to the repeating panel
      self.repeating_panel_1.items = result

  def button_high_risk_click(self, **event_args):
      """This method is called when the button is clicked"""
      lapsed_settings = app_tables.fin_loan_settings.get(loans="NPA fee")
      min_days = lapsed_settings['minimum_days']
      max_days = lapsed_settings['maximum_days']
  
      # Fetch rows from EMI table where days left is within the range
      emi_rows = app_tables.fin_emi_table.search()
      filtered_rows = [row for row in emi_rows if min_days <= row['days_left'] <= max_days]
  
      # Fetch additional details from the loan details table
      result = []
      for row in filtered_rows:
        loan_details = app_tables.fin_loan_details.get(loan_id=row['loan_id'])
        if loan_details:
          combined_data = {
            'emi_number': row['emi_number'],
            'borrower_customer_id': row['borrower_customer_id'],
            'product_name': loan_details['product_name'],
            'borrower_full_name': loan_details['borrower_full_name']
          }
          result.append(combined_data)
      
      # Set the combined data to the repeating panel
      self.repeating_panel_1.items = result
