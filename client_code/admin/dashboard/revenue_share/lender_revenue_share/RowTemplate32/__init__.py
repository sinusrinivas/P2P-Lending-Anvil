# from ._anvil_designer import RowTemplate32Template
# from anvil import *
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables

# class RowTemplate32(RowTemplate32Template):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#     # Set label texts from item properties
#     if 'loan_id' in self.item:
#       self.label_1.text = self.item['loan_id']
#     if 'loan_amount' in self.item:
#       self.label_2.text = self.item['loan_amount']
#     if 'lender_returns' in self.item:
#       self.label_3.text = self.item['lender_returns']



from ._anvil_designer import RowTemplate32Template
from anvil import *

class RowTemplate32(RowTemplate32Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Set label texts from item properties
    if 'loan_id' in self.item:
      self.label_1.text = str(self.item['loan_id'])
    if 'loan_amount' in self.item:
      self.label_2.text = str(self.item['loan_amount'])
    if 'lender_returns' in self.item:
      self.label_3.text = str(self.item['lender_returns'])
    if 'tds_on_lender_roi' in self.item:
      self.label_5.text = str(self.item['tds_on_lender_roi'])
    if 'lender_commission' in self.item:
      self.label_6.text = str(self.item['lender_commission'])
