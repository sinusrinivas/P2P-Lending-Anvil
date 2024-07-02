from ._anvil_designer import borrower_notificationsTemplate
from anvil import *
import anvil.server

class borrower_notifications(borrower_notificationsTemplate):
  def __init__(self, user_Id, **properties):
    self.init_components(**properties)
    self.user_Id = user_Id
    self.load_notifications()

  def load_notifications(self):
    notifications = anvil.server.call('get_notifications', self.user_Id)
    self.repeating_panel_notifications.items = notifications
    anvil.server.call('mark_notifications_as_read', self.user_Id)

  def button_refresh_click(self, **event_args):
    self.load_notifications()

  def back_button_click(self, **event_args):
    open_form('borrower.dashboard')
