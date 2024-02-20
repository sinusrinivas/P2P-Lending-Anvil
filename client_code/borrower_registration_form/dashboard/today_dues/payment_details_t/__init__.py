import anvil.google.auth
import anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth
import anvil.google.drive
from anvil.tables import app_tables
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
from anvil import DataGrid, alert, open_form
from datetime import datetime, timedelta
import anvil.server
from ._anvil_designer import payment_details_tTemplate

class payment_details_t(payment_details_tTemplate):
    def __init__(self, selected_row=None, entered_values=None, **properties):
        self.selected_row = selected_row
        self.init_components(**properties)

        if selected_row:
            self.load_payment_details(selected_row, entered_values)

    def load_payment_details(self, selected_row, entered_values):
      self.load_entered_values(entered_values)
      payment_details = []
  
      # Calculate number of payment details based on emi_payment_type
      num_payments = self.calculate_num_payments(selected_row)
  
      # Initialize beginning_balance to the loan amount
      beginning_balance = selected_row['total_repayment_amount']
      total_repayment_beginning_balance = selected_row['total_repayment_amount']
  
      for month in range(1, num_payments + 1):
          payment_date = self.calculate_payment_date(selected_row, month)
  
          # Call the appropriate calculation method based on emi_payment_type
          if selected_row['emi_payment_type'] == 'Monthly':
              emi, ending_balance, total_repayment_beginning_balance, total_repayment_ending_balance = self.calculate_monthly_emi_and_balance(selected_row, month)
          elif selected_row['emi_payment_type'] == 'Three Month':
              emi, ending_balance, total_repayment_beginning_balance, total_repayment_ending_balance = self.calculate_three_month_emi_and_balance(selected_row, month)
          elif selected_row['emi_payment_type'] == 'Six Month':
              emi, ending_balance, total_repayment_beginning_balance, total_repayment_ending_balance = self.calculate_six_month_emi_and_balance(selected_row, month)
          elif selected_row['emi_payment_type'] == 'One Time':
              emi, ending_balance, total_repayment_beginning_balance, total_repayment_ending_balance = self.calculate_one_time_emi_and_balance(selected_row, month)
          else:
              # Handle unsupported payment types
              emi, ending_balance, total_repayment_ending_balance = 0, 0, total_repayment_beginning_balance
  
          # Fetch extra payment from fin_extension_loan table
          extension_row = app_tables.fin_extends_loan.get(
              loan_id=selected_row['loan_id'],
              emi_number=month
          )
          extra_payment = extension_row['extension_amount'] if extension_row else 0
  
          # Fetch scheduled_payment_made and account_number from the emi_payments table
          emi_row = app_tables.fin_emi_table.get(
              loan_id=selected_row['loan_id'],
              emi_number=month
          )
          scheduled_payment_made = emi_row['scheduled_payment_made'] if emi_row else None
          account_number = emi_row['account_number'] if emi_row else None
  
          # Calculate interest and principal amounts based on the current month
          monthly_interest_rate = (selected_row['interest_rate'] / 100) / 12
          interest_amount = ending_balance * monthly_interest_rate
          principal_amount = emi - interest_amount
  
          # Determine display values for EMIDate and AccountNumber
          scheduled_payment_made_display = f"{scheduled_payment_made:%Y-%m-%d}" if scheduled_payment_made else "N/A"
          emi_time_display = f"{scheduled_payment_made:%I:%M %p}" if scheduled_payment_made else "N/A"
          account_number_display = account_number if account_number else "N/A"
  
          # Format payment date
          formatted_payment_date = f"{payment_date:%Y-%m-%d}" if payment_date else "Awaiting Update"
  
          # Add payment details to the list
          payment_details.append({
              'PaymentNumber': month,
              'PaymentDate': formatted_payment_date,
              'EMIDate': scheduled_payment_made_display,
              'EMITime': emi_time_display,
              'AccountNumber': account_number_display,
              'ScheduledPayment': f"₹ {emi:.2f}",
              'Principal': f"₹ {principal_amount:.2f}",
              'Interest': f"₹ {interest_amount:.2f}",
              'BeginningBalance': f"₹ {beginning_balance:.2f}",
              'ExtraPayment': f"₹ {extra_payment:.2f}" if extra_payment is not None else "N/A",
              'TotalPayment': f"₹ {emi + extra_payment if extra_payment is not None else emi:.2f}",
              'EndingBalance': f"₹ {ending_balance:.2f}",
              'TotalRepaymentBeginningBalance': f"₹ {total_repayment_beginning_balance:.2f}",
              'TotalRepaymentEndingBalance': f"₹ {total_repayment_ending_balance:.2f}"
          })
  
          # Update beginning balance for the next iteration
          beginning_balance = ending_balance
  
      # Set the Data Grid's items property to the list of payment details
      self.repeating_panel_1.items = payment_details
    
    def load_entered_values(self, entered_values):
        if entered_values:
            # Load previously entered values into the form fields
            self.entered_loan_amount = entered_values.get('loan_amount', None)
            self.entered_tenure = entered_values.get('tenure', None)
            self.entered_payment_type = entered_values.get('payment_type', None)

    def calculate_payment_date(self, selected_row, current_month):
        loan_updated_status = selected_row['loan_updated_status'].lower()
        print("Loan Updated Status:", loan_updated_status)

        if loan_updated_status in ['close', 'closed loans', 'disbursed loan', 'foreclosure']:
            try:
                loan_disbursed_timestamp = selected_row['loan_disbursed_timestamp']
                emi_payment_type = selected_row['emi_payment_type']

                if loan_disbursed_timestamp:
                    print("Loan Disbursed Timestamp:", loan_disbursed_timestamp)

                    if emi_payment_type == 'Monthly':
                        # Add months based on current month
                        payment_date = loan_disbursed_timestamp + timedelta(days=current_month * 30)
                    elif emi_payment_type == 'One Time':
                        # Payment date is set for the first month only
                        payment_date = loan_disbursed_timestamp + timedelta(days=30)  # Assuming 30 days per month
                    elif emi_payment_type == 'Three Month':
                        # Add 3 months to the loan disbursal date
                        payment_date = loan_disbursed_timestamp + timedelta(days=current_month * 90)
                    elif emi_payment_type == 'Six Month':
                        # Add 6 months to the loan disbursal date
                        payment_date = loan_disbursed_timestamp + timedelta(days=current_month * 180)
                    else:
                        payment_date = None

                    return payment_date
                else:
                    print("Loan Disbursed Timestamp is None")
                    return None
            except Exception as e:
                print(f"Error in calculate_payment_date: {e}")
                return None
        else:
            print("Loan Updated Status not in expected list")
            return None

    def calculate_monthly_emi_and_balance(self, selected_row, current_month):
      emi = self.calculate_emi(selected_row)
      beginning_balance = selected_row['total_repayment_amount']
  
      # Initialize Total Repayment Beginning Balance (TRBB) and Total Repayment Ending Balance (TREB)
      total_repayment_beginning_balance = selected_row['total_repayment_amount']
      total_repayment_ending_balance = total_repayment_beginning_balance
  
      # For monthly payments, calculate ending balance
      for month in range(1, current_month + 1):
          interest_amount = beginning_balance * (selected_row['interest_rate'] / 100) / 12
          principal_amount = emi - interest_amount
          total_repayment_beginning_balance = total_repayment_ending_balance  # Update TRBB for the next iteration
          total_repayment_ending_balance -= principal_amount  # Update TREB for the next iteration
          beginning_balance -= principal_amount  # Update beginning balance for the next iteration
  
      ending_balance = beginning_balance
      return emi, ending_balance, total_repayment_beginning_balance, total_repayment_ending_balance
  
    def calculate_three_month_emi_and_balance(self, selected_row, current_month):
      emi = self.calculate_emi(selected_row)
      beginning_balance = selected_row['total_repayment_amount']
  
      # Initialize Total Repayment Beginning Balance (TRBB) and Total Repayment Ending Balance (TREB)
      total_repayment_beginning_balance = selected_row['total_repayment_amount']
      total_repayment_ending_balance = total_repayment_beginning_balance
  
      # Calculate ending balance for the current month
      for period in range(1, current_month + 1):
          interest_amount = beginning_balance * (selected_row['interest_rate'] / 100) / (12 * 3)
          principal_amount = emi - interest_amount
          # total_repayment_beginning_balance = total_repayment_ending_balance  # Update TRBB for the next iteration
          # total_repayment_ending_balance -= principal_amount
          beginning_balance -= principal_amount  # Update beginning balance for the next iteration
  
      ending_balance = beginning_balance
      return emi, ending_balance, total_repayment_beginning_balance, total_repayment_ending_balance
    
    def calculate_six_month_emi_and_balance(self, selected_row, current_month):
        emi = self.calculate_emi(selected_row)
        beginning_balance = selected_row['total_repayment_amount']
    
        # Initialize Total Repayment Beginning Balance (TRBB) and Total Repayment Ending Balance (TREB)
        total_repayment_beginning_balance = selected_row['total_repayment_amount']
        total_repayment_ending_balance = total_repayment_beginning_balance
    
        # For six-month payments, calculate ending balance for each 6-month period
        for period in range(1, current_month + 1):
            interest_amount = beginning_balance * (selected_row['interest_rate'] / 100) / (12 * 6)
            principal_amount = emi - interest_amount
            total_repayment_beginning_balance = total_repayment_ending_balance  # Update TRBB for the next iteration
            total_repayment_ending_balance -= principal_amount  # Update TREB for the next iteration
            beginning_balance -= principal_amount  # Update beginning balance for the next iteration
    
        ending_balance = beginning_balance
        return emi, ending_balance, total_repayment_beginning_balance, total_repayment_ending_balance

    def calculate_one_time_emi_and_balance(self, selected_row, current_month):
        emi = self.calculate_emi(selected_row)
        beginning_balance = selected_row['total_repayment_amount']
    
        # Initialize Total Repayment Beginning Balance (TRBB) and Total Repayment Ending Balance (TREB)
        total_repayment_beginning_balance = selected_row['total_repayment_amount']
        total_repayment_ending_balance = total_repayment_beginning_balance
    
        # For one-time payment, calculate ending balance for the single payment
        interest_amount = beginning_balance * (selected_row['interest_rate'] / 100) / 12
        principal_amount = emi - interest_amount
        total_repayment_beginning_balance = total_repayment_ending_balance  # Update TRBB for the next iteration
        total_repayment_ending_balance -= principal_amount  # Update TREB for the next iteration
        beginning_balance -= principal_amount  # Update beginning balance for the next iteration
    
        ending_balance = 0
        return emi, ending_balance, total_repayment_beginning_balance, total_repayment_ending_balance
      
    def calculate_num_payments(self, selected_row):
        tenure = selected_row['tenure']
        payment_type = selected_row['emi_payment_type']

        if payment_type == 'One Time':
            return 1
        elif payment_type == 'Monthly':
            return tenure
        elif payment_type == 'Three Month':
            return tenure // 3
        elif payment_type == 'Six Month':
            return tenure // 6
        else:
            return 0

    def calculate_emi(self, selected_row, tenure=None, repayment_amount=None):
        tenure = selected_row['tenure'] if tenure is None else tenure
        monthly_interest_rate = (selected_row['interest_rate'] / 100) / 12
        loan_amount = selected_row['loan_amount'] - repayment_amount if repayment_amount else selected_row['loan_amount']
    
        if selected_row['emi_payment_type'] == 'Monthly':
            emi = (loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** tenure)) / (((1 + monthly_interest_rate) ** tenure) - 1)
        elif selected_row['emi_payment_type'] == 'One Time':
            emi = loan_amount / tenure
        elif selected_row['emi_payment_type'] == 'Three Month':
            monthly_interest_rate = (selected_row['interest_rate'] / 100) / (12 * 3)  # Corrected calculation for 3 months
            emi = (loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** (tenure / 3))) / (((1 + monthly_interest_rate) ** (tenure / 3)) - 1)
        elif selected_row['emi_payment_type'] == 'Six Month':
            monthly_interest_rate = (selected_row['interest_rate'] / 100) / (12 * 6)  # Corrected calculation for 6 months
            emi = (loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** (tenure / 6))) / (((1 + monthly_interest_rate) ** (tenure / 6)) - 1)
        else:
            emi = 0  # Handle unsupported payment types
    
        return emi

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower_registration_form.dashboard')

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower_registration_form.dashboard.today_dues', selected_row=self.selected_row)