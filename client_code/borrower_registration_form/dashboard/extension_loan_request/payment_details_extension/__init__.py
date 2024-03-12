from ._anvil_designer import payment_details_extensionTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import timedelta

class payment_details_extension(payment_details_extensionTemplate):
    def __init__(self, selected_row=None, loan_extension_months=None, extension_fee=None, **properties):
        self.selected_row = selected_row
        self.loan_extension_months = loan_extension_months
        self.extension_fee = extension_fee
        self.emi = 0
        self.init_components(**properties)

        if selected_row:
            self.load_payment_details(selected_row)

    def load_payment_details(self, selected_row):
        self.load_entered_values()
        payment_details = []

        entered_extension_months = self.loan_extension_months
        total_tenure = selected_row['tenure'] + entered_extension_months

        monthly_interest_rate = (selected_row['interest_rate'] / 100) / 12

        beginning_balance = selected_row['loan_amount']

        extension_fee_percentage = self.extension_fee if self.extension_fee is not None else selected_row.get('extension_fee', 0)
        extension_fee_amount = (extension_fee_percentage / 100) * selected_row['loan_amount']

        last_paid_emi_records = app_tables.fin_emi_table.search(loan_id=selected_row['loan_id'], scheduled_payment_made=q.not_(None))
        last_paid_emi_number = max([record['emi_number'] for record in last_paid_emi_records], default=0)
        print("last_paid_emi_number", last_paid_emi_number)
        last_paid_emi_ending_balance = selected_row['loan_amount']

        payment_number_counter = 1

        for month in range(1, total_tenure + 1):
            emi = 0  # Assign a default value
            payment_date = self.calculate_payment_date(selected_row, month)
            loan_id = selected_row['loan_id']
            emi_number = payment_number_counter
            emi_row = app_tables.fin_emi_table.get(loan_id=loan_id, emi_number=emi_number)

            if emi_row is not None:
                scheduled_payment_made = emi_row['scheduled_payment_made']
                account_number = emi_row['account_number']
            else:
                scheduled_payment_made = None
                account_number = None

            formatted_payment_date = f"{payment_date:%Y-%m-%d}" if payment_date else "Awaiting Update"

            if month <= last_paid_emi_number:
                emi, total_payment = self.calculate_scheduled_payment(selected_row, monthly_interest_rate)
            else:
                emi, total_payment = self.calculate_scheduled_payment_with_extension(selected_row, monthly_interest_rate, extension_fee_amount)

            if emi != 0:
                interest_amount = beginning_balance * monthly_interest_rate
                principal_amount = emi - interest_amount
                ending_balance = beginning_balance - principal_amount

                payment_details.append({
                    'PaymentNumber': payment_number_counter,
                    'PaymentDate': formatted_payment_date,
                    'EMIDate': f"{scheduled_payment_made:%Y-%m-%d}" if scheduled_payment_made else "N/A",
                    'EMITime': f"{scheduled_payment_made:%I:%M %p}" if scheduled_payment_made else "N/A",
                    'AccountNumber': account_number if account_number else "N/A",
                    'ScheduledPayment': f"₹ {emi:.2f}",
                    'Principal': f"₹ {principal_amount:.2f}",
                    'Interest': f"₹ {interest_amount:.2f}",
                    'BeginningBalance': f"₹ {beginning_balance:.2f}" if beginning_balance else "N/A",
                    'ExtensionFee': f"₹ {extension_fee_amount:.2f}" if payment_number_counter == (last_paid_emi_number + 1) else "₹ 0.00",
                    'TotalPayment': f"₹ {total_payment:.2f}",
                    'EndingBalance': f"₹ {ending_balance:.2f}"
                })

                # Set the beginning_balance to the ending_balance for the next iteration
                beginning_balance = ending_balance
                last_paid_emi_ending_balance = ending_balance
                payment_number_counter += 1

        self.repeating_panel_1.items = payment_details

    def calculate_scheduled_payment(self, selected_row, monthly_interest_rate):
        emi = self.calculate_emi(selected_row, selected_row['tenure'], selected_row['loan_amount'], monthly_interest_rate)
        total_payment = emi
        return emi, total_payment

    def calculate_scheduled_payment_with_extension(self, selected_row, monthly_interest_rate, extension_fee_amount):
        emi = self.calculate_emi(selected_row, selected_row['tenure'] + self.loan_extension_months, selected_row['loan_amount'], monthly_interest_rate)
        total_payment = emi + extension_fee_amount
        return emi, total_payment

    def calculate_emi(self, selected_row, tenure, loan_amount, monthly_interest_rate):
        if selected_row['emi_payment_type'] == 'Monthly':
            emi_denominator = ((1 + monthly_interest_rate) ** tenure) - 1
            emi_numerator = loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** tenure)
            emi = emi_numerator / emi_denominator
        elif selected_row['emi_payment_type'] == 'One Time':
            # Implementation for One Time payment type
            emi = loan_amount / tenure
        elif selected_row['emi_payment_type'] == 'Three Month':
            # Implementation for Three Month payment type
            emi_denominator = ((1 + monthly_interest_rate) ** (tenure // 3)) - 1
            emi_numerator = loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** (tenure // 3))
            emi = emi_numerator / emi_denominator
        elif selected_row['emi_payment_type'] == 'Six Month':
            # Implementation for Six Month payment type
            emi_denominator = ((1 + monthly_interest_rate) ** (tenure // 6)) - 1
            emi_numerator = loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** (tenure // 6))
            emi = emi_numerator / emi_denominator
        else:
            emi = None  # Handle unsupported payment types more explicitly

        return emi

    # def calculate_emi(self, selected_row, tenure=None, repayment_amount=None):
    #     tenure = selected_row['tenure'] if tenure is None else tenure
    #     monthly_interest_rate = (selected_row['interest_rate'] / 100) / 12
    #     loan_amount = selected_row['loan_amount'] - repayment_amount if repayment_amount else selected_row['loan_amount']
    
    #     if selected_row['emi_payment_type'] == 'Monthly':
    #         emi = (loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** tenure)) / (((1 + monthly_interest_rate) ** tenure) - 1)
    #       # elif selected_row['emi_payment_type'] == 'One Time':
    #       #     emi = selected_row['total_repayment_amount']
    #     elif selected_row['emi_payment_type'] == 'Three Month':
    #         monthly_interest_rate = (selected_row['interest_rate'] / 100) / (12)  # Convert annual interest rate to monthly
    #         emi = (loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** (tenure ))) / (((1 + monthly_interest_rate) ** (tenure)) - 1)
    #     elif selected_row['emi_payment_type'] == 'Six Month':
    #         monthly_interest_rate = (selected_row['interest_rate'] / 100) / (12 )  # Corrected calculation for 6 months
    #         emi = (loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** (tenure ))) / (((1 + monthly_interest_rate) ** (tenure )) - 1)
    #     else:
    #         emi = 0  # Handle unsupported payment types
    
    #     return emi

    def button_1_click(self, **event_args):
        open_form('borrower_registration_form.dashboard.extension_loan_request.borrower_extension.extension2',
                  selected_row=self.selected_row, loan_extension_months=self.loan_extension_months, new_emi = self.emi)

    def button_2_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('borrower_registration_form.dashboard.extension_loan_request.borrower_extension', selected_row = self.selected_row)
