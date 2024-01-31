from ._anvil_designer import lender_registration_form_2_marriedTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class lender_registration_form_2_married(lender_registration_form_2_marriedTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.userId = user_id
    user_data=app_tables.fin_user_profile.get(customer_id=user_id)
    if user_data:
      self.choose_person_drop_down_1.selected_value=user_data['another_person']
      user_data.update()


    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    open_form('bank_users.user_form')

  def button_next_click(self, **event_args):
    another_person = self.choose_person_drop_down_1.selected_value
    user_id = self.userId
    if not another_person or another_person not in ['Father', 'Mother', 'Spouse', 'Other']:
      Notification("Please select a valid marital status").show()
    else:
      anvil.server.call('add_lendor_married',another_person,user_id)
      if another_person == 'Father':
        open_form('',user_id = user_id)
      elif another_person == 'Mother':
        open_form('',user_id = user_id)
      elif another_person == 'Spouse':
        open_form('',user_id = user_id)
      elif another_person == 'Other':
        open_form('',user_id = user_id)
      else:
        open_form('lendor_registration_form.lender_registration_form_3',user_id = user_id)


  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.lender_registration_form_2_marital_details',user_id=self.userId)
    # Any code you write here will run before the form opens.
