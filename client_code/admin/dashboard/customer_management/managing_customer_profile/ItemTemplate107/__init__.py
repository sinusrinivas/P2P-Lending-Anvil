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
    self.name_label = Label(text="Name", align="left", bold=True)
    self.add_component(self.name_label)
    
    # Add a Label component for the email
    self.email_label = Label(text="Email", align="left", bold=True)
    self.add_component(self.email_label)
    
    # Add a Label component for the alternate email
    self.alt_email_label = Label(text="Alternate Email", align="left", bold=True)
    self.add_component(self.alt_email_label)
    
    # Add an Image component for the photo
    self.photo = Image(source=None)
    self.add_component(self.photo)
