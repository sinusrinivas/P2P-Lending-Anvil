from ._anvil_designer import interest_accrualsTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class interest_accruals(interest_accrualsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.fetch_and_display_data()

  def fetch_and_display_data(self):
    # Fetch all lenders from the database
    lenders = app_tables.fin_lender.search()
    
    filtered_lenders = []
    total_interest_amount = 0
    
    # Iterate through each lender
    for lender in lenders:
      # Fetch user profile based on lender's customer_id
      user_profile = app_tables.fin_user_profile.get(customer_id=lender['customer_id'])
      
      # Fetch all loans associated with this lender
      loans = app_tables.fin_loan_details.search(lender_customer_id=lender['customer_id'])
      
      lender_interest_total = 0
      has_closed_loans = False
      
      # Iterate through each loan
      for loan in loans:
        # Check if the loan status is "closed"
        if loan['loan_updated_status'] == "closed":
          has_closed_loans = True
          # Calculate the total interest amount for closed loans
          lender_interest_total += loan['total_interest_amount']
          total_interest_amount += loan['total_interest_amount']
      
      # Append the lender details to the filtered lenders list
      filtered_lenders.append({
        'user_photo': user_profile['user_photo'],
        'lender_full_name': lender['user_name'],
        'lender_email_id': lender['email_id'],
        'total_interest_amount': lender_interest_total,
        'membership_type': lender['membership'],
        'lending_type': lender['lending_type'],
        'total_commitment': lender['lender_total_commitments'] if lender['lender_total_commitments'] else 0,
        'customer_id': lender['customer_id'],
        'has_closed_loans': has_closed_loans
      })
    
    # Display the filtered lenders in a repeating panel or similar component
    self.repeating_panel_1.items = filtered_lenders
    
    # # Display the total interest amount for closed loans
    # self.label_total_interest_amount.text = total_interest_amount





# from ._anvil_designer import intersest_accrualsTemplate
# from anvil import *
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables


# class intersest_accruals(intersest_accrualsTemplate):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#     # Any code you write here will run before the form opens.
#     self.fetch_and_display_data()

#   def fetch_and_display_data(self):
#     # Fetch all lenders from the database
#     lenders = app_tables.fin_lender.search()
    
#     filtered_loans = []
#     total_interest_amount = 0
    
#     # Iterate through each lender
#     for lender in lenders:
#       # Fetch user profile based on lender's customer_id
#       user_profile = app_tables.fin_user_profile.get(customer_id=lender['customer_id'])
      
#       # Fetch all loans associated with this lender
#       loans = app_tables.fin_loan_details.search(lender_customer_id=lender['customer_id'])
      
#       lender_has_loans = False
      
#       # Iterate through each loan
#       for loan in loans:
#         lender_has_loans = True
#         # Check if the loan status is "closed"
#         if loan['loan_updated_status'] == "closed":
#           # Calculate the total interest amount for closed loans
#           total_interest_amount += loan['total_interest_amount']
          
#           # Append the loan details to the filtered loans list
#           filtered_loans.append({
#             'user_photo': user_profile['user_photo'] if user_profile else None,
#             'lender_full_name': lender['user_name'],
#             'lender_email_id': lender['email_id'],
#             'loan_amount': loan['loan_amount'],
#             'loan_updated_status': loan['loan_updated_status'],
#             'loan_id': loan['loan_id'],
#             'membership_type': lender['membership'],
#             'lending_type': lender['lending_type'],
#             'total_commitment': lender['lender_total_commitments'],
#             'customer_id': lender['customer_id'],
#             'lender_accepted_timestamp': loan['lender_accepted_timestamp']
#           })
      
#       # If the lender has no loans, still include the lender details
#       if not lender_has_loans:
#         filtered_loans.append({
#           'user_photo': user_profile['user_photo'] if user_profile else None,
#           'lender_full_name': lender['user_name'],
#           'lender_email_id': lender['email_id'],
#           'loan_amount': None,
#           'loan_updated_status': None,
#           'loan_id': None,
#           'membership_type': lender['membership'],
#           'lending_type': lender['lending_type'],
#           'total_commitment': lender['lender_total_commitments'],
#           'customer_id': lender['customer_id'],
#           'lender_accepted_timestamp': None
#         })
    
#     # Display the filtered loans in a repeating panel or similar component
#     self.repeating_panel_1.items = filtered_loans
    
#     # Display the total interest amount for closed loans
#     self.label_total_interest_amount.text = total_interest_amount

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.accounting')

