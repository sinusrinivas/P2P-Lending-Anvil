from ._anvil_designer import top_up_amountTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class top_up_amount(top_up_amountTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def button_2_click(self, **event_args):
    

    all_requests = app_tables.top_up.search()
    top_up = self.tp_tb.text
    
    all_requests = app_tables.lender.search(
            tables.order_by("lender_accepted_timestamp", ascending=False)
        )
    final_rta = self.final_rta
    
    if all_requests:
        latest_request = all_requests[0]
        available_balance = latest_request['available_balance']
        final_rta = int(latest_request['available_balance']) + int(top_up)
        #user_name = self.user_name
        self.final_rta.text = f"Total Available Amount: {final_rta}"

        # Call the server function with the correct name and parameter
        anvil.server.call('add_rtr_form', final_rta, available_balance)
        anvil.server.call('add_top_up_amount', top_up)
      
        Notification("Topup added successfully").show()

  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard")

  






