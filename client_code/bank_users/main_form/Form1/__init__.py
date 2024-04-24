from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js import window

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    

def button_mouseover(self, **event_args):
    # Show dropdown content when hovering over the button
    window.get_element_by_id('dropdown-content').style.display = 'block'

def navigate_to_registration_form(self, **event_args):
    # Call server function to navigate to registration form
    anvil.server.call('navigate_to_registration_form')

def navigate_to_loan_application_form(self, **event_args):
    # Call server function to navigate to loan application form
    anvil.server.call('navigate_to_loan_application_form')

  
