from ._anvil_designer import check_outTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import main_form_module as main_form_module
from datetime import datetime

class check_out(check_outTemplate):
    def __init__(self, selected_row, **properties):
        self.selected_row = selected_row
        self.user_id = main_form_module.userId
        self.init_components(**properties)

        loan_amount = selected_row['loan_amount']
        tenure = selected_row['tenure']
        interest_rate = selected_row['interest_rate']

        monthly_interest_rate = interest_rate / 12 / 100
        total_payments = tenure * 12
        emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)

        self.loan_id_label.text = str(selected_row['loan_id'])
        self.loan_amount_label.text = str(loan_amount)
        self.interest_label.text = str(interest_rate)
        self.tenure_label.text = str(tenure)
        self.emi_no_label.text = str(selected_row['emi_number'])
        self.account_no_label.text = str(selected_row['account_number'])
        self.emi_amount_label.text = "{:.2f}".format(emi)

    def button_1_copy_2_click(self, **event_args):
        open_form('borrower_registration_form.dashboard.today_dues')

    def pay_now_click(self, **event_args):
        emi_amount = float(self.emi_amount_label.text)
        borrower_wallet = app_tables.fin_wallet.get(customer_id=self.user_id)

        if borrower_wallet is not None:
            wallet_balance = borrower_wallet['wallet_amount']
            
            if wallet_balance >= emi_amount:
                updated_balance = wallet_balance - emi_amount
                borrower_wallet['wallet_amount'] = updated_balance
                borrower_wallet.update()
                
                self.status_label.text = "Payment successful!"
                
                loan_id = self.selected_row['loan_id']
                current_emi_number = int(self.selected_row['emi_number'])
                account_number = self.selected_row['account_number']
                next_emi_number = current_emi_number + 1
                
                new_emi_row = app_tables.fin_emi_table.add_row(
                    loan_id=loan_id,
                    emi_number=next_emi_number,
                    account_number=account_number,
                    scheduled_payment_made=datetime.now(),
                )
                
                # Update the emi_number in the selected_row
                self.selected_row['emi_number'] = next_emi_number
                self.selected_row.update()
                
                self.status_label.text = "Payment successful..."
            else:
                self.status_label.text = "Insufficient funds to complete payment."
        else:
            self.status_label.text = "Wallet record not found."