# from ._anvil_designer import my_returnsTemplate
# from anvil import *
# import plotly.graph_objects as go
# from anvil.tables import app_tables
# import anvil.tables.query as q
# from .. import main_form_module as main_form_module

# class my_returns(my_returnsTemplate):
#     def __init__(self, **properties):
#         # Set Form properties and Data Bindings.
#         self.init_components(**properties)
#         self.user_id = main_form_module.userId

#         # Check if user_id is correctly set
#         print(f"User ID: {self.user_id}")

#     def create_bar_chart(self):
#         # Fetch investment data for the specific user
#         investments = app_tables.fin_loan_details.search(loan_updated_status=q.like('close%'), lender_customer_id=self.user_id)
        
#         # Debugging: Print fetched investments
#         print(f"Fetched investments for user {self.user_id}: {list(investments)}")
        
#         # Initialize a dictionary to store total investments, returns, and tenure by product
#         product_data = {}
        
#         for investment in investments:
#             product = investment['product_name']
#             if product not in product_data:
#                 product_data[product] = {'total_investment': 0, 'total_returns': 0, 'tenure': investment['tenure']}
#             product_data[product]['total_investment'] += investment['loan_amount']
#             product_data[product]['total_returns'] += investment['lender_returns']

#         # Prepare data for bar chart
#         products = list(product_data.keys())
#         total_investments = [product_data[product]['total_investment'] for product in products]
#         total_returns = [product_data[product]['total_returns'] for product in products]
#         tenures = [product_data[product]['tenure'] for product in products]

#         # Create bar chart traces
#         investment_trace = go.Bar(x=products, y=total_investments, name='Investment', marker_color='blue')
#         returns_trace = go.Bar(x=products, y=total_returns, name='Returns', marker_color='green')

#         # Create annotations for tenure with bold and dark black color
#         annotations = []
#         for i, product in enumerate(products):
#             max_value = max(total_investments[i], total_returns[i])
#             annotations.append(dict(
#                 x=product,
#                 y=max_value + (max(total_investments + total_returns) * 0.05),  # Position above the highest bar
#                 text=f"Tenure: {tenures[i]} months",
#                 showarrow=False,
#                 font=dict(color='black', size=14, weight='bold')  # Set the color of the text to dark black and bold
#             ))

#         # Create a layout with annotations
#         layout = go.Layout(
#             title='Investment and Returns by Product',
#             xaxis=dict(title='Product'),
#             yaxis=dict(title='Amount (0.1M=100000)'),
#             barmode='group',  # Use group mode to display bars side by side
#             annotations=annotations
#         )

#         # Create a figure
#         fig = go.Figure(data=[investment_trace, returns_trace], layout=layout)

#         # Debugging: Print the figure to ensure it's created
#         print(f"Created figure: {fig}")

#         # Set the plot in the Plot component
#         self.plot_1.data = fig['data']
#         self.plot_1.layout = fig['layout']

#         # Debugging: Check if the plot is assigned correctly
#         print(f"Assigned figure to plot_1: {self.plot_1.data}")

  
#     def create_user_bar_chart(self):
#         # Fetch investment data for the specific user
#         investments = app_tables.fin_lender.search(customer_id=self.user_id)
        
#         # Debugging: Print fetched investments
#         print(f"Fetched investments for user {self.user_id}: {list(investments)}")
        
#         # Initialize variables to store total investments and returns
#         total_investment = 0
#         total_returns = 0
        
#         for investment in investments:
#             total_investment += investment['investment']
#             total_returns += investment['return_on_investment']
  
#         # Debugging: Print aggregated values
#         print(f"Total Investment: {total_investment}, Total Returns: {total_returns}")
  
#         # Prepare data for bar chart
#         categories = ['Investment', 'Returns']
#         values = [total_investment, total_returns]
  
#         # Create bar chart trace
#         trace = go.Bar(x=categories, y=values, marker_color=['blue', 'green'])
  
#         # Create a layout
#         layout = go.Layout(
#             title='Investment and Returns for User',
#             xaxis=dict(title='Category'),
#             yaxis=dict(title='Amount (0.1M=100000)'),
#             barmode='group'  # Use group mode to display bars side by side
#         )
  
#         # Create a figure
#         fig = go.Figure(data=[trace], layout=layout)
  
#         # Debugging: Print the figure to ensure it's created
#         print(f"Created figure: {fig}")
  
#         # Set the plot in the Plot component
#         self.plot_2.data = fig['data']
#         self.plot_2.layout = fig['layout']
  
#         # Debugging: Check if the plot is assigned correctly
#         print(f"Assigned figure to plot_2: {self.plot_2.data}")

#     def button_1_click(self, **event_args):
#         """This method is called when the button is clicked"""
#         open_form('lendor.dashboard')
      
#     def button_2_click(self, **event_args):
#         self.plot_2.visible = True
#         self.plot_1.visible = False
#         self.create_user_bar_chart()
      
#     def button_3_click(self, **event_args):
#         self.plot_1.visible = True
#         self.plot_2.visible = False
#         self.create_bar_chart()






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

    def create_bar_chart(self):
        # Fetch investment data for the specific user
        investments = app_tables.fin_loan_details.search(loan_updated_status=q.like('close%'), lender_customer_id=self.user_id)
        
        # Debugging: Print fetched investments
        print(f"Fetched investments for user {self.user_id}: {list(investments)}")
        
        # Initialize lists to store data for the bar chart
        products = []
        total_investments = []
        total_returns = []
        tenures = []
        
        for investment in investments:
            product = investment['product_name']
            products.append(product)
            total_investments.append(investment['loan_amount'])
            total_returns.append(investment['lender_returns'])
            tenures.append(investment['tenure'])

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

    def create_user_bar_chart(self):
        # Fetch investment data for the specific user
        investments = app_tables.fin_lender.search(customer_id=self.user_id)
        
        # Debugging: Print fetched investments
        print(f"Fetched investments for user {self.user_id}: {list(investments)}")
        
        # Initialize variables to store total investments and returns
        total_investment = 0
        total_returns = 0
        
        for investment in investments:
            total_investment += investment['investment']
            total_returns += investment['return_on_investment']
  
        # Debugging: Print aggregated values
        print(f"Total Investment: {total_investment}, Total Returns: {total_returns}")
  
        # Prepare data for bar chart
        categories = ['Investment', 'Returns']
        values = [total_investment, total_returns]
  
        # Create bar chart trace
        trace = go.Bar(x=categories, y=values, marker_color=['blue', 'green'])
  
        # Create a layout
        layout = go.Layout(
            title='Investment and Returns for User',
            xaxis=dict(title='Category'),
            yaxis=dict(title='Amount (0.1M=100000)'),
            barmode='group'  # Use group mode to display bars side by side
        )
  
        # Create a figure
        fig = go.Figure(data=[trace], layout=layout)
  
        # Debugging: Print the figure to ensure it's created
        print(f"Created figure: {fig}")
  
        # Set the plot in the Plot component
        self.plot_2.data = fig['data']
        self.plot_2.layout = fig['layout']
  
        # Debugging: Check if the plot is assigned correctly
        print(f"Assigned figure to plot_2: {self.plot_2.data}")

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('lendor.dashboard')
      
    def button_2_click(self, **event_args):
        self.plot_2.visible = True
        self.plot_1.visible = False
        self.create_user_bar_chart()
      
    def button_3_click(self, **event_args):
        self.plot_1.visible = True
        self.plot_2.visible = False
        self.create_bar_chart()
