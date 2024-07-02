from ._anvil_designer import borrower_notificationsTemplate
from anvil import *
import anvil.server

class borrower_notifications(borrower_notificationsTemplate):
  def __init__(self, user_Id, **properties):
    self.init_components(**properties)
    self.user_Id = user_Id
    self.read_notifications = set()  # Store read notifications
    self.load_notifications()

  def load_notifications(self):
    notifications = anvil.server.call('get_notifications', self.user_Id)
    for notification in notifications:
      notification['read'] = (notification['date'], notification['message']) in self.read_notifications
    self.repeating_panel_1.items = notifications
    self.mark_notifications_as_read()

  def mark_notifications_as_read(self):
    for item in self.repeating_panel_1.items:
      self.read_notifications.add((item['date'], item['message']))
    # No need to call server function since we are not updating the database

  def button_refresh_click(self, **event_args):
    self.load_notifications()

  def back_button_click(self, **event_args):
    open_form('borrower.dashboard')
