from ._anvil_designer import manage_ascend_score_rangeTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class manage_ascend_score_range(manage_ascend_score_rangeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Initially, check if there is any existing ascend category
    self.check_existing_ascend_category()

  def check_existing_ascend_category(self):
    # Define ascend_categorys
    ascend_categorys = ['VeryGood', 'Good', 'Average', 'Bad']

    for ascend_category in ascend_categorys:
        row = app_tables.fin_ascend_score_range.get(ascend_category=ascend_category)

        if row is None:
            self.enable_text_boxes(ascend_category)
            self.disable_edit_button(ascend_category)
        else:
            self.populate_text_boxes(row, ascend_category)
            self.disable_text_boxes(ascend_category)
            self.enable_edit_button(ascend_category)
            self.disable_save_button(ascend_category)


  def populate_text_boxes(self, row, ascend_category):
    # Populate textboxes with existing data
    if ascend_category == 'VeryGood':
      self.text_box_1.text = str(row['min_ascend_score_range'])
      self.text_box_2.text = str(row['max_ascend_score_range'])
      self.text_box_3.text = str(row['color']) 
    elif ascend_category == 'Good':
      self.text_box_4.text = str(row['min_ascend_score_range'])
      self.text_box_5.text = str(row['max_ascend_score_range'])
      self.text_box_6.text = str(row['color']) 
    elif ascend_category == 'Average':
      self.text_box_7.text = str(row['min_ascend_score_range'])
      self.text_box_8.text = str(row['max_ascend_score_range'])
      self.text_box_9.text = str(row['color']) 
    elif ascend_category == 'Bad':
      self.text_box_10.text = str(row['min_ascend_score_range'])
      self.text_box_11.text = str(row['max_ascend_score_range'])
      self.text_box_12.text = str(row['color'])  

  def enable_text_boxes(self, ascend_category):
    # Enable textboxes for the specified membership type
    #if ascend_category == 'VeryGood':
      self.text_box_1.enabled = True
      self.text_box_2.enabled = True
      self.text_box_3.enabled = True
    #elif ascend_category == 'Good':
      self.text_box_4.enabled = True
      self.text_box_5.enabled = True
      self.text_box_6.enabled = True
    #elif ascend_category == 'Average':
      self.text_box_7.enabled = True
      self.text_box_8.enabled = True
      self.text_box_9.enabled = True
    #elif ascend_category == 'Bad':
      self.text_box_10.enabled = True
      self.text_box_11.enabled = True
      self.text_box_12.enabled = True

  def disable_text_boxes(self, ascend_category):
    # Disable textboxes for the specified ascend category
    #if ascend_category == 'VeryGood':
      self.text_box_1.enabled = False
      self.text_box_2.enabled = False
      self.text_box_3.enabled = False
    #elif ascend_category == 'Good':
      self.text_box_4.enabled = False
      self.text_box_5.enabled = False
      self.text_box_6.enabled = False
    #elif ascend_category == 'Average':
      self.text_box_7.enabled = False
      self.text_box_8.enabled = False
      self.text_box_9.enabled = False
    #elif ascend_category == 'Bad':
      self.text_box_10.enabled = False
      self.text_box_11.enabled = False
      self.text_box_12.enabled = False

  def enable_edit_button(self, ascend_category):
    # Enable the corresponding edit button
    if ascend_category == 'VeryGood':
      self.button_1.visible = True
    elif ascend_category == 'Good':
      self.button_1.visible = True
    elif ascend_category == 'Average':
      self.button_1.visible = True
    elif ascend_category == 'Bad':
      self.button_1.visible = True  

  def disable_edit_button(self, ascend_category):
    # Disable the corresponding edit button
    if ascend_category == 'VeryGood':
      self.button_1.visible = False
    elif ascend_category == 'Good':
      self.button_1.visible = False
    elif ascend_category == 'Average':
      self.button_1.visible = False
    elif ascend_category == 'Bad':
      self.button_1.visible = False 
      
  def enable_save_button(self, ascend_category):
    # Enable the corresponding edit button
    if ascend_category == 'VeryGood':
      self.button_2.visible = True
    elif ascend_category == 'Good':
      self.button_2.visible = True
    elif ascend_category == 'Average':
      self.button_2.visible = True
    elif ascend_category == 'Bad':
      self.button_2.visible = True

  def disable_save_button(self, ascend_category):
    # Disable the corresponding edit button
    if ascend_category == 'VeryGood':
      self.button_2.visible = False
    elif ascend_category == 'Good':
      self.button_2.visible = False
    elif ascend_category == 'Bad':
      self.button_2.visible = False
    elif ascend_category == 'Bad':
      self.button_2.visible = False

  
  def save_ascend_score_range(self, ascend_category):
    print("Saving ascend score range for:", ascend_category)
    
    # Determaxe which textboxes to read based on ascend category
    if ascend_category == 'VeryGood':
        min_ascend_score_range = int(self.text_box_1.text)
        max_ascend_score_range = int(self.text_box_2.text)
        color = self.text_box_3.text
        if min_ascend_score_range <= 0:
            alert("verygood Minimum amount must be greater than zero!", title="Error")
            return
        if min_ascend_score_range >= max_ascend_score_range:
            alert("verygood Minimum ascend score range must be less than verygood maximum ascend score range!", title="Error")
            return
        
    elif ascend_category == 'Good':
        min_ascend_score_range = int(self.text_box_4.text)
        max_ascend_score_range = int(self.text_box_5.text)
        color = self.text_box_6.text
        if min_ascend_score_range <= 0:
            alert("Good Minimum ascend score range can't be set as zero, it should be lessthan than verygood max_ascend_score_range and greater than Good max_ascend_score_range!", title="Error")
            return
        if min_ascend_score_range >= max_ascend_score_range:
            alert("good Minimum ascend score range must be less than good maximum ascend score range!", title="Error")
            return
        verygood_max_ascend_score_range = int(self.text_box_2.text)
        if min_ascend_score_range >= verygood_max_ascend_score_range:
            alert("Good's min_ascend_score_range must be lessthan than verygood max_ascend_score_range!", title="Error")
            return  
        # Update VeryGood's min_ascend_score_range to Good's max_ascend_score_range
        very_good_row = app_tables.fin_ascend_score_range.get(ascend_category='VeryGood')
        if very_good_row is not None:
            very_good_row.update(min_ascend_score_range=max_ascend_score_range)   
        
    elif ascend_category == 'Average':
        min_ascend_score_range = int(self.text_box_7.text)
        max_ascend_score_range = int(self.text_box_8.text)
        color = self.text_box_9.text
        if min_ascend_score_range <= 0:
            alert("Average Minimum ascend score range can't be set as zero, it should be lessthan than good max_ascend_score_range and greater than Average max_ascend_score_range!", title="Error")
            return
        if min_ascend_score_range >= max_ascend_score_range:
            alert("average Minimum ascend score range must be less than average maximum ascend score range!", title="Error")
            return
        good_max_ascend_score_range = int(self.text_box_5.text)
        if min_ascend_score_range >= good_max_ascend_score_range:
            alert("good min_ascend_score_range must be lessthan than average max_ascend_score_rage!", title="Error")
            return  
        # Update Good's min_ascend_score_range to Average's max_ascend_score_range
        good_row = app_tables.fin_ascend_score_range.get(ascend_category='Good')
        if good_row is not None:
            good_row.update(min_ascend_score_range=max_ascend_score_range)
    elif ascend_category == 'Bad':
        min_ascend_score_range = int(self.text_box_10.text)
        max_ascend_score_range = int(self.text_box_11.text)
        color = self.text_box_12.text
        if min_ascend_score_range <= 0:
            alert("Bad Minimum ascend score range can't be set as zero, it should be lessthan than average max_ascend_score_range and greater than bad max_ascend_score_range!", title="Error")
            return
        if min_ascend_score_range >= max_ascend_score_range:
            alert("bad Minimum ascend score range must be less than bad maximum ascend score range!", title="Error")
            return
        average_max_ascend_score_range = int(self.text_box_5.text)
        if min_ascend_score_range >= average_max_ascend_score_range:
            alert("average min_ascend_score_range must be lessthan than bad max_ascend_score_rage!", title="Error")
            return 
        # Update Average's min_ascend_score_range to Bad's max_ascend_score_range
        average_row = app_tables.fin_ascend_score_range.get(ascend_category='Average')
        if average_row is not None:
            average_row.update(min_ascend_score_range=max_ascend_score_range) 
      
        # Check if Bad's max_ascend_score_range exceeds any other ascend score range
        for category in ['VeryGood', 'Good', 'Average']:
            if category != ascend_category:
                other_row = app_tables.fin_ascend_score_range.get(ascend_category=category)
                if other_row is not None and other_row['max_ascend_score_range'] is not None and max_ascend_score_range >= other_row['max_ascend_score_range']:
                    alert("Bad's max_ascend_score_range cannot exceed " + category + "'s max_ascend_score_range!", title="Warning")
                    return

      
    print("Min Ascend score range:", min_ascend_score_range)
    print("max Ascend score ranga:", max_ascend_score_range)
    print("Color:", color)
        
    open_form('admin.dashboard.manage_settings.manage_ascend_score_range')

    # Re-enable edit and save buttons
    self.disable_save_button(ascend_category)
    self.enable_edit_button(ascend_category)
    self.disable_text_boxes(ascend_category)
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.home_button_admin_1.visible = False
    for ascend_category in ['VeryGood', 'Good', 'Average', 'Bad']:
        self.edit_ascend_score_range(ascend_category)   

  def edit_ascend_score_range(self, ascend_category):
    print("Editing ascend score range for:", ascend_category)
    # Enable editing for the corresponding ascend_category
    self.enable_text_boxes(ascend_category)
    # Disable the edit button
    self.disable_edit_button(ascend_category)
    self.enable_save_button(ascend_category)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    for ascend_category in ['VeryGood', 'Good', 'Average', 'Bad']:
        self.save_ascend_score_range(ascend_category)
    open_form('admin.dashboard.manage_settings.manage_ascend_score_range')

