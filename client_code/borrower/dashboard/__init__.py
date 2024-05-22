# # from ._anvil_designer import dashboardTemplate
# # from anvil import *
# # import anvil.server
# # import anvil.google.auth, anvil.google.drive
# # from anvil.google.drive import app_files
# # import anvil.users
# # import anvil.tables as tables
# # import anvil.tables.query as q
# # from anvil.tables import app_tables
# # from ...bank_users.main_form import main_form_module
# # from ...bank_users.user_form import user_module

# # class dashboard(dashboardTemplate):
# #     def __init__(self, **properties):
# #         email = main_form_module.email
# #         self.init_components(**properties)
# #         self.email = main_form_module.email
# #         self.user_Id=main_form_module.userId
# #         user_id = self.user_Id

# #         # Fetch the user profile based on the current user's email
# #         user = anvil.users.get_user()
# #         # Check if a user is logged in
# #         if user:
# #             # Fetch the user profile record based on the current user's email
# #             user_profile = app_tables.fin_user_profile.get(email_user=user['email'])
# #             # Check if the user profile record is found
# #             if user_profile:
# #                 # Access the user ID from the user profile record
# #                 user_id = user_profile['customer_id']
# #                 # Filter loan_details table based on the current user's ID
# #                 try:
# #                     customer_loans = app_tables.fin_loan_details.search(borrower_customer_id=user_id)
# #                     print(len(customer_loans))
# #                 except anvil.tables.NoSuchRow:
# #                     customer_loans = []  # Handle the case when no row is found
# #                     alert("No data found")

# #                 # Check if the user has at least 3 loans
# #                 # if len(customer_loans) > 3:
# #                 #     self.extended_loans.visible = True
# #                 # else:
# #                 #     self.extended_loans.visible = False


# #     def home_main_form_link_click(self, **event_args):
# #         """This method is called when the link is clicked"""
# #         open_form("borrower.dashboard")

# #     def button_3_click(self, **event_args):
# #         """This method is called when the button is clicked"""
# #         open_form('borrower.dashboard.view_loans')
# #         open_form('borrower.dashboard.borrower_profile')

# #     def button_4_click(self, **event_args):
# #         """This method is called when the button is clicked"""
    
        

# #     def button_6_click(self, **event_args):
      

# #     def outlined_button_1_click(self, **event_args):
      

# #     def outlined_button_3_click(self, **event_args):
      

# #     def outlined_button_2_click(self, **event_args):
# #       open_form('borrower.dashboard.foreclosure_request')

# #     # def outlined_button_6_click(self, **event_args):
# #     #   open_form('borrower_registration_form.dashboard.dashboard_report_a_problem')

# #     def outlined_button_7_click(self, **event_args):
      

# #     def about_main_form_link_click(self, **event_args):
# #       open_form('borrower.dashboard.dashboard_about')

# #     def notification_link_click(self, **event_args):
# #       open_form('borrower.dashboard.notification')

  
# #     # this button is work for wallet 
# #     def wallet_dashboard_link_click(self, **event_args):
# #       customer_id = self.user_Id
# #       email = self.email
# #       anvil.server.call('fetch_profile_data_and_insert', email, customer_id)
# #       open_form('wallet.wallet')


# #     def extended_loans_click(self, **event_args):
      

# #     def outlined_button_1_copy_3_click(self, **event_args):
      


# #     # this is for logout
# #     def logout_click(self, **event_args):
# #       alert("Logged out successfully")
# #       anvil.users.logout()
# #       open_form('bank_users.main_form')

# #     def borrower_dashboard_product_link_click(self, **event_args):
# #       """This method is called when the link is clicked"""
# #       pass

# #     def contact_main_form_link_click(self, **event_args):
# #       open_form('borrower.dashboard.dashboard_contact')

# #     def Report_A_Problem_click(self, **event_args):
# #       open_form('borrower.dashboard.dashboard_report_a_problem')

# #     def view_profile(self, **event_args):
# #       """This method is called when the button is clicked"""
# #       open_form('borrower.dashboard.borrower_profile')

# #     def outlined_button_06_click(self, **event_args):
# #       """This method is called when the button is clicked"""
      

# #     def button_1_click(self, **event_args):
# #         email = main_form_module.email
    
