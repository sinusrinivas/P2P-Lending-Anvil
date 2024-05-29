from ._anvil_designer import star_1_borrower_registration_form_2_employment_farmerTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re

class star_1_borrower_registration_form_2_employment_farmer(star_1_borrower_registration_form_2_employment_farmerTemplate):
    def __init__(self, user_id, **properties):
        self.userId = user_id
        user_data = app_tables.fin_user_profile.get(customer_id=user_id)
        if user_data:
            self.drop_down_1.selected_value = user_data['land_type']
            self.text_box_1.text = str(user_data['total_acres'])  # Convert to string
            self.text_box_2.text = user_data['crop_name']
            self.text_box_3.text = user_data['farmer_earnings']

            options_2 = app_tables.fin_borrower_land_type.search()
            option_strings_2 = [str(option['land_type']) for option in options_2]
            self.drop_down_1.items = option_strings_2

            user_data.update()

        self.init_components(**properties)

    def button_2_click(self, **event_args):
        land_type = self.drop_down_1.selected_value
        total_acres = self.text_box_1.text
        crop_name = self.text_box_2.text
        farmer_earnings = self.text_box_3.text
        user_id = self.userId
        
        # Validate inputs
        if crop_name.startswith(" "):
            alert('Crop name should not start with a space. Please enter a valid crop name.')
            return
        elif total_acres.startswith(" "):
            alert('Total acres should not start with a space. Please enter a valid total acres.')
            return
        elif farmer_earnings.startswith(" "):
            alert('Farmer earnings should not start with a space. Please enter a valid farmer earnings.')
            return
        elif not re.match(r'^[A-Za-z\s]+$', crop_name):
            alert('Enter a valid crop name.')
        elif not total_acres.isdigit():
            Notification("Acres of Land should be valid").show()
        elif not farmer_earnings.isdigit():
            Notification("Yearly Income should be valid").show()
        elif not land_type or not total_acres or not crop_name or not farmer_earnings:
            Notification("Please fill all the fields").show()
        else:
            anvil.server.call('add_borrower_farmer', land_type, total_acres, crop_name, farmer_earnings, user_id)
            open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_3_marital', user_id=self.userId)

    def button_1_click(self, **event_args):
        user_id = self.userId
        open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment', user_id=self.userId)

    def button_3_click(self, **event_args):
        open_form("bank_users.user_form")

    def file_loader_1_change(self, file, **event_args):
        """This method is called when a new file is loaded into this FileLoader"""
        if file:
            self.image_1.source = self.file_loader_1.file

    def file_loader_2_change(self, file, **event_args):
        """This method is called when a new file is loaded into this FileLoader"""
        if file:
            self.image_2.source = self.file_loader_2.file
