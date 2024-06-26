# from ._anvil_designer import RowTemplate5Template
# from anvil import *
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables

# class RowTemplate5(RowTemplate5Template):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#     # Any code you write here will run before the form opens.

#   def link_1_click(self, **event_args):
#     """This method is called when the link is clicked"""
#     value_to_pass = self.link_1.text
#     open_form('admin.dashboard.manage_products.view_profile',value_to_pass)

#   def delete_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     pass


from ._anvil_designer import RowTemplate5Template
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate5(RowTemplate5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    value_to_pass = self.link_1.text
    open_form('admin.dashboard.manage_products.view_profile', value_to_pass)

  def delete_click(self, **event_args):
    """This method is called when the button is clicked"""
    product_id = self.link_1.text  # Assuming product ID is stored in the link text
    
    # Show a confirmation dialog
    confirm = alert(f"Are you sure you want to delete the product with ID {product_id}?", buttons=[("Yes", True), ("No", False)])
    
    if confirm:
      # Fetch the row from the product_details table
      product_row = app_tables.fin_product_details.get(product_id=product_id)

      if product_row:
        # Delete the row from the table
        product_row.delete()
        # Remove the item from the repeating panel
        self.parent.raise_event('x-refresh')
        # Optionally, show a success message
        alert("Product deleted successfully!")
