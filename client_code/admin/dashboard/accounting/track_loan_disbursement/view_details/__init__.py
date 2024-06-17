from ._anvil_designer import view_detailsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class view_details(view_detailsTemplate):
  def __init__(self, selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.borrower_full_name.text = selected_row['borrower_full_name'],
    self.borrower_email.text = selected_row['borrower_email_id'],
    self.name.text = selected_row['lender_full_name'],
    self.lender_email.text = selected_row['lender_email_id'],
    self.interest.text = selected_row['interest_rate'],
    self.loan_amount.text = selected_row['loan_amount'],
    self.status.text = selected_row['loan_updated_status'],
    self.borrower_full_name.text = selected_row['borrower_full_name'],
    self.borrower_full_name.text = selected_row['borrower_full_name'],
