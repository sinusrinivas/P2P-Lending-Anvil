# # from ._anvil_designer import basic_registration_formTemplate
# # from anvil import *
# # import anvil.server
# # import anvil.google.auth, anvil.google.drive
# # from anvil.google.drive import app_files
# # import anvil.users
# # import anvil.tables as tables
# # import anvil.tables.query as q
# # from anvil.tables import app_tables
# # from datetime import datetime, timedelta
# # from .. import main_form
# # from .. import main_form_module
# # from ...user_form import user_module
# # import re

# # class basic_registration_form(basic_registration_formTemplate):
# #     def __init__(self, **properties):
# #         # Set Form properties and Data Bindings.
# #         self.init_components(**properties)
# #         self.email = main_form_module.email
# #         email = self.email
# #         self.user_id = user_module.find_user_id(email)
# #         print(self.user_id)

# #         user_id = self.user_id
# #         user_data = app_tables.fin_user_profile.get(customer_id=user_id)
# #         if user_data:
# #             self.full_name_text_box.text = user_data['full_name']
# #             self.gender_dd.selected_value = user_data['gender']
# #             self.date_picker_1.date = datetime.strptime(user_data['date_of_birth'], '%Y-%m-%d').date() if user_data['date_of_birth'] else None
# #             self.mobile_number_box.text = user_data['mobile']
# #             self.alternate_email_text_box.text = user_data['another_email']
# #             self.govt_id1_text_box.text = user_data['aadhaar_no']
# #             self.govt_id2_text_box.text = user_data['pan_number']
# #             self.text_box_1.text = user_data['street_adress_1']
# #             self.text_box_2.text = user_data['street_address_2']
# #             self.text_box_3.text = user_data['city']
# #             self.text_box_4.text = user_data['pincode']
# #             self.text_box_5.text = user_data['state']
# #             self.text_box_6.text = user_data['country']
# #             self.drop_down_1.selected_value = user_data['present_address']
# #             self.drop_down_2.selected_value = user_data['duration_at_address']
# #             user_data.update()

# #         options = app_tables.fin_gender.search()
# #         option_strings = [str(option['gender']) for option in options]
# #         self.gender_dd.items = option_strings

# #         options = app_tables.fin_present_address.search()
# #         option_strings = [str(option['present_address']) for option in options]
# #         self.drop_down_1.items = option_strings

# #         options = app_tables.fin_duration_at_address.search()
# #         option_strings = [str(option['duration_at_address']) for option in options]
# #         self.drop_down_2.items = option_strings

# #     def submit_btn_click(self, **event_args):
# #         """This method is called when the button is clicked"""
# #         full_name = self.full_name_text_box.text
# #         gender = self.gender_dd.selected_value
# #         dob = self.date_picker_1.date.strftime('%Y-%m-%d') if self.date_picker_1.date else None
# #         mobile_no = self.mobile_number_box.text
# #         user_photo = self.registration_img_file_loader.file
# #         alternate_email = self.alternate_email_text_box.text
# #         aadhar = self.govt_id1_text_box.text
# #         aadhar_card = self.registration_img_aadhar_file_loader.file
# #         pan = self.govt_id2_text_box.text
# #         pan_card = self.registration_img_pan_file_loader.file
# #         street_adress_1 = self.text_box_1.text
# #         street_address_2 = self.text_box_2.text
# #         city = self.text_box_3.text
# #         pincode = self.text_box_4.text
# #         state = self.text_box_5.text
# #         country = self.text_box_6.text
# #         present = self.drop_down_1.selected_value
# #         duration = self.drop_down_2.selected_value

# #         user_id = self.user_id

# #         # Clear previous error messages
# #         self.full_name_label.text = ''
# #         self.dob_label.text = ''
# #         self.mobile_label.text = ''
# #         self.email_label.text = ''

# #         # Check if all fields are filled
# #         if not (full_name and gender and dob and mobile_no and alternate_email and user_photo and aadhar and aadhar_card and pan and pan_card and (street_adress_1 or street_address_2) and city and pincode and state and country and present and duration):
# #             Notification('Please fill all details').show()
# #             return
            
# #         # Validate country
# #         if not re.match(r'^[A-Za-z]+$', country):
# #             alert('Enter a valid country name')
# #             self.text_box_6.focus()
# #             return

# #         # Validate state
# #         if not re.match(r'^[A-Za-z]+$', state):
# #             alert('Enter a valid state name')
# #             self.text_box_5.focus()
# #             return

# #         # Validate city
# #         if not re.match(r'^[A-Za-z]+$', city):
# #             alert('Enter a valid city name')
# #             self.text_box_3.focus()
# #             return

# #         # Validate full name
# #         if not re.match(r'^[A-Za-z\s]+$', full_name):
# #             self.full_name_label.text = 'Enter a valid full name'
# #             self.full_name_text_box.focus()
# #             return

# #         # Validate date of birth
# #         if not dob or datetime.strptime(dob, '%Y-%m-%d').date() > datetime.now().date():
# #             alert('Enter a valid date of birth')
# #             self.date_picker_1.focus()
# #             return

