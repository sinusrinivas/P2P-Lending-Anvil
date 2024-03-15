from ._anvil_designer import admin_managementTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .add_admin import add_admin

class admin_management(admin_managementTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    

  def home_click(self, **event_args):
    open_form('admin.dashboard')

  def logout__click(self, **event_args):
    anvil.users.logout()
    open_form('bank_users.main_form')

  def add_peopless(self, **event_args):
    self.content_panel.add_component(add_admin(),full_width_row=True)

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
    

  