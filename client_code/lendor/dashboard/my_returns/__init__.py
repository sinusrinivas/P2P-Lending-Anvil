from ._anvil_designer import my_returnsTemplate
from anvil import *
import plotly.graph_objects as go
from anvil.tables import app_tables
import anvil.tables.query as q
from .. import main_form_module as main_form_module

class my_returns(my_returnsTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.user_id = main_form_module.userId

        # Check if user_id is correctly set
        print(f"User ID: {self.user_id}")

        # Any code you write here will run before the form opens.
        self.create_bar_chart()

    def create_bar_chart(self):
        # Fetch investment data for the specific user
        investments = app_tables.fin_loan_details.search(loan_updated_status=q.like('close%'), lender_customer_id=self.user_id)
        
        # Debugging: Print fetched investments
        print(f"Fetched investments for user {self.user_id}: {list(investments)}")
        
        # Initialize a dictionary to store total investments, returns, and tenure by product
        product_data = {}
        
        for investment in investments:
            product = investment['product_name']
            if product not in product_data:
                product_data[product] = {'total_investment': 0, 'total_returns': 0, 'tenure': investment['tenure']}
            product_data[product]['total_investment'] += investment['loan_amount']
            product_data[product]['total_returns'] += investment['lender_returns']

        # Prepare data for bar chart
        products = list(product_data.keys())
        total_investments = [product_data[product]['total_investment'] for product in products]
        total_returns = [product_data[product]['total_returns'] for product in products]
        tenures = [product_data[product]['tenure'] for product in products]

        # Create bar chart traces
        investment_trace = go.Bar(x=products, y=total_investments, name='Investment', marker_color='blue')
        returns_trace = go.Bar(x=products, y=total_returns, name='Returns', marker_color='green')

        # Create annotations for tenure with bold and dark black color
        annotations = []
        for i, product in enumerate(products):
            max_value = max(total_investments[i], total_returns[i])
            annotations.append(dict(
                x=product,
                y=max_value + (max(total_investments + total_returns) * 0.05),  # Position above the highest bar
                text=f"Tenure: {tenures[i]} months",
                showarrow=False,
                font=dict(color='black', size=14, weight='bold')  # Set the color of the text to dark black and bold
            ))

        # Create a layout with annotations
        layout = go.Layout(
            title='Investment and Returns by Product',
            xaxis=dict(title='Product'),
            yaxis=dict(title='Amount (0.1M=100000)'),
            barmode='group',  # Use group mode to display bars side by side
            annotations=annotations
        )

        # Create a figure
        fig = go.Figure(data=[investment_trace, returns_trace], layout=layout)

        # Debugging: Print the figure to ensure it's created
        print(f"Created figure: {fig}")

        # Set the plot in the Plot component
        self.plot_1.data = fig['data']
        self.plot_1.layout = fig['layout']

        # Debugging: Check if the plot is assigned correctly
        print(f"Assigned figure to plot_1: {self.plot_1.data}")

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('lendor.dashboard')





# from ._anvil_designer import my_returnsTemplate
# from anvil import *
# import plotly.graph_objects as go
# from anvil.tables import app_tables
# import anvil.tables.query as q
# from .. import main_form_module as main_form_module

# class my_returns(my_returnsTemplate):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)
#     self.user_id = main_form_module.userId

#     # Check if user_id is correctly set
#     print(f"User ID: {self.user_id}")

#     # Any code you write here will run before the form opens.
#     self.create_bar_chart()

#   def create_bar_chart(self):
#     # Fetch investment data for the specific user
#     investments = app_tables.fin_loan_details.search(loan_updated_status=q.like('close%'), lender_customer_id=self.user_id)
    
#     # Debugging: Print fetched investments
#     print(f"Fetched investments for user {self.user_id}: {list(investments)}")
    
#     # Initialize a dictionary to store total investments and returns by product
#     product_data = {}
    
#     for investment in investments:
#       product = investment['product_name']
#       if product not in product_data:
#         product_data[product] = {'total_investment': 0, 'total_returns': 0}
#       product_data[product]['total_investment'] += investment['loan_amount']
#       product_data[product]['total_returns'] += investment['lender_returns']

#     # Prepare data for bar chart
#     products = list(product_data.keys())
#     total_investments = [product_data[product]['total_investment'] for product in products]
#     total_returns = [product_data[product]['total_returns'] for product in products]

#     # Create bar chart traces
#     investment_trace = go.Bar(x=products, y=total_investments, name='Investment', marker_color='blue')
#     returns_trace = go.Bar(x=products, y=total_returns, name='Returns', marker_color='green')

#     # Create a layout
#     layout = go.Layout(
#       title='Investment and Returns by Product',
#       xaxis=dict(title='Product'),
#       yaxis=dict(title='Amount(0.1M=100000)'),
#       barmode='group'  # Use group mode to display bars side by side
#     )

#     # Create a figure
#     fig = go.Figure(data=[investment_trace, returns_trace], layout=layout)

#     # Debugging: Print the figure to ensure it's created
#     print(f"Created figure: {fig}")

#     # Set the plot in the Plot component
#     self.plot_1.data = fig['data']
#     self.plot_1.layout = fig['layout']

#     # Debugging: Check if the plot is assigned correctly
#     print(f"Assigned figure to plot_1: {self.plot_1.data}")

#   def button_1_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     open_form('lendor.dashboard')
