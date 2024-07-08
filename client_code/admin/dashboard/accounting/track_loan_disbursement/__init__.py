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

        # Initialize instance variables
        self.selected_date = None
        self.disbursed_loan_count = 0
        self.approved_loan_count = 0

        # Hide the DataGrid initially
        self.data_grid_1.visible = False

    def date_picker_1_change(self, **event_args):
        """This method is called when the selected date changes"""
        self.selected_date = self.date_picker_1.date
        print("Selected date:", self.selected_date)

        if self.selected_date:
            # Fetch loans from the database
            loans = app_tables.fin_loan_details.search()
            
            # Initialize an empty list to store filtered loans
            filtered_loans = []
            self.disbursed_loan_count = 0  # Reset count
            self.approved_loan_count = 0  # Reset count

            for loan in loans:
                user_profile = app_tables.fin_user_profile.get(customer_id=loan['borrower_customer_id'])
                
                if user_profile is not None and loan['loan_updated_status'] in ["disbursed", "approved"]:
                    if (loan['loan_disbursed_timestamp'] and loan['loan_disbursed_timestamp'].date() == self.selected_date) or \
                       (loan['lender_accepted_timestamp'] and loan['lender_accepted_timestamp'].date() == self.selected_date):
                        filtered_loans.append({
                            'user_photo': user_profile['user_photo'],
                            'borrower_full_name': loan['borrower_full_name'],
                            'borrower_email_id': loan['borrower_email_id'],
                            'lender_full_name': loan['lender_full_name'],
                            'lender_email_id': loan['lender_email_id'],
                            'ascend_score': user_profile['ascend_value'],
                            'loan_amount': loan['loan_amount'],
                            'loan_updated_status': loan['loan_updated_status'],
                            'loan_id': loan['loan_id'],
                            'total_repayment_amount': loan['total_repayment_amount'],
                            'membership_type': loan['membership_type'],
                            'emi_payment_type': loan['emi_payment_type'],
                            'product_name': loan['product_name'],
                            'loan_disbursed_timestamp': loan['loan_disbursed_timestamp'],
                            'lender_accepted_timestamp': loan['lender_accepted_timestamp']
                        })
                        # Increment the respective count
                        if loan['loan_updated_status'] == 'disbursed':
                            self.disbursed_loan_count += 1
                        elif loan['loan_updated_status'] == 'approved':
                            self.approved_loan_count += 1
            
            if not filtered_loans:
                Notification(f"No Loans with status 'disbursed' or 'approved' found for {self.selected_date}!").show()
                self.data_grid_1.visible = False  # Hide the DataGrid if no loans found
            else:
                # Update RepeatingPanel with filtered results
                self.repeating_panel_1.items = filtered_loans
                self.data_grid_1.visible = True  # Make the DataGrid visible
            
            # Display the counts
            self.label_disbursed_count.text = self.disbursed_loan_count
            self.label_approved_count.text =  self.approved_loan_count
        else:
            Notification("Please select a date!").show()
            self.data_grid_1.visible = False  # Hide the DataGrid if no date is selected

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('admin.dashboard.accounting')



# from ._anvil_designer import track_loan_disbursementTemplate
# from anvil import *
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
# from datetime import datetime

# class track_loan_disbursement(track_loan_disbursementTemplate):
#     def __init__(self, **properties):
#         # Set Form properties and Data Bindings.
#         self.init_components(**properties)

#         # Initialize instance variable to store the selected date
#         self.selected_date = None

#         # Hide the DataGrid initially
#         self.data_grid_1.visible = False

#     def date_picker_1_change(self, **event_args):
#         """This method is called when the selected date changes"""
#         self.selected_date = self.date_picker_1.date
#         print("Selected date:", self.selected_date)

#         if self.selected_date:
#             # Fetch loans from the database
#             loans = app_tables.fin_loan_details.search()
            
#             # Initialize an empty list to store filtered loans
#             filtered_loans = []

#             for loan in loans:
#                 user_profile = app_tables.fin_user_profile.get(customer_id=loan['borrower_customer_id'])
                
#                 if user_profile is not None and loan['loan_updated_status'] in ["disbursed", "approved"]:
#                     if (loan['loan_disbursed_timestamp'] and loan['loan_disbursed_timestamp'].date() == self.selected_date) or \
#                        (loan['lender_accepted_timestamp'] and loan['lender_accepted_timestamp'].date() == self.selected_date):
#                         filtered_loans.append({
#                             'user_photo': user_profile['user_photo'],
#                             'borrower_full_name': loan['borrower_full_name'],
#                             'borrower_email_id': loan['borrower_email_id'],
#                             'lender_full_name': loan['lender_full_name'],
#                             'lender_email_id': loan['lender_email_id'],
#                             'ascend_score': user_profile['ascend_value'],
#                             'loan_amount': loan['loan_amount'],
#                             'loan_updated_status': loan['loan_updated_status'],
#                             'loan_id': loan['loan_id'],
#                             'total_repayment_amount': loan['total_repayment_amount'],
#                             'membership_type': loan['membership_type'],
#                             'emi_payment_type': loan['emi_payment_type'],
#                             'product_name': loan['product_name'],
#                             'loan_disbursed_timestamp': loan['loan_disbursed_timestamp'],
#                             'lender_accepted_timestamp': loan['lender_accepted_timestamp']
#                         })
            
#             if not filtered_loans:
#                 Notification(f"No Loans with status 'disbursed' or 'approved' found for {self.selected_date}!").show()
#                 self.data_grid_1.visible = False  # Hide the DataGrid if no loans found
#             else:
#                 # Update RepeatingPanel with filtered results
#                 self.repeating_panel_1.items = filtered_loans
#                 self.data_grid_1.visible = True  # Make the DataGrid visible
#         else:
#             Notification("Please select a date!").show()
#             self.data_grid_1.visible = False  # Hide the DataGrid if no date is selected

#     def button_1_click(self, **event_args):
#       """This method is called when the button is clicked"""
#       open_form('admin.dashboard.accounting')
