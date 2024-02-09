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
    # self.another_person = None

    guarantor_data=app_tables.fin_guarantor_details.get(customer_id=user_id)
    if guarantor_data:
      self.father_name_text.text=guarantor_data['guarantor_name']
      self.date_picker_1.date=guarantor_data['guarantor_date_of_birth']
      self.father_mbl_no_text.text=guarantor_data['guarantor_mobile_no']
      self.father_address_text.text=guarantor_data['guarantor_address']
      self.father_profession_text.text=guarantor_data['guarantor_profession']
      self.father_company_name_text.text=guarantor_data['guarantor_company_name']
      self.father_annual_earning.text=guarantor_data['guarantor_annual_earning']
      guarantor_data.update()

  
  def button_submit_click(self, **event_args):
    g_full_name = self.father_name_text.text
    g_dob = self.date_picker_1.date
    g_mobile_no = self.father_mbl_no_text.text
    g_address = self.father_address_text.text
    g_profession = self.father_profession_text.text
    g_company_name = self.father_company_name_text.text
    g_annual_earning = self.father_annual_earning.text
    user_id = self.user_id

    self.mbl_label_1.text = ''

    if not re.match(r'\d{10}$', g_mobile_no):
      self.mbl_label_1.text = 'Enter valid mobile no'

    elif not g_full_name or not g_dob or not g_mobile_no or not g_address or not g_profession or not g_company_name or not g_annual_earning:
      Notification('Please fill all details').show()

    else:
      anvil.server.call('add_guarantor_details', g_full_name,g_dob,g_mobile_no,g_address,g_profession,g_company_name,g_annual_earning,user_id)
      open_form('lendor_registration_form.lender_registration_form_4_bank_form_1')   

  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.lender_registration_form_3_marital_details',user_id=self.userId)

    # Any code you write here will run before the form opens.

  def radio_button_1_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    self.grid_panel_1.visible = True
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.button_submit.visible = True

  def radio_button_2_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = True
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.button_submit.visible = True

  def radio_button_3_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = True
    self.grid_panel_4.visible = False
    self.button_submit.visible = True

  def radio_button_4_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = True
    self.button_submit.visible = True
