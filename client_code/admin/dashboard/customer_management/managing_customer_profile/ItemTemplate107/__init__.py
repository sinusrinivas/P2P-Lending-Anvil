from ._anvil_designer import ItemTemplate107Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate107(ItemTemplate107Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
    # Any code you write here will run before the form opens.
  # Add a Label component for the name
    self.label_1 = Label(text="Name", align="left", bold=True)
    self.add_component(self.label_1)
    
    # Add a Label component for the email
    self.label_2 = Label(text="Email_Id:", align="left", bold=True)
    self.add_component(self.label_2)
    
    # Add a Label component for the alternate email
    self.label_4 = Label(text="Alternate_Email_Id:", align="left", bold=True)
    self.add_component(self.label_4)

    self.label_10 = Label(text="User_Type :")
    # Add an Image component for the photo
    self.image_1 = Image(source=None)
    self.add_component(self.image_1)
