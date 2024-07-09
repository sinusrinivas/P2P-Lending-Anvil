from ._anvil_designer import registration_processTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ....bank_users.main_form import main_form_module
from ....bank_users.main_form import main_form
from ....bank_users.user_form import user_module

class registration_process(registration_processTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.email = main_form_module.email
        email = self.email
        self.user_id = user_module.find_user_id(email)
        

        user_id = self.user_id
        
        user_data = app_tables.fin_user_profile.get(customer_id=user_id)
        
        if user_data is not None:
            form_count = user_data['form_count']
            print(form_count)
            if form_count == 0:
                # Highlight the first_label and hide other labels
                self.label_7.bold = True  
                self.label_1.bold = True
            elif form_count == 1:
                self.label_7.bold = True  
                self.label_1.bold = True
                self.label_13.font_weight = 'Bold'
                self.label_2.font_weight = 'Bold'
                self.label_8.font_weight = 'Bold'
            elif form_count == 2:
                self.label_7.bold = True  
                self.label_1.bold = True
                self.label_13.font_weight = 'Bold'
                self.label_2.font_weight = 'Bold'
                self.label_8.font_weight = 'Bold'
                self.label_3.font_weight = 'Bold'
                self.label_9.font_weight = 'Bold'
                self.label_14.font_weight = 'Bold'
            elif form_count == 3:
                self.label_7.bold = True  
                self.label_1.bold = True
                self.label_13.font_weight = 'bold'
                self.label_2.font_weight = 'bold'
                self.label_8.font_weight = 'bold'
                self.label_3.font_weight = 'bold'
                self.label_9.font_weight = 'bold'
                self.label_14.font_weight = 'bold'
                self.label_4.font_weight = 'bold'
                self.label_15.font_weight = 'bold'
                self.label_10.font_weight = 'bold'
            elif form_count == 4:
                self.label_7.bold = True  
                self.label_1.bold = True
                self.label_13.font_weight = 'bold'
                self.label_2.font_weight = 'bold'
                self.label_8.font_weight = 'bold'
                self.label_3.font_weight = 'bold'
                self.label_9.font_weight = 'bold'
                self.label_14.font_weight = 'bold'
                self.label_4.font_weight = 'bold'
                self.label_15.font_weight = 'bold'
                self.label_10.font_weight = 'bold'
                self.label_14.font_weight = 'bold'
                self.label_5.font_weight = 'bold'
                self.label_16.font_weight = 'bold'
                self.label_11.font_weight = 'bold'
            elif form_count == 5:
                self.label_7.bold = True  
                self.label_1.bold = True
                self.label_13.font_weight = 'bold'
                self.label_2.font_weight = 'bold'
                self.label_8.font_weight = 'bold'
                self.label_3.font_weight = 'bold'
                self.label_9.font_weight = 'bold'
                self.label_14.font_weight = 'bold'
                self.label_4.font_weight = 'bold'
                self.label_15.font_weight = 'bold'
                self.label_10.font_weight = 'bold'
                self.label_14.font_weight = 'bold'
                self.label_5.font_weight = 'bold'
                self.label_16.font_weight = 'bold'
                self.label_11.font_weight = 'bold'
                self.label_6.font_weight = 'bold'
                self.label_12.font_weight = 'bold'
                self.label_17.font_weight = 'bold'
                
                
                


# from ._anvil_designer import registration_processTemplate
# from anvil import *
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
# from ....bank_users.main_form import main_form_module
# from ....bank_users.user_form import user_module

# class registration_process(registration_processTemplate):
#     def __init__(self, **properties):
#         # Set Form properties and Data Bindings.
#         self.init_components(**properties)
        
#         self.email = main_form_module.email
#         email = self.email
#         self.user_id = user_module.find_user_id(email)
        
#         user_id = self.user_id
        
#         user_data = app_tables.fin_user_profile.get(customer_id=user_id)
        
#         if user_data is not None:
#             form_count = user_data['form_count']
            
#             # List of labels you want to set bold based on form_count
#             labels_to_bold = [
#                 self.label_7, self.label_1, self.label_13, self.label_2,
#                 self.label_8, self.label_3, self.label_9, self.label_14,
#                 self.label_4, self.label_15, self.label_10, self.label_5,
#                 self.label_16, self.label_11, self.label_6, self.label_12,
#                 self.label_17
#             ]
            
#             # Set all labels' font weight to normal initially
#             for label in labels_to_bold:
#                 label.foreground = 'red'
            
#             # Set font weight to bold for labels up to form_count
#             if form_count is not None:
#                 for i in range(min(form_count, len(labels_to_bold))):
#                     labels_to_bold[i].foreground = 'red'

