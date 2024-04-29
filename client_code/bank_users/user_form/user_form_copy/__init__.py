from ._anvil_designer import user_form_copyTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..user_form import user_module
from ..borrower_rgistration_form import borrower_main_form_module
from ..main_form import main_form_module

class user_form_copy(user_form_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.email = main_form_module.email
    email=self.email
    self.name = user_module.get_name(email)
    self.user_id =  user_module.find_user_id(email)

    self.email = email
    self.user_name_lable.text = self.name
    if main_form_module.alert_mes(main_form_module.flag):
      print("user login")
    else:
      print("user login")

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    alert("Logged out sucessfully")
    anvil.users.logout()
    open_form('bank_users.main_form')

  def home_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("bank_users.main_form")

  def borrower_button_click(self, **event_args):
    userid = self.user_id
    open_form('borrower_registration_form.borrower_registration_form_1_education',user_id=userid)

  def lendor_button_click(self, **event_args):
    userid = self.user_id
    open_form('lendor_registration_form.lender_reg_form_1_education_form',user_id=userid)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form.products_main_form')

  def contact_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form.contact_main_form')

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.user_issue.user_bugreports')
