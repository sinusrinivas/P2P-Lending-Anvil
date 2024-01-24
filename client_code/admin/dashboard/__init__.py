from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class dashboard(dashboardTemplate):
  def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)


  #       loan_status = self.get_loan_status(borrower_customer_id)

  #       if loan_status == 'disbursed':
  #           # Call the server function to add fin_emi_details
  #           result = anvil.server.call('add_fin_emi_details', 
  #                                      borrower_customer_id,
  #                                      borrower_email,
  #                                      scheduled_payment,
  #                                      payment_number,
  #                                      payment_date,
  #                                      loan_id,
  #                                      emi_status)
            
  #           # Handle the result as needed
  #           if result == 'Loan details not found':
  #               print('Error:', result)
  #           else:
  #               print('EMI ID:', result)
  #       else:
  #           print('Loan not disbursed. Cannot generate EMI ID.')

  #   # Function to get loan status
  # def get_loan_status(self, borrower_customer_id):
  #       loan_details = app_tables.loan_details.search(borrower_customer_id == borrower_customer_id)
  #       if loan_details and len(loan_details) > 0:
  #           return loan_details[0]['loan_updated_status']
  #       else:
  #           return 'Loan details not found'
  
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.admin_teams')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.borrowers')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.lenders')

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management')

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products')

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_settings')

  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.revenue_share')

  def button_9_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.risk_pool')

  def button_10_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_cms')

  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_reports')

  def button_13_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.performance_tracker')

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_dropdown')
