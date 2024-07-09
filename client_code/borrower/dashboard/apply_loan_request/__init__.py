from ._anvil_designer import apply_loan_requestTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables
from .. import main_form_module

class apply_loan_request(apply_loan_requestTemplate):
    def __init__(self, **properties):
        self.user_id = main_form_module.userId
        self.product_description = None
        self.init_components(**properties)

        options = app_tables.fin_product_details.search()
        option_strings = [option['product_group'] for option in options if option['product_group'].strip()]
        unique_groups = set(option_strings)  # Remove duplicates using set
        self.name.items = list(unique_groups)
        self.name.selected_value = None 
        self.drop_down_2.items = ['']  # Add your placeholder text here
        self.drop_down_2.selected_value = None
        self.drop_down_1.items = ['']
        self.drop_down_1.selected_value = None
        self.drop_down_3.items = ['']
        self.drop_down_3.selected_value = None
        # self.drop_down_3_change()

    def name_change(self, **event_args):
        self.selected_value = self.name.selected_value

        if self.selected_value:
            self.label_1.visible = True
            self.label_2.visible = True
            self.name.visible = True
            self.drop_down_2.visible = True
            self.label_4.visible = True
            # Fetch product categories based on the selected loan type
            product_categories = app_tables.fin_product_details.search(
                product_group=self.name.selected_value
            )
            # Exclude duplicate categories
            unique_categories = set(category['product_categories'] for category in product_categories if category['product_categories'].strip())
            if unique_categories:
                # Display unique product categories in drop_down_2
                self.drop_down_2.items = list(unique_categories)
                self.drop_down_2.selected_value = None

    def drop_down_2_change(self, **event_args):
        self.selected_value = self.drop_down_2.selected_value
        if self.selected_value:
            self.label_1.visible = True
            self.label_2.visible = True
            self.name.visible = True
            self.drop_down_2.visible = True
            self.label_4.visible = True
            self.label_6.visible = True
            self.label_7.visible = True
            self.drop_down_1.visible = True

            # Fetch product names based on the selected category
            product_names = app_tables.fin_product_details.search(product_categories=self.selected_value)
            if product_names:
                # Extract product names from the list of rows
                product_name_list = [product['product_name'] for product in product_names if product['product_name'].strip()]
                self.drop_down_1.items = product_name_list
                self.drop_down_1.selected_value = None

    def drop_down_1_change(self, **event_args):
        selected_product_name = self.drop_down_1.selected_value
        self.link_2.visible = True
        if selected_product_name:
            product_details = app_tables.fin_product_details.get(product_name=selected_product_name)

            if product_details:
                self.label_8.visible = True
                self.product_description_label.visible = True
                self.product_description_label.text = product_details['product_description']
            else:
                self.label_8.visible = True
                self.product_description_label.visible = True
                self.product_description_label.text = "Product description not available"
        else:
            self.label_8.visible = False
            self.product_description_label.visible = True
            self.product_description_label.text = ""

    def link_2_click(self, **event_args):      
      # self.drop_down_3_change()
      name = self.name.selected_value
      category = self.drop_down_2.selected_value
      product_name = self.drop_down_1.selected_value

      if not name:
          self.label_3.text = "Please select a product group"
          self.label_3.foreground = '#FF0000'
      else:
          self.label_3.text = ""

      if not category:
          self.label_4.text = "Please select a category"
          self.label_4.foreground = '#FF0000'
      else:
          self.label_4.text = ""

      if not product_name:
          self.label_7.text = "Please select a product name"
          self.label_7.foreground = '#FF0000'
      else:
          self.label_7.text = ""

      if name and category and product_name:
          if any(row['product_name'] == product_name for row in app_tables.fin_loan_details.search(borrower_customer_id=self.user_id)):
              self.name.selected_value = None
              self.drop_down_1.selected_value = None
              self.drop_down_2.selected_value = None
              alert(f'Product "{product_name}" already exists. Please choose a different Product name.')
          else:
              # Fetch product details based on the selected product name
              product_details = app_tables.fin_product_details.get(product_name=product_name)
              if product_details:
                  # Set product_description as a class attribute
                  self.product_description = product_details['product_description']
                  # self.interest_rate = product_details['interest_rate']
                  # self.processing_fee = product_details['processing_fee']
                  # self.tenure_months = product_details['tenure_months']
                  # self.loan_amount = product_details['loan_amount']
                  # self.credit_limit = product_details['credit_limit']
                  # self.calculate_and_display_payment_details()
                  self.link_2.visible = False
                  self.label_2_copy.visible = True
                  self.loan_amount_tb.visible = True
                  self.label_22.visible = True
                  self.label_4_copy.visible = True
                  self.label_7_copy.visible = True
                  self.label_20.visible = True
                  self.label_21.visible = True
                  self.label_23.visible = True
                  self.label_3_copy.visible = True
                  self.text_box_1.visible = True
                  self.label_39.visible = True
                  self.drop_down_3.visible = True
                  
                  # self.link_1.visible = True
                  self.product_name = self.drop_down_1.selected_value
                  user_request = app_tables.fin_product_details.get(product_name=self.product_name)
                  if user_request:
                    self.label_7_copy.text = user_request['roi']
                    self.label_21.text = user_request['processing_fee']
              else:
                  self.label_8.visible = True
                  self.product_description_label.text = "Product description not available"

    def link_1_click(self, **event_args):
      self.link_1.visible = False
      self.column_panel_3.visible = True
      self.submit.visible = True
      self.label_28.text = self.loan_amount_tb.text
      self.label_32.text = self.label_21.text

    def link_3_click(self, **event_args):
      self.link_3.visible = False
      self.column_panel_1.visible = True
      

    def drop_down_3_change(self, **event_args):
        # This method is called when an item is selected in drop_down_3
        self.selected_value = self.drop_down_3.selected_value
        product_group = self.name.selected_value
        product_category = self.drop_down_2.selected_value
        product_name = self.drop_down_1.selected_value
        self.link_1.visible = True
    
        if product_group and product_category and product_name:
            # Fetch the data from fin_product_details based on the product_group, product_category, and product_name
            product_details = app_tables.fin_product_details.search(
                product_group=product_group,
                product_categories=product_category,
                product_name=product_name
            )
            product_details = list(product_details)
            if product_details:
                product_detail = product_details[0]
                emi_payment_options = product_detail['emi_payment']
                emi_payment_options = emi_payment_options.split(", ") if emi_payment_options else []
                self.drop_down_3.items = emi_payment_options
                self.link_1.visible = True
                self.column_panel_3.visible = False

    def calculate_and_display_payment_details(self):
        if self.entered_payment_type == "One Time":
            self.display_one_time_payment_details()
        elif self.entered_payment_type == "Monthly":
            self.display_monthly_payment_details()
        elif self.entered_payment_type == "Three Months":
            self.display_three_month_payment_details(total_interest_amount=self.total_interest)
        elif self.entered_payment_type == "Six Months":
            self.display_six_month_payment_details(total_interest_amount=self.total_interest)

    def display_one_time_payment_details(self):
        total_repayment_amount = float(str(self.total_repayment_amount).replace('₹ ', ''))
        total_interest = float(str(self.total_interest).replace('₹ ', ''))
        processing_fee_amount = float(str(self.processing_fee_amount).replace('₹ ', ''))

        payment_details = [{
            'PaymentNumber': '1',
            'Principal': f"₹ {self.loan_amount:.2f}",
            'Interest': f"₹ {total_interest:.2f}",
            'ProcessingFee': f"₹ {processing_fee_amount:.2f}",
            'BeginningBalance': f"₹ {total_repayment_amount:.2f}",
            'TotalPayment': f"₹ {total_repayment_amount:.2f}",
            'EndingBalance': '₹ 0.00',
            'LoanAmountBeginningBalance': f"₹ {self.loan_amount:.2f}",
            'LoanAmountEndingBalance': f"₹ 0.00"
        }]
        self.repeating_panel_1.items = payment_details

    def display_monthly_payment_details(self):
        monthly_interest_rate = float(self.interest_rate / 100) / 12
        emi_denominator = ((1 + monthly_interest_rate) ** self.tenure_months) - 1
        emi_numerator = self.loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** self.tenure_months)
        emi = emi_numerator / emi_denominator
        payment_details = self.calculate_payment_schedule(self.total_repayment_amount, emi, monthly_interest_rate)
        self.repeating_panel_1.items = payment_details

    def calculate_payment_schedule(self, total_repayment_amount, emi, monthly_interest_rate):
        payment_schedule = []
        processing_fee_per_month = (self.processing_fee / 100) * self.loan_amount / self.tenure_months
        beginning_balance = total_repayment_amount
        loan_amount_beginning_balance = self.loan_amount
        for month in range(1, self.tenure_months + 1):
            interest_amount = loan_amount_beginning_balance * monthly_interest_rate
            principal_amount = emi - interest_amount
            total_payment = emi + processing_fee_per_month
            loan_amount_ending_balance = loan_amount_beginning_balance - principal_amount
            payment_schedule.append({
                'PaymentNumber': month,
                'Principal': f"₹ {principal_amount:.2f}",
                'Interest': f"₹ {interest_amount:.2f}",
                'ProcessingFee': f"₹ {processing_fee_per_month:.2f}",
                'LoanAmountBeginningBalance': f"₹ {loan_amount_beginning_balance:.2f}",
                'LoanAmountEndingBalance': f"₹ {loan_amount_ending_balance:.2f}",
                'BeginningBalance': f"₹ {beginning_balance:.2f}",
                'TotalPayment': f"₹ {total_payment:.2f}",
                'EndingBalance': f"₹ {max(0, beginning_balance - total_payment):.2f}"
            })
            beginning_balance -= total_payment
            loan_amount_beginning_balance = loan_amount_ending_balance
        return payment_schedule

    def display_three_month_payment_details(self, total_interest_amount):
        monthly_interest_rate = self.interest_rate / 100 / 12
        emi_denominator = ((1 + monthly_interest_rate) ** self.tenure_months) - 1
        emi_numerator = self.loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** self.tenure_months)
        emi = emi_numerator / emi_denominator
        processing_fee_per_month = (self.processing_fee / 100) * self.loan_amount / self.tenure_months
        payment_schedule = self.calculate_three_month_payment_schedule(emi, monthly_interest_rate, processing_fee_per_month, total_interest_amount)
        self.repeating_panel_1.items = payment_schedule

    def calculate_three_month_payment_schedule(self, emi, monthly_interest_rate, processing_fee_per_month, total_interest_amount):
        payment_schedule = []
        beginning_balance = self.total_repayment_amount
        loan_amount_beginning_balance = self.loan_amount

        for month in range(1, self.tenure_months + 1, 3):
            interest_for_3_months = self.calculate_interest_for_months(emi, loan_amount_beginning_balance, monthly_interest_rate, month, month + 2)
            total_processing_fee_for_3_months = processing_fee_per_month * 3
            total_payment = emi * 3 + total_processing_fee_for_3_months
            payment_schedule.append({
                'PaymentNumber': f"{month}-{month+2}",
                'Principal': f"₹ {emi * 3 - interest_for_3_months:.2f}",
                'Interest': f"₹ {interest_for_3_months:.2f}",
                'ProcessingFee': f"₹ {total_processing_fee_for_3_months:.2f}",
                'LoanAmountBeginningBalance': f"₹ {loan_amount_beginning_balance:.2f}",
                'LoanAmountEndingBalance': f"₹ {loan_amount_beginning_balance - (emi * 3 - interest_for_3_months)::.2f}",
                'BeginningBalance': f"₹ {beginning_balance:.2f}",
                'TotalPayment': f"₹ {total_payment:.2f}",
                'EndingBalance': f"₹ {max(0, beginning_balance - total_payment):.2f}"
            })

            beginning_balance -= total_payment
            loan_amount_beginning_balance -= (emi * 3 - interest_for_3_months)
        return payment_schedule

    def display_six_month_payment_details(self, total_interest_amount):
        monthly_interest_rate = self.interest_rate / 100 / 12
        emi_denominator = ((1 + monthly_interest_rate) ** self.tenure_months) - 1
        emi_numerator = self.loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** self.tenure_months)
        emi = emi_numerator / emi_denominator
        processing_fee_per_month = (self.processing_fee / 100) * self.loan_amount / self.tenure_months
        payment_schedule = self.calculate_six_month_payment_schedule(emi, monthly_interest_rate, processing_fee_per_month, total_interest_amount)
        self.repeating_panel_1.items = payment_schedule

    def calculate_six_month_payment_schedule(self, emi, monthly_interest_rate, processing_fee_per_month, total_interest_amount):
        payment_schedule = []
        beginning_balance = self.total_repayment_amount
        loan_amount_beginning_balance = self.loan_amount
        for month in range(1, self.tenure_months + 1, 6):
            interest_for_6_months = self.calculate_interest_for_months(emi, loan_amount_beginning_balance, monthly_interest_rate, month, month + 5)
            total_processing_fee_for_6_months = processing_fee_per_month * 6

            total_payment = emi * 6 + total_processing_fee_for_6_months

            payment_schedule.append({
                'PaymentNumber': f"{month}-{month+5}",
                'Principal': f"₹ {emi * 6 - interest_for_6_months:.2f}",
                'Interest': f"₹ {interest_for_6_months:.2f}",
                'ProcessingFee': f"₹ {total_processing_fee_for_6_months:.2f}",
                'LoanAmountBeginningBalance': f"₹ {loan_amount_beginning_balance:.2f}",
                'LoanAmountEndingBalance': f"₹ {loan_amount_beginning_balance - (emi * 6 - interest_for_6_months):.2f}",
                'BeginningBalance': f"₹ {beginning_balance:.2f}",
                'TotalPayment': f"₹ {total_payment:.2f}",
                'EndingBalance': f"₹ {max(0, beginning_balance - total_payment):.2f}"
            })

            beginning_balance -= total_payment
            loan_amount_beginning_balance -= (emi * 6 - interest_for_6_months)

        return payment_schedule

    def calculate_interest_for_months(self, emi, loan_amount_beginning_balance, monthly_interest_rate, start_month, end_month):
        total_interest = 0
        for month in range(start_month, end_month + 1):
            interest_amount = loan_amount_beginning_balance * monthly_interest_rate
            loan_amount_beginning_balance -= (emi - interest_amount)
            total_interest += interest_amount
        return total_interest

    def submit_click(self, **event_args):
        result = anvil.server.call('add_loan_details',
                                   self.loan_amount,
                                   self.tenure_months,
                                   self.user_id,
                                   self.interest_rate,
                                   self.total_repayment_amount,
                                   self.product_id,
                                   self.membership_type,
                                   self.credit_limt,
                                   self.product_name,
                                   self.entered_payment_type,
                                   self.processing_fee_amount,
                                   self.total_interest,
                                   self.product_discription,
                                   self.emi)

        print(result)
        alert("Request Submitted")
        open_form('borrower.dashboard')
