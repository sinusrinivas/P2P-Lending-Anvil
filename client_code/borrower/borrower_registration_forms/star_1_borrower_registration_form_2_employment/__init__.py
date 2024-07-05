# from ._anvil_designer import star_1_borrower_registration_form_2_employmentTemplate
# from anvil import *
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
# import re
# from datetime import date, datetime

# class star_1_borrower_registration_form_2_employment(star_1_borrower_registration_form_2_employmentTemplate):
#     def __init__(self, user_id, **properties):
#         super().__init__(**properties)
        
#         self.userId = user_id
#         self.load_user_data(user_id)
#         self.load_business_types()
#         self.load_professions()
        
#         # Set initial visibility of grid_panel_1 based on selected dropdown value
#         self.update_grid_panel_visibility()

#         # Set Form properties and Data Bindings.
#         self.init_components(**properties)

#         # Subscribe to dropdown change event
#         self.Profesion_borrower_registration_form_drop_down.set_event_handler("change", self.dropdown_change)

#     def load_user_data(self, user_id):
#         user_data = app_tables.fin_user_profile.get(customer_id=user_id)
#         if user_data is not None:
#             # Set properties directly from user_data
#             self.text_box_1.text = user_data['business_add']
#             self.text_box_2.text = user_data['business_name']
#             self.drop_down_1.selected_value=user_data['business_type']
#             self.date_picker_1.date = user_data['year_estd']
#             self.text_box_3.text = user_data['industry_type']
#             self.text_box_4.text = user_data['six_month_turnover']
            
#             # Additional fields with proper handling
#             self.text_box_5.text = user_data['din'].replace(' ', '') if 'din' in user_data else ''
#             self.text_box_6.text = user_data['cin'].replace(' ', '') if 'cin' in user_data else ''
#             self.text_box_7.text = user_data['registered_off_add'] if 'registered_off_add' in user_data else ''
            
#             # Uncomment below if file_loader_1 is used for proof verification
#             # self.file_loader_1.url = anvil.media.get_url(user_data['proof_verification'])
#         else:
#             # Handle case where user_data is None or not found
#             print(f"No user data found for user_id: {user_id}")




#     def load_business_types(self):
#         options = app_tables.fin_borrower_business_type.search()
#         self.drop_down_1.items = [option['borrower_business_type'] for option in options]

#     def load_professions(self):
#         options = app_tables.fin_borrower_profession.search()
#         profession_items = [option['borrower_profession'] for option in options]
#         if 'Business' not in profession_items:
#             profession_items.append('Business')
#         self.Profesion_borrower_registration_form_drop_down.items = profession_items

#     def update_grid_panel_visibility(self):
#         selected_value = self.Profesion_borrower_registration_form_drop_down.selected_value
#         self.grid_panel_1.visible = (selected_value == 'Business')

#     def dropdown_change(self, **event_args):
#         self.update_grid_panel_visibility()

#     def button_1_next_click(self, **event_args):
#         status_of_user = self.Profesion_borrower_registration_form_drop_down.selected_value

#         if status_of_user not in ['Student', 'Employee', 'Self employment', 'Business']:
#             Notification("Please select a valid profession status").show()
#             return

#         if not self.userId:
#             Notification("User ID is missing").show()
#             return

#         self.handle_form_submission(status_of_user)

#     def handle_form_submission(self, status_of_user):
#         if status_of_user == 'Business':
#             self.button_2_click()  # Simulate button_2_click action for Business
#         else:
#             self.grid_panel_1.visible = False

#     def button_2_click(self, **event_args):
        
#         din = self.text_box_5.text
#         cin = self.text_box_6.text
#         reg_off_add = self.text_box_7.text
#         proof_verification = self.file_loader_1_copy.file

#         if ' ' in cin:
#             Notification("Spaces are not allowed in the CIN input").show()
#             return

#         if ' ' in din:
#             Notification("Spaces are not allowed in the DIN input").show()
#             return

#         if not din or not cin or not reg_off_add or not proof_verification:
#             Notification("Please fill all the fields").show()
#             return

#         anvil.server.call('add_lendor_institutional_form_3', din, cin, reg_off_add, proof_verification, self.userId)
#         open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_3_marital', user_id=self.userId)

#     def button_1_click(self, **event_args):
#         open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment.star_1_borrower_registration_form_2_employment_business_2', user_id=self.userId)

#     def button_3_click(self, **event_args):
#         open_form("bank_users.user_form")

#     def file_loader_1(self, file, **event_args):
#         if file:
#             self.image_1.source = self.file_loader_1.file

#     def file_loader_1_copy(self, file, **event_args):
#       """This method is called when a new file is loaded into this FileLoader"""
#       if file:
#             self.image_1_copy.source = self.file_loader_1_copy.file




