from ._anvil_designer import manage_membershipTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class manage_membership(manage_membershipTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Initially, check if there is any existing membership data
    self.check_existing_membership_data()

  def check_existing_membership_data(self):
    # Check if there is data in the database for each membership type
    silver_row = app_tables.fin_membership.get(membership_type='Silver')
    gold_row = app_tables.fin_membership.get(membership_type='Gold')
    platinum_row = app_tables.fin_membership.get(membership_type='Platinum')

    if silver_row is None:
      self.enable_text_boxes('Silver')
      self.disable_edit_button('Silver')
    else:
      self.populate_text_boxes(silver_row, 'Silver')
      self.disable_text_boxes('Silver')
      self.enable_edit_button('Silver')
      self.disable_save_button('Silver')

    if gold_row is None:
      self.enable_text_boxes('Gold')
      self.disable_edit_button('Gold')
    else:
      self.populate_text_boxes(gold_row, 'Gold')
      self.disable_text_boxes('Gold')
      self.enable_edit_button('Gold')
      self.disable_save_button('Gold')
      
    if platinum_row is None:
      self.enable_text_boxes('Platinum')
      self.disable_edit_button('Platinum')
    else:
      self.populate_text_boxes(platinum_row, 'Platinum')
      self.disable_text_boxes('Platinum')
      self.enable_edit_button('Platinum')
      self.disable_save_button('Platinum')



  def populate_text_boxes(self, row, membership_type):
    # Populate textboxes with existing data
    if membership_type == 'Silver':
      self.text_box_1.text = row['min_amount']
      self.text_box_2.text = row['max_amount']
    elif membership_type == 'Gold':
      self.text_box_3.text = row['min_amount']
      self.text_box_4.text = row['max_amount']
    elif membership_type == 'Platinum':
      self.text_box_5.text = row['min_amount']
      self.text_box_6.text = row['max_amount']

  def enable_text_boxes(self, membership_type):
    # Enable textboxes for the specified membership type
    #if membership_type == 'Silver':
      self.text_box_1.enabled = True
      self.text_box_2.enabled = True
    #elif membership_type == 'Gold':
      self.text_box_3.enabled = True
      self.text_box_4.enabled = True
    #elif membership_type == 'Platinum':
      self.text_box_5.enabled = True
      self.text_box_6.enabled = True

  def disable_text_boxes(self, membership_type):
    # Disable textboxes for the specified membership type
    #if membership_type == 'Silver':
      self.text_box_1.enabled = False
      self.text_box_2.enabled = False
    #elif membership_type == 'Gold':
      self.text_box_3.enabled = False
      self.text_box_4.enabled = False
    #elif membership_type == 'Platinum':
      self.text_box_5.enabled = False
      self.text_box_6.enabled = False

  def enable_edit_button(self, membership_type):
    # Enable the corresponding edit button
    if membership_type == 'Silver':
      self.button_1.visible = True
    elif membership_type == 'Gold':
      self.button_1.visible = True
    elif membership_type == 'Platinum':
      self.button_1.visible = True

  def disable_edit_button(self, membership_type):
    # Disable the corresponding edit button
    if membership_type == 'Silver':
      self.button_1.visible = False
    elif membership_type == 'Gold':
      self.button_1.visible = False
    elif membership_type == 'Platinum':
      self.button_1.visible = False
      
  def enable_save_button(self, membership_type):
    # Enable the corresponding edit button
    if membership_type == 'Silver':
      self.button_2.visible = True
    elif membership_type == 'Gold':
      self.button_2.visible = True
    elif membership_type == 'Platinum':
      self.button_2.visible = True

  def disable_save_button(self, membership_type):
    # Disable the corresponding edit button
    if membership_type == 'Silver':
      self.button_2.visible = False
    elif membership_type == 'Gold':
      self.button_2.visible = False
    elif membership_type == 'Platinum':
      self.button_2.visible = False
      
  def save_membership(self, membership_type):
    print("Saving membership for:", membership_type)
    # Determine which textboxes to read based on membership type
    if membership_type == 'Silver':
        min_amount = int(self.text_box_1.text)
        max_amount = int(self.text_box_2.text)
    elif membership_type == 'Gold':
        min_amount = int(self.text_box_3.text)
        new_max_amount = int(self.text_box_4.text)
        # Calculate Gold max_amount based on Silver min_amount
        silver_row = app_tables.fin_membership.get(membership_type='Silver')
        if silver_row is not None:
            max_amount = new_max_amount - silver_row['max_amount']
            # Ensure max_amount is not less than Silver max_amount
            if max_amount < silver_row['max_amount']:
                max_amount = silver_row['max_amount']
            # Adjust Platinum min_amount if necessary
            platinum_row = app_tables.fin_membership.get(membership_type='Platinum')
            if platinum_row is not None and platinum_row['min_amount'] <= new_max_amount:
                platinum_row.update(min_amount=new_max_amount + 1)
    elif membership_type == 'Platinum':
        min_amount = int(self.text_box_5.text)
        new_max_amount = int(self.text_box_6.text)
        # Calculate Platinum max_amount based on Gold min_amount
        gold_row = app_tables.fin_membership.get(membership_type='Gold')
        if gold_row is not None:
            max_amount = new_max_amount - gold_row['max_amount']
            # Ensure max_amount is not less than Gold max_amount
            if max_amount < gold_row['max_amount']:
                max_amount = gold_row['max_amount']

    print("Min Amount:", min_amount)
    print("Max Amount:", max_amount)

    print("Min Amount:", min_amount)
    print("Max Amount:", max_amount)

    # Check if a row already exists for this membership type
    existing_row = app_tables.fin_membership.get(membership_type=membership_type)
    if existing_row is not None:
        # Update the existing row
        existing_row.update(min_amount=int(min_amount), max_amount=int(max_amount))
    else:
        # Save data to fin_membership table
        app_tables.fin_membership.add_row(membership_type=membership_type, min_amount=int(min_amount), max_amount=int(max_amount))

    # Perform validation and propagation of changes
    if membership_type == 'Silver':
        # Check if Silver max_amount exceeds Gold min_amount
        gold_row = app_tables.fin_membership.get(membership_type='Gold')
        if gold_row is not None and max_amount >= gold_row['min_amount']:
            # Increase Gold min_amount by 1
            gold_row.update(min_amount=max_amount + 1)
            # Propagate changes to Platinum if necessary
            platinum_row = app_tables.fin_membership.get(membership_type='Platinum')
            if platinum_row is not None and platinum_row['min_amount'] <= gold_row['max_amount']:
                platinum_row.update(min_amount=gold_row['max_amount'] + 1)
    elif membership_type == 'Gold':
        # Check if Gold max_amount exceeds Platinum min_amount
        platinum_row = app_tables.fin_membership.get(membership_type='Platinum')
        if platinum_row is not None and max_amount >= platinum_row['min_amount']:
            # Increase Platinum min_amount by 1
            platinum_row.update(min_amount=max_amount + 1)
    
    
    
    # Alert message after saving
    alert("Saved successfully!", title="Success")
    open_form('admin.dashboard.manage_settings.manage_membership')

    # Re-enable edit and save buttons
    self.disable_save_button(membership_type)
    self.enable_edit_button(membership_type)
    self.disable_text_boxes(membership_type)

  def edit_membership(self, membership_type):
    print("Editing membership for:", membership_type)
    # Enable editing for the corresponding membership type
    self.enable_text_boxes(membership_type)
    # Disable the edit button
    self.disable_edit_button(membership_type)
    self.enable_save_button(membership_type)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.home_button_admin_1.visible = False
    self.edit_membership('Silver')
    

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.save_membership('Silver')
    open_form('admin.dashboard.manage_settings.manage_membership')

# from ._anvil_designer import manage_membershipTemplate
# from anvil import *
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables

# class manage_membership(manage_membershipTemplate):
#     def __init__(self, **properties):
#         # Set Form properties and Data Bindings.
#         self.init_components(**properties)

#         # Initially, check if there is any existing membership data
#         self.check_existing_membership_data()

#     def check_existing_membership_data(self):
#         # Check if there is data in the database for each membership type
#         silver_row = app_tables.fin_membership.get(membership_type='Silver')
#         gold_row = app_tables.fin_membership.get(membership_type='Gold')
#         platinum_row = app_tables.fin_membership.get(membership_type='Platinum')

#         if silver_row is None:
#             self.enable_text_boxes('Silver')
#             self.disable_edit_button('Silver')
#         else:
#             self.populate_text_boxes(silver_row, 'Silver')
#             self.disable_text_boxes('Silver')
#             self.enable_edit_button('Silver')
#             self.disable_save_button('Silver')

#         if gold_row is None:
#             self.enable_text_boxes('Gold')
#             self.disable_edit_button('Gold')
#         else:
#             self.populate_text_boxes(gold_row, 'Gold')
#             self.disable_text_boxes('Gold')
#             self.enable_edit_button('Gold')
#             self.disable_save_button('Gold')

#         if platinum_row is None:
#             self.enable_text_boxes('Platinum')
#             self.disable_edit_button('Platinum')
#         else:
#             self.populate_text_boxes(platinum_row, 'Platinum')
#             self.disable_text_boxes('Platinum')
#             self.enable_edit_button('Platinum')
#             self.disable_save_button('Platinum')

#     def populate_text_boxes(self, row, membership_type):
#         # Populate textboxes with existing data
#         if membership_type == 'Silver':
#             self.text_box_1.text = row['min_amount']
#             self.text_box_2.text = row['max_amount']
#         elif membership_type == 'Gold':
#             self.text_box_3.text = row['min_amount']
#             self.text_box_4.text = row['max_amount']
#         elif membership_type == 'Platinum':
#             self.text_box_5.text = row['min_amount']
#             self.text_box_6.text = row['max_amount']

#     def enable_text_boxes(self, membership_type):
#         # Enable textboxes for the specified membership type
#         if membership_type == 'Silver':
#             self.text_box_1.enabled = True
#             self.text_box_2.enabled = True
#         elif membership_type == 'Gold':
#             self.text_box_3.enabled = True
#             self.text_box_4.enabled = True
#         elif membership_type == 'Platinum':
#             self.text_box_5.enabled = True
#             self.text_box_6.enabled = True

#     def disable_text_boxes(self, membership_type):
#         # Disable textboxes for the specified membership type
#         if membership_type == 'Silver':
#             self.text_box_1.enabled = False
#             self.text_box_2.enabled = False
#         elif membership_type == 'Gold':
#             self.text_box_3.enabled = False
#             self.text_box_4.enabled = False
#         elif membership_type == 'Platinum':
#             self.text_box_5.enabled = False
#             self.text_box_6.enabled = False

#     def enable_edit_button(self, membership_type):
#         # Enable the corresponding edit button
#         if membership_type == 'Silver':
#             self.button_1.visible = True
#         elif membership_type == 'Gold':
#             self.button_1.visible = True
#         elif membership_type == 'Platinum':
#             self.button_1.visible = True

#     def disable_edit_button(self, membership_type):
#         # Disable the corresponding edit button
#         if membership_type == 'Silver':
#             self.button_1.visible = False
#         elif membership_type == 'Gold':
#             self.button_1.visible = False
#         elif membership_type == 'Platinum':
#             self.button_1.visible = False

#     def enable_save_button(self, membership_type):
#         # Enable the corresponding edit button
#         if membership_type == 'Silver':
#             self.button_2.visible = True
#         elif membership_type == 'Gold':
#             self.button_2.visible = True
#         elif membership_type == 'Platinum':
#             self.button_2.visible = True

#     def disable_save_button(self, membership_type):
#         # Disable the corresponding edit button
#         if membership_type == 'Silver':
#             self.button_2.visible = False
#         elif membership_type == 'Gold':
#             self.button_2.visible = False
#         elif membership_type == 'Platinum':
#             self.button_2.visible = False

#     def save_membership(self, membership_type):
#         print("Saving membership for:", membership_type)
#         # Determine which textboxes to read based on membership type
#         if membership_type == 'Silver':
#             min_amount = int(self.text_box_1.text)
#             max_amount = int(self.text_box_2.text)
#         elif membership_type == 'Gold':
#             min_amount = int(self.text_box_3.text)
#             new_max_amount = int(self.text_box_4.text)
#             # Calculate Gold max_amount based on Silver min_amount
#             silver_row = app_tables.fin_membership.get(membership_type='Silver')
#             if silver_row is not None:
#                 max_amount = new_max_amount - silver_row['max_amount']
#                 # Ensure max_amount is not less than Silver max_amount
#                 if max_amount < silver_row['max_amount']:
#                     max_amount = silver_row['max_amount']
#                 # Adjust Platinum min_amount if necessary
#                 platinum_row = app_tables.fin_membership.get(membership_type='Platinum')
#                 if platinum_row is not None and platinum_row['min_amount'] <= new_max_amount:
#                     platinum_row.update(min_amount=new_max_amount + 1)
#         elif membership_type == 'Platinum':
#             min_amount = int(self.text_box_5.text)
#             new_max_amount = int(self.text_box_6.text)
#             # Calculate Platinum max_amount based on Gold min_amount
#             gold_row = app_tables.fin_membership.get(membership_type='Gold')
#             if gold_row is not None:
#                 max_amount = new_max_amount - gold_row['max_amount']
#                 # Ensure max_amount is not less than Gold max_amount
#                 if max_amount < gold_row['max_amount']:
#                     max_amount = gold_row['max_amount']

#         print("Min Amount:", min_amount)
#         print("Max Amount:", max_amount)

#         # Check if a row already exists for this membership type
#         existing_row = app_tables.fin_membership.get(membership_type=membership_type)
#         if existing_row is not None:
#             # Update the existing row
#             existing_row.update(min_amount=int(min_amount), max_amount=int(max_amount))
#         else:
#             # Save data to fin_membership table
#             app_tables.fin_membership.add_row(membership_type=membership_type, min_amount=int(min_amount), max_amount=int(max_amount))

#         if membership_type == 'Silver':
#             # Check if Silver max_amount exceeds Gold min_amount
#             gold_row = app_tables.fin_membership.get(membership_type='Gold')
#             if gold_row is not None and max_amount >= gold_row['min_amount']:
#                 # Increase Gold min_amount by 1
#                 gold_row.update(min_amount=max_amount + 1)
#                 # Propagate changes to Platinum if necessary
#                 platinum_row = app_tables.fin_membership.get(membership_type='Platinum')
#                 if platinum_row is not None and platinum_row['min_amount'] <= gold_row['max_amount']:
#                     platinum_row.update(min_amount=gold_row['max_amount'] + 1)
#         elif membership_type == 'Gold':
#             # Check if Gold max_amount exceeds Platinum min_amount
#             platinum_row = app_tables.fin_membership.get(membership_type='Platinum')
#             if platinum_row is not None and max_amount >= platinum_row['min_amount']:
#                 # Increase Platinum min_amount by 1
#                 platinum_row.update(min_amount=max_amount + 1)

#         # Alert message after saving
#         alert("Saved successfully!", title="Success")

#         # Re-enable edit and save buttons
#         self.disable_save_button(membership_type)
#         self.enable_edit_button(membership_type)
#         self.disable_text_boxes(membership_type)

#     def edit_membership(self, membership_type):
#         print("Editing membership for:", membership_type)
#         # Enable editing for the corresponding membership type
#         self.enable_text_boxes(membership_type)
#         # Disable the edit button
#         self.disable_edit_button(membership_type)
#         self.enable_save_button(membership_type)

#     def button_1_click(self, membership_type, **event_args):
#         """This method is called when the button is clicked"""
#         # membership_type = event_args['membership_type']
#         self.edit_membership("Silver" or "Gold" or "Platinum")

#     def button_2_click(self, membership_type, **event_args):
#         """This method is called when the button is clicked"""
#         # membership_type = event_args['membership_type']
#         self.save_membership("Silver" or "Gold" or "Platinum")

