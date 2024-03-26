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

class star_1_borrower_registration_form_4_loan(star_1_borrower_registration_form_4_loanTemplate):
    def __init__(self, user_id, **properties):
        self.init_components(**properties)
        self.selected_button_index = None
        self.userId = user_id
        user_data = app_tables.fin_user_profile.get(customer_id=user_id)
        if user_data:
            self.set_selected_loan_option(user_data)

    def set_selected_loan_option(self, user_data):
        loan_types = ['home_loan', 'other_loan', 'credit_card_loans', 'vehicle_loan']
        for loan_type in loan_types:
            selected_option = getattr(user_data, loan_type, '').lower()
            self.set_loan_buttons_visibility(loan_type, selected_option)

    def save_selected_loan_option(self, loan_type, selected_option):
        user_data = app_tables.fin_user_profile.get(customer_id=self.userId)
        if user_data:
            setattr(user_data, loan_type, selected_option.lower())
            user_data.save()

    def set_loan_buttons_visibility(self, loan_type, selected_option):
        button_indices = {'home_loan': 0, 'other_loan': 1, 'credit_card_loans': 2, 'vehicle_loan': 3}
        button_index = button_indices[loan_type]
        self.select_button(button_index, selected_option)

    def button_1_click(self, loan_type, button_index, **event_args):
        selected_option = 'Yes' if button_index % 2 == 1 else 'No'
        self.save_selected_loan_option(loan_type, selected_option)
        self.set_loan_buttons_visibility(loan_type, selected_option)
        open_form('borrower_registration_form.star_1_borrower_registration_form_5_bank_1', user_id=self.userId)

    def button_1_1_click(self, **event_args):
        self.select_button(0, 'Yes')

    def button_1_2_click(self, **event_args):
        self.select_button(0, 'No')

    def button_1_3_click(self, **event_args):
        self.select_button(1, 'Yes')

    def button_1_4_click(self, **event_args):
        self.select_button(1, 'No')

    def button_1_5_click(self, **event_args):
        self.select_button(2, 'Yes')

    def button_1_6_click(self, **event_args):
        self.select_button(2, 'No')

    def button_1_7_click(self, **event_args):
        self.select_button(3, 'Yes')

    def button_1_8_click(self, **event_args):
        self.select_button(3, 'No')

    def select_button(self, button_index, selected_option):
        # Update background color of previously selected button
        if self.selected_button_index is not None:
            prev_button_1 = getattr(self, f'button_1_{self.selected_button_index * 2 + 1}')
            prev_button_2 = getattr(self, f'button_1_{self.selected_button_index * 2 + 2}')
            prev_button_1.background = '#939191'
            prev_button_2.background = '#939191'

        # Update background color of newly selected button
        button_1 = getattr(self, f'button_1_{button_index * 2 + 1}')
        button_2 = getattr(self, f'button_1_{button_index * 2 + 2}')
        if selected_option == 'Yes':
            button_1.background = '#0a2346'
            button_2.background = '#939191'
        else:
            button_1.background = '#939191'
            button_2.background = '#0a2346'

        # Update selected button index
        self.selected_button_index = button_index
