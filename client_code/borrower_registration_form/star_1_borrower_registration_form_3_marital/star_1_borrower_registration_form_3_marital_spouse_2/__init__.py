from ._anvil_designer import star_1_borrower_registration_form_3_marital_spouse_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_3_marital_spouse_2(star_1_borrower_registration_form_3_marital_spouse_2Template):
  def __init__(self,user_id, **properties):
    # Set Form properties and Data Bindings.
    self.userId = user_id
    user_data=app_tables.fin_user_profile.get(customer_id=user_id)
    if user_data:
      self.borrower_spouse_profession.text=user_data['spouse_designation']
      self.borrower_company_name.text=user_data['spouse_company_name']
      self.borrower_registration_company_adress_text.text=user_data['spouse_company_address']
      user_data.update()
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_home_button_click(self, **event_args):
    open_form('bank_users.user_form')

  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_3_marital.star_1_borrower_registration_form_3_marital_spouse_1',user_id=self.userId)

  def button_next_click(self, **event_args):
    spouse_company_name = self.borrower_company_name.text
    spouse_company_address = self.borrower_registration_company_adress_text.text
    spouse_profficen = self.borrower_spouse_profession.text
    user_id = self.userId
    anvil.server.call('add_borrower_step5',spouse_company_name,spouse_company_address,spouse_profficen,user_id)
    open_form('borrower_registration_form.star_1_borrower_registration_form_3_marital.star_1_borrower_registration_form_3_marital_spouse_3',user_id=user_id)