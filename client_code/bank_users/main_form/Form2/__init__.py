from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    <CustomHTML
      css="height: 0px; width: 0px;"
      html="""
      <link rel="stylesheet" type="text/css" href="/_static/path/to/your/css/file.css">
      """
    />
    # Any code you write here will run before the form opens.
