from ._anvil_designer import star_1_borrower_registration_form_1_educationTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_1_education(star_1_borrower_registration_form_1_educationTemplate):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # user_data = anvil.server.call('get_user_data', user_id)
    user_data = app_tables.fin_user_profile.get(customer_id=user_id)
    if user_data:
      self.drop_down_1.selected_value = user_data['qualification']
      user_data.update()
    options = app_tables.fin_borrower_qualification.search()
    options_string = [str(option['borrower_qualification']) for option in options]
    self.drop_down_1.items = options_string
    self.drop_down_1.selected_value = None

    # Initialize all column panels to be invisible initially
    self.column_panel_1.visible = False
    self.column_panel_2.visible = False
    self.column_panel_3.visible = False
    self.column_panel_4.visible = False
    self.column_panel_5.visible = False


    # Any code you write here will run before the form opens.
  # def validate_file(self, file):
  #   """Validate file type and size."""
  #   if file is None:
  #     return False, "No file uploaded."

  #   file_type = file.content_type
  #   file_size = file.get_bytes()

  #   if file_type not in ['image/jpeg', 'application/pdf']:
  #     return False, "Only JPEG images and PDF files are allowed."

  #   if len(file_size) > 2 * 1024 * 1024:  # 2MB limit
  #     return False, "File size must be less than 2MB."

  #   return True, ""

  # def handle_file_upload(self, file_loader, image_component):
  #   file = file_loader.file
  #   is_valid, message = self.validate_file(file)
  #   if not is_valid:
  #     Notification(message).show()
  #     file_loader.file = None  # Reset the file loader
  #   else:
  #     image_component.source = file

  # def file_loader_1_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_1, self.image_1)

  # def file_loader_2_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_2, self.image_2)

  # def file_loader_3_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_3, self.image_3)

  # def file_loader_4_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_4, self.image_4)

  # def file_loader_5_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_5, self.image_5)

  # def file_loader_6_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_6, self.image_6)

  # def file_loader_7_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_7, self.image_7)

  # def file_loader_8_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_8, self.image_8)

  # def file_loader_9_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_9, self.image_9)

  # def file_loader_10_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_10, self.image_10)

  # def file_loader_11_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_11, self.image_11)

  # def file_loader_12_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_12, self.image_12)

  # def file_loader_13_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_13, self.image_13)

  # def file_loader_14_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_14, self.image_14)

  # def file_loader_15_change(self, file, **event_args):
  #   self.handle_file_upload(self.file_loader_15, self.image_15)
  

  def button_1_click(self, **event_args):
    user_id = self.userId
    # open_form('lendor_registration_form.Lender_reg_form_2',user_id=user_id)
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    qualification = self.drop_down_1.selected_value
    user_id = self.userId
    # Get the uploaded files
    tenth_class_files = [self.file_loader_1.file, self.file_loader_2.file, self.file_loader_4.file, self.file_loader_7.file, self.file_loader_11.file]
    intermediate_files = [self.file_loader_3.file, self.file_loader_5.file, self.file_loader_8.file, self.file_loader_12.file]
    btech_files = [self.file_loader_6.file, self.file_loader_9.file, self.file_loader_13.file]
    mtech_files = [self.file_loader_10.file, self.file_loader_14.file]
    PhD_file = self.file_loader_15.file
    
    if qualification == '10th standard':
      anvil.server.call('add_education_tenth', tenth_class_files, user_id)
      open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment', user_id=user_id) 
    elif qualification == '12th standard':
      anvil.server.call('add_education_btech', tenth_class_files, intermediate_files, user_id)
      open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment', user_id=user_id) 
    elif qualification == "Bachelor's degree":
      anvil.server.call('add_education_btech', tenth_class_files, intermediate_files, btech_files, user_id)
      open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment', user_id=user_id) 
    elif qualification == "Master's degree":
      anvil.server.call('add_education_mtech', tenth_class_files, intermediate_files, btech_files, mtech_files, user_id)
      open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment', user_id=user_id) 
    elif qualification == 'PhD':
      anvil.server.call('add_education_phd', tenth_class_files, intermediate_files, btech_files, mtech_files, PhD_file, user_id)
      open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment', user_id=user_id) 
    else:
      Notification("Please select a valid qualification status").show()
      return 
    
    if qualification not in  ['10th standard', '12th standard', "Bachelor's degree", "Master's degree", 'PhD']:
      Notification("Please select a valid qualification status").show()
    elif not user_id:
      Notification("User ID is missing").show()
    else:
      anvil.server.call('add_borrower_step1',qualification,user_id)
    
    
    # if qualification == '10th standard':
    #   open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_1_education.star_1_borrower_registration_form_education_10th_class',user_id=user_id)
    # elif qualification == '12th standard':
    #   open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_1_education.star_1_borrower_registration_form_education_intermediate',user_id = user_id)
    # elif qualification == "Bachelor's degree":
    #   open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_1_education.star_1_borrower_registration_form_education_btech',user_id=user_id)
    # elif qualification == "Master's degree":
    #   open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_1_education.star_1_borrower_registration_form_education_mtech',user_id = user_id)
    # elif qualification == 'PhD':
    #   open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_1_education.star_1_borrower_registration_form_education_phd',user_id=user_id)
    # else:
    #   open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_1_education',user_id=user_id)

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

