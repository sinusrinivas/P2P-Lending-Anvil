from ._anvil_designer import lender_portfolioTemplate
from anvil import *
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
import plotly.graph_objects as go


class lender_portfolio(lender_portfolioTemplate):
  def __init__(self,selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.id = selected_row['customer_id']
    self.email = main_form_module.email
    self.user_Id = main_form_module.userId

     # Set the label text with today's date
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    self.label_5.text = "As on " + today_date

    # Any code you write here will run before the form opens.
    ascend = app_tables.fin_user_profile.get(customer_id=self.id)
    self.image_4.source = ascend['user_photo']
    self.label_4.text = "Hello" " " + ascend['full_name']
    self.label_15.text = ascend['mobile']
    self.label_16.text = ascend['date_of_birth']
    self.label_17.text = ascend['gender']
    self.label_18.text = ascend['marital_status']
    self.label_19.text = ascend['present_address']
    self.label_20.text = ascend['qualification']
    self.label_21.text = ascend['occupation_type']
    

    lendor = app_tables.fin_lender.get(customer_id=self.id)
    self.label_3.text = lendor['membership']
    self.label_3_copy.text = lendor['lender_total_commitments']
    self.label_9.text = lendor['return_on_investment']

  def create_user_bar_chart(self):
        # Fetch investment data for the specific user
        investments = app_tables.fin_lender.search(customer_id=self.id)
        
        # Debugging: Print fetched investments
        print(f"Fetched investments for user {self.user_id}: {list(investments)}")
        
        # Initialize variables to store total investments and returns
        total_investment = 0
        total_returns = 0
        
        for investment in investments:
            total_investment += investment['lender_total_commitments']
            total_returns += investment['return_on_investment']
  
        # Calculate the percentage return
        percentage_return = (total_returns / total_investment) * 100 if total_investment != 0 else 0

        # Debugging: Print aggregated values
        print(f"Total Investment: {total_investment}, Total Returns: {total_returns}, Percentage Return: {percentage_return:.2f}%")
  
        # Prepare data for bar chart
        categories = ['Investment', 'Returns']
        values = [total_investment, total_returns]
  
        # Create bar chart trace
        trace = go.Bar(x=categories, y=values, marker_color=['blue', 'green'])
  
        # Create annotations
        annotations = []
        annotations.append(dict(
            x='Returns',
            y=total_returns + (max(values) * 0.01),  # Position above the returns bar
            text=f"{percentage_return:.2f}%",
            showarrow=False,
            font=dict(color='black', size=8, weight='bold'),  # Set the color of the text to dark black and bold
            xanchor="left"
        ))
  
        # Create a layout with annotations
        layout = go.Layout(
            title=dict(text='Investment and Returns ', font=dict(size=16, weight='bold')),
            xaxis=dict(title='Category', tickfont=dict(size=10, weight='bold')),
            yaxis=dict(title='Amount (0.1M=100000)'),
            barmode='group',  # Use group mode to display bars side by side
            annotations=annotations
        )
  
        # Create a figure
        fig = go.Figure(data=[trace], layout=layout)
  
        # Debugging: Print the figure to ensure it's created
        print(f"Created figure: {fig}")
  
        # Set the plot in the Plot component
        self.plot_1.data = fig['data']
        self.plot_1.layout = fig['layout']
  
        # Debugging: Check if the plot is assigned correctly
        print(f"Assigned figure to plot_2: {self.plot_2.data}")
    
