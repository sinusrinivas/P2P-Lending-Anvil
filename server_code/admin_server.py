import anvil.secrets
import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import *
# import plotly.graph_objects as go
# from datetime import datetime, date
# import matplotlib.pyplot as plt
# # from datetime import datetime, date
import anvil.mpl_util
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, date
import io
import anvil.media

# Define server function to navigate to the Invest Now form
@anvil.server.callable
def open_invest_now_form():
    open_form("bank_users.main_form.basic_registration_form")

@anvil.server.callable
def open_apply_for_loan_form():
    open_form("bank_users.main_form.basic_registration_form")



@anvil.server.callable
def product_details(product_id, product_name, product_group,product_description, product_categories,processing_fee,tds,extension_fee, membership_type, interest_type, max_amount, min_amount, min_tenure, max_tenure, roi, foreclose_type, foreclosure_fee, extension_allowed, emi_payment, min_months,lapsed_fee, default_fee, default_fee_amount, npa , npa_amount, occupation,min_extension_month ,default_status, npa_status):
  row = app_tables.fin_product_details.add_row(product_id=product_id,
                                           product_name = product_name,
                                           product_group=product_group,
                                           product_description = product_description,
                                           product_categories = product_categories,
                                           processing_fee=processing_fee,
                                           tds = tds,
                                           extension_fee=extension_fee,
                                           membership_type=membership_type,
                                           interest_type= interest_type,
                                           # late_fee = late_fee,
                                           max_amount = max_amount,
                                           min_amount=min_amount,
                                           # tenure = tenure,
                                           min_tenure = min_tenure,
                                           max_tenure = max_tenure,
                                           roi = roi,
                                           foreclose_type=foreclose_type,
                                           foreclosure_fee = foreclosure_fee,
                                           extension_allowed=extension_allowed,
                                           # lapsed_status=lapsed_status,
                                           emi_payment = emi_payment,
                                           min_months=min_months,                                           
                                           #discount_coupons = discount_coupons,
                                           lapsed_fee = lapsed_fee,
                                           default_fee = default_fee,
                                           default_fee_amount = default_fee_amount,
                                           npa=npa,
                                           npa_amount=npa_amount,
                                           occupation=occupation,
                                           min_extension_months=min_extension_month,
                                           default_select_percentage_amount = default_status,
                                           npa_select_percentage_amount=npa_status
                                          )



@anvil.server.callable
def manage_products(groups,category):
  row = app_tables.fin_product_categories.add_row(product_group=groups,product_category=category)


@anvil.server.callable
def user_issues_bugreports(user_issues, specific_issue, user_discription, image, feedback_form, email_user,coustmer_id):
 row = app_tables.fin_user_issues_bugreports.add_row(user_issues=user_issues,
                                                 user_discription=user_discription,
                                                 specific_issue=specific_issue,
                                                 image=image,
                                                 feedback_form=feedback_form,
                                                 email_user=email_user,
                                                 customer_id=coustmer_id)

# code for basic details
@anvil.server.callable
def add_basic_details(full_name, gender, dob, mobile_no, user_photo, alternate_email, aadhar, aadhar_card, pan, pan_card, street_adress_1, street_address_2, city, pincode, state, country, user_id, user_age ,present, duration):
  row = app_tables.fin_user_profile.search(customer_id=user_id)
  if row:
    row[0]['full_name'] = full_name
    row[0]['gender'] = gender
    row[0]['date_of_birth'] = dob
    row[0]['mobile']=mobile_no
    row[0]['user_photo']=user_photo
    row[0]['another_email']= alternate_email
    row[0]['aadhaar_no']=aadhar
    row[0]['aadhaar_photo']=aadhar_card
    row[0]['pan_number']=pan
    row[0]['pan_photo']=pan_card
    row[0]['street_adress_1'] = street_adress_1
    row[0]['street_address_2'] = street_address_2
    row[0]['city'] = city
    row[0]['state'] = state
    row[0]['country'] = country
    row[0]['pincode'] = pincode
    row[0]['user_age'] = user_age
    row[0]['present_address'] = present
    row[0]['duration_at_address'] = duration
    row[0]['form_count'] = 0

@anvil.server.callable
def generate_admin_id():
    full_table = app_tables.fin_user_profile.search()
    if full_table:
        highest_customer_id = find_highest_customer_id()
        return highest_customer_id + 1
    else:
        return 100000

def find_highest_customer_id():
    table_data = app_tables.fin_user_profile.search()
    highest_id = 99999
    for row in table_data:
        customer_id = row['customer_id']
        if customer_id > highest_id:
            highest_id = customer_id
    return highest_id



import bcrypt

@anvil.server.callable
def hash_password(password):
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password.decode()

# for view admins
@anvil.server.callable
def get_admin_emails():
    # Fetch all admin emails from the fin_admin_users table
    admin_emails = [admin['admin_email'] for admin in app_tables.fin_admin_users.search()]
    return admin_emails

