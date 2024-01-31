# from ._anvil_designer import borrower_extensionTemplate
# from anvil import *
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables

# class borrower_extension(borrower_extensionTemplate):
#     def __init__(self, selected_row, **properties):
#         # Set Form properties and Data Bindings.
#         self.init_components(**properties)

#         # Any code you write here will run before the form opens.
#         self.selected_row = selected_row
#         self.label_loan_id.text = f"{selected_row['loan_id']}"
#         self.label_name.text = f"{selected_row['borrower_full_name']}"
#         self.label_loan_amount.text = f"{selected_row['loan_amount']}"
#         self.label_loan_tenure.text = f"{selected_row['tenure']} Months"
#         self.label_interest_rate.text = f"{selected_row['interest_rate']} % pa"  
#         self.label_5_copy.text = "Loan Extension Request is Under Process..."
#         self.label_5_copy_2.text = "Loan Extension Request is Accepted"
#         self.label_5_copy_3.text = "Loan Extension Request is Rejected"
#         product_id_to_search = selected_row['product_id']
#         data = tables.app_tables.fin_product_details.search(product_id=product_id_to_search)
#         self.foreclosure_type_lst = [] 
#         self.extension_fee_lst = []
#         for i in data:
#             self.foreclosure_type_lst.append(i['extension_allowed'])
#             self.extension_fee_lst.append(i['extension_fee'])
        
#         self.extension_allow.text = self.foreclosure_type_lst[0]
#         self.extension_fee.text = self.extension_fee_lst[0]

#         # Check status for the selected loan ID
#         loan_id = selected_row['loan_id']
#         extend_rows = app_tables.fin_extends_loan.search(loan_id=loan_id)

#         approved_status = False
#         rejected_status = False

#         for row in extend_rows:
#             if row['status'] == 'approved':
#                 approved_status = True
#                 break
#             elif row['status'] == 'rejected':
#                 rejected_status = True
#                 break

#         if approved_status:
#             self.label_5_copy_2.visible = True
#             self.button_1_copy.visible = True
#             self.button_1.visible = False
#             self.button_2.visible = False
#             loan_details_row = loan_details_row['loan_extension_months']
#             self.text_box_1.text = str(loan_details_row)
#             Notification("Your request has been accepted.").show(
#         elif rejected_status:
#             # If there is a reject status, show an alert
#             self.label_5_copy_3.visible = True
#             self.button_1_copy.visible = True
#             self.button_1.visible = False
#             self.button_2.visible = False
#             loan_details_row = loan_details_row['loan_extension_months']
#             self.text_box_1.text = str(loan_details_row)
#             Notification('Your request has been rejected.').show()
#         else:
#             # If there is no approved or reject status, check if the loan ID is in foreclosure table
#             existing_requests = app_tables.fin_extends_loan.search(loan_id=loan_id)
#             if len(existing_requests) == 0 :
#                 # If the loan ID is not in the foreclosure table, make "Foreclose" button and button2 visible                
#                 self.button_2.visible = True               
#             else:
#                 loan_details_row = loan_details_row['loan_extension_months']
#                 self.text_box_1.text = str(loan_details_row)
#                 self.button_2.visible = False 
#                 self.label_5_copy.visible = True
#                 self.button_1_copy.visible = True
#                 self.button_1.visible = False 
                

#     def button_1_click(self, **event_args):
#         """This method is called when the Back button is clicked"""
#         open_form('borrower_registration_form.dashboard.Extension_loan_request')

#     def button_3_click(self, **event_args):
#         """This method is called when the Close button is clicked"""
#         open_form('borrower_registration_form.dashboard')

#     def button_2_click(self, **event_args):
#         """This method is called when the Submit Extension Request button is clicked"""
#         # Validate extension months before allowing the borrower to proceed
#         if self.validate_extension_months():
#             # Get the loan_id and extension months
#             loan_id = self.selected_row['loan_id']
#             loan_extension_months = int(self.text_box_1.text.strip())

#             # Check if a row with the specified loan_id already exists in loan_details
#             existing_row = app_tables.fin_loan_details.get(loan_id=loan_id)

#             if existing_row is not None:
#                 # Update the existing row
#                 existing_row.update(loan_extension_months=loan_extension_months)
#             else:
#                 # Create a new row
#                 app_tables.fin_loan_details.add_row(
#                     loan_id=loan_id,
#                     loan_extension_months=loan_extension_months
#                 )

#             # Close the current form or navigate to another form if needed
#             open_form('borrower_registration_form.dashboard.Extension_loan_request.borrower_extension.extension2', selected_row = self.selected_row, loan_extension_months = loan_extension_months)

#     def validate_extension_months(self):
#         """Validate the extension months entered by the borrower"""
#         extension_months = self.text_box_1.text.strip()

