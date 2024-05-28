from ._anvil_designer import my_returnsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class my_returns(my_returnsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.create_bar_chart()

  def create_bar_chart(self):
    # Sample data
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [10, 15, 13, 17, 20]

    # Create a bar chart
    trace = go.Bar(x=categories, y=values, name='Bar Chart')
    layout = go.Layout(title='Sample Bar Chart', xaxis=dict(title='Category'), yaxis=dict(title='Value'))
    fig = go.Figure(data=[trace], layout=layout)
    # Set the plot in the Plot component
    self.plot_1.data = fig