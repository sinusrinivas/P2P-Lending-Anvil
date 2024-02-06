from ._anvil_designer import view_borrower_loan_requestTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import lendor_main_form_module as main_form_module

class view_borrower_loan_request(view_borrower_loan_requestTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id=main_form_module.userId
    
    self.repeating_panel_1.items=app_tables.fin_loan_details.search(loan_updated_status="under process")
    #under process
   # anvil.server.call('transfer_user_profile_to_loan_details', email) 
    # Fetch data from fin_lender table
    lender_data = data_tables.fin_lender.search(customer_id=self.user_id)
        
        # Check if there is any matching data
    if lender_data:
      lender_row = lender_data[0]  # Assuming there is only one row for the user_id
            
      # Extract lender details
      lender_customer_id = lender_row['customer_id']
      lender_email_id = lender_row['email_id']
            
      # Update fin_loan_details table
      loan_details_data = {'lender_customer_id': lender_customer_id,
                            'lender_email_id': lender_email_id}
      data_tables.fin_loan_details.add_row(**loan_details_data)
            
      # Display the details in your form (replace with your actual components)
      self.label_lender_customer_id.text = lender_customer_id
      self.label_lender_email_id.text = lender_email_id
    else:
      # Handle the case where no lender data is found for the user_id
      print("No lender data found for user_id:", self.user_id)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.opbal")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard")

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.avlbal")

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.ld")

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vlo")

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.td")

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vcl")

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vler")

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vlfr")

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.rta")

  def link_10_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vdp")

  def link_11_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vep")

  def link_12_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vsn")

  def link_13_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.cp")





    # Any code you write here will run before the form opens.
