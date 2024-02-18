import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


# user data 

#users = app_tables.fin_user_profile.search(email_user=)

# this function is force push to total points in bessem table
def final_points_update_bessem_table():
  final_points = general_points()+loan_points()+loan_and_trust_user_model()+occupation_point_and_government_id_model()
  general_check = fake_detection()
  if general_check:
    if final_points<= 1000:
      return final_points
    else:
      fake_control()
  else:
    block_user()

 
# caluculate from user_profile table
def general_points():
  return 400



# this function is working on underwriting 
def loan_points():
  return 100

# this function is working on underwriting
def loan_and_trust_user_model():
  return 200

# this function have to check by admin
def occupation_point_and_government_id_model():
  
  return 300






# this function goes to be create


def fake_control():
  return 500


def fake_detection():
  
  return True


def block_user():
  pass
  # if this function is call the is going to be block




# outer call function