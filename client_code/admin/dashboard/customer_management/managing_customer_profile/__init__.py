from ._anvil_designer import managing_customer_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class managing_customer_profile(managing_customer_profileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user = anvil.users.get_user()
    if user:
      user_profile = app_tables.fin_user_profile.get(user=user)
      if user_profile:
        self.text_box_1.text = user_profile['full_name']
        self.text_box_2.text = user_profile['email_user']
        self.email_id.text = user_profile['email_user']
        self.text_box_3.text = user_profile['mobile']
        self.text_box_4.text = user_profile['another_email']
        self.image_1 = user_profile['user_photo']
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.customer_management')


