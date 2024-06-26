from ._anvil_designer import manage_dropdownsTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class manage_dropdowns(manage_dropdownsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
 


    

  def button_1_copy_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_cms')


  def button_9_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_cms.add_borrower_dropdown_details')

  def button_14_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_cms.add_lender_dropdown_details')

  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_cms.add_general_dropdowns')

  def image_4_copy_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.manage_cms.add_borrower_dropdown_details')

  def image_4_copy_10_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.manage_cms.add_lender_dropdown_details')

  def image_4_copy_5_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.manage_cms.add_general_dropdowns')



