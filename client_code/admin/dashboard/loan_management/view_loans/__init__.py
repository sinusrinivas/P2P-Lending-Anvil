from ._anvil_designer import view_loansTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class view_loans(view_loansTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.approved_loans')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.rejected_loans')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loanst.under_process')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.open_loans')

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.closed_loans')

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.loan_disbursed')

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.lapsed_loans')

  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.default_loans')

  def button_6_copy_click(self, **event_args):
    open_form('admin.dashboard.loan_management.view_loans.not_payable_amount')

  def button_6_copy_2_click(self, **event_args):
    open_form('admin.dashboard.loan_management.view_loans.one_time_settlement')




  # new buttons
  def button_19_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.one_time_settlement')

  def button_18_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.not_payable_amount')

  def button_9_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.approved_loans')

  def button_10_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.rejected_loans')

  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.under_process')

  def button_12_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.open_loans')

  def button_13_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.loan_disbursed')

  def button_14_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.lapsed_loans')

  def button_16_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.default_loans')

  def button_17_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management.view_loans.closed_loans')

  def image_4_copy_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.loan_management.view_loans.approved_loans')

  def image_4_copy_3_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.loan_management.view_loans.rejected_loans')

  def image_4_copy_5_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.loan_management.view_loans.under_process')

  def image_4_copy_7_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.loan_management.view_loans.open_loans')

  def image_4_copy_2_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.loan_management.view_loans.loan_disbursed')

  def image_4_copy_10_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.loan_management.view_loans.lapsed_loans')

  def image_4_copy_6_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.loan_management.view_loans.default_loans')

  def image_4_copy_9_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.loan_management.view_loans.closed_loans')

  def image_4_copy_8_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.loan_management.view_loans.not_payable_amount')

  def image_4_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.loan_management.view_loans.one_time_settlement')

  def button_1_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management')







    

 

