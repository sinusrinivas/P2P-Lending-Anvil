from ._anvil_designer import choose_grooup_categorisTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class choose_grooup_categoris(choose_grooup_categorisTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products.add_group')

  def button_2_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products.add_product_categories_and_groups')

  # def link_1_click(self, **event_args):
  #   """This method is called when the link is clicked"""
  #   open_form('admin.dashboard.manage_products')

  def button_1_copy_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products')
