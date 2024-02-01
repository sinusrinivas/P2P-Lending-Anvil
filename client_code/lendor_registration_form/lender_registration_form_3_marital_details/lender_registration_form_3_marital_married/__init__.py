from ._anvil_designer import lender_registration_form_3_marital_marriedTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class lender_registration_form_3_marital_married(lender_registration_form_3_marital_marriedTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.userId = user_id
    self.another_person = none

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    open_form('bank_users.user_form')

  def radio_button_change(self, **event_args):
    selected_button = self.radio_buttons.selected_button
    self.another_person = selected_button.text.lower()
    # Hide other radio buttons
    for button in self.radio_buttons.components:
      if button != selected_button:
        button.visible = False

    # Call the server function to update the database
        anvil.server.call('update_another_person', user_profile_id=self.user_profile_id, selected_person=self.another_person)
  
  def button_next_click(self, **event_args):
    another_person = self.choose_person_drop_down_1.selected_value
    user_id = self.userId
    open_form('lendor_registration_form.lender_registration_form_4_bank_form_1')
    # if not another_person or another_person not in ['Father', 'Mother', 'Spouse', 'Other']:
    #   Notification("Please select a valid marital status").show()
    # else:
    #   anvil.server.call('add_lendor_married',another_person,user_id)
    #   if another_person == 'Father':
    #     open_form('borrower_registration_form.star_1_borrower_registration_form_begin_7',user_id = user_id)
    #   elif another_person == 'Mother':
    #     open_form('',user_id = user_id)
    #   elif another_person == 'Spouse':
    #     open_form('',user_id = user_id)
    #   elif another_person == 'Other':
    #     open_form('',user_id = user_id)
    #   else:
    #     open_form('',user_id = user_id)


  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.lender_registration_form_3_marital_details',user_id=self.userId)

    # Any code you write here will run before the form opens.
