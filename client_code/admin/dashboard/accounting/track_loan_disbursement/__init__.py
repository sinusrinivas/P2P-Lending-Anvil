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


# # Import necessary modules
# from ._anvil_designer import track_loan_disbursementTemplate
# from anvil import *
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables

# class track_loan_disbursement(track_loan_disbursementTemplate):
#     def __init__(self, **properties):
#         # Set Form properties and Data Bindings.
#         self.init_components(**properties)

#         # Hide the RepeatingPanel initially
#         self.data_grid_1.visible = False
#     def date_picker_1_change(self, **event_args):
#       """This method is called when the selected date changes"""
#       self.date = self.date_picker_1.date
#       print("dateeeeeeeee", self.date)
      
#     def button_filter_click(self, **event_args):
#         # Event handler for filter button click
#           # Debug: Print selected date to check

#         if self.date:
#             # Calculate start and end of selected date
#             start_date = self.date.replace(hour=0, minute=0, second=0, microsecond=0)
#             end_date = self.date.replace(hour=23, minute=59, second=59, microsecond=999999)

#             # Fetch loans for the selected date and matching timestamps
#             loans = app_tables.fin_loan_details.search(
#                 q.or_(
#                     q.and_(
#                         q.date_equal('loan_disbursed_timestamp', self.date),
#                         q.date_equal('lender_accepted_timestamp', self.date)
#                     ),
#                     q.and_(
#                         q.date_between('loan_disbursed_timestamp', start_date, end_date),
#                         q.date_between('lender_accepted_timestamp', start_date, end_date)
#                     )
#                 )
#             )

#             # Filter loans with status 'disbursed' or 'approved'
#             filtered_loans = [
#                 {
#                     'borrower_full_name': loan['borrower_full_name'],
#                     'borrower_email_id': loan['borrower_email_id'],
#                     'lender_full_name': loan['lender_full_name'],
#                     'lender_email_id': loan['lender_email_id'],
#                     'interest_rate': loan['interest_rate'],
#                     'loan_amount': loan['loan_amount'],
#                     'loan_updated_status': loan['loan_updated_status'],
#                     'loan_id': loan['loan_id'],
#                     'total_repayment_amount': loan['total_repayment_amount'],
#                     'membership_type': loan['membership_type'],
#                     'emi_payment_type': loan['emi_payment_type'],
#                     'product_name': loan['product_name'],
#                     'loan_disbursed_timestamp': loan['loan_disbursed_timestamp'],
#                     'lender_accepted_timestamp': loan['lender_accepted_timestamp']
#                 }
#                 for loan in loans
#                 if loan['loan_updated_status'] in ["disbursed", "approved"]
#             ]

#             if not filtered_loans:
#                 Notification(f"No Loans with status 'disbursed' or 'approved' found for {self.date}!").show()
#             else:
#                 # Update RepeatingPanel with filtered results
#                 self.repeating_panel_1.items = filtered_loans
#                 self.data_grid_1.visible = True  # Make the RepeatingPanel visible
#         else:
#             # Handle case where date is not selected
#             Notification("Please select a date!").show()
#             self.data_grid_1.visible = False  # Hide the RepeatingPanel if no date is selected

    


# Import necessary modules
from ._anvil_designer import track_loan_disbursementTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

class track_loan_disbursement(track_loan_disbursementTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Initialize instance variable to store the selected date
        self.selected_date = None

        # Hide the DataGrid initially
        self.data_grid_1.visible = False
        self.button_filter_click()

    def date_picker_1_change(self, **event_args):
        """This method is called when the selected date changes"""
        self.selected_date = self.date_picker_1.date
        print("Selected date:", self.selected_date)

    def button_filter_click(self, **event_args):
        # Event handler for filter button click
        if self.selected_date:
            selected_date = self.selected_date
            print("Filter button clicked with date:", selected_date)

            # Normalize selected_date to remove the time component
            start_date = selected_date.replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = selected_date.replace(hour=23, minute=59, second=59, microsecond=999999)

            # Fetch loans from the database
            loans = app_tables.fin_loan_details.search(
                q.or_(
                    q.date_between('loan_disbursed_timestamp', start_date, end_date),
                    q.date_between('lender_accepted_timestamp', start_date, end_date)
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
            ]

            if not filtered_loans:
                Notification(f"No Loans with status 'disbursed' or 'approved' found for {selected_date.date()}!").show()
                self.data_grid_1.visible = False  # Hide the DataGrid if no loans found
            else:
                # Update RepeatingPanel with filtered results
                self.repeating_panel_1.items = filtered_loans
                self.data_grid_1.visible = True  # Make the DataGrid visible
        else:
            # Handle case where date is not selected
            Notification("Please select a date!").show()
            self.data_grid_1.visible = False  # Hide the DataGrid if no date is selected
