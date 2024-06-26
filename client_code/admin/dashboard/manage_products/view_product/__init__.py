from ._anvil_designer import view_productTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class view_product(view_productTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.fetch_and_populate_data()
        self.repeating_panel_1.set_event_handler('x-refresh', self.refresh_repeating_panel)

    def fetch_and_populate_data(self):
        self.data = tables.app_tables.fin_product_details.search()

        if not self.data:
            Notification("No Data Available Here!").show()
        else:
            self.result = [{'product_id': i['product_id'],
                            'product_group': i['product_group'],
                            'product_categories': i['product_categories'],
                            'processing_fee': i['processing_fee'],
                            'product_name': i['product_name'],
                            'product_description': i['product_description'],
                            'extension_fee': i['extension_fee']}
                           
                           for i in self.data]

            self.repeating_panel_1.items = self.result

    def link_1_click(self, **event_args):
        open_form('admin.dashboard.manage_products')

    def button_1_click(self, **event_args):
        open_form('admin.dashboard.manage_products.edit_form')

    def button_2_click(self, **event_args):
        open_form('admin.dashboard.manage_products.update_form')

    def button_1_copy_3_click(self, **event_args):
      open_form('admin.dashboard.manage_products')


    def refresh_repeating_panel(self, **event_args):
      self.repeating_panel_1.items = app_tables.fin_product_details.search()
        
          