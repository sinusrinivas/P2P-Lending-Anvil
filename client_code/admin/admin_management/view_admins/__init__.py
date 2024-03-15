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
        admin_emails = anvil.server.call('get_admin_emails')

        # Clear the repeating panel
        self.repeating_panel.items = []

        # Populate the repeating panel with fetched data
        for email in admin_emails:
            # Call the server function to fetch admin details based on email
            admin_details = anvil.server.call('get_admin_details', email)
            if admin_details:
                # Append the admin details to the repeating panel items
                self.repeating_panel.items.append(admin_details)
