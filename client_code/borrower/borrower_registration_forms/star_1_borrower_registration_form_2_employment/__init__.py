from ._anvil_designer import star_1_borrower_registration_form_2_employmentTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re
from datetime import date, datetime

# class star_1_borrower_registration_form_2_employment(star_1_borrower_registration_form_2_employmentTemplate):
#   def __init__(self,user_id, **properties):
#     self.userId = user_id
#     user_data=app_tables.fin_user_profile.get(customer_id=user_id)
#     if user_data:
#      self.Profesion_borrower_registration_form_drop_down.selected_value=user_data['profession']
#      user_data.update()

#     options = app_tables.fin_borrower_profession.search()
#     option_strings = [str(option['borrower_profession']) for option in options]
#     self.Profesion_borrower_registration_form_drop_down.items = option_strings
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#     # Any code you write here will run before the form opens.

#   def home_borrower_registration_form_copy_1_click(self, **event_args):
#     open_form('bank_users.user_form')

#   def button_1_click(self, **event_args):
#     open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_1_education',user_id=self.userId)

#   def button_1_next_click(self, **event_args):
#     status_of_user = self.Profesion_borrower_registration_form_drop_down.selected_value
#     user_id = self.userId
#     if status_of_user not in ['Student', 'Employee', 'Self employment']:
#       Notification("Please select a valid profession status").show()
#     elif not user_id:
#       Notification("User ID is missing").show()
#     else:
#      anvil.server.call('add_borrower_step2',status_of_user,user_id)
#     if status_of_user == 'Student':
#       open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment.star_1_borrower_registration_form_2_employment_student',user_id=user_id)
#     elif status_of_user == 'Employee':
#       open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment.star_1_borrower_registration_form_2_employment_emp_detail_1',user_id=user_id)
#     elif status_of_user == 'Self employment':
#       open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment.star_1_borrower_registration_form_2_self_employment',user_id=user_id) 
#     # else:
#     #   open_form('borrower_registration_form.star_1_borrower_registration_form_2_employment',user_id=user_id)
#     #   alert('Please select a valid Profesion')



# class star_1_borrower_registration_form_2_employment(star_1_borrower_registration_form_2_employmentTemplate):
#     def __init__(self, user_id, **properties):
#         self.userId = user_id
#         user_data = app_tables.fin_user_profile.get(customer_id=user_id)
        
#         # Initialize components from the first snippet
#         if user_data:
#             self.text_box_1.text = user_data['business_name']
#             self.text_box_3.text = user_data['business_add']
#             self.drop_down_1.selected_value = user_data['business_type']
#             options_2 = app_tables.fin_borrower_no_of_employees.search()
#             option_strings_2 = [str(option['borrower_no_of_employees']) for option in options_2]
#             self.drop_down_2.items = option_strings_2
#             self.drop_down_2.selected_value = user_data['employees_working']
#             user_data.update()
        
#         # Fetch all business types
#         options_1 = app_tables.fin_borrower_business_type.search()
#         option_strings_1 = [str(option['borrower_business_type']) for option in options_1]
#         self.drop_down_1.items = option_strings_1
        
#         # Fetch all professions including 'Business' from the second snippet
#         options = app_tables.fin_borrower_profession.search()
#         option_strings = [str(option['borrower_profession']) for option in options]
#         if 'Business' not in option_strings:
#             option_strings.append('Business')
#         self.Profesion_borrower_registration_form_drop_down.items = option_strings

#         # Set initial visibility of grid_panel_1 based on selected dropdown value
#         self.grid_panel_1.visible = self.Profesion_borrower_registration_form_drop_down.selected_value == 'Business'

#         # Set Form properties and Data Bindings.
#         self.init_components(**properties)

#         # Any code you write here will run before the form opens.

#         # Subscribe to dropdown change event
#         self.Profesion_borrower_registration_form_drop_down.set_event_handler("change", self.dropdown_change)

#     def dropdown_change(self, **event_args):
#         selected_value = self.Profesion_borrower_registration_form_drop_down.selected_value
#         self.grid_panel_1.visible = (selected_value == 'Business')

#     def home_borrower_registration_form_copy_1_click(self, **event_args):
#         open_form('bank_users.user_form')

#     def button_1_click(self, **event_args):
#         open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_1_education', user_id=self.userId)

#     def button_1_next_click(self, **event_args):
#         status_of_user = self.Profesion_borrower_registration_form_drop_down.selected_value
#         user_id = self.userId

