from ._anvil_designer import view_loan_foreclosure_RequestsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class view_loan_foreclosure_Requests(view_loan_foreclosure_RequestsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel.items=app_tables.fin_foreclosure.search()

    self.repeating_panel_1.items = app_tables.fin_foreclosure.search(status=q.like('approved%'))
    self.label_5.text = str(len(self.repeating_panel_1.items))

    self.repeating_panel_2.items = app_tables.fin_foreclosure.search(status=q.like('rejected%'))
    self.label_6.text = str(len(self.repeating_panel_2.items))

    self.repeating_panel_3.items = app_tables.fin_foreclosure.search(status=q.like('under process%'))
    self.label_5_copy.text = str(len(self.repeating_panel_3.items))

    self.repeating_panel_4.items = app_tables.fin_foreclosure.search(status=q.like('under process%'))
    self.new_request.text = str(len(self.repeating_panel_4.items))

    self.all.text = str(len(self.repeating_panel.items))

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.view_available_balance")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard")

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.view_borrower_loan_request")

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.view_opening_balance")

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.view_borrower_loan_request.Borr_loan_request")

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.view_lost_oppurtunities")

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.today_dues")

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.lender_view_loans")

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.view_loan_extension_requests")

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.top_up_amount")

  def link_10_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.view_loan_foreclosure_Requests")

  def link_11_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.view_or_download_portfolio")

  def link_12_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.view_profile")

  def link_13_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.change_password")


  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_2.visible = True
    self.data_grid_2.visible = True
    self.label_3.visible = False
    self.data_grid_2_copy.visible = False
    self.label_4.visible = False
    self.data_grid_3.visible = False
    self.new.visible = False
    self.data_grid_4.visible = False
    self.label_1.visible = False
    self.data_grid_1.visible = False

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_3.visible = True
    self.data_grid_2_copy.visible = True
    self.label_4.visible = False
    self.data_grid_3.visible = False
    self.label_2.visible = False
    self.data_grid_2.visible = False
    self.new.visible = False
    self.data_grid_4.visible = False
    self.label_1.visible = False
    self.data_grid_1.visible = False

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_4.visible = True
    self.data_grid_3.visible = True
    self.label_2.visible = False
    self.data_grid_2.visible = False
    self.label_3.visible = False
    self.data_grid_2_copy.visible = False
    self.new.visible = False
    self.data_grid_4.visible = False
    self.label_1.visible = False
    self.data_grid_1.visible = False

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_grid_4.visible = not self.data_grid_4.visible
    self.new.visible = True
    self.data_grid_4.visible = True
    self.label_4.visible = False
    self.data_grid_3.visible = False
    self.label_2.visible = False
    self.data_grid_2.visible = False
    self.label_3.visible = False
    self.data_grid_2_copy.visible = False
    self.label_1.visible = False
    self.data_grid_1.visible = False

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_grid_1.visible = True
    self.label_1.visible = True
    self.label_4.visible = False
    self.data_grid_3.visible = False
    self.label_2.visible = False
    self.data_grid_2.visible = False
    self.label_3.visible = False
    self.data_grid_2_copy.visible = False
    self.new.visible = False
    self.data_grid_4.visible = False
    
    
    





   
