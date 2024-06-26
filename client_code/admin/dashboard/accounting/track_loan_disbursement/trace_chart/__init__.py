# from ._anvil_designer import trace_chartTemplate
# from anvil import *
# import plotly.graph_objects as go
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
# import plotly.graph_objects as go

# class trace_chart(trace_chartTemplate):
#   def __init__(self, selected_row, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)
#     self.loan_id = selected_row['loan_id']
 
#     loan_data = app_tables.fin_loan_details.get(loan_id=self.loan_id)
#     if loan_data:
#         loan_created = loan_data['borrower_loan_created_timestamp']
#         lender_accepted = loan_data['lender_accepted_timestamp']
#         loan_disbursed = loan_data['loan_disbursed_timestamp']
#         self.create_loan_disbursement_graph(loan_created, lender_accepted, loan_disbursed)
#     else:
#         Notification("No data found for the selected loan ID!").show()
        
#   def create_loan_disbursement_graph(self, loan_created, lender_accepted, loan_disbursed):
#         # Call server function to get Plotly figure
#         fig = anvil.server.call('create_loan_disbursement_graph', loan_created, lender_accepted, loan_disbursed)
        
#         # Update Plotly component with the retrieved figure
#         self.plot_1.figure = fig

#   def button_1_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     open_form('admin.dashboard.accounting.track_loan_disbursement')


from ._anvil_designer import trace_chartTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.users
import anvil.tables as tables
from anvil.tables import app_tables
from datetime import datetime, date
# import anvil.plotly as plotly
import plotly.graph_objects as go

class trace_chart(trace_chartTemplate):
  def __init__(self, selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.loan_id = selected_row['loan_id']
    
    loan_data = app_tables.fin_loan_details.get(loan_id=self.loan_id)
    if loan_data:
        loan_created = loan_data['borrower_loan_created_timestamp']
        lender_accepted = loan_data['lender_accepted_timestamp']
        loan_disbursed = loan_data['loan_disbursed_timestamp']
        self.create_loan_disbursement_graph(loan_created, lender_accepted, loan_disbursed)
    else:
        Notification("No data found for the selected loan ID!").show()
        
  def create_loan_disbursement_graph(self, loan_created, lender_accepted, loan_disbursed):
    # Convert timestamps to naive datetime objects if necessary
    dates = []
    if loan_created:
        dates.append(('Loan Created', self.convert_to_naive_datetime(loan_created)))
    if lender_accepted:
        dates.append(('Lender Accepted', self.convert_to_naive_datetime(lender_accepted)))
    if loan_disbursed:
        dates.append(('Loan Disbursed', self.convert_to_naive_datetime(loan_disbursed)))
    
    # Sort dates by timestamp
    dates.sort(key=lambda x: x[1])
    
    # Extract labels and timestamps
    labels = [label for label, _ in dates]
    timestamps = [timestamp for _, timestamp in dates]

    # Create a Plotly figure using Anvil's built-in capabilities
    trace = go.Scatter(
        x=timestamps,
        y=labels,
        mode='lines+markers',
        line=dict(shape='linear'),
        marker=dict(size=12),
        text=labels,
        textposition='top center'
    )

    fig = go.Figure(data=[trace])
    
    # Update layout
    fig.update_layout(
        title='Loan Disbursement Timeline',
        xaxis_title='Timestamp',
        yaxis_title='Stage',
        xaxis=dict(type='date'),
        yaxis=dict(tickmode='array', tickvals=labels, automargin=True),
        margin=dict(l=100)
    )
    
    # Display the Plotly figure using Anvil's built-in Plot component
    self.plot_1.figure = fig

  def convert_to_naive_datetime(self, dt):
    if isinstance(dt, datetime):
        # Convert aware datetime to naive datetime by removing timezone info
        return dt.replace(tzinfo=None)
    elif isinstance(dt, date):
        # Convert date to datetime and make it naive
        return datetime.combine(dt, datetime.min.time())
    else:
        raise TypeError(f"Expected datetime or date object, got {type(dt)}")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.accounting.track_loan_disbursement')
