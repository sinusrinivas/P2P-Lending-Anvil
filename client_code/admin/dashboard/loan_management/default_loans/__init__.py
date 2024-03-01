from ._anvil_designer import default_loansTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

class default_loans(default_loansTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.fin_loan_details.search()

    a = -1
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    self.list_4 = []
    self.list_5 = []
    self.list_6 = []
    self.list_7 = []
    self.list_8 = []
    self.list_9 = []
    self.list_10 = []
    
    
    for i in self.data:
      a+=1
      self.list_1.append(i['loan_id'])
      self.list_2.append(i['borrower_customer_id'])
      self.list_3.append(i['borrower_full_name'])
      self.list_4.append(i['loan_updated_status'])
      self.list_5.append(i['lender_full_name'])
      self.list_6.append(i['lender_customer_id'])
      self.list_7.append(i['interest_rate'])
      self.list_8.append(i['tenure'])
      self.list_9.append(i['loan_amount'])
      self.list_10.append(i['lender_accepted_timestamp'])
    print(a)

    self.result = []
    self.index = []
    if a == -1:
      alert("No Data Available Here!")
    else:
      b = -1
      for i in self.list_4:
        b+=1
        if i == "default loan" or i == 'Default loan' or i == "Default Loan":
          self.index.append(b)
          
      for i in self.index:
        self.result.append({'loan_id' : self.list_1[i], 'coustmer_id' : self.list_2[i], 'full_name' : self.list_3[i], 'loan_status' : self.list_4[i],'lendor_full_name' : self.list_5[i],'lender_customer_id':self.list_6[i],'interest_rate':self.list_7[i],'tenure':self.list_8[i],'loan_amount':self.list_9[i],'lender_timestamp':self.list_10[i]})

      self.repeating_panel_2.items = self.result

  #   # Any code you write here will run before the form opens.
  #   self.loan = tables.app_tables.fin_loan_details.search()
  #   self.fourcloser = tables.app_tables.foreclosure.search()
  #   self.today = datetime.now().date()
  #   print(self.today)

  #   self.due_list = []
  #   self.loan_amont = []
  #   self.paid_amount = []
  #   self.intrest = []
  #   self.loan_due_amount = []

  #   self.id = []
  #   self.c_id = []
  #   self.full_name = []
  #   self.status = []
  #   for i in self.loan:
  #     self.due_list.append(i['due_date'].date())
  #     self.loan_amont.append(i['loan_amount'])
  #     self.id.append(i['loan_id'])
  #     self.intrest.append(i['interest_rate'])
  #     self.loan_due_amount.append(i['total_repayment_amount'])
  #     self.c_id.append(i['borrower_customer_id'])
  #     self.full_name.append(i['borrower_full_name'])
  #     self.status.append(i['loan_updated_status'])


  #   self.index = []  
  #   b = -1
  #   for i in self.id:
  #     b += 1
  #     if (self.loan_due_amount[b] != 0) and (self.status[b] != "closed"):
  #       self.index.append(self.id[b])

  #   print(self.index)
  #   self.result = []
  #   self.days = {}
  #   for i in self.index:
  #     c = self.id.index(i)
  #     print(c)
  #     d = ((self.today - self.due_list[c]).days > 3) and ((self.today - self.due_list[c]).days < 90)
  #     if (self.due_list[c] < self.today) and (d):
  #       annual_interest_rate = self.intrest[c]
  #       days_in_year = 365
  #       daily_interest_rate = (annual_interest_rate / 100) / days_in_year
        
  #       self.result.append(self.id[c])
  #       interest_per_day = self.loan_due_amount[c] * daily_interest_rate
  #       days_late = (self.today - self.due_list[c]).days
  #       penalty = interest_per_day * days_late
  #       total_due = self.loan_due_amount[c] + penalty
  #       self.days[self.id[c]] = total_due
    
    
  #   self.index1 = []
  #   self.final = []
  #   self.total = []
  #   for id, total in self.days.items():
  #     self.index1.append(self.id.index(id))
  #     self.total.append(total)

  #   a = -1
  #   for i in self.index1:
  #     a += 1
  #     self.final.append({'loan_id' : self.id[i], 'coustmer_id' : self.c_id[i], 'full_name' : self.full_name[i], 'amount': int(self.total[a])})

  #   self.repeating_panel_1.items = self.final
  # # def link_1_click(self, **event_args):
  # #   """This method is called when the link is clicked"""
  #   open_form('admin.dashboard.loan_management')

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management')
