from ._anvil_designer import RowTemplate72Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate72(RowTemplate72Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh_data_bindings()
    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    # self.item['next_payment'] = self.date_picker_2.date
    self.item['foreclosure_emi_num'] = int(self.text_box_3.text)
    self.item['requested_on'] = self.date_picker_1.date
    self.item.update()
    self.refresh_data_bindings()
    alert('data saved')
