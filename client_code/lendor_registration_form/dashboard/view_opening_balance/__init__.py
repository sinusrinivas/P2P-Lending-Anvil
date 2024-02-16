from ._anvil_designer import view_opening_balanceTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class view_opening_balance(view_opening_balanceTemplate):
  def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Fetch all rows from the table and get the latest one based on timestamp
        all_requests = app_tables.fin_lender.search(
            tables.order_by("lender_accepted_timestamp", ascending=False)
        )

        if all_requests:
            # Extract the necessary information from the latest row
            latest_request = all_requests[0]
            final_rta = latest_request['final_rta']
            self.output_lbl.text = f" {final_rta}"
          
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard")



 
