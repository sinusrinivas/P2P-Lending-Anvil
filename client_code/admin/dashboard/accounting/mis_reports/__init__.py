# from ._anvil_designer import mis_reportsTemplate
# from anvil import *
# import plotly.graph_objects as go
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables


# class mis_reports(mis_reportsTemplate):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#     # Any code you write here will run before the form opens.

#   def button_1_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     open_form('admin.dashboard.accounting')





from ._anvil_designer import mis_reportsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
import pandas as pd


class mis_reports(mis_reportsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.plot_data()

  def plot_data(self):
    # Fetch data from tables
    loan_details = app_tables.fin_loan_details.search()
    lenders = app_tables.fin_lender.search()
    borrowers = app_tables.fin_borrower.search()
    
    # Convert to DataFrame if needed (assuming fetching as dictionary)
    loan_details_df = pd.DataFrame(list(loan_details))
    lenders_df = pd.DataFrame(list(lenders))
    borrowers_df = pd.DataFrame(list(borrowers))

    # Calculate metrics
    no_of_loans_disbursed = loan_details_df[loan_details_df['l'] == 'disbursed loan'].shape[0]
    no_of_loans_closed = loan_details_df[loan_details_df['status'] == 'closed'].shape[0]
    no_of_loans_rejected = loan_details_df[loan_details_df['status'] == 'rejected'].shape[0]
    amount_disbursed = loan_details_df[loan_details_df['status'] == 'disbursed']['amount'].sum()
    no_of_borrowers = borrowers_df.shape[0]
    no_of_lenders = lenders_df.shape[0]
    lenders_commitment = lenders_df['commitment'].sum()

    # Data for the pie chart
    values = [
        no_of_loans_disbursed,
        no_of_loans_closed,
        no_of_loans_rejected,
        amount_disbursed,
        no_of_borrowers,
        no_of_lenders,
        lenders_commitment
    ]
    labels = [
        'No of Loans Disbursed: {}'.format(no_of_loans_disbursed),
        'No of Loans Closed: {}'.format(no_of_loans_closed),
        'No of Loans Rejected: {}'.format(no_of_loans_rejected),
        'Amount Disbursed: {}'.format(amount_disbursed),
        'No of Borrowers: {}'.format(no_of_borrowers),
        'No of Lenders: {}'.format(no_of_lenders),
        'Lenders Commitment: {}'.format(lenders_commitment)
    ]

    # Create the pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent')])

    # Update layout for better appearance
    fig.update_layout(title_text='Financial Loan Details')

    # Embed the plot in the Anvil app
    self.plot_pane.clear()
    self.plot_pane.add_component(go.FigureWidget(fig))

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.accounting')
