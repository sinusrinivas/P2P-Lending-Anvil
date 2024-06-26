from ._anvil_designer import risk_view_detailsTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class risk_view_details(risk_view_detailsTemplate):
  def __init__(self,selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.selected_row = selected_row
    # Any code you write here will run before the form opens.

    self.borrower_id.text = f"{selected_row['borrower_customer_id']}"
    self.loan_id.text = f"{selected_row['loan_id']}"
    self.borrower_full_name.text = f"{selected_row['borrower_full_name']}"
    self.borrower_email.text = f"{selected_row['borrower_email']}"
    self.lender_email.text = f"{selected_row['lender_email']}"
    self.product_name.text = f"{selected_row['product_name']}"
    self.emi_number.text = f"{selected_row['emi_number']}"
    self.days_left.text = f"{selected_row['days_left']}"
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.reporting_and_analytical_modules.risk_pool')
