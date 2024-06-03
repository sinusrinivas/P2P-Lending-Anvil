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

    # Any code you write here will run before the form opens.
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