# #         # Validate age (must be 18 or older)
# #         if datetime.now().date() - datetime.strptime(dob, '%Y-%m-%d').date() < timedelta(days=365 * 18):
# #             self.dob_label.text = 'You must be at least 18 years old'
# #             self.date_picker_1.focus()
# #             return

# #         # Validate mobile number
# #         if not re.match(r'^\d{10}$', mobile_no):
# #             self.mobile_label.text = 'Enter valid mobile no'
# #             self.mobile_number_box.focus()
# #             return

# #         # Validate alternate email
# #         if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', alternate_email):
# #             self.email_label.text = 'Enter a valid email address'
# #             self.alternate_email_text_box.focus()
# #             return

        

# #         # Check if the entered alternate email matches the existing alternate email for the user
# #         user_data = app_tables.fin_user_profile.get(customer_id=user_id)
# #         if user_data and alternate_email == user_data['email_user']:
# #             alert('Alternate email already exists')
# #             self.alternate_email_text_box.focus()
# #             return

# #         # Calculate user age
# #         user_age = datetime.now().year - datetime.strptime(dob, '%Y-%m-%d').year - ((datetime.now().month, datetime.now().day) < (datetime.strptime(dob, '%Y-%m-%d').month, datetime.strptime(dob, '%Y-%m-%d').day))

# #         # Call server function to add basic details
# #         anvil.server.call('add_basic_details', full_name, gender, dob, mobile_no, user_photo, alternate_email,
# #                           aadhar, aadhar_card, pan, pan_card, street_adress_1, street_address_2, city, pincode,
# #                           state, country, user_id, user_age, present, duration)
# #         Notification("Basic details form filled up submitted successfully").show()

# #         # Navigate to the appropriate form based on user type
# #         if user_data['usertype'] == 'lender':
# #             open_form('lendor.lendor_registration_forms.lender_registration_form_1_education_form', user_id=user_id)
# #         elif user_data['usertype'] == 'borrower':
# #             open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_1_education', user_id=user_id)
# #         else:
# #             open_form('bank_users.user_form')

#     # def registration_img_aadhar_file_loader_change(self, file, **event_args):
#     #     # Function to handle aadhar card file upload event
#     #     if file is not None:
#     #         # Display the image in an Image component
#     #         self.image_aadhar.source = self.registration_img_aadhar_file_loader.file

#     # def registration_img_pan_file_loader_change(self, file, **event_args):
#     #     # Function to handle pan card file upload event
#     #     if file is not None:
#     #         # Display the image in an Image component
#     #         self.image_pan.source = self.registration_img_pan_file_loader.file

#     # def registration_img_file_loader_change(self, file, **event_args):
#     #     # Function to handle user photo file upload event
#     #     if file is not None:
#     #         # Display the image in an Image component
#     #         self.image_profile.source = self.registration_img_file_loader.file

#     # def gender_dd_change(self, **event_args):
#     #     """This method is called when an item is selected"""
#     #     pass

#     # def logout_click(self, **event_args):
#     #     """This method is called when the button is clicked"""
#     #     alert("Logged out successfully")
#     #     anvil.users.logout()
#     #     open_form('bank_users.main_form')







# # from ._anvil_designer import basic_registration_formTemplate
# # from anvil import *
# # import anvil.server
# # import anvil.google.auth, anvil.google.drive
# # from anvil.google.drive import app_files
# # import anvil.users
# # import anvil.tables as tables
# # import anvil.tables.query as q
# # from anvil.tables import app_tables
# # from datetime import datetime, timedelta
# # from .. import main_form
# # from .. import main_form_module
# # from ...user_form import user_module
# # import re

# # class basic_registration_form(basic_registration_formTemplate):
# #     def __init__(self, **properties):
# #         # Set Form properties and Data Bindings.
# #         self.init_components(**properties)
# #         self.email = main_form_module.email
# #         email = self.email
# #         self.user_id = user_module.find_user_id(email)
# #         print(self.user_id)

# #         user_id = self.user_id
# #         user_data = app_tables.fin_user_profile.get(customer_id=user_id)
# #         if user_data:
# #             self.full_name_text_box.text = user_data['full_name']
# #             self.gender_dd.selected_value = user_data['gender']
# #             self.date_picker_1.date = datetime.strptime(user_data['date_of_birth'], '%Y-%m-%d').date() if user_data['date_of_birth'] else None
# #             self.mobile_number_box.text = user_data['mobile']
# #             self.alternate_email_text_box.text = user_data['another_email']
# #             self.govt_id1_text_box.text = user_data['aadhaar_no']
# #             self.govt_id2_text_box.text = user_data['pan_number']
# #             self.text_box_1.text = user_data['street_adress_1']
# #             self.text_box_2.text = user_data['street_address_2']
# #             self.text_box_3.text = user_data['city']
# #             self.text_box_4.text = user_data['pincode']
# #             self.text_box_5.text = user_data['state']
# #             self.text_box_6.text = user_data['country']
# #             self.drop_down_1.selected_value = user_data['present_address']
# #             self.drop_down_2.selected_value = user_data['duration_at_address']
# #             user_data.update()

