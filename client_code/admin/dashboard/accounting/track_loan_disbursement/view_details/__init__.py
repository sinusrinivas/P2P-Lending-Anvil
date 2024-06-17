from ._anvil_designer import view_detailsTemplate
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

class view_details(view_detailsTemplate):
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
        # Call server function to get Plotly figure
        fig = anvil.server.call('create_loan_disbursement_graph', loan_created, lender_accepted, loan_disbursed)
        
        # Update Plotly component with the retrieved figure
        self.plot_1.figure = fig