from ._anvil_designer import borrower_portfolioTemplate
from anvil import *
import plotly.graph_objects as go
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

class borrower_portfolio(borrower_portfolioTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.email = main_form_module.email
    self.user_Id = main_form_module.userId

    # Set the label text with today's date
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    self.label_2.text = "As on " + today_date

    rows = app_tables.fin_loan_details.search(borrower_customer_id=self.user_Id, loan_updated_status=q.any_of(
          q.like('accept%'),
          q.like('Approved%'),
          q.like('approved%'),
          q.like('foreclosure%'),
          q.like('disbursed loan%'),
          q.like('Disbursed loan%'),
        ))
    self.label_5_copy.text = len(rows)
    
    row = app_tables.fin_loan_details.search(borrower_customer_id=self.user_Id, loan_updated_status=q.any_of(
          q.like('closed%'),
          q.like('Closed%'),
          q.like('CLOSED%'),
        ))
    self.label_9.text = len(row)
    
    no_of_disbursed_loans = app_tables.fin_loan_details.search(borrower_customer_id=self.user_Id, loan_updated_status=q.any_of(
          q.like('disbursed loan%'),
          q.like('Disbursed loan%')
        ))
    self.label_3_copy.text = len(no_of_disbursed_loans)

    amount_of_disbursed_loans = app_tables.fin_loan_details.search(
    borrower_customer_id=self.user_Id,
    loan_updated_status="disbursed loan"
)

    if amount_of_disbursed_loans:
        # Calculate total loan amount
        total_amount = sum(loan['loan_amount'] for loan in amount_of_disbursed_loans)
        self.label_9_copy.text=total_amount
        print("Total disbursed loan amount:", total_amount)
    else:
        print("No disbursed loans found for this borrower.")

      
    
    # Fetch the loan status data for the given customer_id
    loan_status_data = self.get_loan_status_data(self.user_Id)
    
    # Create the pie chart with the fetched data
    self.create_pie_chart(loan_status_data)
    
  def get_loan_status_data(self, borrower_customer_id):
    # Query the database to get loan status data for the given customer_id
    rows = app_tables.fin_loan_details.search(borrower_customer_id=borrower_customer_id)
    loan_status_counts = {}
    
    # Count the occurrences of each loan status
    for row in rows:
        status = row['loan_updated_status']
        if status in loan_status_counts:
            loan_status_counts[status] += 1
        else:
            loan_status_counts[status] = 1
            
    return loan_status_counts

  def create_pie_chart(self, data):
    labels = list(data.keys())
    values = list(data.values())
    
    # Create the pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, 
                                 textinfo='label+percent', insidetextorientation='radial', hole=.3)])
    
    fig.update_layout(title_text='Loan Status Distribution')
    
    # Bind the plotly figure to the Plot component
    self.plot_1.figure = fig


# class borrower_portfolio(borrower_portfolioTemplate):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)
#     self.email = main_form_module.email
#     self.user_Id = main_form_module.userId

#     # Set the label text with today's date
#     today_date = datetime.datetime.now().strftime("%Y-%m-%d")
#     self.label_2.text = "As on " + today_date

    # no_of_disbursed_loans = app_tables.fin_loan_details.search(borrower_customer_id=self.user_Id, loan_updated_status=q.any_of(
    #   q.like('disbursed loan%'),
    #   q.like('Disbursed loan%'),
    # ))
#     self.label_3_copy.text = len(no_of_disbursed_loans)

#     # Any code you write here will run before the form opens.
#     # Fetch the loan status data for the given customer_id
#     self.update_loan_status_data(self.user_Id)

#   def update_loan_status_data(self, borrower_customer_id):
#     # Define status categories and their corresponding queries
#     status_queries = {
#         'Running Loans': q.any_of(
#             q.like('accept%'),
#             q.like('Approved%'),
#             q.like('approved%'),
#             q.like('foreclosure%'),
#             q.like('foreclosure%'),
#             q.like('disbursed loan%'),
#             q.like('Disbursed loan%'),
#             q.like('extension%'),
#             q.like('Extension%')
#         ),
        
#         'Closed Loans': q.any_of(
#             q.like('closed%'),
#             q.like('Closed%'),
#             q.like('CLOSED%')
#         ),
#         'Under Process Loans': q.any_of(
#             q.like('under process%'),
#             q.like('Under Process%'),
#             q.like('UNDER PROCESS%')
#         ),
        
#         'Total Loans': q.any_of(
#             q.like('accept%'),
#             q.like('Accept%'),
#             q.like('Approved%'),
#             q.like('approved%'),
#             q.like('foreclosure%'),
#             q.like('Foreclosure%'),
#             q.like('disbursed loan%'),
#             q.like('Disbursed loan%'),
#             q.like('Rejected%'),
#             q.like('rejected%'),
#             q.like('extension%'),
#             q.like('Extension%'),
#         ),
#     }

#     # Initialize counts
#     loan_status_counts = {}

#     # Query and count each status category
#     for status, query in status_queries.items():
#         rows = app_tables.fin_loan_details.search(borrower_customer_id=borrower_customer_id, loan_updated_status=query)
#         loan_status_counts[status] = len(rows)

#     # Update labels with the counts
#     self.label_5_copy.text = loan_status_counts['Running Loans']
#     self.label_9.text = loan_status_counts['Closed Loans']
#     # You can add similar label updates for 'Under Process Loans' and 'Open Loans' if needed

#     # Create the pie chart with the counts
#     self.create_pie_chart(loan_status_counts)

#   def create_pie_chart(self, data):
#     # Remove 'Total Loans' from pie chart data
#     del data['Total Loans']

#     labels = list(data.keys())
#     values = list(data.values())
    
#     # Create the pie chart
#     fig = go.Figure(data=[go.Pie(labels=labels, values=values, 
#                                  textinfo='label+percent', insidetextorientation='radial', hole=.3)])
    
#     fig.update_layout(title_text='Loan Status Distribution')
    
#     # Bind the plotly figure to the Plot component
#     self.plot_1.figure = fig
