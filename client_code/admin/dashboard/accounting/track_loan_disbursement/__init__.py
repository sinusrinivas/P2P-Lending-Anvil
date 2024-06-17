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
        self.result = [{'borrower_full_name': i['borrower_full_name'],
                        'borrower_email_id': i['borrower_email_id'] ,
                        'lender_full_name': i['lender_full_name'], 
                        'lender_email_id': i['lender_email_id'] ,
                        'interest_rate': i['interest_rate'],
                        'loan_amount': i['loan_amount'],
                        'loan_updated_status': i['loan_updated_status'],
                        'loan_id': i['loan_id'],
                        'total_repayment_amount': i['total_repayment_amount'] ,
                        'membership_type': i['membership_type'], 
                        'emi_payment_type': i['emi_payment_type'], 
                        'product_name': i['product_name'] 
                       }
                       for i in self.result if i['loan_updated_status'] in ["disbursed", "approved"]]

        if not self.result:
            Notification("No Loans with status 'disbursed' or 'approved' found!").show()
        else:
            self.repeating_panel_1.items = self.result