# #         options = app_tables.fin_gender.search()
# #         option_strings = [str(option['gender']) for option in options]
# #         self.gender_dd.items = option_strings

# #         options = app_tables.fin_present_address.search()
# #         option_strings = [str(option['present_address']) for option in options]
# #         self.drop_down_1.items = option_strings

# #         options = app_tables.fin_duration_at_address.search()
# #         option_strings = [str(option['duration_at_address']) for option in options]
# #         self.drop_down_2.items = option_strings

# #         # Add event handlers for real-time validation
# #         self.full_name_text_box.add_event_handler('change', self.validate_full_name)
# #         self.date_picker_1.add_event_handler('change', self.validate_dob)
# #         self.mobile_number_box.add_event_handler('change', self.validate_mobile_no)
# #         self.alternate_email_text_box.add_event_handler('change', self.validate_alternate_email)
# #         self.text_box_3.add_event_handler('change', self.validate_city)
# #         self.text_box_5.add_event_handler('change', self.validate_state)
# #         self.text_box_6.add_event_handler('change', self.validate_country)

# #     def validate_full_name(self, **event_args):
# #         full_name = self.full_name_text_box.text
# #         if re.match(r'^[A-Za-z\s]+$', full_name):
# #             self.full_name_label.text = ''
# #         else:
# #             self.full_name_label.text = 'Enter a valid full name'

# #     def validate_dob(self, **event_args):
# #         dob = self.date_picker_1.date.strftime('%Y-%m-%d') if self.date_picker_1.date else None
# #         if dob and datetime.strptime(dob, '%Y-%m-%d').date() <= datetime.now().date():
# #             self.dob_label.text = ''
# #             if datetime.now().date() - datetime.strptime(dob, '%Y-%m-%d').date() < timedelta(days=365 * 18):
# #                 self.dob_label.text = 'You must be at least 18 years old'
# #         else:
# #             self.dob_label.text = 'Enter a valid date of birth'

# #     def validate_mobile_no(self, **event_args):
# #         mobile_no = self.mobile_number_box.text
# #         if re.match(r'^\d{10}$', mobile_no):
# #             self.mobile_label.text = ''
# #         else:
# #             self.mobile_label.text = 'Enter valid mobile no'

# #     def validate_alternate_email(self, **event_args):
# #         alternate_email = self.alternate_email_text_box.text
# #         if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', alternate_email):
# #             self.email_label.text = ''
# #         else:
# #             self.email_label.text = 'Enter a valid email address'

# #     def validate_city(self, **event_args):
# #         city = self.text_box_3.text
# #         if re.match(r'^[A-Za-z]+$', city):
# #             alert('Enter a valid city name')

# #     def validate_state(self, **event_args):
# #         state = self.text_box_5.text
# #         if re.match(r'^[A-Za-z]+$', state):
# #             alert('Enter a valid state name')

# #     def validate_country(self, **event_args):
# #         country = self.text_box_6.text
# #         if re.match(r'^[A-Za-z]+$', country):
# #             alert('Enter a valid country name')

# #     def submit_btn_click(self, **event_args):
# #         """This method is called when the button is clicked"""
# #         full_name = self.full_name_text_box.text
# #         gender = self.gender_dd.selected_value
# #         dob = self.date_picker_1.date.strftime('%Y-%m-%d') if self.date_picker_1.date else None
# #         mobile_no = self.mobile_number_box.text
# #         user_photo = self.registration_img_file_loader.file
# #         alternate_email = self.alternate_email_text_box.text
# #         aadhar = self.govt_id1_text_box.text
# #         aadhar_card = self.registration_img_aadhar_file_loader.file
# #         pan = self.govt_id2_text_box.text
# #         pan_card = self.registration_img_pan_file_loader.file
# #         street_adress_1 = self.text_box_1.text
# #         street_address_2 = self.text_box_2.text
# #         city = self.text_box_3.text
# #         pincode = self.text_box_4.text
# #         state = self.text_box_5.text
# #         country = self.text_box_6.text
# #         present = self.drop_down_1.selected_value
# #         duration = self.drop_down_2.selected_value

# #         user_id = self.user_id

# #         # Clear previous error messages
# #         self.full_name_label.text = ''
# #         self.dob_label.text = ''
# #         self.mobile_label.text = ''
# #         self.email_label.text = ''

# #         # Validate country
# #         if not re.match(r'^[A-Za-z]+$', country):
# #             alert('Enter a valid country name')
# #             self.text_box_6.focus()
# #             return

# #         # Validate state
# #         if not re.match(r'^[A-Za-z]+$', state):
# #             alert('Enter a valid state name')
# #             self.text_box_5.focus()
# #             return

# #         # Validate city
# #         if not re.match(r'^[A-Za-z]+$', city):
# #             alert('Enter a valid city name')
# #             self.text_box_3.focus()
# #             return

