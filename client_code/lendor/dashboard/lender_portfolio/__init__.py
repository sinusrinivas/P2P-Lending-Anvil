from ._anvil_designer import lender_portfolioTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ....bank_users.main_form import main_form_module
from ....bank_users.user_form import user_form
from ....bank_users.user_form import user_module
import datetime
import plotly.graph_objects as go


class lender_portfolio(lender_portfolioTemplate):
  def __init__(self,selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.id = selected_row['customer_id']
    self.email = main_form_module.email
    self.user_Id = main_form_module.userId

     # Set the label text with today's date
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    self.label_5.text = "As on " + today_date

    # Any code you write here will run before the form opens.
    ascend = app_tables.fin_user_profile.get(customer_id=self.id)
    self.image_4.source = ascend['user_photo']
    self.label_4.text = "Hello" " " + ascend['full_name']
    self.label_15.text = ascend['mobile']
    self.label_16.text = ascend['date_of_birth']
    self.label_17.text = ascend['gender']
    self.label_18.text = ascend['marital_status']
    self.label_19.text = ascend['present_address']
    self.label_20.text = ascend['qualification']
    self.label_21.text = ascend['occupation_type']
    

    lendor = app_tables.fin_lender.get(customer_id=self.id)
    self.label_3.text = lendor['membership']
    self.label_3_copy.text = lendor['lender_total_commitments']
    self.label_9.text = lendor['return_on_investment']
    