#         if status_of_user not in ['Student', 'Employee', 'Self employment', 'Business']:
#             Notification("Please select a valid profession status").show()
#         elif not user_id:
#             Notification("User ID is missing").show()
#         else:
#             # Call server function to handle the form submission
#             self.handle_form_submission(status_of_user, user_id)

#     def handle_form_submission(self, status_of_user, user_id):
#         # Perform necessary actions on form submission
#         if status_of_user == 'Student':
#             open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment.star_1_borrower_registration_form_2_employment_student', user_id=user_id)
#         elif status_of_user == 'Employee':
#             open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment.star_1_borrower_registration_form_2_emp_detail_1', user_id=user_id)
#         elif status_of_user == 'Self employment':
#             open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment.star_1_borrower_registration_form_2_self_employment', user_id=user_id)
#         elif status_of_user == 'Business':
#             self.button_2_click()  # Simulate button_2_click action for Business
#         else:
#             # Hide the grid panel for other cases
#             self.grid_panel_1.visible = False

#     def button_2_click(self, **event_args):
#         business_name = self.text_box_1.text
#         business_add = self.text_box_3.text
#         business_type = self.drop_down_1.selected_value
#         employees_working = self.drop_down_2.selected_value
#         user_id = self.userId

#         if not re.match(r'^[A-Za-z\s]+$', business_name):
#             alert('Enter valid business name')
#         elif not business_name or not business_add or not business_type or not employees_working:
#             Notification("Please fill all the fields").show()
#         else:
#             anvil.server.call('add_lendor_institutional_form_1', business_name, business_add, business_type, employees_working, user_id)
#             open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment.star_1_borrower_registration_form_2_employment_business_2', user_id=user_id)

#     def button_3_click(self, **event_args):
#         open_form("bank_users.user_form")




# class star_1_borrower_registration_form_2_employment(star_1_borrower_registration_form_2_employmentTemplate):
#     def __init__(self, user_id, **properties):
#         self.userId = user_id
        
#         # Initialize components and load user data
#         self.load_user_data(user_id)
        
#         # Fetch all business types
#         self.load_business_types()

#         # Fetch all professions including 'Business'
#         self.load_professions()

#         # Set initial visibility of grid_panel_1 based on selected dropdown value
#         self.grid_panel_1.visible = self.Profesion_borrower_registration_form_drop_down.selected_value == 'Business'

#         # Set Form properties and Data Bindings.
#         self.init_components(**properties)

#         # Subscribe to dropdown change event
#         self.Profesion_borrower_registration_form_drop_down.set_event_handler("change", self.dropdown_change)

#     def load_user_data(self, user_id):
#         user_data = app_tables.fin_user_profile.get(customer_id=user_id)
#         if user_data:
#             self.date_picker_1.date = user_data['year_estd']
#             self.text_box_1.text = user_data['industry_type']
#             self.text_box_2.text = user_data['six_month_turnover']
#             # if user_data['last_six_month_bank_proof']:
#             #   self.file_loader_1.file = user_data['last_six_month_bank_proof']

#     def load_business_types(self):
#         options_1 = app_tables.fin_borrower_business_type.search()
#         option_strings_1 = [str(option['borrower_business_type']) for option in options_1]
#         self.drop_down_1.items = option_strings_1

#     def load_professions(self):
#         options = app_tables.fin_borrower_profession.search()
#         option_strings = [str(option['borrower_profession']) for option in options]
#         if 'Business' not in option_strings:
#             option_strings.append('Business')
#         self.Profesion_borrower_registration_form_drop_down.items = option_strings

#     def dropdown_change(self, **event_args):
#         selected_value = self.Profesion_borrower_registration_form_drop_down.selected_value
#         self.grid_panel_1.visible = (selected_value == 'Business')

#     def button_1_click(self, **event_args):
#         open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment.star_1_borrower_registration_form_2_employment_business_1', user_id=self.userId)

#     def home_borrower_registration_form_copy_1_click(self, **event_args):
#         open_form('bank_users.user_form')

#     def button_1_next_click(self, **event_args):
#         status_of_user = self.Profesion_borrower_registration_form_drop_down.selected_value
#         user_id = self.userId

#         if status_of_user not in ['Student', 'Employee', 'Self employment', 'Business']:
#             Notification("Please select a valid profession status").show()
#         elif not user_id:
#             Notification("User ID is missing").show()
#         else:
#             self.handle_form_submission(status_of_user, user_id)

#     def handle_form_submission(self, status_of_user, user_id):
#         if status_of_user == 'Business':
#             self.button_2_click()  # Simulate button_2_click action for Business
#         else:
#             # Handle other status_of_user cases as needed
#             self.grid_panel_1.visible = False

