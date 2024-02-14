import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
import base64
import os  # Import the os module for file existence che
from anvil import *
import anvil.media
from anvil import Media








@anvil.server.callable
def calculate_extension_details(loan_id, loan_extension_months):
    # Fetch necessary loan details from the Anvil data tables
    loan_row = app_tables.loan_details.get(loan_id=loan_id)

    if loan_row is not None:
        # Extract loan details
        total_loan_amount = loan_row['total_repayment_amount']
        loan_amount = loan_row['loan_amount']
        tenure = loan_row['tenure']
        interest_rate = loan_row['interest_rate']
        product_id = loan_row['product_id']
        loan_disbursed_timestamp = loan_row['loan_disbursed_timestamp']

        # Fetch the last emi row for the specified loan_id
        last_emi_rows = app_tables.fin_emi_table.search(loan_id=loan_id)
        total_payments_made = 0

        if last_emi_rows:
            # Sort the list of rows based on the 'emi_number' column in reverse order
            last_emi_list = list(last_emi_rows)
            last_emi_list.sort(key=lambda x: x['emi_number'], reverse=True)

            # Extract the 'emi_number' from the first row, which represents the highest 'emi_number'
            total_payments_made = last_emi_list[0]['emi_number']

        # Calculate the monthly interest rate
        monthly_interest_rate = interest_rate / (12 * 100)

        # Calculate the EMI using the formula for EMI calculation
        factor = (1 + monthly_interest_rate) ** tenure
        emi = loan_amount * monthly_interest_rate * factor / (factor - 1)

        # Fetch the extension fee from the product details
        extension_fee = 0
        product_data = tables.app_tables.fin_product_details.search(product_id=product_id)
        for row in product_data:
            extension_fee = row['extension_fee']

        # Calculate the extension amount based on the extension fee
        extension_amount = (extension_fee * loan_amount) / 100

        # Calculate the total amount of EMIs paid
        emi_paid = total_payments_made * emi

        # Calculate the remaining loan amount
        remaining_loan_amount = total_loan_amount - emi_paid

        # Calculate the total extension months
        total_extension_months = tenure + loan_extension_months

        # Calculate the schedule payment date for each EMI
        payment_schedule = []
        for month in range(1, total_extension_months + 1):
            # Calculate the payment date by adding months to the loan disbursed timestamp
            payment_date = loan_disbursed_timestamp + timedelta(days=30 * month)

            # Append the payment date to the schedule
            payment_schedule.append(payment_date)

        # Return the calculated values
        return {
            'total_extension_months': total_extension_months,
            'extension_fee_comp_value': extension_fee,
            'remaining_loan_amount': remaining_loan_amount,
            'extension_amount': extension_amount,
            'emi_paid': emi_paid,
            'emi': emi,
            'payment_schedule': payment_schedule
        }
    else:
        return "Loan details not found"

