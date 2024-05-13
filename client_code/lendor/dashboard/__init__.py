from ._anvil_designer import dashboardTemplate
from anvil import *
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
        email = self.email
        self.load_data(None)
        existing_loans = app_tables.fin_loan_details.search(loan_updated_status=q.any_of(
                            q.like('under process%'),
                            q.like('Under Process%'),
                            q.like('under process')))  
        self.label_9.text = str(len(existing_loans))
        investment = app_tables.fin_lender.get(customer_id=self.user_id)
        if investment:
            self.label_3.text = investment['investment']
        opening_bal = app_tables.fin_wallet.get(customer_id=self.user_id)
        if opening_bal:
            self.label_5.text = opening_bal['wallet_amount']
        

    def load_data(self,status):
      if status == 'close':
        closed_loans = app_tables.fin_loan_details.search(loan_updated_status=q.like('close%'), lender_customer_id=self.user_id)
        self.repeating_panel_1.items = self.process_data(closed_loans)
      elif status == 'disbursed loan':
        disbursed_loans = app_tables.fin_loan_details.search(loan_updated_status=q.like('disbursed loan%'), lender_customer_id=self.user_id)
        self.repeating_panel_1.items = self.process_data(disbursed_loans)

      elif status == 'under process':
        underprocess_loans = app_tables.fin_loan_details.search(loan_updated_status=q.any_of(q.like('under process%'),q.like('under process')))
        self.repeating_panel_1.items = self.process_data(underprocess_loans)

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
                    'borrower_loan_created_timestamp': loan['borrower_loan_created_timestamp']
                })
        return profiles_with_loans


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
        open_form('wallet.wallet')

    def button_1_copy_click(self, **event_args):
        self.data_grid_new_loan_request.visible = True
        self.repeating_panel_1.visible = True
        self.load_data('under process')

    def button_2_copy_click(self, **event_args):
        self.data_grid_new_loan_request.visible = True
        self.repeating_panel_1.visible = True
        self.load_data('disbursed loan')


    def button_3_copy_click(self, **event_args):
        self.data_grid_new_loan_request.visible = True
        self.repeating_panel_1.visible = True
        self.load_data('lost opportunities')

    def button_4_copy_click(self, **event_args):
        self.data_grid_new_loan_request.visible = True
        self.repeating_panel_1.visible = True
        self.load_data('close')


    def button_5_copy_click(self, **event_args):
        self.data_grid_new_loan_request.visible = True
        self.repeating_panel_1.visible = True
        self.load_data('extension')

    def button_1_click(self, **event_args):
      self.View_Loan_Requests.visible = True
      self.View_Loan_Extension.visible = True
      self.View_Loan_Foreclosure.visible = True
      self.Todays_Due.visible = True
      self.View_Loans.visible = True
      self.View_Lost_Opportunities.visible = True
      self.Change_Password.visible = True
      self.historyView_Transaction_History.visible = True
      self.View_Edit_Profile.visible = True
      self.View_Send_Notifications.visible = True