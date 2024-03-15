import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# from passlib.hash import pbkdf2_sha256

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
  

# @anvil.server.callable
# def add_admin_details(email, name, mobile_no, dob, gender, role, password, created_date, status):
#     admin_users = app_tables.fin_admin_users.get(admin_email=email)
#     if admin_users:
#         return False
#     else:
#         hashed_password = pbkdf2_sha256.hash(password)  # Hash the password
#         app_tables.users.add_row(email=email, enabled=True, password_hash=hashed_password)
#         app_tables.fin_admin_users.add_row(admin_email=email, admin_role=role, full_name=name, mobile_no=mobile_no, join_date=created_date, gender=gender, status=status)
#         return True


def add_admin_details(email,name,mobile_no,dob,gender,role,password,created_date,status):
  admin_users = app_tables.fin_admin_users.get(admin_email=email)
  if admin_users:
    return False
  else:
    app_tables.users.add_row(email=email,enabled=True,password_hash=password)
    app_tables.fin_admin_users.add_row(admin_email=email,admin_role=role,full_name=name, mobile_no=mobile_no, join_date = created_date, gender=gender, status=status )
    return True   

