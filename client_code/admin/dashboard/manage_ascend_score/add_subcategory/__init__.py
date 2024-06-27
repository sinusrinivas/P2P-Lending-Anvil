from ._anvil_designer import add_subcategoryTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class add_subcategory(add_subcategoryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh()
    self.contenttt.visible = False

    # Any code you write here will run before the form opens.

  def refresh(self):
    """Refresh repeating panels with the latest data"""
    self.repeating_panel_1.items = app_tables.fin_admin_ascend_categories.search(group_name="gender")
    self.repeating_panel_2.items = app_tables.fin_admin_ascend_categories.search(group_name="qualification")
    self.repeating_panel_3.items = app_tables.fin_admin_ascend_categories.search(group_name="marital_status")
    self.repeating_panel_5.items = app_tables.fin_admin_ascend_categories.search(group_name="profession")
    self.repeating_panel_6.items = app_tables.fin_admin_ascend_categories.search(group_name="organization_type")
    self.repeating_panel_7.items = app_tables.fin_admin_ascend_categories.search(group_name="present_address")
    self.repeating_panel_8.items = app_tables.fin_admin_ascend_categories.search(group_name="duration_at_address")
    self.repeating_panel_9.items = app_tables.fin_admin_ascend_categories.search(group_name="salary_type")
    self.repeating_panel_10.items = app_tables.fin_admin_ascend_categories.search(group_name='spouse_profession')
    self.repeating_panel_11.items = app_tables.fin_admin_ascend_categories.search(group_name='age_of_business')
    self.repeating_panel_12.items = app_tables.fin_admin_ascend_categories.search(group_name="home_loan")
    self.repeating_panel_13.items = app_tables.fin_admin_ascend_categories.search(group_name="other_loan")
    self.repeating_panel_14.items = app_tables.fin_admin_ascend_categories.search(group_name="credit_card_loan")
    self.repeating_panel_15.items = app_tables.fin_admin_ascend_categories.search(group_name="vehicle_loan")
  
  def back_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("admin.dashboard.manage_ascend_score")
    
  def gender_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_sub = self.text_box_1.text.lower()
    entered_min_pts = int(self.text_box_2.text)
    new_row = app_tables.fin_admin_ascend_categories.add_row(group_name='gender',sub_category=entered_sub,min_points=entered_min_pts)
    self.text_box_1.text = ' '
    self.text_box_2.text = ' '
    self.refresh()

    existing_min_points = [row["min_points"] for row in app_tables.fin_admin_ascend_categories.search(group_name='gender')]

    max_points = max(existing_min_points + [entered_min_pts])

    existing_group_row  = app_tables.fin_admin_ascend_groups.get(group_name="gender")
    if existing_group_row:
      existing_group_row['max_points'] = max_points
      existing_group_row.update()

    else:
      new_group_row = app_tables.fin_admin_ascend_groups.add_row(
            group_name="gender", max_points=max_points
        )

  def qualification_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_sub = self.text_box_3.text.lower()
    entered_min_pts = int(self.text_box_4.text)
    new_row = app_tables.fin_admin_ascend_categories.add_row(group_name='qualification',sub_category=entered_sub,min_points=entered_min_pts)
    self.text_box_3.text = ' '
    self.text_box_4.text = ' '
    self.refresh()

    existing_min_points = [row["min_points"] for row in app_tables.fin_admin_ascend_categories.search(group_name='qualification')]

    max_points = max(existing_min_points + [entered_min_pts])

    existing_group_row  = app_tables.fin_admin_ascend_groups.get(group_name="qualification")
    if existing_group_row:
      existing_group_row['max_points'] = max_points
      existing_group_row.update()

    else:
      new_group_row = app_tables.fin_admin_ascend_groups.add_row(
            group_name="qualification", max_points=max_points
        )

  def marrital_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_sub = self.text_box_5.text.lower()
    entered_age = self.text_box_5a.text.lower()
    entered_min_pts = int(self.text_box_6.text)
    new_row = app_tables.fin_admin_ascend_categories.add_row(group_name='marital_status',sub_category=entered_sub,min_points=entered_min_pts,age=entered_age)
    self.text_box_5.text = ' '
    self.text_box_5a.text = ' '
    self.text_box_6.text = ' '
    self.refresh()

    existing_min_points = [row["min_points"] for row in app_tables.fin_admin_ascend_categories.search(group_name='marital_status')]

    max_points = max(existing_min_points + [entered_min_pts])

    existing_group_row  = app_tables.fin_admin_ascend_groups.get(group_name="marital_status")
    if existing_group_row:
      existing_group_row['max_points'] = max_points
      existing_group_row.update()

    else:
      new_group_row = app_tables.fin_admin_ascend_groups.add_row(
            group_name="marital_status", max_points=max_points
        )

  def profession_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_sub = self.text_box_7.text.lower()
    # valid_statuses = ['student', 'employee', 'self employment']
    # if entered_sub not in valid_statuses:
    #     alert("Please enter a valid profession: 'Student', 'Employee', 'Self employment'.")
    #     return
    entered_min_pts = int(self.text_box_8.text)
    new_row = app_tables.fin_admin_ascend_categories.add_row(group_name='profession',sub_category=entered_sub,min_points=entered_min_pts)
    self.text_box_7.text = ' '
    self.text_box_8.text = ' '
    self.refresh()

    existing_min_points = [row["min_points"] for row in app_tables.fin_admin_ascend_categories.search(group_name='profession')]

    max_points = max(existing_min_points + [entered_min_pts])

    existing_group_row  = app_tables.fin_admin_ascend_groups.get(group_name="profession")
    if existing_group_row:
      existing_group_row['max_points'] = max_points
      existing_group_row.update()

    else:
      new_group_row = app_tables.fin_admin_ascend_groups.add_row(
            group_name="profession", max_points=max_points
        )
    

  def organization_type_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_sub = self.text_box_12.text.lower()
    entered_min_pts = int(self.text_box_13.text)
    new_row = app_tables.fin_admin_ascend_categories.add_row(group_name='organization_type',sub_category=entered_sub,min_points=entered_min_pts)
    self.text_box_12.text = ' '
    self.text_box_13.text = ' '
    self.refresh()

    existing_min_points = [row["min_points"] for row in app_tables.fin_admin_ascend_categories.search(group_name='organization_type')]

    max_points = max(existing_min_points + [entered_min_pts])

    existing_group_row  = app_tables.fin_admin_ascend_groups.get(group_name="organization_type")
    if existing_group_row:
      existing_group_row['max_points'] = max_points
      existing_group_row.update()

    else:
      new_group_row = app_tables.fin_admin_ascend_groups.add_row(
            group_name="organization_type", max_points=max_points
        )

  def present_address_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_sub = self.text_box_14.text.lower()
    entered_min_pts = int(self.text_box_15.text)
    new_row = app_tables.fin_admin_ascend_categories.add_row(group_name='present_address',sub_category=entered_sub,min_points=entered_min_pts)
    self.text_box_14.text = ' '
    self.text_box_15.text = ' '
    self.refresh()

    existing_min_points = [row["min_points"] for row in app_tables.fin_admin_ascend_categories.search(group_name='present_address')]

    max_points = max(existing_min_points + [entered_min_pts])

    existing_group_row  = app_tables.fin_admin_ascend_groups.get(group_name="present_address")
    if existing_group_row:
      existing_group_row['max_points'] = max_points
      existing_group_row.update()

    else:
      new_group_row = app_tables.fin_admin_ascend_groups.add_row(
            group_name="present_address", max_points=max_points
        )

  def duration_at_address_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_sub = self.text_box_16.text.lower()
    entered_min_pts = int(self.text_box_17.text)
    new_row = app_tables.fin_admin_ascend_categories.add_row(group_name='duration_at_address',sub_category=entered_sub,min_points=entered_min_pts)
    self.text_box_16.text = ' '
    self.text_box_17.text = ' '
    self.refresh()

    existing_min_points = [row["min_points"] for row in app_tables.fin_admin_ascend_categories.search(group_name='duration_at_address')]

    max_points = max(existing_min_points + [entered_min_pts])

    existing_group_row  = app_tables.fin_admin_ascend_groups.get(group_name="duration_at_address")
    if existing_group_row:
      existing_group_row['max_points'] = max_points
      existing_group_row.update()

    else:
      new_group_row = app_tables.fin_admin_ascend_groups.add_row(
            group_name="duration_at_address", max_points=max_points
        )

  def salarytype_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_sub = self.text_box_18.text.lower()
    entered_min_pts = int(self.text_box_19.text)
    new_row = app_tables.fin_admin_ascend_categories.add_row(group_name='salary_type',sub_category=entered_sub,min_points=entered_min_pts)
    self.text_box_18.text = ' '
    self.text_box_19.text = ' '
    self.refresh()

    existing_min_points = [row["min_points"] for row in app_tables.fin_admin_ascend_categories.search(group_name='salary_type')]

    max_points = max(existing_min_points + [entered_min_pts])

    existing_group_row  = app_tables.fin_admin_ascend_groups.get(group_name="salary_type")
    if existing_group_row:
      existing_group_row['max_points'] = max_points
      existing_group_row.update()

    else:
      new_group_row = app_tables.fin_admin_ascend_groups.add_row(
            group_name="salary_type", max_points=max_points
        )

  def spouse_profession_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    entered_sub = self.text_box_20.text.lower()
    entered_min_pts = int(self.text_box_21.text)
    new_row = app_tables.fin_admin_ascend_categories.add_row(group_name='spouse_profession',sub_category=entered_sub,min_points=entered_min_pts)
    self.text_box_20.text = ' '
    self.text_box_21.text = ' '
    self.refresh()

    existing_min_points = [row["min_points"] for row in app_tables.fin_admin_ascend_categories.search(group_name='spouse_profession')]

    max_points = max(existing_min_points + [entered_min_pts])

    existing_group_row  = app_tables.fin_admin_ascend_groups.get(group_name="spouse_profession")
    if existing_group_row:
      existing_group_row['max_points'] = max_points
      existing_group_row.update()

    else:
      new_group_row = app_tables.fin_admin_ascend_groups.add_row(
            group_name="spouse_profession", max_points=max_points
        )

  def age_of_business_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_sub = self.text_box_22.text.lower()
    entered_min_pts = int(self.text_box_23.text)
    new_row = app_tables.fin_admin_ascend_categories.add_row(group_name='age_of_business',sub_category=entered_sub,min_points=entered_min_pts)
    self.text_box_22.text = ' '
    self.text_box_23.text = ' '
    self.refresh()

    existing_min_points = [row["min_points"] for row in app_tables.fin_admin_ascend_categories.search(group_name='age_of_business')]

    max_points = max(existing_min_points + [entered_min_pts])

    existing_group_row  = app_tables.fin_admin_ascend_groups.get(group_name="age_of_business")
    if existing_group_row:
      existing_group_row['max_points'] = max_points
      existing_group_row.update()

    else:
      new_group_row = app_tables.fin_admin_ascend_groups.add_row(
            group_name="age_of_business", max_points=max_points
        )

  def home_loan_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_sub = self.text_box_24.text.lower()
    valid_statuses = ['yes', 'no']
    if entered_sub not in valid_statuses:
        alert("Kindly input either 'yes' or 'no'.")
        return
    entered_min_pts = int(self.text_box_25.text)
    new_row = app_tables.fin_admin_ascend_categories.add_row(group_name='home_loan',sub_category=entered_sub,min_points=entered_min_pts)
    self.text_box_24.text = ' '
    self.text_box_25.text = ' '
    self.refresh()

    existing_min_points = [row["min_points"] for row in app_tables.fin_admin_ascend_categories.search(group_name='home_loan')]

    max_points = max(existing_min_points + [entered_min_pts])

    existing_group_row  = app_tables.fin_admin_ascend_groups.get(group_name="home_loan")
    if existing_group_row:
      existing_group_row['max_points'] = max_points
      existing_group_row.update()

    else:
      new_group_row = app_tables.fin_admin_ascend_groups.add_row(
            group_name="home_loan", max_points=max_points
        )

  def other_loan_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_sub = self.text_box_26.text.lower()
    valid_statuses = ['yes', 'no']
    if entered_sub not in valid_statuses:
        alert("Kindly input either 'yes' or 'no'.")
        return
    entered_min_pts = int(self.text_box_27.text)
    new_row = app_tables.fin_admin_ascend_categories.add_row(group_name='other_loan',sub_category=entered_sub,min_points=entered_min_pts)
    self.text_box_26.text = ' '
    self.text_box_27.text = ' '
    self.refresh()

    existing_min_points = [row["min_points"] for row in app_tables.fin_admin_ascend_categories.search(group_name='other_loan')]

    max_points = max(existing_min_points + [entered_min_pts])

    existing_group_row  = app_tables.fin_admin_ascend_groups.get(group_name="other_loan")
    if existing_group_row:
      existing_group_row['max_points'] = max_points
      existing_group_row.update()

    else:
      new_group_row = app_tables.fin_admin_ascend_groups.add_row(
            group_name="other_loan", max_points=max_points
        )

  def credit_card_loan_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_sub = self.text_box_28.text.lower()
    valid_statuses = ['yes', 'no']
    if entered_sub not in valid_statuses:
        alert("Kindly input either 'yes' or 'no'.")
        return
    entered_min_pts = int(self.text_box_29.text)
    new_row = app_tables.fin_admin_ascend_categories.add_row(group_name='credit_card_loan',sub_category=entered_sub,min_points=entered_min_pts)
    self.text_box_28.text = ' '
    self.text_box_29.text = ' '
    self.refresh()

    existing_min_points = [row["min_points"] for row in app_tables.fin_admin_ascend_categories.search(group_name='credit_card_loan')]

    max_points = max(existing_min_points + [entered_min_pts])

    existing_group_row  = app_tables.fin_admin_ascend_groups.get(group_name="credit_card_loan")
    if existing_group_row:
      existing_group_row['max_points'] = max_points
      existing_group_row.update()

    else:
      new_group_row = app_tables.fin_admin_ascend_groups.add_row(
            group_name="credit_card_loan", max_points=max_points
        )

  def vehicle_loan_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    entered_sub = self.text_box_30.text.lower()
    valid_statuses = ['yes', 'no']
    if entered_sub not in valid_statuses:
        alert("Kindly input either 'yes' or 'no'.")
        return
    entered_min_pts = int(self.text_box_31.text)
    new_row = app_tables.fin_admin_ascend_categories.add_row(group_name='vehicle_loan',sub_category=entered_sub,min_points=entered_min_pts)
    self.text_box_30.text = ' '
    self.text_box_31.text = ' '
    self.refresh()

    existing_min_points = [row["min_points"] for row in app_tables.fin_admin_ascend_categories.search(group_name='vehicle_loan')]

    max_points = max(existing_min_points + [entered_min_pts])

    existing_group_row  = app_tables.fin_admin_ascend_groups.get(group_name="vehicle_loan")
    if existing_group_row:
      existing_group_row['max_points'] = max_points
      existing_group_row.update()

    else:
      new_group_row = app_tables.fin_admin_ascend_groups.add_row(
            group_name="vehicle_loan", max_points=max_points
        )
  
  def salary_type_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    
  def gender_click(self, **event_args):
    """This method is called when the button is clicked"""
    

  def qualification_click(self, **event_args):
    """This method is called when the button is clicked"""
    

  def marrital_status_click(self, **event_args):
    """This method is called when the button is clicked"""
    

  def profession_click(self, **event_args):
    """This method is called when the button is clicked"""
    

  def organization_type_click(self, **event_args):
    """This method is called when the button is clicked"""
    

  def present_address_click(self, **event_args):
    """This method is called when the button is clicked"""
    

  def duration_at_address_click(self, **event_args):
    """This method is called when the button is clicked"""
    

  def spouse_profession_click(self, **event_args):
    """This method is called when the button is clicked"""
    

  def age_of_business_click(self, **event_args):
    """This method is called when the button is clicked"""
    

  def home_loan_click(self, **event_args):
    """This method is called when the button is clicked"""
    

  def other_loan_click(self, **event_args):
    """This method is called when the button is clicked"""
    

  def credit_card_loan_click(self, **event_args):
    """This method is called when the button is clicked"""
    

  def vehicle_loan_click(self, **event_args):
    """This method is called when the button is clicked"""
    

  def button_9_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_1.visible = True
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def button_10_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = True
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = True
    self.grid_panel_4.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def button_12_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = True
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def button_13_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = True
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def button_14_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = True
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def button_16_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_6.visible = True
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def button_17_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = True
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def button_19_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = True
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = True
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = True
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = True
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def button_18_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = True
    self.grid_panel_15.visible = False

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = True

  def image_4_copy_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    self.grid_panel_1.visible = True
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def image_4_copy_3_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = True
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def image_4_copy_5_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = True
    self.grid_panel_4.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def image_4_copy_7_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = True
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def image_4_copy_2_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = True
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def image_4_copy_10_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = True
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def image_4_copy_6_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_6.visible = True
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def image_4_copy_9_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = True
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def image_4_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = True
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def image_4_copy_4_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = True
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def image_4_copy_4_copy_copy_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = True
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def image_4_copy_4_copy_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = True
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = False

  def image_4_copy_8_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = True
    self.grid_panel_15.visible = False

  def image_4_copy_4_copy_copy_2_mouse_up(self, x, y, button, **event_args):
    """This method is called when a mouse button is released on this component"""
    self.grid_panel_1.visible = False
    self.grid_panel_2.visible = False
    self.grid_panel_3.visible = False
    self.grid_panel_4.visible = False
    self.grid_panel_5.visible = False
    self.grid_panel_6.visible = False
    self.grid_panel_7.visible = False
    self.grid_panel_8.visible = False
    self.grid_panel_9.visible = False
    self.grid_panel_10.visible = False
    self.grid_panel_11.visible = False
    self.grid_panel_12.visible = False
    self.grid_panel_13.visible = False
    self.grid_panel_14.visible = False
    self.grid_panel_15.visible = True

  

  

  
 