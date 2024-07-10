from ._anvil_designer import lender_registration_Institutional_form_1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime
import re


class lender_registration_Institutional_form_1(lender_registration_Institutional_form_1Template):
  def __init__(self, user_id,**properties):
        self.userId = user_id
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        user_data=app_tables.fin_user_profile.get(customer_id=user_id)
        if user_data:
              self.text_box_1_copy.text = user_data['business_add']
              self.text_box_2_copy.text = user_data['business_name']
              self.drop_down_12.selected_value = user_data['business_type']
              self.date_picker_1.date = user_data['year_estd']
              self.text_box_3.text = user_data['industry_type']
              self.text_box_4.text = user_data['six_month_turnover']      
            
              self.text_box_5.text = user_data['din'].replace(' ', '') if 'din' in user_data else ''
              self.text_box_6.text = user_data['cin'].replace(' ', '') if 'cin' in user_data else ''
              self.text_box_7.text = user_data['registered_off_add'] if 'registered_off_add' in user_data else ''
        
        
              options = app_tables.fin_lendor_business_type.search()
              options_string = [str(option['lendor_business_type']) for option in options]
              self.drop_down_12.items = options_string

              self.text_box_1_copy.add_event_handler('change',self.validate_business_add)
              self.text_box_2_copy.add_event_handler('change',self.validate_business_name)
              self.date_picker_1.add_event_handler('change',self.validate_year_estd)
              self.text_box_3.add_event_handler('change',self.validate_industry_type)
              self.text_box_4.add_event_handler('change',self.validate_six_month_turnover)
              self.text_box_5.add_event_handler('change',self.validate_din)
              self.text_box_6.add_event_handler('change',self.validate_cin)
              self.text_box_7.add_event_handler('change',self.validate_registered_off_add)
        
  def validate_business_add(self, **event_args):
        Business_add = self.text_box_1_copy.text
        if re.match(r'^[A-Za-z\s]+$', Business_add):
            self.text_box_1_copy.background = None
        else:
            self.text_box_1_copy.background = '#FF0000'  # Red background for invalid input

  def validate_business_name(self, **event_args):
        business_name = self.text_box_2_copy.text
        if re.match(r'^[A-Za-z\s]+$', business_name):
            self.text_box_2_copy.background = None
        else:
            self.text_box_2_copy.background = '#FF0000'  # Red background for invalid input
        # Get today's date
        today = datetime.today()
    
  def validate_year_estd(self, **event_args):
        year = self.date_picker_1.date.strftime('%Y-%m-%d') if self.date_picker_1.date else None
        if year and year.year > today.year:
          alert("The year cannot be in the future. Please select a valid year.", title="Invalid Year")
          self.text_box_1_copy.background = '#FF0000'
        elif year and year.year > today.year:
          alert("The year cannot be in the future. Please select a valid year.", title="Invalid Year")
          self.text_box_1_copy.background = '#FF0000'
        elif year and year.year == today.year and year.month > today.month:
          alert("The month cannot be in the future. Please select a valid month.", title="Invalid Month")
          self.text_box_1_copy.background = '#FF0000'
        elif year and year.year == today.year and year.month == today.month and year.day > today.day:
          alert("The date cannot be in the future. Please select a valid date.", title="Invalid Date")
          self.text_box_1_copy.background = '#FF0000'
        else:
            self.text_box_1_copy.background = '#FF0000'  # Red background for invalid input
            
  def validate_industry_type(self, **event_args):
        industry_type = self.text_box_3.text
        if re.match(r'^[A-Za-z\s]+$', industry_type):
            self.text_box_3.background = None
        else:
            self.text_box_3.background = '#FF0000'  # Red background for invalid input

  def validate_six_month_turnover(self, **event_args):
        six_month_turnover = self.text_box_4.text
        if re.match(r'^\d+$', six_month_turnover):
            self.text_box_4.background = None
        else:
            self.text_box_4.background = '#FF0000'  # Red background for invalid input

  def validate_din(self, **event_args):
        din = self.text_box_5.text
        if re.match(r'^\d+$', din):
            self.text_box_5.background = None
        else:
            Notification("Spaces are not allowed in the DIN input").show()
            self.text_box_5.background = '#FF0000'  # Red background for invalid input

  def validate_cin(self, **event_args):
        cin = self.text_box_6.text
        if re.match(r'^\d+$', cin):
            self.text_box_6.background = None
        else:
            self.text_box_6.background = '#FF0000'  # Red background for invalid input

  def validate_registered_off_add(self, **event_args):
        registered_off_add = self.text_box_7.text
        if re.match(r'^[A-Za-z\s]+$', registered_off_add):
            self.text_box_7.background = None
        else:
            Notification("Spaces are not allowed in the DIN input").show()
            self.text_box_7.background = '#FF0000'  # Red background for invalid input

        business_name = self.text_box_2_copy.text
        business_add = self.text_box_1_copy.text
        # business_type = self.drop_down_12.selected_value        
        # empolyees_working = self.drop_down_4.selected_value
        # year = self.date_picker_1.date
        industry_type = self.text_box_3.text
        six_month_turnover = self.text_box_4.text
        # last_six_statements = self.file_loader_1.file
        din = self.text_box_5.text
        cin = self.text_box_6.text
        registered_off_add = self.text_box_7.text
        # proof_verification = self.file_loader_1_copy.file

        if not business_add:
            self.text_box_1_copy.background = '#FF0000'
            self.text_box_1_copy.focus()
            Notification('Please fill all details').show()
        elif not re.match(r'^[A-Za-z\s]+$', business_add):
            Notification('Enter a valid Business address')
            self.text_box_1_copy.background = '#FF0000 '
            self.text_box_1_copy.focus()
            return
          
        if not business_name:
            self.text_box_2_copy.background = '#FF0000'
            self.text_box_2_copy.focus()
            Notification('Please fill all details').show()
        elif not re.match(r'^[A-Za-z\s]+$', business_name):
            alert('Enter a valid Business name')
            # Notification('Enter a valid Business name')
            self.text_box_2_copy.background = '#FF0000 '
            self.text_box_2_copy.focus()
            return

        if not industry_type:
            self.text_box_3.background = '#FF0000'
            self.text_box_3.focus()
            Notification('Please fill all details').show()
        elif not re.match(r'^[A-Za-z\s]+$', industry_type):
            Notification('Enter a valid industry type')
            self.text_box_3.background = '#FF0000 '
            self.text_box_3.focus()
            return
          
        if not six_month_turnover:
            self.text_box_4.background = '#FF0000'
            self.text_box_4.focus()
            Notification('Please fill all details').show()
        elif not re.match(r'^[A-Za-z\s]+$', six_month_turnover):
            Notification('Enter a valid six month turn over')
            self.text_box_4.background = '#FF0000 '
            self.text_box_4.focus()
            return

        if not din:
            self.text_box_5.background = '#FF0000'
            self.text_box_5.focus()
            Notification('Please fill all details').show()
        elif not re.match(r'^[A-Za-z\s]+$', din):
            Notification('Enter a valid din number')
            self.text_box_5.background = '#FF0000 '
            self.text_box_5.focus()
            return

        if not cin:
            self.text_box_6.background = '#FF0000'
            self.text_box_6.focus()
            Notification('Please fill all details').show()
        elif not re.match(r'^[A-Za-z\s]+$', cin):
            Notification('Enter a valid din number')
            self.text_box_6.background = '#FF0000 '
            self.text_box_6.focus()
            return

        if not registered_off_add:
            self.text_box_7.background = '#FF0000'
            self.text_box_7.focus()
            Notification('Please fill all details').show()
        elif not re.match(r'^[A-Za-z\s]+$', registered_off_add):
            Notification('Enter a valid din number')
            self.text_box_7.background = '#FF0000 '
            self.text_box_7.focus()
            return
          
  def button_2_click(self, **event_args):
      business_name = self.text_box_2_copy.text
      business_add = self.text_box_1_copy.text
      business_type = self.drop_down_12.selected_value        
      empolyees_working = self.drop_down_4.selected_value
      year = self.date_picker_1.date
      industry_type = self.text_box_3.text
      turn_over = self.text_box_4.text
      last_six_statements = self.file_loader_1.file
      din = self.text_box_5.text
      cin = self.text_box_6.text
      reg_off_add = self.text_box_7.text
      proof_verification = self.file_loader_1_copy.file
        
      user_id = self.userId     

      # Validation for Business
      if not re.match(r'^[A-Za-z\s]+$', business_name):
        alert('Enter valid business name')
      elif not business_name or not business_add or not business_type or not empolyees_working:
        Notification("Please fill all the fields").show()
  
      elif year and year.year > today.year:
        alert("The year cannot be in the future. Please select a valid year.", title="Invalid Year")
        return
      elif year and year.year == today.year and year.month > today.month:
        alert("The month cannot be in the future. Please select a valid month.", title="Invalid Month")
        return
      elif year and year.year == today.year and year.month == today.month and year.day > today.day:
        alert("The date cannot be in the future. Please select a valid date.", title="Invalid Date")
        return              
      elif not year or not industry_type or not turn_over or not last_six_statements:
        alert("Please fill all the fields", title="Missing Information")
      elif ' ' in cin:
        Notification("Spaces are not allowed in the CIN input").show()
        return    
      # DIN Validation
      elif ' ' in din:
        Notification("Spaces are not allowed in the DIN input").show()
        return
      # Other field validations
      elif not din or not cin or not reg_off_add or not proof_verification:
        Notification("Please fill all the fields").show()
      else:
        anvil.server.call('add_lendor_institutional_form_1',business_name,business_add,business_type,empolyees_working,user_id)
        months = (datetime.now().year - year.year) * 12 + (datetime.now().month - year.month)
        anvil.server.call('add_lendor_institutional_form_2', year, months, industry_type, turn_over, last_six_statements, user_id)
        anvil.server.call('add_lendor_institutional_form_3', din, cin, reg_off_add, proof_verification, user_id)
        open_form('lendor.lendor_registration_forms.lender_registration_form_3_marital_details',user_id=user_id)

  def validate_file_upload(self, **event_args):
        file_loader = event_args['sender']
        file = file_loader.file
        max_size = 2 * 1024 * 1024  # 2MB in bytes
        allowed_types = ['image/jpeg', 'image/png', 'image/jpg', 'application/pdf']
    
        if file:
            file_size = len(file.get_bytes())
            if file_size > max_size:
                alert('File size should be less than 2MB')
                file_loader.clear()
                return
    
            if file.content_type not in allowed_types:
                alert('Invalid file type. Only JPEG, PNG, jpg and PDF are allowed')
                file_loader.clear()
                return
              
  def file_loader_1(self, file, **event_args):
        """This method is called when a new file is loaded into this FileLoader"""
        if file:
                self.label_1.text = file.name if file else ''
                content_type = file.content_type
                
                if content_type in ['image/jpeg', 'image/png', 'image/jpg']:
                    # Display the image directly
                    self.image_1.source = self.file_loader_1.file
                elif content_type == 'application/pdf':
                    # Display a default PDF image temporarily
                    self.image_1.source = '_/theme/bank_users/default%20pdf.png'
                else:
                    alert('Invalid file type. Only JPEG, PNG, and PDF are allowed')
                    self.file_loader_1.clear()

  def file_loader_1_copy(self, file, **event_args):
        """This method is called when a new file is loaded into this FileLoader"""
        if file:
                  self.label_3.text = file.name if file else ''
                  content_type = file.content_type
                  
                  if content_type in ['image/jpeg', 'image/png', 'image/jpg']:
                      # Display the image directly
                      self.image_1_copy.source = self.file_loader_1_copy.file
                  elif content_type == 'application/pdf':
                      # Display a default PDF image temporarily
                      self.image_1_copy.source = '_/theme/bank_users/default%20pdf.png'
                  else:
                      alert('Invalid file type. Only JPEG, PNG, and PDF are allowed')
                      self.file_loader_1_copy.clear()

  def button_3_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form("bank_users.user_form")
    
  def button_1_click(self, **event_args):
        user_id = self.userId
        open_form('lendor.lendor_registration_forms.lender_registration_form_2',user_id = user_id)
        """This method is called when the button is clicked"""

    



