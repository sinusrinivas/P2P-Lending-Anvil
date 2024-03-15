from ._anvil_designer import view_adminsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class view_admins(view_adminsTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        self.populate_admins()

    def populate_admins(self):
        # Call the server function to fetch admin users data
        admin_users = anvil.server.call('get_admin_users')

        # Clear the repeating panel
        self.repeating_panel.items = []

        # Populate the repeating panel with fetched data
        for admin_user in admin_users:
            # Extract values from the row object and create a dictionary
            admin_data = {
                'full_name': admin_user['full_name'],
                'admin_email': admin_user['admin_email'],
                'admin_role': admin_user['admin_role'],
                'ref_admin_name': admin_user['ref_admin_name'],
                'join_dates': admin_user['join_date']
                
            }
            # Append the dictionary to the repeating panel items
            self.repeating_panel.items.append(admin_data)
