from ._anvil_designer import lender_registration_form_1_education_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class lender_registration_form_1_education_form(lender_registration_form_1_education_formTemplate):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_data = app_tables.fin_user_profile.get(customer_id=user_id)
    if user_data:
      self.drop_down_1.selected_value = user_data['qualification']
      user_data.update()
    
    
    options = app_tables.fin_lendor_qualification.search()
    options_string = [str(option['lendor_qualification']) for option in options]
    self.drop_down_1.items = options_string

    # Initialize all column panels to be invisible initially
    self.column_panel_1.visible = False
    self.column_panel_2.visible = False
    self.column_panel_3.visible = False
    self.column_panel_4.visible = False
    self.column_panel_5.visible = False

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    qualification = self.drop_down_1.selected_value
    user_id = self.userId
    qualification = self.drop_down_1.selected_value
    user_id = self.userId

    # Get the uploaded files
    tenth_class_files = [self.file_loader_1.file, self.file_loader_2.file, self.file_loader_4.file, self.file_loader_7.file, self.file_loader_11.file]
    intermediate_files = [self.file_loader_3.file, self.file_loader_5.file, self.file_loader_8.file, self.file_loader_12.file]
    btech_files = [self.file_loader_6.file, self.file_loader_9.file, self.file_loader_13.file]
    mtech_files = [self.file_loader_10.file, self.file_loader_14.file]
    phd_file = self.file_loader_15.file

    # Call the appropriate server function based on the qualification
    if qualification == '10th standard':
        anvil.server.call('add_education_tenth', tenth_class_files, user_id)
    elif qualification == '12th standard':
        anvil.server.call('add_education_int', tenth_class_files, intermediate_files, user_id)
    elif qualification == "Bachelor's degree":
        anvil.server.call('add_education_btech', tenth_class_files, intermediate_files, btech_files, user_id)
    elif qualification == "Master's degree":
        anvil.server.call('add_education_mtech', tenth_class_files, intermediate_files, btech_files, mtech_files, user_id)
    elif qualification == 'PhD':
        anvil.server.call('add_education_phd', tenth_class_files, intermediate_files, btech_files, mtech_files, phd_file, user_id)
    else:
        Notification("Please select a valid qualification status").show()
    
    if qualification not in  ['10th standard', '12th standard', "Bachelor's degree", "Master's degree", 'PhD']:
      Notification("Please select a valid qualification status").show()
    elif not user_id:
      Notification("User ID is missing").show()
    else:
      anvil.server.call('add_lender_step1',qualification,user_id)
      
    # If all checks pass, proceed with server call and form navigation
    # anvil.server.call('add_education_phd', 'add_education_tenth', 'add_education_int', 'add_education_btech', 'add_education_mtech', 'add_education_phd', user_id)
    open_form('lendor.lendor_registration_forms.lender_registration_form_2', user_id=user_id)  

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    qualification = self.drop_down_1.selected_value
    # Hide all column panels first
    self.column_panel_1.visible = False
    self.column_panel_2.visible = False
    self.column_panel_3.visible = False
    self.column_panel_4.visible = False
    self.column_panel_5.visible = False
    
    # Show the appropriate column panel based on the selected qualification
    if qualification == '10th standard':
        self.column_panel_1.visible = True
    elif qualification == '12th standard':
        self.column_panel_2.visible = True
    elif qualification == "Bachelor's degree":
        self.column_panel_3.visible = True
    elif qualification == "Master's degree":
        self.column_panel_4.visible = True
    elif qualification == 'PhD':
        self.column_panel_5.visible = True

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_1.source = self.file_loader_1.file

  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_2.source = self.file_loader_2.file

  def file_loader_3_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_3.source = self.file_loader_3.file

  def file_loader_4_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_4.source = self.file_loader_4.file

  def file_loader_5_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_5.source = self.file_loader_5.file

  def file_loader_6_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_6.source = self.file_loader_6.file

  def file_loader_7_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_7.source = self.file_loader_7.file

  def file_loader_8_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_8.source = self.file_loader_8.file

  def file_loader_9_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_9.source = self.file_loader_9.file

  def file_loader_10_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_10.source = self.file_loader_10.file

  def file_loader_11_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_11.source = self.file_loader_11.file

  def file_loader_12_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_12.source = self.file_loader_12.file

  def file_loader_13_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_13.source = self.file_loader_13.file

  def file_loader_14_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_14.source = self.file_loader_14.file

  def file_loader_15_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_15.source = self.file_loader_15.file
    

    

  
   