# #         user_profile = app_tables.fin_user_profile.get(email_user=email)
    
# #         if user_profile:
# #             user_id = user_profile['customer_id']
    
# #             # Count the number of loans the user already has (based on specific patterns)
# #             try:
# #                 existing_loans = app_tables.fin_loan_details.search(
# #                     borrower_customer_id=user_id,
# #                     loan_updated_status=q.any_of(
# #                         q.like('accept%'),
# #                         q.like('Approved%'),
# #                         q.like('approved%'),
# #                         q.like('under process%'),
# #                         q.like('foreclosure%'),
# #                         # q.like('close%'),
# #                         # q.like('Close%'),
# #                         # q.like('closed loans%'),
# #                         q.like('disbursed loan%'),
# #                         q.like('Disbursed loan%'),
# #                         q.like('Under Process%')
# #                     )
# #                 )
# #                 num_existing_loans = len(existing_loans)
# #                 print(f"User ID: {user_id}, Existing Loans: {num_existing_loans}")
    
# #                 # Check if the user has more than 5 loans
# #                 if num_existing_loans >= 5:
# #                     alert("You already have 5 loans. Cannot open a new loan request.")
# #                 else:
# #                     wallet_row = app_tables.fin_wallet.get(customer_id=user_id)
    
# #                     if wallet_row and wallet_row['wallet_id'] is not None:
# #                         open_form('borrower.dashboard.new_loan_request')
# #                     else:
# #                         alert("Wallet not found. Please create a wallet.")
    
# #             except anvil.tables.TableError as e:
# #                 # Check if the error message contains information about the non-existent row
# #                 if "Row not found" in str(e):
# #                     # Handle the case when no row is found
# #                     alert("No data found.")
# #                 else:
# #                     # Handle other table errors
# #                     alert("Error fetching existing loans.")

# #     def button_2_click(self, **event_args):
# #       """This method is called when the button is clicked"""
# #       open_form('borrower.dashboard.today_dues')

# #     def button_4_copy_click(self, **event_args):
# #       """This method is called when the button is clicked"""
# #       open_form('borrower.dashboard.foreclosure_request')

# #     def button_5_click(self, **event_args):
# #       """This method is called when the button is clicked"""
# #       open_form('borrower.dashboard.application_tracker')

# #     def button_8_click(self, **event_args):
# #       """This method is called when the button is clicked"""
# #       open_form('borrower.dashboard.discount_coupons')

# #     def button_7_click(self, **event_args):
# #       """This method is called when the button is clicked"""
# #       open_form('borrower.dashboard.view_transaction_history')

# #     def button_6_copy_click(self, **event_args):
# #       """This method is called when the button is clicked"""
      
      
# from ._anvil_designer import dashboardTemplate
# from anvil import *
# import anvil.server
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
# from ...bank_users.main_form import main_form_module
# from ...bank_users.user_form import user_module

# class dashboard(dashboardTemplate):
#     def __init__(self, **properties):
#         email = main_form_module.email
#         self.init_components(**properties)
#         self.email = main_form_module.email
#         self.user_Id = main_form_module.userId
#         user_id = self.user_Id
#         self.populate_loan_history()

        
#             # Fetch the user profile record based on the current user's email
#         user_profile = app_tables.fin_user_profile.get(customer_id=user_id)
#         if user_profile:
#             self.label_3.text = user_profile['mobile']
#             self.image_1_copy_copy.source = user_profile['user_photo']
#             self.image_1.source = user_profile['user_photo']
#             self.label_9.text = user_profile['full_name']
        
#         try:
#             customer_loans = app_tables.fin_loan_details.search(borrower_customer_id=user_id)
#             if customer_loans:
#                 print(len(customer_loans))
#                 self.label_2_copy.text = "Welcome" +" " + customer_loans[0]['borrower_full_name']
#                 self.label_7.text = customer_loans[0]['member_since']
#                 self.label_5.text = customer_loans[0]['credit_limit']
#         except anvil.tables.NoSuchRow:
#             customer_loans = []  # Handle the case when no row is found
#             alert("No data found")

#     def populate_loan_history(self):
        
#         self.data = tables.app_tables.fin_loan_details.get(borrower_customer_id=self.user_Id)

