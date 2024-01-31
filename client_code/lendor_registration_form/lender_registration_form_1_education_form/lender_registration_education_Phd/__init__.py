from ._anvil_designer import lender_registration_education_PhdTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class lender_registration_education_Phd(lender_registration_education_PhdTemplate):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    



    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    user_id = self.userId
    open_form('lendor_registration_form.lender_registration_form_1_education_form',user_id=user_id)
    
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    user_id = self.userId
    open_form('lendor_registration_form.lender_registration_form_2_marital_details',user_id=user_id)

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")
