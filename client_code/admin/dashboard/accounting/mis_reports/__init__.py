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


class mis_reports(mis_reportsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.plot_data()
    self.plot_loan_data()

  def plot_data(self):
    # Fetch data from tables
    loan_details = app_tables.fin_loan_details.search(loan_updated_status=q.any_of('closed loan', 'rejected', 'disbursed loan'))
    lenders = app_tables.fin_lender.search()
    users = app_tables.fin_user_profile.search(usertype=q.any_of('lender', 'borrower'))

    # Calculate metrics
    no_of_loans_disbursed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'disbursed loan'])
    no_of_loans_closed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'closed loan'])
    no_of_loans_rejected = len([loan for loan in loan_details if loan['loan_updated_status'] == 'rejected'])
    # no_of_loans_extended = len([loan for loan in loan_details if loan['loan_updated_status'] == 'extension'])
    amount_disbursed = sum([loan['lender_returns'] for loan in loan_details])
    no_of_borrowers = len([user for user in users if user['usertype'] == 'borrower'])
    no_of_lenders = len([user for user in users if user['usertype'] == 'lender'])
    lenders_commitment = sum([lender['return_on_investment'] for lender in lenders])

    # Data for the pie chart
    values = [
        no_of_loans_disbursed,
        no_of_loans_closed,
        no_of_loans_rejected,
        # no_of_loans_extended,
        amount_disbursed,
        no_of_borrowers,
        no_of_lenders,
        lenders_commitment
    ]
    labels = [
        'No of Loans Disbursed: {}'.format(no_of_loans_disbursed),
        'No of Loans Closed: {}'.format(no_of_loans_closed),
        'No of Loans Rejected: {}'.format(no_of_loans_rejected),
        # 'No of Loans Extended: {}'.format(no_of_loans_extended),
        'Amount Disbursed: {}'.format(amount_disbursed),
        'No of Borrowers: {}'.format(no_of_borrowers),
        'No of Lenders: {}'.format(no_of_lenders),
        'Lenders Commitment: {}'.format(lenders_commitment)
    ]

    # Create the pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent')])


    fig.update_layout(title={'text': 'Financial Loan Details', 'font': {'size': 24, 'color': 'black', 'family': 'Arial', 'bold': True}})

    # Embed the plot in the Anvil app
    self.plot_1.figure = fig

  def plot_loan_data(self):
    # Fetch data from tables
    loan_details = app_tables.fin_loan_details.search(loan_updated_status=q.any_of('closed loan', 'rejected', 'disbursed loan', 'foreclosure', 'lost opportunities', 'accepted', 'under process'))

    # Calculate metrics
    no_of_loans_disbursed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'disbursed loan'])
    no_of_loans_closed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'closed loan'])
    no_of_loans_rejected = len([loan for loan in loan_details if loan['loan_updated_status'] == 'rejected'])
    no_of_loans_foreclosed = len([loan for loan in loan_details if loan['loan_updated_status'] == 'foreclosure'])
    no_of_loans_lost_opportunity = len([loan for loan in loan_details if loan['loan_updated_status'] == 'lost opportunities'])
    no_of_loans_accepted = len([loan for loan in loan_details if loan['loan_updated_status'] == 'accepted'])
    no_of_loans_under_process = len([loan for loan in loan_details if loan['loan_updated_status'] == 'under process'])
    # Data for the pie chart
    values = [
        no_of_loans_disbursed,
        no_of_loans_closed,
        no_of_loans_rejected,
        no_of_loans_foreclosed,
        no_of_loans_lost_opportunity,
        no_of_loans_accepted,
        no_of_loans_under_process

    ]
    labels = [
        'No of Loans Disbursed: {}'.format(no_of_loans_disbursed),
        'No of Loans Closed: {}'.format(no_of_loans_closed),
        'No of Loans Rejected: {}'.format(no_of_loans_rejected),
        'No of Loans Foreclosed: {}'.format(no_of_loans_foreclosed),
        'No of Loans Lost Opportunity: {}'.format(no_of_loans_lost_opportunity),
        'No of Loans Accepted: {}'.format(no_of_loans_accepted),
        'No of Loans Under Process: {}'.format(no_of_loans_under_process)

    ]

    # Create the pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent')])

    # Update layout for better appearance
    fig.update_layout(title={'text': 'Financial Details on Loans', 'font': {'size': 24, 'color': 'black', 'family': 'Arial', 'bold': True}})

    # Embed the plot in the Anvil app
    self.plot_2.figure = fig

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.accounting')
