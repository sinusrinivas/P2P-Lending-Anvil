from ._anvil_designer import borrower_portfolio_first_pageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class borrower_portfolio_first_page(borrower_portfolio_first_pageTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self.data = tables.app_tables.fin_borrower.search()

        if not self.data:
            Notification("No Data Available Here!").show()
        else:
            self.result = [{'name': i['user_name'],
                            'email': i['email_id'],
                            'ascend': i['ascend_score'],
                            'member_since': i['borrower_since'],
                            'customer_id' : i['customer_id']
                           }
                             for i in self.data]

            self.repeating_panel_1.items = self.result

    def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        # Retrieve the customer_id associated with the clicked link
        customer_id = event_args['sender'].item['customer_id']
        open_form('borrower.dashboard.borrower_portfolio', customer_id=customer_id)