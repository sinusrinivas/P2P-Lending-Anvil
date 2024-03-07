from ._anvil_designer import view_lost_oppurtunitiesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import lendor_main_form_module as main_form_module


class view_lost_oppurtunities(view_lost_oppurtunitiesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id = main_form_module.userId
    #self.repeating_panel_1.items = app_tables.fin_loan_details.search(loan_updated_status=q.like('lost opportunities%'))
    lost_opportunities = app_tables.fin_loan_details.search(loan_updated_status=q.like('lost opportunities%'))
    borrower_customer_ids = [loan['lender_customer_id'] for loan in lost_opportunities]

        # Retrieve profiles for each borrower customer ID
    borrower_profiles = []
    for customer_id in borrower_customer_ids:
            user_profile = app_tables.fin_user_profile.get(customer_id=customer_id)
            if user_profile is not None:
                borrower_profiles.append(user_profile.to_dict())

        # Update UI with borrower profiles
    self.repeating_panel_1.items = borrower_profiles
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard")

  