from ._anvil_designer import View_DetailsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta
from .. import main_form_module as main_form_module

class View_Details(View_DetailsTemplate):
    def __init__(self, selected_row, **properties):
      self.selected_row = selected_row
      self.user_id = main_form_module.userId
      self.init_components(**properties)
  
      loan_id = selected_row['loan_id']
      extension_amount = self.get_extension_amount(loan_id, selected_row['emi_number'])
  
      loan_amount = selected_row['loan_amount']
      tenure = selected_row['tenure']
      interest_rate = selected_row['interest_rate']
      emi_payment_type = selected_row['emi_payment_type']
  
      monthly_interest_rate = interest_rate / 12 / 100
      total_payments = tenure * 12
  
      if emi_payment_type == 'One Time':
            emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** 12) / ((1 + monthly_interest_rate) ** 12 - 1)
            total_emi = emi + extension_amount  # Add extension amount to 12-month EMI total
      elif emi_payment_type == 'Monthly':
          # Calculate monthly EMI amount
          emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)
          total_emi = emi + extension_amount  # Add extension amount to monthly EMI
      elif emi_payment_type == 'Three Month':
          # Calculate EMI amount for 3 months
          emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** 3) / ((1 + monthly_interest_rate) ** 3 - 1)
          total_emi = emi + extension_amount  # Add extension amount to 3-month EMI
      elif emi_payment_type == 'Six Month':
          # Calculate EMI amount for 6 months
          emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** 6) / ((1 + monthly_interest_rate) ** 6 - 1)
          total_emi = emi + extension_amount  # Add extension amount to 6-month EMI
      else:
          # Default to monthly calculation
          emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)
          total_emi = emi + extension_amount  # Add extension amount to monthly EMI
  
      # Display the calculated EMI amount in the EMI amount label
      self.emi_amount_label.text = "{:.2f}".format(emi)  # Show only the EMI amount without extension
  
      # Update labels based on the presence of extension amount
      if extension_amount > 0:
          self.total_emi_amount_label.text = "{:.2f}".format(total_emi)
          self.extension_amount_label.text = "{:.2f}".format(extension_amount)
          self.total_emi_amount_label.visible = True
          self.extension_amount_label.visible = True
      else:
          self.total_emi_amount_label.visible = False
          self.extension_amount_label.visible = False
          self.label_6.visible = False
          self.label_3.visible = False
  
      # Update other labels
      self.loan_id_label.text = str(selected_row['loan_id'])
      self.loan_amount_label.text = str(loan_amount)
      self.interest_label.text = str(interest_rate)
      self.tenure_label.text = str(tenure)
      self.account_no_label.text = str(selected_row['account_number'])
  
      # Display total EMI amount including extension amount
      self.update_total_emi_amount(total_emi)
      
    def get_extension_amount(self, loan_id, emi_number):
      extension_row = app_tables.fin_extends_loan.get(
          loan_id=loan_id,
          emi_number=emi_number
      )
      if extension_row is not None:
          extension_amount = extension_row['extension_amount']
          if extension_amount is not None:
              return extension_amount
      return 0

    def update_total_emi_amount(self, total_emi):
        self.total_emi_amount_label.text = "{:.2f}".format(total_emi)

    def button_1_copy_2_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('lendor_registration_form.dashboard.today_dues')