#         if not self.data:
#             Notification("No Data Available Here!").show()
#         else:
#             self.result = [{'loan_id': i['loan_id'],
#                             'loan_amount': i['loan_amount'],
#                             'tenure': i['tenure'],
#                             'interest_rate': i['interest_rate'],
#                             'total_repayment_amount': i['total_repayment_amount'],
#                             'loan_updated_status': i['loan_updated_status'] 
                            
#                            }
#                            for i in self.data]

#             self.repeating_panel_1.items = self.result

  
#     def home_main_form_link_click(self, **event_args):
#         """This method is called when the link is clicked"""
#         open_form("borrower.dashboard")

#     def button_3_click(self, **event_args):
#         """This method is called when the button is clicked"""
#         open_form('borrower.dashboard.view_loans')
        

#     def button_4_click(self, **event_args):
#         """This method is called when the button is clicked"""
#         pass  # Placeholder

#     def outlined_button_2_click(self, **event_args):
#         open_form('borrower.dashboard.foreclosure_request')

#     def outlined_button_7_click(self, **event_args):
#         pass  # Placeholder

#     def about_main_form_link_click(self, **event_args):
#         open_form('borrower.dashboard.dashboard_about')

#     def notification_link_click(self, **event_args):
#         open_form('borrower.dashboard.notification')

#     def wallet_dashboard_link_click(self, **event_args):
#         customer_id = self.user_Id
#         email = self.email
#         anvil.server.call('fetch_profile_data_and_insert', email, customer_id)
#         open_form('wallet.wallet')

#     def logout_click(self, **event_args):
#         alert("Logged out successfully")
#         anvil.users.logout()
#         open_form('bank_users.main_form')

#     def borrower_dashboard_product_link_click(self, **event_args):
#         """This method is called when the link is clicked"""
#         pass  # Placeholder

#     def contact_main_form_link_click(self, **event_args):
#         open_form('borrower.dashboard.dashboard_contact')

#     def Report_A_Problem_click(self, **event_args):
#         open_form('borrower.dashboard.dashboard_report_a_problem')

#     def view_profile(self, **event_args):
#         """This method is called when the button is clicked"""
#         open_form('borrower.dashboard.borrower_profile')

#     def outlined_button_06_click(self, **event_args):
#         pass  # Placeholder

#     def button_1_click(self, **event_args):
      

#             try:
#                 existing_loans = app_tables.fin_loan_details.search(
#                     borrower_customer_id=self.user_Id,
#                     loan_updated_status=q.any_of(
#                         q.like('accept%'),
#                         q.like('Approved%'),
#                         q.like('approved%'),
#                         q.like('under process%'),
#                         q.like('foreclosure%'),
#                         q.like('disbursed loan%'),
#                         q.like('Disbursed loan%'),
#                         q.like('Under Process%')
#                     )
#                 )
#                 num_existing_loans = len(existing_loans)
#                 print(f"User ID: {self.user_Id}, Existing Loans: {num_existing_loans}")

#                 if num_existing_loans >= 5:
#                     alert("You already have 5 loans. Cannot open a new loan request.")
#                 else:
#                     wallet_row = app_tables.fin_wallet.get(customer_id=self.user_Id)

#                     if wallet_row and wallet_row['wallet_id'] is not None:
#                         open_form('borrower.dashboard.new_loan_request')
#                     else:
#                         alert("Wallet not found. Please create a wallet.")

#             except anvil.tables.TableError as e:
#                 if "Row not found" in str(e):
#                     alert("No data found.")
#                 else:
#                     alert("Error fetching existing loans.")

#     def button_2_click(self, **event_args):
#         """This method is called when the button is clicked"""
#         open_form('borrower.dashboard.today_dues')

#     def button_4_copy_click(self, **event_args):
#         """This method is called when the button is clicked"""
#         open_form('borrower.dashboard.foreclosure_request')

#     def button_5_click(self, **event_args):
#         """This method is called when the button is clicked"""
#         open_form('borrower.dashboard.application_tracker')

#     def button_8_click(self, **event_args):
#         """This method is called when the button is clicked"""
#         open_form('borrower.dashboard.discount_coupons')

