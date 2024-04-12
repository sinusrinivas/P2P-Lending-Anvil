import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables




        
# def get_group_points():
#     groups = app_tables.fin_admin_beseem_groups.search()

#     if groups:
#         group_points = 0

#         for group_row in groups:
#             group_points += group_row['max_points']

#         return group_points
#     return None
