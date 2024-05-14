from ._anvil_designer import RowTemplate7Template
from anvil import *
import anvil.server
import anvil.google.auth
import anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...bank_users.main_form import main_form_module
from ...bank_users.user_form import user_module

class RowTemplate7(RowTemplate7Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.email = main_form_module.email
        self.user_Id = main_form_module.userId

        try:
            customer_loans = app_tables.fin_loan_details.search(borrower_customer_id=self.user_Id)
            if customer_loans:
                
        except anvil.tables.NoSuchRow:
            customer_loans = []  # Handle the case when no row is found
            alert("No data found")

    # Any code you write here will run before the form opens.
