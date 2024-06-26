from ._anvil_designer import adminTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..main_form import main_form_module


class admin(adminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id=main_form_module.userId
    user_data=app_tables.fin_user_profile.get(customer_id=self.user_id)
    if user_data:
      self.image_1.source= user_data['user_photo']


    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    value_to_pass = self.loan_id.text
    open_form('admin.dashboard.loan_management.not_payable_amount.view_profile_9', value_to_pass)
 