#     def button_7_click(self, **event_args):
#         """This method is called when the button is clicked"""
#         open_form('borrower.dashboard.view_transaction_history')

#     def button_6_copy_click(self, **event_args):
#         """This method is called when the button is clicked"""
#         open_form('borrower.dashboard.extension_loan_request')

#     def button_12_click(self, **event_args):
#       """This method is called when the button is clicked"""
#       open_form('borrower.dashboard.borrower_profile')

#     # def button_11_click(self, **event_args):
#     #   """This method is called when the button is clicked"""
#     #   email = main_form_module.email

#     #     user_profile = app_tables.fin_user_profile.get(email_user=email)

#     #     if user_profile:
#     #         user_id = user_profile['customer_id']

#     #         try:
#     #             existing_loans = app_tables.fin_loan_details.search(
#     #                 borrower_customer_id=user_id,
#     #                 loan_updated_status=q.any_of(
#     #                     q.like('accept%'),
#     #                     q.like('Approved%'),
#     #                     q.like('approved%'),
#     #                     q.like('under process%'),
#     #                     q.like('foreclosure%'),
#     #                     q.like('disbursed loan%'),
#     #                     q.like('Disbursed loan%'),
#     #                     q.like('Under Process%')
#     #                 )
#     #             )
#     #             num_existing_loans = len(existing_loans)
#     #             print(f"User ID: {user_id}, Existing Loans: {num_existing_loans}")

#     #             if num_existing_loans >= 5:
#     #                 alert("You already have 5 loans. Cannot open a new loan request.")
#     #             else:
#     #                 wallet_row = app_tables.fin_wallet.get(customer_id=user_id)

#     #                 if wallet_row and wallet_row['wallet_id'] is not None:
#     #                     open_form('borrower.dashboard.new_loan_request')
#     #                 else:
#     #                     alert("Wallet not found. Please create a wallet.")

#     #         except anvil.tables.TableError as e:
#     #             if "Row not found" in str(e):
#     #                 alert("No data found.")
#     #             else:
#     #                 alert("Error fetching existing loans.")



from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...bank_users.main_form import main_form_module
from ...bank_users.user_form import user_module

