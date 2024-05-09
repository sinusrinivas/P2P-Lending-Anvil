from ._anvil_designer import all_transactionTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...borrower.dashboard import main_form_module


class all_transaction(all_transactionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.repeating_panel_1.items = app_tables.fin_wallet_transactions.search()
    self.repeating_panel_1.items = app_tables.fin_wallet_transactions.search(
    transaction_type=q.any_of('deposit', 'withdraw'))
    # Any code you write here will run before the form opens.

  

  def back_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("wallet.wallet")

  def about_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor.dashboard.dasboard_about")

  def contact_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor.dashboard.dasboard_contact")

  def notification_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('lendor.dashboard.notification')

  def wallet_dashboard_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('wallet.wallet')