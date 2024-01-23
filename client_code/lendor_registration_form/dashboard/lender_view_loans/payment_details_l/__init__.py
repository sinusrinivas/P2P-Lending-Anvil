import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta
import anvil.server
import anvil.tables as tables
from anvil import DataGrid, alert, open_form
from ._anvil_designer import payment_details_lTemplate
class payment_details_l(payment_details_lTemplate):
    def __init__(self, selected_row=None, entered_values=None, **properties):
        self.selected_row = selected_row
        self.init_components(**properties)

        if selected_row:
            self.load_payment_details(selected_row, entered_values)

    def load_payment_details(self, selected_row, entered_values):
        self.load_entered_values(entered_values)
        payment_details = []
        monthly_interest_rate = (self.selected_row['interest_rate'] / 100) / 12
        extra_payment = 0
        emi = (self.selected_row['loan_amount'] * monthly_interest_rate * ((1 + monthly_interest_rate) ** self.selected_row['tenure'])) / (
                ((1 + monthly_interest_rate) ** self.selected_row['tenure']) - 1)
        beginning_balance = self.selected_row['loan_amount']
        for month in range(1, self.selected_row['tenure'] + 1):
            payment_date = self.calculate_payment_date(selected_row, month)
            formatted_payment_date = f"{payment_date:%Y-%m-%d}" if payment_date else "Awaiting Update"
            if payment_date is None:
                self.label_1.enabled = True
                self.label_1.text = "Payment Date will be updated after loan disbursed"
            else:
                self.label_1.enabled = False
                self.label_1.text = ""

            interest_amount = beginning_balance * monthly_interest_rate
            principal_amount = emi - interest_amount
            ending_balance = beginning_balance - principal_amount

            payment_details.append({
                'PaymentNumber': month,
                'PaymentDate': formatted_payment_date,
                'ScheduledPayment': f"₹ {emi:.2f}",
                'Principal': f"₹ {principal_amount:.2f}",
                'Interest': f"₹ {interest_amount:.2f}",
                'BeginningBalance': f"₹ {beginning_balance:.2f}",
                'ExtraPayment': f"₹ {extra_payment:.2f}",
                'TotalPayment': f"₹ {emi + extra_payment:.2f}",
                'EndingBalance': f"₹ {ending_balance:.2f}"
            })

            beginning_balance = ending_balance

        self.repeating_panel_1.items = payment_details

    def load_entered_values(self, entered_values):
        if entered_values:
            # Load previously entered values into the form fields
            self.entered_loan_amount = entered_values.get('loan_amount', None)
            self.entered_tenure = entered_values.get('tenure', None)
            self.entered_payment_type = entered_values.get('payment_type', None)

    def calculate_payment_date(self, selected_row, current_month):
        loan_updated_status = selected_row['loan_updated_status'].lower()
    
        if loan_updated_status in ['close', 'closed loans', 'disbursed loan', 'foreclosure']:
            try:
                loan_disbursed_timestamp = selected_row['loan_disbursed_timestamp']
    
                if loan_disbursed_timestamp:
                    fin_product_details_row = app_tables.fin_product_details.get(
                        product_id=selected_row['product_id']
                    )
                    first_emi_payment = fin_product_details_row['first_emi_payment']
    
                    # Calculate payment date based on loan_disbursed_timestamp and first_emi_payment
                    if current_month == 1:
                        payment_date = loan_disbursed_timestamp + timedelta(
                            days=int(first_emi_payment * 30.44)
                        )
                    else:
                        payment_date = loan_disbursed_timestamp + timedelta(
                            days=int(first_emi_payment * 30.44) + (current_month - 1) * 30  # Assuming an average of 30 days in a month
                        )
    
                    return payment_date
                else:
                    return None
            except Exception as e:
                print(f"Error in calculate_payment_date: {e}")
                return None
        else:
            return None

    def button_1_click(self, **event_args):
        open_form('lendor_registration_form.dashboard')

    def button_2_click(self, **event_args):
        # Pass the selected_row to view_details_1 form
        open_form('lendor_registration_form.dashboard.lender_view_loans.view_details_1', selected_row=self.selected_row)