@anvil.server.callable
def get_admin_details(email):
    # Fetch admin details based on email from the fin_admin_users table
    admin = app_tables.fin_admin_users.get(admin_email=email)
    if admin:
        admin_details = {
            'admin_email': admin['admin_email'],
            'full_name': admin['full_name'],
            'admin_role':admin['admin_role'],
            'ref_admin_name':admin['ref_admin_name'],
            'joined_date':admin['join_date']
        }
        return admin_details
    else:
        return None


@anvil.server.callable
def get_user_for_login(email):
  user_by_username = app_tables.users.get(email=email)

  if user_by_username:
            return user_by_username
  else:
            return None


@anvil.server.callable
def hash_password_1(password ,password_hash):
    # Hash the password using bcrypt
    hashed_password = bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
    return hashed_password

@anvil.server.callable
def hash_password_2(password):
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password.decode()

@anvil.server.callable
def search_borrower(query):
  result = app_tables.fin_user_profile.search(usertype=q.like('borrower'))
  if query:
    result = [
      x for x in result
      if query in str(x['customer_id'])
      or query in str(x['full_name'])
      or query in str(x['mobile'])
      or query in str(x['email_user'])
    ]
  return result

@anvil.server.callable
def search_lender(query):
  result = app_tables.fin_user_profile.search(usertype=q.like('lender'))
  if query:
    result = [
      x for x in result
      if query in str(x['customer_id'])
      or query in str(x['full_name'])
      or query in str(x['mobile'])
      or query in str(x['email_user'])
    ]
  return result

# # Server module: manage_credit_limit.py


@anvil.server.callable
def save_credit_limit(new_value):
    row = app_tables.fin_manage_credit_limit.get()  # Get the single row in the table
    if row:
        row['credit_limit'] = new_value  # Update the existing row
    else:
        app_tables.fin_manage_credit_limit.add_row(credit_limit=new_value)  # Add a new row if none exists

#manage_customer and contact details server code

def load_customer_data(self):
  # Fetch the customer data from the server function
  user_profile = anvil.server.call('get_customer_data')
  
  # Set the items property of the repeating panel to the fetched data
  self.repeating_panel_1.items = user_profile


@anvil.server.callable
def get_combined_user_and_guarantor_data():
    # Fetch user profiles excluding "super admin" and "admin"
    user_profiles = app_tables.fin_user_profile.search()
    
    # Fetch all guarantors
    guarantors = app_tables.fin_guarantor_details.search()

    # Create a list of customer_ids to exclude (super admin and admin)
    restricted_customer_ids = [profile['customer_id'] for profile in user_profiles if profile['usertype'] in ['super admin', 'admin']]
    
    # Filter user profiles to exclude restricted customer_ids
    user_profiles_filtered = [profile for profile in user_profiles if profile['customer_id'] not in restricted_customer_ids]
    
    # Filter guarantors to exclude restricted customer_ids
    guarantors_filtered = [guarantor for guarantor in guarantors if guarantor['customer_id'] not in restricted_customer_ids]

    # Combine the data into a single list, interleaving records
    combined_data = []

    # Determine the maximum length to iterate up to the maximum of both lists
    max_length = max(len(user_profiles_filtered), len(guarantors_filtered))

    for i in range(max_length):
        if i < len(user_profiles_filtered) and i < len(guarantors_filtered):
            user_profile = user_profiles_filtered[i]
            guarantor = guarantors_filtered[i]
            combined_data.append({
                'user_photo': user_profile['user_photo'],  
                'full_name': user_profile['full_name'],   
                'email_user': user_profile['email_user'],  
                'mobile': user_profile['mobile'],  
                'usertype': user_profile['usertype'],
                'another_person': guarantor['another_person'],  
                'guarantor_name': guarantor['guarantor_name'],   
                'guarantor_mobile_no': guarantor['guarantor_mobile_no']
            })
        

    return combined_data


@anvil.server.callable
def get_combined_user_and_guarantor_data_2():
    # Fetch user profiles
    user_profiles = app_tables.fin_user_profile.search()

    # Create a list of customer_ids to exclude (super admin and admin)
    restricted_customer_ids = [profile['customer_id'] for profile in user_profiles if profile['usertype'] in ['super admin', 'admin']]
    
    # Filter user profiles to exclude restricted customer_ids
    user_profiles_filtered = [profile for profile in user_profiles if profile['customer_id'] not in restricted_customer_ids]

    # Combine the data into a single list
    combined_data = []
    for user_profile in user_profiles_filtered:
        combined_data.append({
            'customer_id': user_profile['customer_id'],
            'full_name': user_profile['full_name'],
            'email_user': user_profile['email_user'],
            'usertype': user_profile['usertype'],
            'account_name': user_profile['account_name'],
            'account_type': user_profile['account_type'],
            'account_number': user_profile['account_number'],
            'bank_name': user_profile['bank_name'],
            'bank_id': user_profile['bank_id'],
            'account_bank_branch': user_profile['account_bank_branch']
        })

    return combined_data
