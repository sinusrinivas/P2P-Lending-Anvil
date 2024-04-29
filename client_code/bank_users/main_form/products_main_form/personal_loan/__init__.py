from ._anvil_designer import personal_loanTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class personal_loan(personal_loanTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_16_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form.products_main_form.personal_loan.travel_loan')

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form.products_main_form.personal_loan.marriage_loan')

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form.products_main_form.personal_loan.debt_consolidation_loan')

  def link_14_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form.products_main_form.personal_loan.credit_card_loan')

  def link_15_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form.products_main_form.personal_loan.home_renovation_loan')

  def link_17_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form.products_main_form.personal_loan.medical_loan')

  def link_18_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form.products_main_form.personal_loan.educational_loan')

  def link_20_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form.products_main_form.business_loan')

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
