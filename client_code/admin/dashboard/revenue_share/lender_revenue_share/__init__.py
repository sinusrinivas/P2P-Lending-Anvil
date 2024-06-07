from ._anvil_designer import lender_revenue_shareTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import open_form



class lender_revenue_share(lender_revenue_shareTemplate):
  def __init__(self, customer_id, **properties):
    # self.selected_row = selected_row
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.loan_data = app_tables.fin_loan_details.get(lender_customer_id=customer_id)
    if self.loan_data:
        # Fetch user type from user_profile based on borrower_customer_id
        # user_profile_data = app_tables.fin_user_profile.get(customer_id=self.loan_data['borrower_customer_id'])
        # if user_profile_data:
        #     self.label_34.text = user_profile_data['usertype']

        self.label_1.text = self.loan_data['loan_id']
        self.label_2.text = self.loan_data['loan_amount']
        self.label_3.text = self.loan_data['lender_returns']
        self.label_4.text = self.loan_data['r']
        # # self.label_10.text = self.loan_data['application_status']
        # # self.label_12.text = self.loan_data['min_amount']
        # # self.label_14.text = self.loan_data['max_amount']
        # self.label_16.text = self.loan_data['interest_rate']
        # self.label_18.text = self.loan_data['borrower_loan_created_timestamp']
        # self.label_20.text = self.loan_data['total_repayment_amount']
        # # self.label_22.text = self.loan_data['total_payments_made']
        # # self.label_24.text = self.loan_data['member_rom']
        # self.label_26.text = self.loan_data['beseem_score']
        # self.label_28.text = self.loan_data['borrower_email_id']
        # self.label_30.text = self.loan_data['tenure']
        # self.label_32.text = self.loan_data['loan_updated_status']
