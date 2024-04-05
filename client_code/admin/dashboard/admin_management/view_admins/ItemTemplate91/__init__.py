from ._anvil_designer import ItemTemplate91Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate91(ItemTemplate91Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    #self.user_id = main_form_module.userId
    
    user_data = app_tables.fin_admin_users.search()
        
        # Iterate over each row in user_data
    for row in user_data:
            self.image_1.source = row['photo']
            #lender_customer_id = row['lender_customer_id']