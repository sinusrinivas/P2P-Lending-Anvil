from ._anvil_designer import track_loan_disbursementTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class track_loan_disbursement(track_loan_disbursementTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.result = app_tables.fin_loan_details.search()
    if not self.result:
        Notification("No Data Available Here!").show()
    else:
        self.result = [{'name': i['borrower_full_name'],
                        'loan_amount': i['loan_amount'],
                        'interest': i['interest_rate'],
                        'loan_status': i['loan_updated_status'],
                        'loan_id': i['loan_id'],
                        
                       }
                       for i in self.result]

        self.repeating_panel_1.items = self.result
