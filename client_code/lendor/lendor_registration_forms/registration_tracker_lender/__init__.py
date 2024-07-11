from ._anvil_designer import registration_tracker_lenderTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class registration_tracker_lender(registration_tracker_lenderTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.email = main_form_module.email
        email = self.email
        self.user_id = user_module.find_user_id(email)
        
        user_id = self.user_id
        
        user_data = app_tables.fin_user_profile.get(customer_id=user_id)
        
        # List of labels to be highlighted based on form count
        labels = [
            (self.label_7, self.label_1),
            (self.label_13, self.label_2),
            (self.label_8, self.label_3),
            (self.label_9, self.label_4),
            (self.label_14, self.label_5),
            (self.label_15, self.label_6)
        ]
        
        # Set initial opacity for all labels
        for label_pair in labels:
            for label in label_pair:
                label.foreground = "rgba(0, 0, 0, 0.5)"  # Set to semi-transparent

        if user_data is not None:
            form_count = user_data['form_count']
            print(form_count)
            
            for i in range(form_count + 1):
                if i < len(labels):
                    for label in labels[i]:
                        label.bold = True
                        label.foreground = "rgba(0, 0, 0, 1)"  # Set to fully opaque
                        
                    # Set the icon for the first label in each pair
                    if i == 0:
                        self.label_7.icon = '_/theme/bank_users/circle-1_1.png'                    
                    elif i == 1:
                        self.label_8.icon = '_/theme/bank_users/circle-2%20(2).png'
                    elif i == 2:
                        self.label_9.icon = '_/theme/bank_users/circle-3%20(2).png'
                    elif i == 3:
                        self.label_10.icon = '_/theme/bank_users/circle-4%20(2).png'
                    elif i == 4:
                        self.label_11.icon = '_/theme/bank_users/circle-5%20(2).png'
                    else :
                        self.label_12.icon = '_/theme/bank_users/circle-6%20(2).png'
