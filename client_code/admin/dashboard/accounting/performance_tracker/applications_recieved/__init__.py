from ._anvil_designer import applications_recievedTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class applications_recieved(applications_recievedTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.drop_down_1.items = ['', 'daily', 'monthly']
    self.column_panel_1.visible = False  # Ensure column_panel_1 is initially hidden
    self.column_panel_2.visible = False  # Ensure column_panel_2 is initially hidden

    # Initialize month and year dropdowns
    self.drop_down_month.items = [(month, i+1) for i, month in enumerate(
            ["January", "February", "March", "April", "May", "June", 
             "July", "August", "September", "October", "November", "December"]
    )]
    self.text_box_year.text = str(datetime.now().year)

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    self.selected_date = self.date_picker_1.date
    print("Selected date:", self.selected_date)

    if self.selected_date:
        # Fetch loans from the database
        loans = app_tables.fin_loan_details.search()
                
        # Initialize an empty list to store filtered loans
        filtered_loans = []

        for loan in loans:
            user_profile = app_tables.fin_user_profile.get(customer_id=loan['borrower_customer_id'])
                    
            if user_profile is not None and loan['loan_updated_status'] in ["under process"]:
                # Directly compare loan['borrower_loan_created_timestamp'] with self.selected_date
                if loan['borrower_loan_created_timestamp'] == self.selected_date: 
                    filtered_loans.append({
                            'user_photo': user_profile['user_photo'],
                            'borrower_full_name': loan['borrower_full_name'],
                            'borrower_email_id': loan['borrower_email_id'],
                            'lender_full_name': loan['lender_full_name'],
                            'lender_email_id': loan['lender_email_id'],
                            'ascend_score': user_profile['ascend_value'],
                            'loan_amount': loan['loan_amount'],
                            'loan_updated_status': loan['loan_updated_status'],
                            'loan_id': loan['loan_id'],
                            'total_repayment_amount': loan['total_repayment_amount'],
                            'membership_type': loan['membership_type'],
                            'product_name': loan['product_name'],
                            'borrower_loan_created_timestamp': loan['borrower_loan_created_timestamp'],
                    })
                         
                
        if not filtered_loans:
            Notification(f"No Loans with status 'under process' found for {self.selected_date}!").show()
            self.data_grid_1.visible = False  # Hide the DataGrid if no loans found
        else:
            # Update RepeatingPanel with filtered results
            self.repeating_panel_1.items = filtered_loans
            self.data_grid_1.visible = True  # Make the DataGrid visible


  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    selected_filter = self.drop_down_1.selected_value
    print("Selected filter:", selected_filter)  # Debugging print
        
    if selected_filter == 'daily':
        self.column_panel_1.visible = True      # Make the column_panel_1 visible
        self.column_panel_2.visible = False     # Hide column_panel_2
        self.update_daily_panel()
    elif selected_filter == 'monthly':
        self.column_panel_1.visible = False     # Hide the column_panel_1
        self.column_panel_2.visible = True      # Make the column_panel_2 visible
        self.update_monthly_panel()
    else:
        self.column_panel_1.visible = False     # Hide both panels if neither 'daily' nor 'monthly' is selected
        self.column_panel_2.visible = False

  def update_daily_panel(self):
      # Your implementation for updating the daily panel
      pass

  def update_monthly_panel(self):
      # Your implementation for updating the monthly panel
      selected_month = self.drop_down_month.selected_value
      selected_year = self.text_box_year.text

      if selected_month and selected_year:
          try:
              selected_year = int(selected_year)
          except ValueError:
              Notification("Please enter a valid year!").show()
              return

          loans = app_tables.fin_loan_details.search()

          filtered_loans = []

          for loan in loans:
              user_profile = app_tables.fin_user_profile.get(customer_id=loan['borrower_customer_id'])

              if user_profile is not None and loan['loan_updated_status'] in ["under process"]:
                  if loan['borrower_loan_created_timestamp'].month == selected_month and loan['borrower_loan_created_timestamp'].year == selected_year:
                      filtered_loans.append({
                            'user_photo': user_profile['user_photo'],
                            'borrower_full_name': loan['borrower_full_name'],
                            'borrower_email_id': loan['borrower_email_id'],
                            'lender_full_name': loan['lender_full_name'],
                            'lender_email_id': loan['lender_email_id'],
                            'ascend_score': user_profile['ascend_value'],
                            'loan_amount': loan['loan_amount'],
                            'loan_updated_status': loan['loan_updated_status'],
                            'loan_id': loan['loan_id'],
                            'total_repayment_amount': loan['total_repayment_amount'],
                            'membership_type': loan['membership_type'],
                            'product_name': loan['product_name'],
                            'borrower_loan_created_timestamp': loan['borrower_loan_created_timestamp'],
                      })

          if not filtered_loans:
              Notification(f"No Loans with status 'under process' found for {self.drop_down_month.items[selected_month-1][0]} {selected_year}!").show()
              self.data_grid_2.visible = False
          else:
              self.repeating_panel_2.items = filtered_loans
              self.data_grid_2.visible = True

  

  def drop_down_month_change(self, **event_args):
    """This method is called when an item is selected"""
    self.update_monthly_panel()
    
  def text_box_year_change(self, **event_args):
      """This method is called when the text is changed"""
      self.update_monthly_panel()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.accounting.performance_tracker')

              

