from ._anvil_designer import defaultersTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class defaulters(defaultersTemplate):
  def __init__(self, **properties):

        self.init_components(**properties)
        self.defaulters_data()

  def defaulters_data(self):
        # Fetch data from the fin_loan_details table where loan_updated_status is 'extension'
        loan_details = app_tables.fin_emi_table.search()
        

        result = []
        for borrower_id, details in borrower_loans.items():
            if len(details['loans']) >= 2:
                result.append({
                    'borrower_customer_id': borrower_id,
                    'borrower_full_name': details['borrower_full_name'],
                    'borrower_email_id': details['borrower_email_id'],
                    'mobile_no': details['mobile_no'],
                    'loans_count': len(details['loans']),
                    'product_names': ", ".join(details['product_names'])  # Convert set to a comma-separated string
                })
        
        # Debug: Print the final result before setting it to the repeating panel
        print("Final result:", result)
        
        # Set the filtered data to the repeating panel
        self.repeating_panel_1.items = result


    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.accounting.mis_reports.behavioural_report')
