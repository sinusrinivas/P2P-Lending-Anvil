from ._anvil_designer import navigation_bar_main_lenderTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class navigation_bar_main_lender(navigation_bar_main_lenderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def borrower_dashboard_home_linkhome_borrower_registration_button_copy_1_click(self, **event_args):
    open_form("lendor_registration_form.dashboard")


  def report_problem_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def contact_main_form_link_click(self, **event_args):
    open_form("lendor_registration_form.dasboard_contact_lendor_registration_form")

  def help_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def About_Us_click(self, **event_args):
    open_form('lendor_registration_form.dasboard_about_lendor_registration_form')
    
