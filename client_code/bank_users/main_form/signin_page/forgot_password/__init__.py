from ._anvil_designer import forgot_passwordTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class forgot_password(forgot_passwordTemplate):
  def __init__(self, email, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.role = "no-scroll"
    self.text_box_1.text = email

    self.label_2.show = self.label_2_show

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    password = self.text_box_2.text.strip()
    retype_password = self.text_box_2_copy.text.strip()
    email = self.text_box_1.text.strip()

    if password != retype_password:
      self.error_label.text = 'Passwords do not match. Please re-enter.'
      self.error_label.foreground = 'red'
      self.error_label.visible = True
      return

    user = app_tables.users.get(email=email)
    if user:
      hashed_password = anvil.server.call('hash_password_2', password)
      user['password_hash'] = hashed_password
      self.error_label.text = 'Password updated successfully.'
      self.error_label.foreground = 'green'
      open_form('bank_users.main_form.signin_page')
    else:
      self.error_label.text = 'User not found.'
      self.error_label.foreground = 'red'
    
    self.error_label.visible = True

  def check_box_1_change(self, **event_args):
    self.password_visible = self.check_box_1.checked
    if self.password_visible:
      self.text_box_2.hide_text = False  # Show decrypted password
      self.text_box_2_copy.hide_text = False
    else:
      self.text_box_2.hide_text = True
      self.text_box_2_copy.hide_text = True

  def send_otp_click(self, **event_args):
    email = self.text_box_1.text.strip()
    if not email:
      alert("Please fill the email")
      return

    self.otp = anvil.server.call('send_email_otp', email)
    if self.otp:
      alert(f"OTP has been sent to {email}")
      self.show_otp_input()
    else:
      self.error_label.text = 'Failed to send OTP. Please try again later.'
      self.error_label.foreground = 'red'
      self.error_label.visible = True

  def show_otp_input(self):
    self.text_box_otp.visible = True
    self.verify_otp_button.visible = True
    self.send_otp.text = "Resend"  # Change text of send_otp link
    self.send_otp.visible = True

  def verify_otp_button_click(self, **event_args):
    entered_otp = self.text_box_otp.text.strip()
    if str(self.otp) == entered_otp:
      self.error_label.text = 'OTP verified successfully'
      self.error_label.foreground = 'green'
      self.error_label.visible = True
      
      # Update email verified status in user table
      email = self.text_box_1.text.strip()
      anvil.server.call('update_user_status', email, email_verified=True)

      self.label_2.visible = True
      self.label_5.visible = True
      self.label_5_copy.visible = True
      self.text_box_2.visible = True
      self.text_box_2_copy.visible = True
      self.check_box_1.visible = True
      self.send_otp.visible = False
      self.text_box_otp.visible = False
      self.verify_otp_button.visible = False
      self.button_1.visible = True
    else:
      self.retype_password_error_label.text = 'Invalid OTP. Please try again.'
      self.retype_password_error_label.foreground = 'red'
      self.retype_password_error_label.visible = True
      self.send_otp.visible = True

  def label_2_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    self.text_box_2.hide_text = True