# #         # Validate full name
# #         if not re.match(r'^[A-Za-z\s]+$', full_name):
# #             self.full_name_label.text = 'Enter a valid full name'
# #             self.full_name_text_box.focus()
# #             return

# #         # Validate date of birth
# #         if not dob or datetime.strptime(dob, '%Y-%m-%d').date() > datetime.now().date():
# #             alert('Enter a valid date of birth')
# #             self.date_picker_1.focus()
# #             return

# #         # Validate age (must be 18 or older)
# #         if datetime.now().date() - datetime.strptime(dob, '%Y-%m-%d').date() < timedelta(days=365 * 18):
# #             self.dob_label.text = 'You must be at least 18 years old'
# #             self.date_picker_1.focus()
# #             return

# #         # Validate mobile number
# #         if not re.match(r'^\d{10}$', mobile_no):
# #             self.mobile_label.text = 'Enter valid mobile no'
# #             self.mobile_number_box.focus()
# #             return

# #         # Validate alternate email
# #         if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', alternate_email):
# #             self.email_label.text = 'Enter a valid email address'
# #             self.alternate_email_text_box.focus()
# #             return

# #         # Check if all fields are filled
# #         if not (full_name and gender and dob and mobile_no and user_photo and aadhar and aadhar_card and pan and pan_card and (street_adress_1 or street_address_2) and city and pincode and state and country and present and duration):
# #             Notification('Please fill all details').show()
# #             return

# #         # Check if the entered alternate email matches the existing alternate email for the user
# #         user_data = app_tables.fin_user_profile.get(customer_id=user_id)
# #         if user_data and alternate_email == user_data['email_user']:
# #             alert('Alternate email already exists')
# #             self.alternate_email_text_box.focus()
# #             return

# #         # Calculate user age
# #         user_age = datetime.now().year - datetime.strptime(dob, '%Y-%m-%d').year - ((datetime.now().month, datetime.now().day) < (datetime.strptime(dob, '%Y-%m-%d').month, datetime.strptime(dob, '%Y-%m-%d').day))

# #         # Call server function to add basic details
# #         anvil.server.call('add_basic_details', full_name, gender, dob, mobile_no, user_photo, alternate_email,
# #                           aadhar, aadhar_card, pan, pan_card, street_adress_1, street_address_2, city, pincode,
# #                           state, country, user_id, user_age, present, duration)
# #         Notification("Basic details form filled up submitted successfully").show()

# #         # Navigate to the appropriate form based on user type
# #         if user_data['usertype'] == 'lender':
# #             open_form('lendor.lendor_registration_forms.lender_registration_form_1_education_form', user_id=user_id)
# #         elif user_data['usertype'] == 'borrower':
# #             open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_1_education', user_id=user_id)
# #         else:
# #             open_form('bank_users.user_form')

#     # def registration_img_aadhar_file_loader_change(self, file, **event_args):
#     #     # Function to handle aadhar card file upload event
#     #     if file is not None:
#     #         # Display the image in an Image component
#     #         self.image_aadhar.source = self.registration_img_aadhar_file_loader.file

#     # def registration_img_pan_file_loader_change(self, file, **event_args):
#     #     # Function to handle pan card file upload event
#     #     if file is not None:
#     #         # Display the image in an Image component
#     #         self.image_pan.source = self.registration_img_pan_file_loader.file

#     # def registration_img_file_loader_change(self, file, **event_args):
#     #     # Function to handle user photo file upload event
#     #     if file is not None:
#     #         # Display the image in an Image component
#     #         self.image_profile.source = self.registration_img_file_loader.file

#     # def gender_dd_change(self, **event_args):
#     #     """This method is called when an item is selected"""
#     #     pass

#     # def logout_click(self, **event_args):
#     #     """This method is called when the button is clicked"""
#     #     alert("Logged out successfully")
#     #     anvil.users.logout()
#     #     open_form('bank_users.main_form') 






from ._anvil_designer import basic_registration_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta
from .. import main_form
from .. import main_form_module
from ...user_form import user_module
import re


