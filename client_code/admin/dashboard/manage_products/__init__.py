from ._anvil_designer import manage_productsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class manage_products(manage_productsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.manage_producs1')

  def button_1_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.view_product')

  def button_1_copy_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.choose_grooup_categoris')

  def button_1_copy_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard')

  def button_1_copy_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.view_products_and_categories')

  def button_1_copy_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.view_categories')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products.view_products_and_categories')


  def button_9_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products.choose_grooup_categoris')

  def button_14_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products.manage_producs1')


  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products.view_product')


  def button_13_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products.view_products_and_categories')


  def button_10_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products.view_categories')

  def image_4_copy_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.manage_products.choose_grooup_categoris')

  def image_4_copy_10_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.manage_products.manage_producs1')

  def image_4_copy_2_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.manage_products.view_products_and_categories')

  def image_4_copy_3_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.manage_products.view_categories')

  def image_4_copy_5_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    open_form('admin.dashboard.manage_products.view_product')







 
 

