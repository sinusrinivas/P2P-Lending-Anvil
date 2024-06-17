# from ._anvil_designer import track_loan_disbursementTemplate
# from anvil import *
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables


# class track_loan_disbursement(track_loan_disbursementTemplate):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#     # Any code you write here will run before the form opens.
#     self.result = app_tables.fin_loan_details.search()
#     if not self.result:
#         Notification("No Data Available Here!").show()
#     else:
#         self.result = [{'borrower_full_name': i['borrower_full_name'],
#                         'borrower_email_id': i['borrower_email_id'] ,
#                         'lender_full_name': i['lender_full_name'], 
#                         'lender_email_id': i['lender_email_id'] ,
#                         'interest_rate': i['interest_rate'],
#                         'loan_amount': i['loan_amount'],
#                         'loan_updated_status': i['loan_updated_status'],
#                         'loan_id': i['loan_id'],
#                         'total_repayment_amount': i['total_repayment_amount'] ,
#                         'membership_type': i['membership_type'], 
#                         'emi_payment_type': i['emi_payment_type'], 
#                         'product_name': i['product_name'] 
#                        }
#                        for i in self.result if i['loan_updated_status'] in ["disbursed", "approved"]]

#         if not self.result:
#             Notification("No Loans with status 'disbursed' or 'approved' found!").show()
#         else:
#             self.repeating_panel_1.items = self.result


# Import necessary modules
from ._anvil_designer import track_loan_disbursementTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class track_loan_disbursement(track_loan_disbursementTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Hide the RepeatingPanel initially
        self.repeating_panel_1.visible = False

    def button_filter_click(self, **event_args):
        # Event handler for filter button click
        selected_date = self.date_picker.date
        
        if selected_date:
            # Fetch loans for the selected date
            loans = app_tables.fin_loan_details.search(
                q.or_(
                    q.date_equal('loan_disbursed_timestamp', selected_date),
                    q.date_equal('lender_accepted_timestamp', selected_date)
                )
            )

            # Filter loans with status 'disbursed' or 'approved'
            filtered_loans = [
                {
                    'borrower_full_name': loan['borrower_full_name'],
                    'borrower_email_id': loan['borrower_email_id'],
                    'lender_full_name': loan['lender_full_name'],
                    'lender_email_id': loan['lender_email_id'],
                    'interest_rate': loan['interest_rate'],
                    'loan_amount': loan['loan_amount'],
                    'loan_updated_status': loan['loan_updated_status'],
                    'loan_id': loan['loan_id'],
                    'total_repayment_amount': loan['total_repayment_amount'],
                    'membership_type': loan['membership_type'],
                    'emi_payment_type': loan['emi_payment_type'],
                    'product_name': loan['product_name'],
                    'loan_disbursed_timestamp': loan['loan_disbursed_timestamp'],
                    'lender_accepted_timestamp': loan['lender_accepted_timestamp']
                }
                for loan in loans
                if loan['loan_updated_status'] in ["disbursed", "approved"]
                   and (loan['loan_disbursed_timestamp'].date() == selected_date
                        or loan['lender_accepted_timestamp'].date() == selected_date)
            ]

            if not filtered_loans:
                Notification(f"No Loans with status 'disbursed' or 'approved' found for {selected_date}!").show()
            else:
                # Update RepeatingPanel with filtered results
                self.repeating_panel_1.items = filtered_loans
                self.repeating_panel_1.visible = True  # Make the RepeatingPanel visible
        else:
            # Handle case where date is not selected
            Notification("Please select a date!").show()
            self.repeating_panel_1.visible = False  # Hide the RepeatingPanel if no date is selected
