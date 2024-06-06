from ._anvil_designer import revenue_shareTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class revenue_share(revenue_shareTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_data(None)

  def load_data(self, status):
    if status == 'close':
      closed_loans = app_tables.fin_loan_details.search(loan_updated_status=q.like('close%'))
      self.new_loan = len(closed_loans)
      self.repeating_panel_1.items = self.process_data(closed_loans)

  def process_data(self, data):
    unique_users = set()
    profiles_with_loans = []
    
    for loan in data:
      lender_customer_id = loan['lender_customer_id']
      if lender_customer_id not in unique_users:
        unique_users.add(lender_customer_id)
        user_profile = app_tables.fin_user_profile.get(customer_id=lender_customer_id)
        if user_profile is not None:
          profiles_with_loans.append({
            'loan_amount': loan['loan_amount'],
            'loan_id': loan['loan_id'],
            'loan_updated_status': loan['loan_updated_status'],
            'interest_rate': loan['interest_rate'],
            'lender_customer_id': lender_customer_id
          })
          
    return profiles_with_loans

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard')

  def button_1_copy_3_click(self, **event_args):
    open_form('admin.dashboard.manage_settings')
