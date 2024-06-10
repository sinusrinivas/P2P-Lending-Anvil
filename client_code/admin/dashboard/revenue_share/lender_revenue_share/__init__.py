# from ._anvil_designer import lender_revenue_shareTemplate
# from anvil import *
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
# from anvil import open_form

# class lender_revenue_share(lender_revenue_shareTemplate):
#   def __init__(self, customer_id, **properties):
#     # self.selected_row = selected_row
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#     # Any code you write here will run before the form opens.
#     self.load_loan_data(customer_id)

#   def load_loan_data(self, customer_id):
#     loans = app_tables.fin_loan_details.search(lender_customer_id=customer_id)
    
#     if loans:
#       self.repeating_panel_1.items = loans

#   def button_1_click(self, **event_args):
#     open_form("admin.dashboard.revenue_share.lender_revenue_share")





from ._anvil_designer import lender_revenue_shareTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class lender_revenue_share(lender_revenue_shareTemplate):
  def __init__(self, customer_id, **properties):
    self.init_components(**properties)
    self.customer_id = customer_id
    self.load_loan_data()

  def load_loan_data(self):
    loans = app_tables.fin_loan_details.search(lender_customer_id=self.customer_id)
    loan_details = [{
      'loan_id': loan['loan_id'],
      'loan_amount': loan['loan_amount'],
      'lender_returns': loan['lender_returns']
      # Add other fields as necessary
    } for loan in loans]
    
    self.repeating_panel_1.items = loan_details

  def button_1_click(self, **event_args):
    open_form("admin.dashboard.revenue_share.lender_revenue_share")
