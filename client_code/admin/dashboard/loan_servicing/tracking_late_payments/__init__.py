from ._anvil_designer import tracking_late_paymentsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class tracking_late_payments(tracking_late_paymentsTemplate):
  def __init__(self, **properties):
    # Initialize form properties and components
    self.init_components(**properties)

    # Set up the dropdown options
    self.drop_down_1.items = ['All', 'Lapsed', 'Default', 'NPA']
    self.drop_down_1.selected_value = 'All'  # Set default value

    # Initially populate all repeating panels
    self.update_all_data_panel()

  def fetch_lapsed_data(self):
    emi_rows = app_tables.fin_emi_table.search(lapsed_fee=q.greater_than(0))
    return self._fetch_loan_details(emi_rows)

  def fetch_default_data(self):
    emi_rows = app_tables.fin_emi_table.search(default_fee=q.greater_than(0))
    return self._fetch_loan_details(emi_rows)

  def fetch_npa_data(self):
    emi_rows = app_tables.fin_emi_table.search(npa_fee=q.greater_than(0))
    return self._fetch_loan_details(emi_rows)

  def fetch_all_data(self):
    emi_rows = app_tables.fin_emi_table.search(
      q.any_of(
        lapsed_fee=q.greater_than(0),
        default_fee=q.greater_than(0),
        npa_fee=q.greater_than(0)
      )
    )
    return self._fetch_loan_details(emi_rows)

  def _fetch_loan_details(self, emi_rows):
    data = []
    for emi_row in emi_rows:
        loan_row = app_tables.fin_loan_details.get(loan_id=emi_row['loan_id'])
        if loan_row:
            # Fetch the corresponding user profile based on borrower_customer_id
            user_profile_row = app_tables.fin_user_profile.get(customer_id=loan_row['borrower_customer_id'])
            if user_profile_row:
                borrower_image = user_profile_row['user_photo']
            else:
                borrower_image = None
            
            data.append({
                'loan_id': loan_row['loan_id'],
                'borrower_full_name': loan_row['borrower_full_name'],
                'borrower_email_id': loan_row['borrower_email_id'],
                'product_name': loan_row['product_name'],
                'emi_number': emi_row['emi_number'],
                'lapsed_fee': emi_row['lapsed_fee'],
                'default_fee': emi_row['default_fee'],
                'npa_fee': emi_row['npa_fee'],
                'total_fees': emi_row['lapsed_fee'] + emi_row['default_fee'] + emi_row['npa_fee'],
                'image': borrower_image  # Include the image
            })
    return data

  def update_lapsed_panel(self):
    self.repeating_panel_lapsed.items = self.fetch_lapsed_data()
    self.data_grid_2.visible = True
    self.data_grid_3.visible = False
    self.data_grid_4.visible = False
    self.data_grid_1.visible = False
    print("Lapsed panel updated with items:", self.repeating_panel_lapsed.items)  # Debugging print

  def update_default_panel(self):
    self.repeating_panel_default.items = self.fetch_default_data()
    self.data_grid_2.visible = False
    self.data_grid_3.visible = True
    self.data_grid_4.visible = False
    self.data_grid_1.visible = False
    print("Default panel updated with items:", self.repeating_panel_default.items)  # Debugging print

  def update_npa_panel(self):
    self.repeating_panel_npa.items = self.fetch_npa_data()
    self.data_grid_2.visible = False
    self.data_grid_3.visible = False
    self.data_grid_4.visible = True
    self.data_grid_1.visible = False
    print("NPA panel updated with items:", self.repeating_panel_npa.items)  # Debugging print

  def update_all_data_panel(self):
    self.repeating_panel_all.items = self.fetch_all_data()
    self.data_grid_2.visible = False
    self.data_grid_3.visible = False
    self.data_grid_4.visible = False
    self.data_grid_1.visible = True
    print("All data panel updated with items:", self.repeating_panel_all.items)  # Debugging print

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected in the dropdown"""
    selected_filter = self.drop_down_1.selected_value
    print("Selected filter:", selected_filter)  # Debugging print
    if selected_filter == 'Lapsed':
      self.update_lapsed_panel()
    elif selected_filter == 'Default':
      self.update_default_panel()
    elif selected_filter == 'NPA':
      self.update_npa_panel()
    else:
      self.update_all_data_panel()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_servicing')

# Ensure you open the form correctly elsewhere in your application
# form = tracking_late_payments()
