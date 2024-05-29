from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('lendor.dashboard')

  def contact_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor.dashboard.dasboard_contact")

  def about_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('lendor.dashboard.dasboard_about')

  def link_11_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('lendor.dashboard.dashboard_report_a_problem')

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    customer_id = self.user_id
    email = self.email
    anvil.server.call('fetch_profile_data_and_insert', email, customer_id)
    open_form("wallet.wallet")
