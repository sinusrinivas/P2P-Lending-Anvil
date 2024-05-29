from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from anvil import open_form
from ...bank_users.main_form import main_form_module
from ...bank_users.user_form import user_module

class dashboard(dashboardTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.email = main_form_module.email
        self.user_id = main_form_module.userId
        self.email = self.email
        self.user_id = self.user_id
        self.components_visible = False  # Flag to keep track of component visibility
        self.load_data(None)
        existing_loans = app_tables.fin_loan_details.search(loan_updated_status=q.any_of(
                            q.like('under process%'),
                            q.like('Under Process%'),
                            q.like('under process')))
        self.label_9.text = str(len(existing_loans) or 0)
        
        investment = app_tables.fin_lender.get(customer_id=self.user_id)
        self.label_3.text = str(investment['investment'] or 0)

        opening_bal = app_tables.fin_wallet.get(customer_id=self.user_id)
        self.label_5.text = str(opening_bal['wallet_amount'] or 0)

        my_returns = app_tables.fin_lender.get(customer_id=self.user_id)
        self.label_7.text = str(my_returns['return_on_investment'] or 0)

        disbursed_loan = app_tables.fin_loan_details.search(loan_updated_status=q.like('disbursed loan%'), lender_customer_id=self.user_id)
        Lost_Opportunities =app_tables.fin_loan_details.search(loan_updated_status=q.like('lost opportunities%'), lender_customer_id=self.user_id)
        Closed = app_tables.fin_loan_details.search(loan_updated_status=q.like('close%'), lender_customer_id=self.user_id)
        Extended = app_tables.fin_loan_details.search(loan_updated_status=q.like('extension%'), lender_customer_id= self.user_id)
        self.button_1_copy.text = f"New Loan Requests ({len(existing_loans)})"
        self.button_2_copy.text = f"Loan Disbursed ({len(disbursed_loan)})"
        self.button_3_copy.text = f"Lost Opportunities ({len(Lost_Opportunities)})"
        self.button_4_copy.text = f"Closed ({len(Closed)})"
        self.button_5_copy.text = f"Extended ({len(Extended)})"
        self.column_panel_8.width = '100%'

        # Set the column_panel_3 to full height initially
        # self.column_panel_3.height = '100%'
        # self.spacer_2.height = '100%'
        
        

    def load_data(self,status):
        if status == 'close':
            closed_loans = app_tables.fin_loan_details.search(loan_updated_status=q.like('close%'), lender_customer_id=self.user_id)
            self.new_loan =len(closed_loans)
            self.repeating_panel_1.items = self.process_data(closed_loans)
        elif status == 'disbursed loan':
            disbursed_loans = app_tables.fin_loan_details.search(loan_updated_status=q.like('disbursed loan%'), lender_customer_id=self.user_id)
            self.repeating_panel_1.items = self.process_data(disbursed_loans)

        elif status == 'under process':
            underprocess_loans = app_tables.fin_loan_details.search(loan_updated_status=q.any_of(q.like('under process%'),q.like('under process')))
            self.repeating_panel_2.items = self.process_data(underprocess_loans)
            

        elif status == 'lost opportunities':
            lost_opportunities = app_tables.fin_loan_details.search(loan_updated_status=q.like('lost opportunities%'), lender_customer_id=self.user_id)
            self.repeating_panel_1.items = self.process_data(lost_opportunities)

        elif status == 'extension':
            extension_loans = app_tables.fin_loan_details.search(loan_updated_status=q.like('extension%'), lender_customer_id=self.user_id)
            self.repeating_panel_1.items = self.process_data(extension_loans)

    def process_data(self, data):
        profiles_with_loans = []
        for loan in data:
            user_profile = app_tables.fin_user_profile.get(customer_id=loan['borrower_customer_id'])
            
            if user_profile is not None:
                profiles_with_loans.append({
                    'loan_amount': loan['loan_amount'],
                    'tenure': loan['tenure'],
                    'borrower_full_name': loan['borrower_full_name'],
                    'loan_id': loan['loan_id'],
                    'bessem_value': user_profile['bessem_value'],
                    'loan_updated_status': loan['loan_updated_status'],
                    'interest_rate': loan['interest_rate'],
                    'borrower_loan_created_timestamp': loan['borrower_loan_created_timestamp'],
                    'borrower_customer_id': loan['borrower_customer_id'],
                    'beseem_score': user_profile['bessem_value'],
                    'credit_limit': loan['credit_limit'],
                    'product_name': loan['product_name']})
        return profiles_with_loans

    def toggle_components_visibility(self):      
        self.column_panel_3.visible = self.components_visible
        self.View_Loan_Requests.visible = self.components_visible
        self.View_Loan_Extension.visible = self.components_visible
        self.View_Loan_Foreclosure.visible = self.components_visible
        self.Todays_Due.visible = self.components_visible
        self.View_Loans.visible = self.components_visible
        self.View_Lost_Opportunities.visible = self.components_visible
        self.Change_Password.visible = self.components_visible
        self.historyView_Transaction_History.visible = self.components_visible
        self.View_Edit_Profile.visible = self.components_visible
        self.View_Send_Notifications.visible = self.components_visible
        # self.part_payment.visible = self.components_visible
        self.spacer_4.visible = self.components_visible
        self.image_6.visible = self.components_visible
        self.image_7.visible = self.components_visible
        self.image_8.visible = self.components_visible
        self.image_9.visible = self.components_visible
        self.image_10.visible = self.components_visible
        self.image_11.visible = self.components_visible
        self.image_12.visible = self.components_visible
        self.image_13.visible = self.components_visible
        self.image_14.visible = self.components_visible
        self.image_15.visible = self.components_visible
        # self.column_panel_3.width = '0%'
        # self.column_panel_1.width = '100%'
        
        
      

    def button_1_click(self, **event_args):
        self.components_visible = not self.components_visible  # Toggle visibility flag
        self.toggle_components_visibility()

    def button_3_click(self, **event_args):
        open_form("lendor.dashboard.view_opening_balance")

    def button_4_click(self, **event_args):
        open_form("lendor.dashboard.view_available_balance")

    def View_Loan_Requests_click(self, **event_args):
        open_form("lendor.dashboard.view_borrower_loan_request")

    def button_6_click(self, **event_args):
        open_form("lendor.dashboard.loan_disbursement")

    def Todays_Due_click(self, **event_args):
        open_form("lendor.dashboard.today_dues")

    def View_Lost_Opportunities_click(self, **event_args):
        open_form("lendor.dashboard.view_lost_oppurtunities")

    def View_Loans_click(self, **event_args):
        open_form("lendor.dashboard.lender_view_loans")

    def View_Loan_Extension_click(self, **event_args):
        open_form("lendor.dashboard.view_loan_extension_requests")

    def View_Loan_Foreclosure_click(self, **event_args):
        open_form("lendor.dashboard.view_loan_foreclosure_Requests")

    def View_Edit_Profile_click(self, **event_args):
        open_form("lendor.dashboard.lender_profile")

    def View_Send_Notifications_click(self, **event_args):
        open_form("lendor.dashboard.view_or_send_notifications")

    def Change_Password_click(self, **event_args):
        open_form("lendor.dashboard.change_password")

    def historyView_Transaction_History_click(self, **event_args):
        open_form("lendor.dashboard.view_transaction_history")

    def login_signup_button_click(self, **event_args):
        alert("Logged out successfully")
        anvil.users.logout()
        open_form('bank_users.main_form')

    def home_main_form_link_click(self, **event_args):
        open_form("lendor.dashboard")

    def about_main_form_link_click(self, **event_args):
        open_form("lendor.dashboard.dasboard_about")

    def contact_main_form_link_click(self, **event_args):
        open_form("lendor.dashboard.dasboard_contact")

    def button_click(self, **event_args):
        pass

    def button_show(self, **event_args):
        pass

    def button_hide(self, **event_args):
        pass

    def toggleswitch_1_x_change(self, **event_args):
        if self.toggleswitch_1.checked:
            self.button_status.text = "ONLINE"
            self.button_status.background = '#0876e8' 
            self.button_status.foreground = '#FFFFFF'  
            lender_row = app_tables.fin_lender.search()
            lender_row[0]['make_visibility'] = True
            lender_row[0].update()
        else:
            self.button_status.text = "OFFLINE"
            self.button_status.background = '#FFFFFF'  
            self.button_status.foreground = '#FF0000'  
            lender_row = app_tables.fin_lender.search()
            lender_row[0]['make_visibility'] = False
            lender_row[0].update()

    def notification_link_click(self, **event_args):
        open_form('lendor.dashboard.notification')

    def wallet_dashboard_link_click(self, **event_args):
        customer_id = self.user_id
        email = self.email
        anvil.server.call('fetch_profile_data_and_insert', email, customer_id)
        open_form("wallet.wallet")

    def button_1_copy_click(self, **event_args):
        self.data_grid_new_loan_request.visible = False
        self.repeating_panel_1.visible = False
        self.data_grid_1.visible = True
        self.repeating_panel_2.visible = True
        self.load_data('under process')

    def button_2_copy_click(self, **event_args):
        self.data_grid_1.visible = False
        self.repeating_panel_2.visible = False
        self.data_grid_new_loan_request.visible = True
        self.repeating_panel_1.visible = True
        self.load_data('disbursed loan')


    def button_3_copy_click(self, **event_args):
        self.data_grid_1.visible = False
        self.repeating_panel_2.visible = False
        self.data_grid_new_loan_request.visible = True
        self.repeating_panel_1.visible = True
        self.load_data('lost opportunities')

    def button_4_copy_click(self, **event_args):
        self.data_grid_1.visible = False
        self.repeating_panel_2.visible = False
        self.data_grid_new_loan_request.visible = True
        self.repeating_panel_1.visible = True
        self.load_data('close')


    def button_5_copy_click(self, **event_args):
        self.data_grid_1.visible = False
        self.repeating_panel_2.visible = False
        self.data_grid_new_loan_request.visible = True
        self.repeating_panel_1.visible = True
        self.load_data('extension')

    def borrower_dashboard_home_linkhome_borrower_registration_button_copy_1_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("lendor.dashboard")

    def About_Us_click(self, **event_args):
      open_form('lendor.dashboard.dasboard_about')

    def Report_A_Problem_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form('lendor.dashboard.dashboard_report_a_problem')

    def help_link_click(self, **event_args):
      """This method is called when the link is clicked"""
      pass


    def image_6_mouse_up(self, x, y, button, **event_args):
      open_form("lendor.dashboard.view_borrower_loan_request")

    def image_7_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form("lendor.dashboard.view_loan_extension_requests")

    def image_8_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form("lendor.dashboard.view_loan_foreclosure_Requests")

    def image_9_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form("lendor.dashboard.today_dues")

    def image_10_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form("lendor.dashboard.lender_view_loans")

    def image_11_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form("lendor.dashboard.view_lost_oppurtunities")

    def image_12_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form("lendor.dashboard.change_password")

    def image_13_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form("lendor.dashboard.view_transaction_history")

    def image_14_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form("lendor.dashboard.lender_profile")

    def image_15_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form("lendor.dashboard.view_or_send_notifications")

    def label_6_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('lendor.dashboard.my_returns')

    def image_3_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form('lendor.dashboard.my_returns')

    def button_2_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('lendor.Form1')