class dashboard(dashboardTemplate):
    def __init__(self, **properties):
        email = main_form_module.email
        self.init_components(**properties)
        self.email = main_form_module.email
        self.user_Id = main_form_module.userId
        user_id = self.user_Id
        self.populate_loan_history()

        wallet = app_tables.fin_wallet.get(customer_id=self.user_Id)
        if wallet:
          self.label_8.text = wallet['wallet_amount']

        user_profile = app_tables.fin_user_profile.get(customer_id=user_id)
        if user_profile:
            self.label_3.text = user_profile['mobile']
            self.image_1_copy_copy.source = user_profile['user_photo']
            

    def populate_loan_history(self):
        try:
            customer_loans = app_tables.fin_loan_details.search(borrower_customer_id=self.user_Id)
            if customer_loans:
                self.label_2_copy.text = "Welcome" + " " + customer_loans[0]['borrower_full_name']
                self.label_7.text = customer_loans[0]['member_since']
                self.label_5.text = customer_loans[0]['credit_limit']
                self.data = [{'loan_id': loan['product_name'], 'loan_amount': loan['loan_amount'],
                              'tenure': loan['tenure'], 'interest_rate': loan['interest_rate'],
                              'total_repayment_amount': round(loan['total_repayment_amount'], 2),
                              'loan_updated_status': loan['loan_updated_status']} for loan in customer_loans]
                self.repeating_panel_1.items = self.data
            else:
                Notification("No Data Available Here!").show()
        except anvil.tables.NoSuchRow:
            alert("No data found")

    def home_main_form_link_click(self, **event_args):
        open_form("borrower.dashboard")

    def button_3_click(self, **event_args):
        open_form('borrower.dashboard.view_loans')

    def outlined_button_2_click(self, **event_args):
        open_form('borrower.dashboard.foreclosure_request')

    def about_main_form_link_click(self, **event_args):
        open_form('borrower.dashboard.dashboard_about')

    def notification_link_click(self, **event_args):
        open_form('borrower.dashboard.notification')

    def wallet_dashboard_link_click(self, **event_args):
        customer_id = self.user_Id
        email = self.email
        anvil.server.call('fetch_profile_data_and_insert', email, customer_id)
        open_form('wallet.wallet')

    def logout_click(self, **event_args):
        alert("Logged out successfully")
        anvil.users.logout()
        open_form('bank_users.main_form')

    def contact_main_form_link_click(self, **event_args):
        open_form('borrower.dashboard.dashboard_contact')

    def Report_A_Problem_click(self, **event_args):
        open_form('borrower.dashboard.dashboard_report_a_problem')

    def view_profile(self, **event_args):
        open_form('borrower.dashboard.borrower_profile')

    def button_1_click(self, **event_args):
        try:
            existing_loans = app_tables.fin_loan_details.search(
                borrower_customer_id=self.user_Id,
                loan_updated_status=q.any_of(
                    q.like('accept%'),
                    q.like('Approved%'),
                    q.like('approved%'),
                    q.like('under process%'),
                    q.like('foreclosure%'),
                    q.like('disbursed loan%'),
                    q.like('Disbursed loan%'),
                    q.like('Under Process%')
                )
            )
            num_existing_loans = len(existing_loans)
            if num_existing_loans >= 5:
                alert("You already have 5 loans. Cannot open a new loan request.")
            else:
                wallet_row = app_tables.fin_wallet.get(customer_id=self.user_Id)
                if wallet_row and wallet_row['wallet_id'] is not None:
                    open_form('borrower.dashboard.new_loan_request')
                else:
                    alert("Wallet not found. Please create a wallet.")
        except anvil.tables.TableError as e:
            alert("Error fetching existing loans.")

    def button_2_click(self, **event_args):
        open_form('borrower.dashboard.today_dues')

    def button_4_copy_click(self, **event_args):
        open_form('borrower.dashboard.foreclosure_request')

    def button_5_click(self, **event_args):
        open_form('borrower.dashboard.application_tracker')

    def button_8_click(self, **event_args):
        open_form('borrower.dashboard.discount_coupons')

    def button_7_click(self, **event_args):
        open_form('borrower.dashboard.view_transaction_history')

    def button_6_copy_click(self, **event_args):
        open_form('borrower.dashboard.extension_loan_request')

    def button_12_click(self, **event_args):
        open_form('borrower.dashboard.borrower_profile')

    def toggle_panel_visibility(self):
        # Toggle the visibility of content_panel_copy_3
        self.content_panel_copy_3.visible = not self.content_panel_copy_3.visible
        self.panel_visible = self.content_panel_copy_3.visible
      
    def button_9_click(self, **event_args):
      """This method is called when the button is clicked"""
      self.toggle_panel_visibility()

    def image_3_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      try:
            existing_loans = app_tables.fin_loan_details.search(
                borrower_customer_id=self.user_Id,
                loan_updated_status=q.any_of(
                    q.like('accept%'),
                    q.like('Approved%'),
                    q.like('approved%'),
                    q.like('under process%'),
                    q.like('foreclosure%'),
                    q.like('disbursed loan%'),
                    q.like('Disbursed loan%'),
                    q.like('Under Process%')
                )
            )
            num_existing_loans = len(existing_loans)
            if num_existing_loans >= 5:
                alert("You already have 5 loans. Cannot open a new loan request.")
            else:
                wallet_row = app_tables.fin_wallet.get(customer_id=self.user_Id)
                if wallet_row and wallet_row['wallet_id'] is not None:
                    open_form('borrower.dashboard.new_loan_request')
                else:
                    alert("Wallet not found. Please create a wallet.")
      except anvil.tables.TableError as e:
          alert("Error fetching existing loans.")

    def image_4_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form('borrower.dashboard.today_dues')

    def image_5_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form('borrower.dashboard.view_loans')

    def image_7_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form('borrower.dashboard.foreclosure_request')

    def image_6_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form('borrower.dashboard.application_tracker')

    def image_8_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form('borrower.dashboard.extension_loan_request')

    def image_9_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form('borrower.dashboard.view_transaction_history')

    def image_10_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form('borrower.dashboard.discount_coupons')

    def button_4_click(self, **event_args):
      """This method is called when the button is clicked"""
      pass

    def image_1_copy_copy_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form('borrower.dashboard.borrower_profile')
      
