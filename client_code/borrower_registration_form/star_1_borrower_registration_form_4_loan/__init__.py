from ._anvil_designer import star_1_borrower_registration_form_4_loanTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_4_loan(star_1_borrower_registration_form_4_loanTemplate):
  def __init__(self,user_id, **properties):
    self.init_components(**properties)
    self.userId = user_id
    user_data=app_tables.fin_user_profile.get(customer_id=user_id)
    if user_data:
      self.text_box_1.text=user_data['running_Home_Loan']
      self.text_box_2.text=user_data['running_or_live loans']
      self.text_box_3.text=user_data['other_loan']
      user_data.update()
  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_3_marital',user_id = self.userId)

  def button_2_click(self, **event_args):
    home_loan = self.text_box_1.text.lower()
    other_loan = self.text_box_2.text.lower()
    live_loan = self.text_box_3.text.lower()
    user_id = self.userId
    if home_loan not in ['yes', 'no'] or other_loan not in ['yes', 'no'] or live_loan not in ['yes', 'no']:
      Notification("Please enter 'yes' or 'no' for all fields").show()
    else:
      anvil.server.call('add_borrower_step4',home_loan,other_loan,live_loan,user_id)
      open_form('borrower_registration_form.star_1_borrower_registration_form_5_bank_1',user_id=user_id)

  def home_borrower_registration_form_click(self, **event_args):
    open_form('bank_users.user_form')
