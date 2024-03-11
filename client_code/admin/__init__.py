import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

user = None

def admin_check(email):
  admin_user = app_tables.fin_admin_users.search(admin_email=email)
  if admin_user:
    role = admin_user[0]['admin_role']
    if (role == "super admin"):
      return True
    else:
      return False
  else:
    return False
  


def add_admin_details(email,):
  admin_users = app_tables.fin_admin_users.search()