from ._anvil_designer import intersest_accrualsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class intersest_accruals(intersest_accrualsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    lenders = app_tables.fin_lender.search()

    filtered_loans = []
    for lender in lenders:
      user_profile = app_tables.fin_user_profile.get(customer_id=lender['customer_id'])
      loans = app_tables.fin_loan_details.get(lender_customer_id=lender['customer_id'])
      if loans['loan_updated_status']
    
