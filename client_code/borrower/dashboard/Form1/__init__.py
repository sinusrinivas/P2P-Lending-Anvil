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
    self.content_panel_copy_2_copy_2.width = '0%'
    

    # Any code you write here will run before the form opens.

  def button_1_copy_click(self, **event_args):
    self.content_panel_copy_2_copy_2.visible = True
    self.content_panel_copy_2_copy_2.width = '100%'