from ._anvil_designer import part_paymentTemplate
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
from datetime import date


class part_payment(part_paymentTemplate):
  def __init__(self,loan_details, **properties):
    self.loan_details = loan_details
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.loan_id_label.text = loan_details['loan_id']
    self.loan_amount_label.text = loan_details['loan_amount']
    self.total_emi_amount_label.text = loan_details['total_emi_amount']
    self.emi_amount_label.text = loan_details['emi_amount']
    self.account_no_label.text = loan_details['account_no']
    self.tenure_label.text = loan_details['tenure']
    self.interest_label.text = loan_details['interest_amount']
    self.remainining_amount.text = loan_details['remainining_amount']
    current_emi_number = loan_details['current_emi_number']
    extra_fee = loan_details['extra_fee']
    prev_next_payment = loan_details['prev_next_payment']
    prev_scheduled_payment = loan_details['prev_scheduled_payment']
    borrower_email = loan_details['borrower_email']
    lender_email = loan_details['lender_email']
    emi_payment_type = loan_details['emi_payment_type']


    if self.loan_details['payment_type'] == 'part payment':
        # Fetch part payment amount from fin_emi_table based on loan ID and emi number
        loan_id = self.loan_details['loan_id']
        emi_number = self.loan_details['current_emi_number']
        print(emi_number)
        emi_row = app_tables.fin_emi_table.get(
            loan_id=loan_id,
            emi_number=emi_number + 1
        )
        part_payment_amount = emi_row['part_payment_amount']
        total_emi_amount = float(self.total_emi_amount_label.text)

        # Calculate the remaining amount after deducting the part payment amount
        remaining_part_payment_amount = total_emi_amount - part_payment_amount

        # Display the remaining amount in the text box
        self.text_box_1.text = str(remaining_part_payment_amount)
        self.text_box_1.enabled = False

  def pay_now_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_amount = float(self.text_box_1.text)  # Get the amount entered by the user
    total_emi_amount = float(self.total_emi_amount_label.text)  # Get the total EMI amount

    if self.loan_details['payment_type'] == 'pay now':
      
        if entered_amount <= total_emi_amount:
            # Proceed with the payment process
            borrower_wallet = app_tables.fin_wallet.get(customer_id=self.loan_details['borrower_customer_id'])
            lender_wallet = app_tables.fin_wallet.get(customer_id=self.loan_details['lender_customer_id'])
    
            if borrower_wallet is not None and lender_wallet is not None:
                # Deduct from borrower's wallet
                borrower_balance = borrower_wallet['wallet_amount']
                new_borrower_balance = borrower_balance - entered_amount
                borrower_wallet['wallet_amount'] = new_borrower_balance
                borrower_wallet.update()
    
                # Add to lender's wallet
                lender_balance = lender_wallet['wallet_amount']
                new_lender_balance = lender_balance + entered_amount
                lender_wallet['wallet_amount'] = new_lender_balance
                lender_wallet.update()
    
                # Update remaining amount in loan details table
                remaining_amount = float(self.loan_details['remainining_amount']) - entered_amount
                loan_id = self.loan_details['loan_id']
    
      
                loan_row = app_tables.fin_loan_details.get(loan_id=loan_id)
                if loan_row is not None:
                    loan_row['remaining_amount'] = remaining_amount
                    total_paid = float(loan_row['total_amount_paid']) + entered_amount
                    loan_row['total_amount_paid'] = total_paid
                    loan_row.update()
    
                    current_emi_number = self.loan_details['current_emi_number']
                    extra_fee = self.loan_details['extra_fee']
                    prev_next_payment = self.loan_details['prev_next_payment']
                    prev_scheduled_payment = self.loan_details['prev_scheduled_payment']
                    borrower_email = self.loan_details['borrower_email']
                    lender_email = self.loan_details['lender_email']
                    emi_payment_type = self.loan_details['emi_payment_type']
                    borrower_customer_id = self.loan_details['borrower_customer_id']
                    lender_customer_id = self.loan_details['lender_customer_id']
                    account_no = self.loan_details['account_no']
    
                    if emi_payment_type in ['One Time', 'Monthly', 'Three Months', 'Six Months']:
                            
                      if emi_payment_type == 'Monthly':
                                next_scheduled_payment = prev_scheduled_payment + timedelta(days=30)
                                next_next_payment = prev_next_payment + timedelta(days=30)
                      elif emi_payment_type == 'Three Months':
                                next_scheduled_payment = prev_scheduled_payment + timedelta(days=90)
                                next_next_payment = prev_next_payment + timedelta(days=90)
                        
                      elif emi_payment_type == 'Six Months':
                                next_scheduled_payment = prev_scheduled_payment + timedelta(days=180)
                                next_next_payment = prev_next_payment + timedelta(days=180)
                      elif emi_payment_type == 'One Time':
                              if tenure:
                                next_scheduled_payment = prev_scheduled_payment + timedelta(days=30 * tenure)
                                next_next_payment = self.selected_row['next_payment'] + timedelta(days=30 * tenure)                
                    else:
                            # Default to monthly calculation
                            next_scheduled_payment = prev_scheduled_payment + timedelta(days=30)
                            next_next_payment = prev_next_payment + timedelta(days=30)
    
                        # Add a new row to fin_emi_table
                    new_emi_row = app_tables.fin_emi_table.add_row(
                            loan_id=loan_id,
                            emi_number=current_emi_number + 1,
                            account_number=account_no,
                            scheduled_payment_made=datetime.now(),
                            scheduled_payment=next_scheduled_payment,
                            next_payment=next_next_payment,
                            amount_paid= entered_amount,
                            extra_fee=extra_fee,
                            borrower_customer_id=borrower_customer_id,
                            lender_customer_id=lender_customer_id,
                            borrower_email=borrower_email,
                            lender_email=lender_email,
                            payment_type='part payment',
                            part_payment_date=datetime.today().date(),
                            
                            
                        )
    
                        # Update the emi_number and next_payment in the selected_row
                    self.loan_details['emi_number'] = current_emi_number + 1
                    self.loan_details['next_payment'] = next_next_payment
                    self.loan_details.update()
                  
    
                alert("Payment successful!")
            else:
                alert("Error: Wallet record not found.")
        else:
            # Show an alert if the entered amount is greater than the total EMI amount
            alert("Entered amount exceeds the total EMI amount. Please enter a valid amount.")

