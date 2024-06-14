from ._anvil_designer import dashboard_report_a_problemTemplate
from anvil import *
import anvil.server
import datetime
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class dashboard_report_a_problem(dashboard_report_a_problemTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Any code you write here will run before the form opens.
        self.usertype = properties.get('usertype', 'borrower')  # Default value is 'borrower'
        self.subcategory = app_tables.fin_report_issue_category.search()
        self.category = app_tables.fin_category.search()
        self.drop_down_1.items = [(c['category'], c['category']) for c in self.category]
        self.drop_down_1.selected_value = self.category[0]['category']  # Set default value
        # Set up event handler for category dropdown change
        self.drop_down_1.set_event_handler('change', self.update_subcategory)

        # Call the update_subcategory method to initialize the subcategory dropdown
        self.update_subcategory()

    def update_subcategory(self, **event_args):
        selected_category = self.drop_down_1.selected_value
        if selected_category == 'Loan Issue':
            self.drop_down_2.items = [(sli['borrower_subcategory_loan_issue'], sli['borrower_subcategory_loan_issue']) for sli in self.subcategory]
        elif selected_category == 'Technical Issue':
            self.drop_down_2.items = [(sti['subcategory_technical_issue'], sti['subcategory_technical_issue']) for sti in self.subcategory]
        else:
            self.drop_down_2.items = [(sli['borrower_subcategory_loan_issue'], sli['borrower_subcategory_loan_issue']) for sli in self.subcategory]
    def img_file_loader_change(self, file, **event_args):
        # Function to handle user photo file upload event
        if file is not None:
            # Display the image in an Image component 
          self.image_issue.source =file
    def button_2_click(self, **event_args):
        # Get input values from text boxes
        name = self.name_box.text
        email = self.email_box.text
        mobile = self.mobile_box.text
        issue_photo =self.img_file_loader.file
        category = self.drop_down_1.selected_value
        subcategory = self.drop_down_2.selected_value
        description = self.description_box.text

        # Validate if all required fields are filled
        if not name or not email or not mobile or not issue_photo or not category or not subcategory or not description:
            alert("Please fill in all required fields.")
            return
  
        # Validate mobile number
        try:
            mobile = int(mobile)
        except ValueError:
            alert("Mobile number must be a valid number.")
            return

        # Check if a file is uploaded
        if not self.img_file_loader.file:
            alert("Please upload a file.")
            return

        current_datetime = datetime.datetime.now()

        # Get the file uploaded via file_loader_1
        Iss = self.imd_file_loader.file
         # Check if the checkbox is checked
        it_is_urgent = self.check_box_1.checked

        # Add a row to the fin_reported_problems table with file details
        app_tables.fin_reported_problems.add_row(name=name,
                                                  email=email,
                                                  mobile_number=mobile,
                                                  category = category,
                                                  subcategory = subcategory ,
                                                  issue_description=description,
                                                  report_date=current_datetime,
                                                  issue_photo=issue_photo,
                                                  it_is_urgent=it_is_urgent,
                                                  usertype=self.usertype)

        # Show success message to the user
        alert('Problem reported successfully. Thank you for your feedback!')

        # Open dashboard form or any other form
        open_form('borrower.dashboard' if self.usertype == 'borrower' else 'lender.dashboard')

    def image_1_copy_2_mouse_up(self, x, y, button, **event_args):
      """This method is called when a mouse button is released on this component"""
      open_form('borrower.dashboard.dashboard_report_a_problem')

