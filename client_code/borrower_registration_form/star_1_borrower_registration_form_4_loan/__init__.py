from ._anvil_designer import star_1_borrower_registration_form_4_loanTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

# class star_1_borrower_registration_form_4_loan(star_1_borrower_registration_form_4_loanTemplate):
#   def __init__(self,user_id, **properties):
#     self.init_components(**properties)
#     self.userId = user_id
#     user_data=app_tables.fin_user_profile.get(customer_id=user_id)
#     if user_data:
#       self.text_box_1.text=user_data['home_loan']
#       self.text_box_2.text=user_data['other_loan']
#       self.text_box_4.text = user_data['credit_card_loans']
#       self.text_box_5.text = user_data['vehicle_loan']
#       user_data.update()
      
#   def button_1_click(self, **event_args):
#     open_form('borrower_registration_form.star_1_borrower_registration_form_3_marital',user_id = self.userId)

#   def button_2_click(self, **event_args):
#     home_loan = self.text_box_1.text.lower()
#     other_loan = self.text_box_2.text.lower()
#     credit_card = self.text_box_4.text.lower()
#     wheeler = self.text_box_5.text.lower()
#     user_id = self.userId
#     if home_loan not in ['yes', 'no'] or other_loan not in ['yes', 'no'] or credit_card not in ['yes', 'no'] or wheeler not in ['yes', 'no']:
#       Notification("Please enter 'yes' or 'no' for all fields").show()
#     else:
#       anvil.server.call('add_borrower_step4',home_loan,other_loan,user_id,credit_card,wheeler)
#       open_form('borrower_registration_form.star_1_borrower_registration_form_5_bank_1',user_id=user_id)

#   def home_borrower_registration_form_click(self, **event_args):
#     open_form('bank_users.user_form')

#   def button_1_1_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     pass

  # def set_selected_homeloan(self, home_loan):
  #       button_names = ["Yes", "No"]
  #       for i, loan_option in enumerate(button_names):
  #           button = getattr(self, f'button_{i + 1}_1')
  #           if loan_option == home_loan:
  #               button.background = '#0a2346'
  #           else:
  #               button.background = '#939191'

class BorrowerRegistrationForm(BorrowerRegistrationFormTemplate):
    def __init__(self, user_id, **properties):
        # Set up default properties and event handlers
        self.init_components(**properties)
        
        # Store the user ID
        self.user_id = user_id
        
        # Initialize loan status variables
        self.home_loan_status = ''
        self.other_loan_status = ''
        self.credit_card_loan_status = ''
        self.vehicle_loan_status = ''
        
        # Load user loan status if available
        self.load_loan_status()
    
    def load_loan_status(self):
        # Load user loan status if available
        user_data = app_tables.fin_user_profile.get(customer_id=self.user_id)
        if user_data:
            self.home_loan_status = user_data['home_loan']
            self.other_loan_status = user_data['other_loan']
            self.credit_card_loan_status = user_data['credit_card_loan']
            self.vehicle_loan_status = user_data['vehicle_loan']
            self.update_buttons_visibility()

    def update_buttons_visibility(self):
        # Update button visibility based on loan status
        self.button_1_1.visible = self.home_loan_status != 'yes'
        self.button_2_1.visible = self.home_loan_status == 'yes'
        
        self.button_1_2.visible = self.other_loan_status != 'yes'
        self.button_2_2.visible = self.other_loan_status == 'yes'
        
        self.button_1_3.visible = self.credit_card_loan_status != 'yes'
        self.button_2_3.visible = self.credit_card_loan_status == 'yes'
        
        self.button_1_4.visible = self.vehicle_loan_status != 'yes'
        self.button_2_4.visible = self.vehicle_loan_status == 'yes'

    def update_loan_status(self, loan_type, status):
        # Update loan status and save to database
        user_data = app_tables.fin_user_profile.get(customer_id=self.user_id)
        if user_data:
            user_data[loan_type] = status
            user_data.save()
            # Update visibility after status change
            self.load_loan_status()

    def button_1_1_click(self, **event_args):
        self.update_loan_status('home_loan', 'yes')

    def button_2_1_click(self, **event_args):
        self.update_loan_status('home_loan', 'no')

    def button_1_2_click(self, **event_args):
        self.update_loan_status('other_loan', 'yes')

    def button_2_2_click(self, **event_args):
        self.update_loan_status('other_loan', 'no')

    def button_1_3_click(self, **event_args):
        self.update_loan_status('credit_card_loan', 'yes')

    def button_2_3_click(self, **event_args):
        self.update_loan_status('credit_card_loan', 'no')

    def button_1_4_click(self, **event_args):
        self.update_loan_status('vehicle_loan', 'yes')

    def button_2_4_click(self, **event_args):
        self.update_loan_status('vehicle_loan', 'no')