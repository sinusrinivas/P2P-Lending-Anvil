from ._anvil_designer import transaction_detailsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class transaction_details(transaction_detailsTemplate):
  def __init__(self,selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_3.text = selected_row['transaction_id']
    self.label_5.text = selected_row['user_email']
    self.label_7.text = selected_row['wallet_id']
    self.label_9.text = selected_row['transaction_type']
    self.label_11.text = selected_row['amount']
    self.label_13.text = selected_row['transaction_time_stamp']
    self.label_15.text = selected_row['status']
    self.label_17.text = selected_row['receiver_email']

  def back_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('wallet.wallet.all_transaction')

  def home_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    user_request = app_tables.fin_user_profile.get(customer_id=self.user_id)
    if user_request:
      self.user_type = user_request['usertype']

    if self.user_type == "lender":
        open_form("lendor.dashboard")
    else:
        open_form("borrower.dashboard")

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