from ._anvil_designer import star_1_borrower_registration_form_2_employmentTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables
from datetime import date

class star_1_borrower_registration_form_2_employment(star_1_borrower_registration_form_2_employmentTemplate):
    def __init__(self, user_id, **properties):
        super().__init__(**properties)
        
        self.userId = user_id
        self.load_user_data(user_id)
        self.load_business_types()
        self.load_professions()
        
        # Set initial visibility of grid panels based on selected dropdown value
        self.update_grid_panel_visibility()

        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Subscribe to dropdown change event
        self.Profesion_borrower_registration_form_drop_down.set_event_handler("change", self.dropdown_change)

    def load_user_data(self, user_id):
        user_data = app_tables.fin_user_profile.get(customer_id=user_id)
        if user_data is not None:
            # Set properties directly from user_data
            self.text_box_1.text = user_data['business_add'] if 'business_add' in user_data else ''
            self.text_box_2.text = user_data['business_name'] if 'business_name' in user_data else ''
            self.drop_down_1.selected_value = user_data['business_type'] if 'business_type' in user_data else ''
            self.date_picker_1.date = user_data['year_estd'] if 'year_estd' in user_data else date.today()
            self.text_box_3.text = user_data['industry_type'] if 'industry_type' in user_data else ''
            self.text_box_4.text = user_data['six_month_turnover'] if 'six_month_turnover' in user_data else ''
            
            # Additional fields with proper handling
            self.text_box_5.text = user_data['din'].replace(' ', '') if 'din' in user_data else ''
            self.text_box_6.text = user_data['cin'].replace(' ', '') if 'cin' in user_data else ''
            self.text_box_7.text = user_data['registered_off_add'] if 'registered_off_add' in user_data else ''
            
            # Uncomment below if file_loader_1 is used for proof verification
            # self.file_loader_1.url = anvil.media.get_url(user_data['proof_verification'])
        else:
            # Handle case where user_data is None or not found
            print(f"No user data found for user_id: {user_id}")

    def load_business_types(self):
        options = app_tables.fin_borrower_business_type.search()
        self.drop_down_1.items = [option['borrower_business_type'] for option in options]

    def load_professions(self):
        options = app_tables.fin_borrower_profession.search()
        profession_items = [option['borrower_profession'] for option in options]
        if 'Business' not in profession_items:
            profession_items.append('Business')
        self.Profesion_borrower_registration_form_drop_down.items = profession_items

    def update_grid_panel_visibility(self):
        selected_value = self.Profesion_borrower_registration_form_drop_down.selected_value
        
        if selected_value == 'Business':
            self.grid_panel_1.visible = True
            self.grid_panel_2.visible = False
        elif selected_value == 'Student':
            self.grid_panel_1.visible = False
            self.grid_panel_2.visible = True
        else:
            self.grid_panel_1.visible = False
            self.grid_panel_2.visible = False

    def dropdown_change(self, **event_args):
        self.update_grid_panel_visibility()

    def button_1_next_click(self, **event_args):
        status_of_user = self.Profesion_borrower_registration_form_drop_down.selected_value

        if status_of_user != 'Student':
            Notification("Please select 'Student' to proceed").show()
            return

        if not self.userId:
            Notification("User ID is missing").show()
            return

        self.store_grid_panel_data()

    def store_grid_panel_data(self):
        # Retrieve data from Grid Panel 2
        text_box_1_value = self.text_box_1_in_grid_panel_2.text
        text_box_2_value = self.text_box_2_in_grid_panel_2.text
        file_upload_value = self.file_loader_in_grid_panel_2.file
        image_value = self.image_in_grid_panel_2.source
        text_area_value = self.text_area_in_grid_panel_2.text

        # Validate if necessary fields are filled
        if not text_box_1_value or not text_box_2_value or not file_upload_value or not image_value or not text_area_value:
            Notification("Please fill all fields in Grid Panel 2").show()
            return

        # Store data into fin_user_profile table
        try:
            app_tables.fin_user_profile.add_row(
                customer_id=self.userId,
                field_name_1=text_box_1_value,
                field_name_2=text_box_2_value,
                file_upload=file_upload_value,
                image_url=image_value,
                text_area_value=text_area_value
            )
            Notification("Data saved successfully").show()
        except Exception as e:
            print(f"Error storing data: {e}")
            Notification("Failed to save data. Please try again.").show()

    def button_1_click(self, **event_args):
        open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment.star_1_borrower_registration_form_2_employment_business_2', user_id=self.userId)

    def button_3_click(self, **event_args):
        open_form("bank_users.user_form")

    def file_loader_1_change(self, file, **event_args):
        """This method is called when a new file is loaded into file_loader_1"""
        if file:
            self.image_1.source = self.file_loader_1.file
