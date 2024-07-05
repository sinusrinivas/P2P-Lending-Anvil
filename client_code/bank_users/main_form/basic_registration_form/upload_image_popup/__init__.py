from ._anvil_designer import upload_image_popupTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class upload_image_popup(upload_image_popupTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def confirm_upload_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        if self.image_loader.file is not None:
            self.raise_event('x-upload-image', image_file=self.image_loader.file)
        self.remove_from_parent()
