# from ._anvil_designer import accruals_chartTemplate
# from anvil import *
# import plotly.graph_objects as go
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables


# class accruals_chart(accruals_chartTemplate):
#   def __init__(self, selected_row, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#     self.customer_id = selected_row['customer_id']
#     print(self.customer_id)
    
#     # Fetch all closed loans associated with this lender
#     loans = app_tables.fin_loan_details.search(lender_customer_id=self.customer_id, loan_updated_status='closed')
    
#     total_interest_amount = 0
      
#     # Calculate total interest amount and prepare detailed loan information
#     for loan in loans:
#       total_interest_amount += loan['total_interest_amount']
#       self.label_total_interest_amount.text = total_interest_amount


from ._anvil_designer import accruals_chartTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class accruals_chart(accruals_chartTemplate):
  def __init__(self, selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.customer_id = selected_row['customer_id']
    self.lender_name = selected_row['lender_full_name']
    
    # Fetch all closed loans associated with this lender
    loans = app_tables.fin_loan_details.search(lender_customer_id=self.customer_id, loan_updated_status='closed')
    
    # Prepare data for the pie chart
    loan_ids = []
    interest_amounts = []
    
    total_interest_amount = 0
    
    for loan in loans:
      loan_ids.append(loan['loan_id'])
      interest_amounts.append(loan['total_interest_amount'])
      total_interest_amount += loan['total_interest_amount']
    
    # Display the total interest amount
    self.label_total_interest_amount.text = total_interest_amount
    
    # Create the pie chart
    fig = go.Figure(data=[go.Pie(labels=loan_ids, values=interest_amounts, hole=.3)])
    
    # Set chart title with the lender's name
    fig.update_layout(title_text=f'Interest Accruals of {self.lender_name}')
    
    # Display the chart
    self.plot_1.figure = fig

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.accounting.interest_accruals')
