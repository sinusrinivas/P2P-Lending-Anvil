from ._anvil_designer import lender_registration_form_3_marital_marriedTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class lender_registration_form_3_marital_married(lender_registration_form_3_marital_marriedTemplate):
  def __init__(self,user_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.userId = user_id
    self.another_person = None

    # Any code you write here will run before the form opens.

  # def home_borrower_registration_form_copy_1_click(self, **event_args):
  #   open_form('bank_users.user_form')

  def radio_button_change(self, **event_args):
    selected_button = self.radio_buttons.selected_button
    self.another_person = selected_button.text.lower()
    
    # Hide other radio buttons
    for button in self.radio_buttons.components:
      if button != selected_button:
        button.visible = False

    # Call the server function to update the database
        anvil.server.call('update_another_person', self.userId, self.another_person)
  
  def button_submit_click(self, **event_args):
    # Check the selected radio button and show the corresponding grid panel
    if self.another_person == 'Father':
      self.grid_panel_1.visible = True
      self.grid_panel_2.visible = False
      self.grid_panel_3.visible = False
      self.grid_panel_4.visible = False
    elif self.another_person == 'Mother':
      self.grid_panel_1.visible = False
      self.grid_panel_2.visible = True
      self.grid_panel_3.visible = False
      self.grid_panel_4.visible = False
    elif self.another_person == 'Spouse':
      self.grid_panel_1.visible = False
      self.grid_panel_2.visible = False
      self.grid_panel_3.visible = True
      self.grid_panel_4.visible = False
    elif self.another_person == 'Other':
      self.grid_panel_1.visible = False
      self.grid_panel_2.visible = False
      self.grid_panel_3.visible = False
      self.grid_panel_4.visible = True   

  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.lender_registration_form_3_marital_details',user_id=self.userId)

    # Any code you write here will run before the form opens.

  
