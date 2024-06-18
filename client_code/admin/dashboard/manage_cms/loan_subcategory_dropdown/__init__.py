from ._anvil_designer import loan_subcategory_dropdownTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class loan_subcategory_dropdown(loan_subcategory_dropdownTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('admin.dashboard.manage_cms')

  def borrower_loan_issue(self, **event_args):
    self.repeating_panel_1.items = app_tables.fin_report_issue_category.search()
    self.column_panel_10.visible = True
    self.column_panel_11_copy.visible = False
    self.column_panel_12_copy_2.visible = False

  def lender_loan_issue(self, **event_args):
    self.repeating_panel_3.items = app_tables.fin_report_issue_category.search()
    self.column_panel_10.visible = False
    self.column_panel_11_copy.visible = False
    self.column_panel_12_copy_2.visible = True

  def technical_issue(self, **event_args):
    self.repeating_panel_2.items = app_tables.fin_report_issue_category.search()
    self.column_panel_10.visible = False
    self.column_panel_11_copy.visible = True
    self.column_panel_12_copy_2.visible = False

  def refresh(self):
    self.repeating_panel_1.items = app_tables.fin_report_issue_category.search()
    self.repeating_panel_2.items = app_tables.fin_report_issue_category.search()
    self.repeating_panel_3.items = app_tables.fin_report_issue_category.search()

  def borrower_issue(self, **event_args):
    enter_data = self.text_box_9.text

    if not enter_data:
        alert("Please enter a valid Borrower Loan Issues: 'Loan Not Approved', 'Loan declained', 'Other'.")
        return
    new_row = app_tables.fin_report_issue_category.add_row(borrower_subcategory_loan_issue=enter_data)
    self.text_box_9.text = ' '
    self.refresh()

  def technical_issue_click(self, **event_args):
    enter_data = self.text_box_9_copy.text
  
    if not enter_data:
          alert("Please enter a valid Technical Issues: 'Button Not Working', 'Page Not Working', 'Other'.")
          return
    new_row = app_tables.fin_report_issue_category.add_row(subcategory_technical_issue=enter_data)
    self.text_box_9_copy.text = ' '
    self.refresh()

  def lender_issue_click(self, **event_args):
    enter_data = self.text_box_9_copy_2.text
  
    if not enter_data:
          alert("Please enter a valid Technical Issues: 'Loan Not Approved', 'Amount Not Credited', 'Other'.")
          return
    new_row = app_tables.fin_report_issue_category.add_row(lendor_subcategory_loan_issue=enter_data)
    self.text_box_9_copy_2.text = ' '
    self.refresh()

