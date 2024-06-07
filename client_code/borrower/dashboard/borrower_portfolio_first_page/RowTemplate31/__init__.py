# from ._anvil_designer import RowTemplate31Template
# from anvil import *
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables


# class RowTemplate31(RowTemplate31Template):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#     # Assuming self.item contains the row data
#     disbursed = app_tables.fin_loan_details.search(lender_customer_id=self.item['customer_id'])
#     if disbursed:
#       self.status = disbursed['loan_updated_status']
#     else:
#       self.status = None

#     # Set visibility based on the status
#     self.link_1.visible = self.status == "disbursed loan"
#     self.lender_portfolio_component.visible = not self.link_1.visible

#   def link_1_click(self, **event_args):
#     """This method is called when the link is clicked"""
#     selected_row = self.item
#     open_form('lendor.dashboard.lender_portfolio', selected_row=selected_row)


from ._anvil_designer import RowTemplate31Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate31(RowTemplate31Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Assuming self.item contains the row data
    disbursed_list = list(app_tables.fin_loan_details.search(lender_customer_id=self.item['customer_id']))
    disbursed = disbursed_list[0] if disbursed_list else None

    if disbursed:
      self.status = disbursed['loan_updated_status']
    else:
      self.status = None

    # Set visibility based on the status
    self.link_1.visible = self.status == "disbursed loan"
    self.lender_portfolio_component.visible = not self.link_1.visible

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    selected_row = self.item
    open_form('lendor.dashboard.lender_portfolio', selected_row=selected_row)