class basic_registration_form(basic_registration_formTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.email = main_form_module.email
        email = self.email
        self.user_id = user_module.find_user_id(email)
        print(self.user_id)

        user_id = self.user_id
        user_data = app_tables.fin_user_profile.get(customer_id=user_id)
        if user_data:
            self.full_name_text_box.text = user_data['full_name']
            self.gender_dd.selected_value = user_data['gender']
            self.date_picker_1.date = datetime.strptime(user_data['date_of_birth'], '%Y-%m-%d').date() if user_data['date_of_birth'] else None
            self.mobile_number_box.text = user_data['mobile']
            self.alternate_email_text_box.text = user_data['another_email']
            self.govt_id1_text_box.text = user_data['aadhaar_no']
            self.govt_id2_text_box.text = user_data['pan_number']
            self.text_box_1.text = user_data['street_adress_1']
            self.text_box_2.text = user_data['street_address_2']
            self.text_box_3.text = user_data['city']
            self.text_box_4.text = user_data['pincode']
            self.text_box_5.text = user_data['state']
            self.text_box_6.text = user_data['country']
            self.drop_down_1.selected_value = user_data['present_address']
            self.drop_down_2.selected_value = user_data['duration_at_address']
            user_data.update()

        options = app_tables.fin_gender.search()
        option_strings = [str(option['gender']) for option in options]
        self.gender_dd.items = option_strings

        options = app_tables.fin_present_address.search()
        option_strings = [str(option['present_address']) for option in options]
        self.drop_down_1.items = option_strings

        options = app_tables.fin_duration_at_address.search()
        option_strings = [str(option['duration_at_address']) for option in options]
        self.drop_down_2.items = option_strings

        # Add event handlers for real-time validation
        self.full_name_text_box.add_event_handler('change', self.validate_full_name)
        self.date_picker_1.add_event_handler('change', self.validate_dob)
        self.mobile_number_box.add_event_handler('change', self.validate_mobile_no)
        self.alternate_email_text_box.add_event_handler('change', self.validate_alternate_email)
        self.text_box_3.add_event_handler('change', self.validate_city)
        self.text_box_5.add_event_handler('change', self.validate_state)
        self.text_box_6.add_event_handler('change', self.validate_country)
        self.text_box_4.add_event_handler('change',self.validate_zip)
        

    def validate_full_name(self, **event_args):
        full_name = self.full_name_text_box.text
        if re.match(r'^[A-Za-z\s]+$', full_name):
            self.full_name_text_box.background = None
        else:
            self.full_name_text_box.background = '#FF0000'  # Red background for invalid input
            
    def validate_zip(self, **event_args):
        zip = self.text_box_4.text
        if re.match(r'^\d+$', zip):
            self.text_box_4.background = None
        else:
            self.text_box_4.background = '#FF0000'
        
    def validate_dob(self, **event_args):
        dob = self.date_picker_1.date.strftime('%Y-%m-%d') if self.date_picker_1.date else None
        if dob and datetime.strptime(dob, '%Y-%m-%d').date() <= datetime.now().date():
            self.date_picker_1.background = None
        else:
            self.date_picker_1.background = '#FF0000'  # Red background for invalid input

    def validate_mobile_no(self, **event_args):
        mobile_no = self.mobile_number_box.text
        if re.match(r'^\d{10}$', mobile_no):
            self.mobile_number_box.background = None
        else:
            self.mobile_number_box.background = '#FF0000'  # Red background for invalid input

    def validate_alternate_email(self, **event_args):
        alternate_email = self.alternate_email_text_box.text
        if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', alternate_email):
            self.alternate_email_text_box.background = None
        else:
            self.alternate_email_text_box.background = '#FF0000'  # Red background for invalid input

    def validate_city(self, **event_args):
        city = self.text_box_3.text
        if re.match(r'^[A-Za-z]+$', city):
            self.text_box_3.background = None
        else:
            self.text_box_3.background = '#FF0000'  # Red background for invalid input

    def validate_state(self, **event_args):
        state = self.text_box_5.text
        if re.match(r'^[A-Za-z]+$', state):
            self.text_box_5.background = None
        else:
            self.text_box_5.background = '#FF0000'  # Red background for invalid input

    def validate_country(self, **event_args):
        country = self.text_box_6.text
        if re.match(r'^[A-Za-z]+$', country):
            self.text_box_6.background = None
        else:
            self.text_box_6.background = '#FF0000 ' # Red background for invalid 

    

    def submit_btn_click(self, **event_args):
        """This method is called when the button is clicked"""
        full_name = self.full_name_text_box.text
        gender = self.gender_dd.selected_value
        dob = self.date_picker_1.date.strftime('%Y-%m-%d') if self.date_picker_1.date else None
        mobile_no = self.mobile_number_box.text
        user_photo = self.registration_img_file_loader.file
        alternate_email = self.alternate_email_text_box.text
        aadhar = self.govt_id1_text_box.text
        aadhar_card = self.registration_img_aadhar_file_loader.file
        pan = self.govt_id2_text_box.text
        pan_card = self.registration_img_pan_file_loader.file
        street_adress_1 = self.text_box_1.text
        street_address_2 = self.text_box_2.text
        city = self.text_box_3.text
        pincode = self.text_box_4.text
        state = self.text_box_5.text
        country = self.text_box_6.text
        present = self.drop_down_1.selected_value
        duration = self.drop_down_2.selected_value

        user_id = self.user_id

        # Clear previous error backgrounds
        self.full_name_text_box.background = None
        self.date_picker_1.background = None
        self.mobile_number_box.background = None
        self.alternate_email_text_box.background = None
        self.text_box_3.background = None
        self.text_box_5.background = None
        self.text_box_6.background = None

        # Validate country
        if not re.match(r'^[A-Za-z]+$', country):
            alert('Enter a valid country name')
            self.text_box_6.background = '#FF0000 '  # Highlight input field with red background
            self.text_box_6.focus()
            return

        # Validate state
        if not re.match(r'^[A-Za-z]+$', state):
            alert('Enter a valid state name')
            self.text_box_5.background = '#FF0000 '
            self.text_box_5.focus()
            return

        # Validate city
        if not re.match(r'^[A-Za-z]+$', city):
            alert('Enter a valid city name')
            self.text_box_3.background = '#FF0000 '
            self.text_box_3.focus()
            return

        # Validate full name
        if not re.match(r'^[A-Za-z\s]+$', full_name):
            self.full_name_text_box.background = '#FF0000 '
            self.full_name_text_box.focus()
            return

        # Validate date of birth
        if not dob or datetime.strptime(dob, '%Y-%m-%d').date() > datetime.now().date():
            alert('Enter a valid date of birth')
            self.date_picker_1.background = '#FF0000 '
            self.date_picker_1.focus()
            return

        # Validate age (must be 18 or older)
        if datetime.now().date() - datetime.strptime(dob, '%Y-%m-%d').date() < timedelta(days=365 * 18):
            alert('You must be at least 18 years old')
            self.date_picker_1.background = '#FF0000 '
            self.date_picker_1.focus()
            return

        # Validate mobile number
        if not re.match(r'^\d{10}$', mobile_no):
            alert('Enter valid mobile no')
            self.mobile_number_box.background = '#FF0000 '
            self.mobile_number_box.focus()
            return

        # Validate alternate email
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', alternate_email):
            alert('Enter a valid email address')
            self.alternate_email_text_box.background = '#FF0000 '
            self.alternate_email_text_box.focus()
            return

        # Check if all fields are filled
        if not (full_name and gender and dob and mobile_no and alternate_email and user_photo and aadhar and aadhar_card and pan and pan_card and (street_adress_1 or street_address_2) and city and pincode and state and country and present and duration):
            Notification('Please fill all details').show()
            return

        # Check if the entered alternate email matches the existing alternate email for the user
        user_data = app_tables.fin_user_profile.get(customer_id=user_id)
        if user_data and alternate_email == user_data['email_user']:
            alert('Alternate email already exists')
            self.alternate_email_text_box.background = '#ffb3b3'
            self.alternate_email_text_box.focus()
            return

        # Calculate user age
        user_age = datetime.now().year - datetime.strptime(dob, '%Y-%m-%d').year - ((datetime.now().month, datetime.now().day) < (datetime.strptime(dob, '%Y-%m-%d').month, datetime.strptime(dob, '%Y-%m-%d').day))

        # Call server function to add basic details
        anvil.server.call('add_basic_details', full_name, gender, dob, mobile_no, user_photo, alternate_email,
                          aadhar, aadhar_card, pan, pan_card, street_adress_1, street_address_2, city, pincode,
                          state, country, user_id, user_age, present, duration)
        Notification("Basic details form filled up submitted successfully").show()

        # Navigate to the appropriate form based on user type
        if user_data['usertype'] == 'lender':
            open_form('lendor.lendor_registration_forms.lender_registration_form_1_education_form', user_id=user_id)
        elif user_data['usertype'] == 'borrower':
            open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_1_education', user_id=user_id)
        else:
            open_form('bank_users.user_form')


    def registration_img_aadhar_file_loader_change(self, file, **event_args):
        # Function to handle aadhar card file upload event
        if file is not None:
            # Display the image in an Image component
            self.image_aadhar.source = self.registration_img_aadhar_file_loader.file

    def registration_img_pan_file_loader_change(self, file, **event_args):
        # Function to handle pan card file upload event
        if file is not None:
            # Display the image in an Image component
            self.image_pan.source = self.registration_img_pan_file_loader.file

    def registration_img_file_loader_change(self, file, **event_args):
        # Function to handle user photo file upload event
        if file is not None:
            # Display the image in an Image component
            self.image_profile.source = self.registration_img_file_loader.file

    def gender_dd_change(self, **event_args):
        """This method is called when an item is selected"""
        pass

    def logout_click(self, **event_args):
        """This method is called when the button is clicked"""
        alert("Logged out successfully")
        anvil.users.logout()
        open_form('bank_users.main_form') 

    def label_04_show(self, **event_args):
        """This method is called when the Label is shown on the screen"""
        pass






# from ._anvil_designer import basic_registration_formTemplate
# from anvil import *
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
# from datetime import datetime, timedelta
# from .. import main_form
# from .. import main_form_module
# from ...user_form import user_module
# import re

# class basic_registration_form(basic_registration_formTemplate):
#     def __init__(self, **properties):
#         # Set Form properties and Data Bindings.
#         self.init_components(**properties)
#         self.email = main_form_module.email
#         email = self.email
#         self.user_id = user_module.find_user_id(email)
#         print(self.user_id)

#         user_id = self.user_id
#         user_data = app_tables.fin_user_profile.get(customer_id=user_id)
#         if user_data:
#             self.full_name_text_box.text = user_data['full_name']
#             self.gender_dd.selected_value = user_data['gender']
#             self.date_picker_1.date = datetime.strptime(user_data['date_of_birth'], '%Y-%m-%d').date() if user_data['date_of_birth'] else None
#             self.mobile_number_box.text = user_data['mobile']
#             self.alternate_email_text_box.text = user_data['another_email']
#             self.govt_id1_text_box.text = user_data['aadhaar_no']
#             self.govt_id2_text_box.text = user_data['pan_number']
#             self.text_box_1.text = user_data['street_adress_1']
#             self.text_box_2.text = user_data['street_address_2']
#             self.text_box_3.text = user_data['city']
#             self.text_box_4.text = user_data['pincode']
#             self.text_box_5.text = user_data['state']
#             self.text_box_6.text = user_data['country']
#             self.drop_down_1.selected_value = user_data['present_address']
#             self.drop_down_2.selected_value = user_data['duration_at_address']
#             user_data.update()

#         options = app_tables.fin_gender.search()
#         option_strings = [str(option['gender']) for option in options]
#         self.gender_dd.items = option_strings

#         options = app_tables.fin_present_address.search()
#         option_strings = [str(option['present_address']) for option in options]
#         self.drop_down_1.items = option_strings

#         options = app_tables.fin_duration_at_address.search()
#         option_strings = [str(option['duration_at_address']) for option in options]
#         self.drop_down_2.items = option_strings

#         # Add event handlers for real-time validation
#         self.full_name_text_box.add_event_handler('change', self.validate_full_name)
#         self.date_picker_1.add_event_handler('change', self.validate_dob)
#         self.mobile_number_box.add_event_handler('change', self.validate_mobile_no)
#         self.alternate_email_text_box.add_event_handler('change', self.validate_alternate_email)
#         self.text_box_3.add_event_handler('change', self.validate_city)
#         self.text_box_5.add_event_handler('change', self.validate_state)
#         self.text_box_6.add_event_handler('change', self.validate_country)

#     def set_border_red(self, component):
#         component.role = 'border-red'
#         component.style['border'] = '1px solid red'

#     def clear_border(self, component):
#         component.role = None
#         component.style['border'] = ''

#     def validate_full_name(self, **event_args):
#         full_name = self.full_name_text_box.text
#         if re.match(r'^[A-Za-z\s]+$', full_name):
#             self.clear_border(self.full_name_text_box)
#         else:
#             self.set_border_red(self.full_name_text_box)

#     def validate_dob(self, **event_args):
#         dob = self.date_picker_1.date.strftime('%Y-%m-%d') if self.date_picker_1.date else None
#         if dob and datetime.strptime(dob, '%Y-%m-%d').date() <= datetime.now().date():
#             self.clear_border(self.date_picker_1)
#         else:
#             self.set_border_red(self.date_picker_1)

#     def validate_mobile_no(self, **event_args):
#         mobile_no = self.mobile_number_box.text
#         if re.match(r'^\d{10}$', mobile_no):
#             self.clear_border(self.mobile_number_box)
#         else:
#             self.set_border_red(self.mobile_number_box)

#     def validate_alternate_email(self, **event_args):
#         alternate_email = self.alternate_email_text_box.text
#         if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', alternate_email):
#             self.clear_border(self.alternate_email_text_box)
#         else:
#             self.set_border_red(self.alternate_email_text_box)

#     def validate_city(self, **event_args):
#         city = self.text_box_3.text
#         if re.match(r'^[A-Za-z]+$', city):
#             self.clear_border(self.text_box_3)
#         else:
#             self.set_border_red(self.text_box_3)

#     def validate_state(self, **event_args):
#         state = self.text_box_5.text
#         if re.match(r'^[A-Za-z]+$', state):
#             self.clear_border(self.text_box_5)
#         else:
#             self.set_border_red(self.text_box_5)

#     def validate_country(self, **event_args):
#         country = self.text_box_6.text
#         if re.match(r'^[A-Za-z]+$', country):
#             self.clear_border(self.text_box_6)
#         else:
#             self.set_border_red(self.text_box_6)

#     def submit_btn_click(self, **event_args):
#         """This method is called when the button is clicked"""
#         full_name = self.full_name_text_box.text
#         gender = self.gender_dd.selected_value
#         dob = self.date_picker_1.date.strftime('%Y-%m-%d') if self.date_picker_1.date else None
#         mobile_no = self.mobile_number_box.text
#         user_photo = self.registration_img_file_loader.file
#         alternate_email = self.alternate_email_text_box.text
#         aadhar = self.govt_id1_text_box.text
#         aadhar_card = self.registration_img_aadhar_file_loader.file
#         pan = self.govt_id2_text_box.text
#         pan_card = self.registration_img_pan_file_loader.file
#         street_adress_1 = self.text_box_1.text
#         street_address_2 = self.text_box_2.text
#         city = self.text_box_3.text
#         pincode = self.text_box_4.text
#         state = self.text_box_5.text
#         country = self.text_box_6.text
#         present = self.drop_down_1.selected_value
#         duration = self.drop_down_2.selected_value

#         user_id = self.user_id

#         # Clear previous error borders
#         self.clear_border(self.full_name_text_box)
#         self.clear_border(self.date_picker_1)
#         self.clear_border(self.mobile_number_box)
#         self.clear_border(self.alternate_email_text_box)
#         self.clear_border(self.text_box_3)
#         self.clear_border(self.text_box_5)
#         self.clear_border(self.text_box_6)

#         # Validate country
#         if not re.match(r'^[A-Za-z]+$', country):
#             alert('Enter a valid country name')
#             self.set_border_red(self.text_box_6)
#             self.text_box_6.focus()
#             return

#         # Validate state
#         if not re.match(r'^[A-Za-z]+$', state):
#             alert('Enter a valid state name')
#             self.set_border_red(self.text_box_5)
#             self.text_box_5.focus()
#             return

#         # Validate city
#         if not re.match(r'^[A-Za-z]+$', city):
#             alert('Enter a valid city name')
#             self.set_border_red(self.text_box_3)
#             self.text_box_3.focus()
#             return

#         # Validate full name
#         if not re.match(r'^[A-Za-z\s]+$', full_name):
#             self.set_border_red(self.full_name_text_box)
#             self.full_name_text_box.focus()
#             return

#         # Validate date of birth
#         if not dob or datetime.strptime(dob, '%Y-%m-%d').date() > datetime.now().date():
#             alert('Enter a valid date of birth')
#             self.set_border_red(self.date_picker_1)
#             self.date_picker_1.focus()
#             return

#         # Validate age (must be 18 or older)
#         if datetime.now().date() - datetime.strptime(dob, '%Y-%m-%d').date() < timedelta(days=365 * 18):
#             alert('You must be at least 18 years old')
#             self.set_border_red(self.date_picker_1)
#             self.date_picker_1.focus()
#             return

#         # Validate mobile number
#         if not re.match(r'^\d{10}$', mobile_no):
#             alert('Enter valid mobile no')
#             self.set_border_red(self.mobile_number_box)
#             self.mobile_number_box.focus()
#             return

#         # Validate alternate email
#         if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', alternate_email):
#             alert('Enter a valid email address')
#             self.set_border_red(self.alternate_email_text_box)
#             self.alternate_email_text_box.focus()
#             return

#         # Check if all fields are filled
#         if not (full_name and gender and dob and mobile_no and alternate_email and user_photo and aadhar and aadhar_card and pan and pan_card and (street_adress_1 or street_address_2) and city and pincode and state and country and present and duration):
#             Notification('Please fill all details').show()
#             return

#         # Check if the entered alternate email matches the existing alternate email for the user
#         user_data = app_tables.fin_user_profile.get(customer_id=user_id)
#         if user_data and alternate_email == user_data['email_user']:
#             alert('Alternate email already exists')
#             self.set_border_red(self.alternate_email_text_box)
#             self.alternate_email_text_box.focus()
#             return

#         # Calculate user age
#         user_age = datetime.now().year - datetime.strptime(dob, '%Y-%m-%d').year - ((datetime.now().month, datetime.now().day) < (datetime.strptime(dob, '%Y-%m-%d').month, datetime.strptime(dob, '%Y-%m-%d').day))

#         # Call server function to add basic details
#         anvil.server.call('add_basic_details', full_name, gender, dob, mobile_no, user_photo, alternate_email,
#                           aadhar, aadhar_card, pan, pan_card, street_adress_1, street_address_2, city, pincode,
#                           state, country, user_id, user_age, present, duration)
#         Notification("Basic details form filled up submitted successfully").show()

#         # Navigate to the appropriate form based on user type
#         if user_data['usertype'] == 'lender':
#             open_form('lendor.lendor_registration_forms.lender_registration_form_1_education_form', user_id=user_id)
#         elif user_data['usertype'] == 'borrower':
#             open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_1_education', user_id=user_id)
#         else:
#             open_form('bank_users.user_form')

#     def registration_img_aadhar_file_loader_change(self, file, **event_args):
#         # Function to handle aadhar card file upload event
#         if file is not None:
#             # Display the image in an Image component
#             self.image_aadhar.source = self.registration_img_aadhar_file_loader.file

#     def registration_img_pan_file_loader_change(self, file, **event_args):
#         # Function to handle pan card file upload event
#         if file is not None:
#             # Display the image in an Image component
#             self.image_pan.source = self.registration_img_pan_file_loader.file

#     def registration_img_file_loader_change(self, file, **event_args):
#         # Function to handle user photo file upload event
#         if file is not None:
#             # Display the image in an Image component
#             self.image_profile.source = self.registration_img_file_loader.file

#     def gender_dd_change(self, **event_args):
#         """This method is called when an item is selected"""
#         pass

#     def logout_click(self, **event_args):
#         """This method is called when the button is clicked"""
#         alert("Logged out successfully")
#         anvil.users.logout()
#         open_form('bank_users.main_form')