#         if extension_months and extension_months.isdigit():
#             loan_extension_months = int(extension_months)
#             if 0 < loan_extension_months <= 6:
#                 return True
#             else:
#                 alert("Extension months must be between 1 and 6.", title="Validation Error")
#         else:
#             alert("Please enter a valid number of extension months.", title="Validation Error")
        
#         return False


from ._anvil_designer import borrower_extensionTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class borrower_extension(borrower_extensionTemplate):
    def __init__(self, selected_row, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        self.selected_row = selected_row
        self.label_loan_id.text = f"{selected_row['loan_id']}"
        self.label_name.text = f"{selected_row['borrower_full_name']}"
        self.label_loan_amount.text = f"{selected_row['loan_amount']}"
        self.label_loan_tenure.text = f"{selected_row['tenure']} Months"
        self.label_interest_rate.text = f"{selected_row['interest_rate']} % pa"  
        self.label_5_copy.text = "Loan Extension Request is Under Process..."
        self.label_5_copy_2.text = "Loan Extension Request is Accepted"
        self.label_5_copy_3.text = "Loan Extension Request is Rejected"
        product_id_to_search = selected_row['product_id']
        data = tables.app_tables.fin_product_details.search(product_id=product_id_to_search)
        self.foreclosure_type_lst = [] 
        self.extension_fee_lst = []
        for i in data:
            self.foreclosure_type_lst.append(i['extension_allowed'])
            self.extension_fee_lst.append(i['extension_fee'])
        
        self.extension_allow.text = self.foreclosure_type_lst[0]
        self.extension_fee.text = self.extension_fee_lst[0]

        # Check status for the selected loan ID
        loan_id = selected_row['loan_id']
        extend_rows = app_tables.fin_extends_loan.search(loan_id=loan_id)

        approved_status = False
        rejected_status = False

        for row in extend_rows:
            if row['status'] == 'approved':
                approved_status = True
                break
            elif row['status'] == 'rejected':
                rejected_status = True
                break

        if approved_status:
            self.label_5_copy_2.visible = True
            self.button_1_copy.visible = True
            self.button_1.visible = False
            self.button_2.visible = False
            loan_details_row = loan_details_row['loan_extension_months']
            self.text_box_1.text = str(loan_details_row)
            Notification("Your request has been accepted.").show()
        elif rejected_status:
            # If there is a reject status, show an alert
            self.label_5_copy_3.visible = True
            self.button_1_copy.visible = True
            self.button_1.visible = False
            self.button_2.visible = False
            loan_details_row = loan_details_row['loan_extension_months']
            self.text_box_1.text = str(loan_details_row)
            Notification('Your request has been rejected.').show()
        else:
            # If there is no approved or reject status, check if the loan ID is in foreclosure table
            existing_requests = app_tables.fin_extends_loan.search(loan_id=loan_id)
            if len(existing_requests) == 0 :
                # If the loan ID is not in the foreclosure table, make "Foreclose" button and button2 visible                
                self.button_2.visible = True               
            else:
                loan_details_row = loan_details_row['loan_extension_months']
                self.text_box_1.text = str(loan_details_row)
                self.button_2.visible = False 
                self.label_5_copy.visible = True
                self.button_1_copy.visible = True
                self.button_1.visible = False 
                

    def button_1_click(self, **event_args):
        """This method is called when the Back button is clicked"""
        open_form('borrower_registration_form.dashboard.Extension_loan_request')

    def button_3_click(self, **event_args):
        """This method is called when the Close button is clicked"""
        open_form('borrower_registration_form.dashboard')

    def button_2_click(self, **event_args):
        """This method is called when the Submit Extension Request button is clicked"""
        # Validate extension months before allowing the borrower to proceed
        if self.validate_extension_months():
            # Get the loan_id and extension months
            loan_id = self.selected_row['loan_id']
            loan_extension_months = int(self.text_box_1.text.strip())

            # Check if a row with the specified loan_id already exists in loan_details
            existing_row = app_tables.fin_loan_details.get(loan_id=loan_id)

            if existing_row is not None:
                # Update the existing row
                existing_row.update(loan_extension_months=loan_extension_months)
            else:
                # Create a new row
                app_tables.fin_loan_details.add_row(
                    loan_id=loan_id,
                    loan_extension_months=loan_extension_months
                )

            # Close the current form or navigate to another form if needed
            open_form('borrower_registration_form.dashboard.Extension_loan_request.borrower_extension.extension2', selected_row = self.selected_row, loan_extension_months = loan_extension_months)

    def validate_extension_months(self):
        """Validate the extension months entered by the borrower"""
        extension_months = self.text_box_1.text.strip()

        if extension_months and extension_months.isdigit():
            loan_extension_months = int(extension_months)
            if 0 < loan_extension_months <= 6:
                return True
            else:
                alert("Extension months must be between 1 and 6.", title="Validation Error")
        else:
            alert("Please enter a valid number of extension months.", title="Validation Error")
        
        return False
