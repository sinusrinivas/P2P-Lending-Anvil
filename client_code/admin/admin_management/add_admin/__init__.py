from ._anvil_designer import add_adminTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date
from .... import admin


class add_admin(add_adminTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # self.user_id = main_form_module.userId
        self.date_lable.text = date.today().strftime('%d %b %Y')
        self.customer_id = anvil.server.call('generate_admin_id')
        print(self.customer_id)
        # Any code you write here will run before the form opens.
        user = anvil.users.get_user()
        # Check if a user is logged in
        if user:
            # Fetch the user profile record based on the current user's email
            user_profile = app_tables.fin_user_profile.get(email_user=user['email'])
            # Check if the user profile record is found
            if user_profile:
                # Access the user ID from the user profile record
                self.user_mail = user_profile['email_user']
                self.user_name = user_profile['full_name']
                print(self.user_mail)
                print(self.user_name)

    def save_all_fields_click(self, **event_args):
        email = self.admin_email.text 
        name = self.admin_name.text
        mobile_no = int(self.mobile_number.text)
        dob = self.dob.date
        gender = self.gender.selected_value
        role = self.role.selected_value
        password = self.create_password_text.text
        hashed_password = anvil.server.call('hash_password', password)
        retype = self.re_enter_password.text
        created_date = date.today()
        status = True
        ref_admin_name = self.user_name
        ref_admin_email = self.user_mail
        customer_id = self.customer_id
        
        if email and name and mobile_no and dob and gender and role and password:
            if password == retype:  # Check if passwords match
                result = admin.add_admin_details(email, name, mobile_no, dob, gender, role, hashed_password, created_date, status, ref_admin_name, ref_admin_email, customer_id)
                if result:
                    self.label_7.text = "Data added Successfully"
                else:
                    self.label_7.text = "User already exists"
            else:
                alert("Passwords do not match. Please re-enter.")
        else:
            alert("Fill all the fields")

    def clear_function_click(self, **event_args):
        open_form()
