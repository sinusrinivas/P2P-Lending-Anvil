import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# MouseHoverEffects.py

from anvil import alert

def apply_mouse_hover_effect(component):
    # Event handler for mouse enter event
    def mouse_enter_handler(**event_args):
        # Change component properties or styles on mouse enter
        component.background = '#05264d'  # Change background color
        # You can add more changes here, like changing text color, size, etc.
        alert("Mouse entered component!")

    # Event handler for mouse leave event
    def mouse_leave_handler(**event_args):
        # Revert component properties or styles on mouse leave
        component.background = '#FFFFFF'  # Revert background color
        # Revert any other changes made in mouse enter event
        alert("Mouse left component!")

    # Assign event handlers to the component
    component.set_event_handler('mouse_enter', mouse_enter_handler)
    component.set_event_handler('mouse_leave', mouse_leave_handler)

