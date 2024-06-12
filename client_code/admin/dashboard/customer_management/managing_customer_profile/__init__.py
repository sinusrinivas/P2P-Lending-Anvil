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


   # Any code you write here will run before the form opens.
    self.load_user_profile()
  
  def load_user_profile(self):
    """Fetch user profile details from fin_user_profile table and display in the form"""
    # Assuming there's a method to get the user profile
    # For example, get the profile of the currently logged-in user
    user = anvil.users.get_user()
    if user:
      user_profile = app_tables.fin_user_profile.get(user=user)
      if user_profile:
        self.text_box_1.text = user_profile['full_name']
        self.email_label.text = user_profile['email_user']
        self.alt_email_label.text = user_profile['another_email']
        self.photo.image = user_profile['user_photo']

  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.customer_management')


