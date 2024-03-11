from ._anvil_designer import add_peopleTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date

class add_people(add_peopleTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.date_lable.text = date.today().strftime('%d %b %Y')
    # Any code you write here will run before the form opens.
