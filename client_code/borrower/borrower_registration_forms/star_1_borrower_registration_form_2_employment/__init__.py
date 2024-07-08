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
            
        #     Additional fields with proper handling
        #     self.text_box_5.text = user_data['din'].replace(' ', '') if 'din' in user_data else ''
        #     self.text_box_6.text = user_data['cin'].replace(' ', '') if 'cin' in user_data else ''
        #     self.text_box_7.text = user_data['registered_off_add'] if 'registered_off_add' in user_data else ''
            
        #     # Uncomment below if file_loader_1 is used for proof verification
        #     # self.file_loader_1.url = anvil.media.get_url(user_data['proof_verification'])
        # else:
        #     # Handle case where user_data is None or not found
        #     print(f"No user data found for user_id: {user_id}")




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

# Profesion_borrower_registration_form_drop_down



from ._anvil_designer import star_1_borrower_registration_form_2_employmentTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re
from datetime import date, datetime

class star_1_borrower_registration_form_2_employment(star_1_borrower_registration_form_2_employmentTemplate):
    def __init__(self, user_id, **properties):
        super().__init__(**properties)        
        self.user_id = user_id
        
        # Initialize all grid panels as invisible
        self.grid_panel_1.visible = False
        self.grid_panel_2.visible = False
        self.grid_panel_3.visible = False
        self.grid_panel_4.visible = False
        self.grid_panel_5.visible = False
        
        # Fetch user data from the database
        user_data = app_tables.fin_user_profile.get(customer_id=user_id)
        
        if user_data:
            # Populate form fields if user data exists
            self.text_box_1.text = user_data['business_add']
            self.text_box_2.text = user_data['business_name']
            self.drop_down_1.selected_value = user_data['business_type']
            self.date_picker_1.date = user_data['year_estd']
            self.text_box_3.text = user_data['industry_type']
            self.text_box_4.text = user_data['six_month_turnover']          
            self.text_box_5.text = user_data['din'].replace(' ', '') if 'din' in user_data else ''
            self.text_box_6.text = user_data['cin'].replace(' ', '') if 'cin' in user_data else ''
            self.text_box_7.text = user_data['registered_off_add'] if 'registered_off_add' in user_data else ''
          
            self.borrower_college_name_text.text = user_data['college_name']
            self.borrower_college_id_text.text=user_data['college_id']
            self.borrower_college_address_text.text=user_data['college_address']
          
            self.drop_down_1_copy_3.selected_value = user_data['land_type']
            self.text_box_1_copy_4.text = str(user_data['total_acres'])  # Convert to string
            self.text_box_2_copy_3.text = user_data['crop_name']
            self.text_box_3_copy_2.text = user_data['farmer_earnings']

            options_2 = app_tables.fin_borrower_land_type.search()
            option_strings_2 = [str(option['land_type']) for option in options_2]
            self.drop_down_1_copy_3.items = option_strings_2
            
            # Handle initial visibility based on user type
            user_type = user_data['user_type'] if 'user_type' in user_data else ''
            self.update_visibility(user_type)
        else:
            print(f"No user data found for user_id: {user_id}")
            # Handle case where user_data is None or not found
        
        # Set up event handler for dropdown change
        self.drop_down_1.set_event_handler('change', self.drop_down_1_change_handler)
        
        # Initialize visibility of components inside grid_panel_3
        self.drop_down_2.visible = True
        self.grid_panel_4.visible = False
        self.grid_panel_5.visible = False
        
        # Set up event handler for drop_down_2 change
        self.drop_down_2.set_event_handler('change', self.drop_down_2_change_handler)
    
    def update_visibility(self, user_type):
        # Reset all grid panel visibilities
        self.grid_panel_1.visible = False
        self.grid_panel_2.visible = False
        self.grid_panel_3.visible = False
        self.grid_panel_4.visible = False
        self.grid_panel_5.visible = False
        
        # Set visibility based on user_type
        if user_type == 'Student':
            self.grid_panel_1.visible = True
        elif user_type == 'Employee':
            self.grid_panel_2.visible = True
        elif user_type == 'Self Employement':
            self.grid_panel_3.visible = True
        else:
            # Handle other user types or default case
            pass
    
    def drop_down_1_change_handler(self, **event_args):
        selected_value = self.drop_down_1.selected_value
        self.update_visibility(selected_value)
    
    def drop_down_2_change_handler(self, **event_args):
        selected_value = self.drop_down_2.selected_value
        
        if selected_value == 'Business':  # Replace with your actual dropdown values
            self.grid_panel_4.visible = True
            self.grid_panel_5.visible = False
        elif selected_value == 'Farmer':  # Replace with your actual dropdown values
            self.grid_panel_4.visible = False
            self.grid_panel_5.visible = True
        else:
            self.grid_panel_4.visible = False
            self.grid_panel_5.visible = False

    def button_1_next_click(self, **event_args):
        college_name=self.borrower_college_name_text.text
        college_id=self.borrower_college_id_text.text
        college_proof=self.borrower_college_proof_img.file
        college_address=self.borrower_college_address_text.text
        land_type = self.drop_down_1_copy_3.selected_value
        total_acres = self.text_box_1_copy_4.text
        crop_name = self.text_box_2_copy_3.text
        farmer_earnings = self.text_box_3_copy_2.text
        user_id=self.user_id
      
        selected_value_drop_down_1 = self.drop_down_1.selected_value
        selected_value_drop_down_2 = self.drop_down_2.selected_value
        if selected_value_drop_down_1 == 'Student':
          if not re.match(r'^[A-Za-z\s]+$', college_name):
              alert('enter valid college name')
              
          elif not college_name or not college_id or not college_proof or not college_address:
              Notification("please fill all requrired fields").show()
          else:
              anvil.server.call('add_borrower_student',college_name,college_id,college_proof,college_address,user_id)
              open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_3_marital',user_id=user_id)

        elif selected_value_drop_down_1 == 'Employee':
              # Validation for Employee
              # Implement validation logic for Employee if needed
              pass
    
        elif selected_value_drop_down_1 == 'Self Employement':
            # Validation for Self Employement
            # Implement validation logic for Self Employement if needed
            pass

        if selected_value_drop_down_2 == 'Business':
            # Validation for Business
            if not re.match(r'^[A-Za-z\s]+$', land_type):
                alert('Enter valid land type')
            elif not land_type or not total_acres:
                Notification("Please fill all required fields").show()
            else:
                anvil.server.call('add_business_details', land_type, total_acres, crop_name, farmer_earnings, user_id)
                open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_3_marital', user_id=user_id)
        
        elif selected_value_drop_down_2 == 'Farmer':
        # Validation for Farmer
            if not re.match(r'^[A-Za-z\s]+$', crop_name):
                alert('Enter valid crop name')
            elif not total_acres.isdigit():
                Notification("Acres of Land should be valid").show()
            elif not farmer_earnings.isdigit():
                Notification("Yearly Income should be valid").show()
            elif not crop_name or not total_acres or not farmer_earnings:
                Notification("Please fill all the fields").show()
            else:
                anvil.server.call('add_borrower_farmer', land_type, total_acres, crop_name, farmer_earnings, user_id)
                open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_3_marital', user_id=user_id)

  
    def borrower_college_proof_img_change(self, file, **event_args):
      """This method is called when a new file is loaded into this FileLoader"""
      if file:
            self.image_1_copy_2.source = self.borrower_college_proof_img.file

    
    # def update_visibility(self, user_type):
    #     if user_type == 'Student':
    #         self.grid_panel_1.visible = True
    #         self.grid_panel_2.visible = False
    #         self.grid_panel_3.visible = False
    #         self.grid_panel_4.visible = False
    #         # Additional logic to populate grid_panel_2 components if needed
    #     elif user_type == 'Employee':
    #         self.grid_panel_1.visible = False
    #         self.grid_panel_2.visible = True
    #         self.grid_panel_3.visible = False
    #         self.grid_panel_4.visible = False        
    #     elif user_type == 'Self Employement':
    #         self.grid_panel_1.visible = False
    #         self.grid_panel_3.visible = True
    #         self.grid_panel_2.visible = False
    #         self.grid_panel_4.visible = False
    #         # Additional logic to populate grid_panel_1 components if needed
    #     else:
    #         # Handle other user types or default case
    #         self.grid_panel_1.visible = False
    #         self.grid_panel_2.visible = False
    #         self.grid_panel_3.visible = False
    #         self.grid_panel_4.visible = False
    
    # def drop_down_1_change_handler(self, **event_args):
    #     selected_value = self.drop_down_1.selected_value
    #     self.update_visibility(selected_value)

    def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('bank_users.user_form')

    

    