#     def button_2_click(self, **event_args):
#         year = self.date_picker_1.date
#         industry_type = self.text_box_1.text
#         turn_over = self.text_box_2.text
#         last_six_statements = self.file_loader_1.file
#         user_id = self.userId
        
#         # Get today's date
#         today = date.today()
        
#         if year and year.year > today.year:
#             alert("The year cannot be in the future. Please select a valid year.", title="Invalid Year")
#             return
#         elif year and year.year == today.year and year.month > today.month:
#             alert("The month cannot be in the future. Please select a valid month.", title="Invalid Month")
#             return
#         elif year and year.year == today.year and year.month == today.month and year.day > today.day:
#             alert("The date cannot be in the future. Please select a valid date.", title="Invalid Date")
#             return

#         if not year or not industry_type or not turn_over or not last_six_statements:
#             alert("Please fill all the fields", title="Missing Information")
#         else:
#             months = (datetime.now().year - year.year) * 12 + (datetime.now().month - year.month)
#             anvil.server.call('add_lendor_institutional_form_2', year, months, industry_type, turn_over, last_six_statements, user_id)
#             open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment.star_1_borrower_registration_form_2_employment_business_3', user_id=user_id)

#     def button_3_click(self, **event_args):
#         open_form("bank_users.user_form")

#     def file_loader_1_change(self, file, **event_args):
#         if file:
#             self.image_1.source = self.file_loader_1.file

class star_1_borrower_registration_form_2_employment(star_1_borrower_registration_form_2_employmentTemplate):
    def __init__(self, user_id, **properties):
        super().__init__(**properties)
        
        self.userId = user_id
        self.load_user_data(user_id)
        self.load_business_types()
        self.load_professions()
        
        # Set initial visibility of grid_panel_1 based on selected dropdown value
        self.update_grid_panel_visibility()

        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Subscribe to dropdown change event
        self.Profesion_borrower_registration_form_drop_down.set_event_handler("change", self.dropdown_change)

    def load_user_data(self, user_id):
        user_data = app_tables.fin_user_profile.get(customer_id=user_id)
        if user_data:
            self.date_picker_1.date = user_data.get('year_estd')
            self.text_box_1.text = user_data.get('industry_type')
            self.text_box_2.text = user_data.get('six_month_turnover')
            # Uncomment below if file_loader_1 is used for bank proof
            # self.file_loader_1.file = user_data.get('last_six_month_bank_proof')

            # Additional user data fields
            self.text_box_3.text = user_data.get('din', '').replace(' ', '')
            self.text_box_4.text = user_data.get('cin', '').replace(' ', '')
            self.text_box_1_copy_2.text = user_data.get('registered_off_add')
            # Uncomment below if file_loader_1 is used for proof verification
            # self.file_loader_1.url = anvil.media.get_url(user_data.get('proof_verification'))

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
        self.grid_panel_1.visible = (selected_value == 'Business')

    def dropdown_change(self, **event_args):
        self.update_grid_panel_visibility()

    def button_1_next_click(self, **event_args):
        status_of_user = self.Profesion_borrower_registration_form_drop_down.selected_value

        if status_of_user not in ['Student', 'Employee', 'Self employment', 'Business']:
            Notification("Please select a valid profession status").show()
            return

        if not self.userId:
            Notification("User ID is missing").show()
            return

        self.handle_form_submission(status_of_user)

    def handle_form_submission(self, status_of_user):
        if status_of_user == 'Business':
            self.button_2_click()  # Simulate button_2_click action for Business
        else:
            self.grid_panel_1.visible = False

    def button_2_click(self, **event_args):
        din = self.text_box_3.text
        cin = self.text_box_4.text
        reg_off_add = self.text_box_1_copy_2.text
        proof_verification = self.file_loader_1.file

        if ' ' in cin:
            Notification("Spaces are not allowed in the CIN input").show()
            return

        if ' ' in din:
            Notification("Spaces are not allowed in the DIN input").show()
            return

        if not din or not cin or not reg_off_add or not proof_verification:
            Notification("Please fill all the fields").show()
            return

        anvil.server.call('add_lendor_institutional_form_3', din, cin, reg_off_add, proof_verification, self.userId)
        open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_3_marital', user_id=self.userId)

    def button_1_click(self, **event_args):
        open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment.star_1_borrower_registration_form_2_employment_business_2', user_id=self.userId)

    def button_3_click(self, **event_args):
        open_form("bank_users.user_form")

    def file_loader_1_change(self, file, **event_args):
        if file:
            self.image_1.source = self.file_loader_1.file
