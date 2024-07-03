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
        message = self.item['message']
        date = self.item['date'].strftime('%Y-%m-%d, %A')
        self.label_1.text = f"{message} - {date}"
        self.label_1.bold = not self.item['read']

    def button_pay_now_click(self, **event_args):
        if 'pay_now' in self.item:
            alert(self.item['pay_now'])

    def label_1_click(self, **event_args):
        self.item['read'] = True
        self.update_display()
        open_form('borrower.dashboard.borrower_notifications.notifications_view_profile', self.item['customer_id'], self.item['loan_id'],self.label_1.text)
