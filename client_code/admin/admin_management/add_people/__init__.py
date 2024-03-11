from ._anvil_designer import add_peopleTemplate
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

class add_people(add_peopleTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.date_lable.text = date.today().strftime('%d %b %Y')
    # Any code you write here will run before the form opens.

  def save_all_fields_click(self, **event_args):
    email = self.admin_email.text 
    name = self.admin_name.text
    mobile_no = self.mobile_number.text
    dob = self.dob.date
    gender = self.gender.selected_value
    role = self.role.selected_value
    password = self.create_password_text.text
    retype = self.re_enter_password.text
    created_date = date.today()
    if email and name and mobile_no and dob and gender and role and password:
      result = admin.add_admin_details(email,name,mobile_no,dob,gender,role,password,created_date)
      if result:
        self.label_6.text = "Data added Successfully"
      else:
        self.label_6.text = "User already exist"
    else:
      alert("fill all the fields")

  def clear_function_click(self, **event_args):
    open_form()
      

    