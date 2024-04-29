from ._anvil_designer import educational_loanTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class educational_loan(educational_loanTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def home_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form')

  def about_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form.about_main_form')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form.products_main_form')

  def contact_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form.contact_main_form')

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.user_issue.user_bugreports')

  def button_10_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.main_form.investNow_applyForLoan')

