from ._anvil_designer import part_paymentTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


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

  def pay_now_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_amount = float(self.text_box_1.text)  # Get the amount entered by the user
    total_emi_amount = float(self.total_emi_amount_label.text)  # Get the total EMI amount

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
               

            alert("Payment successful!")
        else:
            alert("Error: Wallet record not found.")
    else:
        # Show an alert if the entered amount is greater than the total EMI amount
        alert("Entered amount exceeds the total EMI amount. Please enter a valid amount.")