from ._anvil_designer import ItemTemplate117Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate117(ItemTemplate117Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.item = properties.get('item', {})
    self.update_display()

  def update_display(self):
    self.label_message.text = self.item['message']
    self.label_date.text = self.item['date'].strftime('%Y-%m-%d, %A')
    self.label_message.bold = not self.item['read']

  def button_pay_now_click(self, **event_args):
    if 'pay_now' in self.item:
      alert(self.item['pay_now'])