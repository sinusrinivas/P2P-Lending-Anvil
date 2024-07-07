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

  def validate_file(self, file):
    """Validate file type and size."""
    if file is None:
      return False, "No file uploaded."

    file_type = file.content_type
    file_size = len(file.get_bytes())  # Use len to get size in bytes

    if file_type not in ['image/jpeg', 'application/pdf']:
      return False, "Only JPG images and PDF files are allowed."

    if file_size > 2 * 1024 * 1024:  # 2MB limit
      return False, "File size must be less than 2MB."

    return True, ""
  
  def button_1_click(self, **event_args):
    user_id = self.userId
    # open_form('lendor_registration_form.Lender_reg_form_2',user_id=user_id)
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    qualification = self.drop_down_1.selected_value
    user_id = self.userId
    # Get the uploaded files
    tenth_class = self.file_loader_1.file 
    tenth_class = self.file_loader_2.file
    tenth_class = self.file_loader_4.file
    tenth_class = self.file_loader_7.file
    tenth_class = self.file_loader_11.file
    intermediate = self.file_loader_3.file
    intermediate = self.file_loader_5.file 
    intermediate = self.file_loader_8.file
    intermediate = self.file_loader_12.file
    btech = self.file_loader_6.file
    btech = self.file_loader_9.file
    btech = self.file_loader_13.file 
    mtech = self.file_loader_10.file
    mtech = self.file_loader_14.file
    phd = self.file_loader_15.file

    tenth_class = self.file_loader_1.file #,self.file_loader_2.file]
    tenth_class_1 = self.file_loader_2.file
    tenth_class_2 = self.file_loader_4.file
    tenth_class_3 = self.file_loader_7.file
    tenth_class_4 = self.file_loader_11.file
    intermediate = self.file_loader_3.file
    intermediate_1 = self.file_loader_5.file 
    intermediate_2 = self.file_loader_8.file
    intermediate_3 = self.file_loader_12.file
    btech = self.file_loader_6.file
    btech_1 = self.file_loader_9.file
    btech_2 = self.file_loader_13.file 
    mtech = self.file_loader_10.file
    mtech_1 = self.file_loader_14.file
    phd = self.file_loader_15.file
      
    # Validate files based on qualification
    if qualification == '10th standard' and not tenth_class:
        Notification('Please upload All document before proceeding.').show()
        return
    if qualification == '12th standard' and (not tenth_class_1 or not intermediate):
        Notification('Please upload All documents before proceeding.').show()
        return
    elif qualification == "Bachelor's degree" and (not tenth_class_2 or not intermediate_1 or not btech):
        Notification("Please upload All documents before proceeding.").show()
        return
    elif qualification == "Master's degree" and (not tenth_class_3 or not intermediate_2 or not btech_1 or not mtech):
        Notification("Please upload All documents before proceeding.").show()
        return
    elif qualification == 'PhD' and (not tenth_class_4 or not intermediate_3 or not btech_2 or not mtech_1 or not phd):
        Notification('Please upload all documents before proceeding.').show()
        return
   
    if qualification == '10th standard':
      anvil.server.call('add_education_tenth', tenth_class, user_id)
      open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment', user_id=user_id) 
    elif qualification == '12th standard':
      anvil.server.call('add_education_int', tenth_class_1, intermediate, user_id)
      open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment', user_id=user_id) 
    elif qualification == "Bachelor's degree":
      anvil.server.call('add_education_btech', tenth_class_2, intermediate_1, btech, user_id)
      open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment', user_id=user_id) 
    elif qualification == "Master's degree":
      anvil.server.call('add_education_mtech', tenth_class_3, intermediate_2, btech_1, mtech, user_id)
      open_form('borrower.borrower_registration_forms.star_1_borrower_registration_form_2_employment', user_id=user_id) 
    elif qualification == 'PhD':
      anvil.server.call('add_education_phd', tenth_class_4, intermediate_3, btech_2, mtech_1, phd, user_id)
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
    valid, message = self.validate_file(file)
    if valid:
      self.image_1.source = file
    else:
      Notification(message).show()
      self.file_loader_1.clear()
      
  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    valid, message = self.validate_file(file)
    if valid:
      self.image_2.source = file
    else:
      Notification(message).show()
      self.file_loader_2.clear()
      
  def file_loader_3_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    valid, message = self.validate_file(file)
    if valid:
      self.image_3.source = file
    else:
      Notification(message).show()
      self.file_loader_3.clear()
      
  def file_loader_4_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    valid, message = self.validate_file(file)
    if valid:
      self.image_4.source = file
    else:
      Notification(message).show()
      self.file_loader_4.clear()
  def file_loader_5_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    valid, message = self.validate_file(file)
    if valid:
      self.image_5.source = file
    else:
      Notification(message).show()
      self.file_loader_5.clear()
      
  def file_loader_6_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    valid, message = self.validate_file(file)
    if valid:
      self.image_6.source = file
    else:
      Notification(message).show()
      self.file_loader_6.clear()
      
  def file_loader_7_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    valid, message = self.validate_file(file)
    if valid:
      self.image_7.source = file
    else:
      Notification(message).show()
      self.file_loader_7.clear()
      
  def file_loader_8_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    valid, message = self.validate_file(file)
    if valid:
      self.image_8.source = file
    else:
      Notification(message).show()
      self.file_loader_8.clear()
      
  def file_loader_9_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    valid, message = self.validate_file(file)
    if valid:
      self.image_9.source = file
    else:
      Notification(message).show()
      self.file_loader_9.clear()
      
  def file_loader_10_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    valid, message = self.validate_file(file)
    if valid:
      self.image_10.source = file
    else:
      Notification(message).show()
      self.file_loader_10.clear()
      
  def file_loader_11_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    valid, message = self.validate_file(file)
    if valid:
      self.image_11.source = file
    else:
      Notification(message).show()
      self.file_loader_11.clear()
  def file_loader_12_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    valid, message = self.validate_file(file)
    if valid:
      self.image_12.source = file
    else:
      Notification(message).show()
      self.file_loader_12.clear()
      
  def file_loader_13_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    valid, message = self.validate_file(file)
    if valid:
      self.image_13.source = file
    else:
      Notification(message).show()
      self.file_loader_13.clear()
  def file_loader_14_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    valid, message = self.validate_file(file)
    if valid:
      self.image_14.source = file
    else:
      Notification(message).show()
      self.file_loader_14.clear()
      
  def file_loader_15_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    valid, message = self.validate_file(file)
    if valid:
      self.image_15.source = file
    else:
      Notification(message).show()
      self.file_loader_15.clear()
