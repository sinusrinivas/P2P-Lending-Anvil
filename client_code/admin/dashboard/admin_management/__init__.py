from ._anvil_designer import admin_managementTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .add_admin import add_admin

class admin_management(admin_managementTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.user_type = self.get_user_type()  # Fetch user_type based on customer_id
        self.check_user_type()

    def get_user_type(self):
        user = anvil.users.get_user()
        if user:
            email = user['email']
            profile = app_tables.fin_user_profile.get(email_user=email)
            if profile:
                return profile['usertype']
        return None

    def check_user_type(self):
        if self.user_type == 'super admin':
            self.add_people.visible = True
            self.view_people.visible = True
            self.button_1.visible = False
        elif self.user_type == 'admin':
            self.add_people.visible = False
            self.view_people.visible = False
            self.button_1.visible = True
        else:
            self.add_people.visible = False
            self.view_people.visible = False

    def home_click(self, **event_args):
        open_form('admin.dashboard')

    def logout__click(self, **event_args):
        anvil.users.logout()
        open_form('bank_users.main_form')

    def add_peopless(self, **event_args):
        # self.content_panel.add_component(add_admin(), full_width_row=True)
        open_form('admin.dashboard.admin_management.add_admin')

    def view_people_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('admin.dashboard.admin_management.view_admins')

    def button_1_copy_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('admin.dashboard.admin_management.view_admins')

    def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('admin.dashboard.admin_management.view_admins')