# @anvil.server.callable
# def create_loan_disbursement_graph(loan_created, lender_accepted, loan_disbursed):
#     # Create scatter plot traces directly
#     loan_created_trace = go.Scatter(x=[loan_created], y=['Loan Created'], mode='markers', name='Loan Created', marker=dict(color='blue'))
#     lender_accepted_trace = go.Scatter(x=[lender_accepted], y=['Lender Accepted'], mode='markers', name='Lender Accepted', marker=dict(color='orange'))
#     loan_disbursed_trace = go.Scatter(x=[loan_disbursed], y=['Loan Disbursed'], mode='markers', name='Loan Disbursed', marker=dict(color='green'))

#     # Create the figure with traces
#     fig = go.Figure(data=[loan_created_trace, lender_accepted_trace, loan_disbursed_trace])

#     # Update layout
#     fig.update_layout(
#         title='Loan Disbursement Timeline',
#         xaxis_title='Timestamp',
#         yaxis_title='Event',
#         yaxis=dict(showticklabels=False),
#         showlegend=True
#     )

#     # Return the figure object directly
#     return fig


# @anvil.server.callable
# def create_loan_disbursement_graph(loan_created, lender_accepted, loan_disbursed):
#     # Convert timestamps to datetime objects if necessary
#     dates = []
#     if loan_created:
#         dates.append(('Loan Created', convert_to_naive_datetime(loan_created)))
#     if lender_accepted:
#         dates.append(('Lender Accepted', convert_to_naive_datetime(lender_accepted)))
#     if loan_disbursed:
#         dates.append(('Loan Disbursed', convert_to_naive_datetime(loan_disbursed)))
    
#     # Sort dates by timestamp
#     dates.sort(key=lambda x: x[1])
    
#     # Extract labels and timestamps
#     labels = [label for label, _ in dates]
#     timestamps = [timestamp for _, timestamp in dates]
    
#     # Create a Plotly figure
#     fig = go.Figure()
    
#     # Add a scatter trace with lines
#     fig.add_trace(go.Scatter(
#         x=timestamps,
#         y=labels,
#         mode='lines+markers',
#         line=dict(shape='linear'),
#         marker=dict(size=10),
#         text=labels,
#         textposition='top center'
#     ))
    
#     # Update layout
#     fig.update_layout(
#         title='Loan Disbursement Timeline',
#         xaxis_title='Timestamp',
#         yaxis_title='Stage',
#         xaxis=dict(type='date')
#     )
    
#     return fig

# def convert_to_naive_datetime(dt):
#     if isinstance(dt, datetime):
#         # Convert aware datetime to naive datetime by removing timezone info
#         return dt.replace(tzinfo=None)
#     elif isinstance(dt, date):
#         # Convert date to datetime and make it naive
#         return datetime.combine(dt, datetime.min.time())
#     else:
#         raise TypeError(f"Expected datetime or date object, got {type(dt)}")



@anvil.server.callable
def create_loan_disbursement_graph(loan_created, lender_accepted, loan_disbursed):
    # Convert timestamps to datetime objects if necessary
    dates = []
    if loan_created:
        dates.append(('Loan Created', convert_to_naive_datetime(loan_created)))
    if lender_accepted:
        dates.append(('Lender Accepted', convert_to_naive_datetime(lender_accepted)))
    if loan_disbursed:
        dates.append(('Loan Disbursed', convert_to_naive_datetime(loan_disbursed)))
    
    # Sort dates by timestamp
    dates.sort(key=lambda x: x[1])
    
    # Extract labels and timestamps
    labels = [label for label, _ in dates]
    timestamps = [timestamp for _, timestamp in dates]
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(timestamps, labels, marker='o', linestyle='-', color='b')
    
    # Annotate points with their labels
    for i, label in enumerate(labels):
        ax.annotate(label, (timestamps[i], labels[i]), textcoords="offset points", xytext=(0,10), ha='center')
    
    # Set titles and labels
    ax.set_title('Loan Disbursement Timeline')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Stage')
    
    # Rotate dates on x-axis for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout for better fit
    plt.tight_layout()
    
    # Save plot to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Create a Media object and return it
    media = anvil.media.from_file(buf, 'image/png')
    return media

def convert_to_naive_datetime(dt):
    if isinstance(dt, datetime):
        # Convert aware datetime to naive datetime by removing timezone info
        return dt.replace(tzinfo=None)
    elif isinstance(dt, date):
        # Convert date to datetime and make it naive
        return datetime.combine(dt, datetime.min.time())
    else:
        raise TypeError(f"Expected datetime or date object, got {type(dt)}")
