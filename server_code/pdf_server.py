import anvil.secrets
import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.pdf

@anvil.server.callable
def create_pdf(name, image_source):
    
    # Your PDF creation logic here
    pdf = anvil.pdf.PDFRenderer(page_size='A4').render_form("bank_users.main_form.about_main_form")  # Replace with your actual PDF creation code
    return pdf
    

@anvil.server.callable
def create_pdf1(name, image_source):
    
    # Your PDF creation logic here
    pdf = anvil.pdf.PDFRenderer(page_size='A4').render_form("borrower.dashboard.borrower_portfolio")  # Replace with your actual PDF creation code
    return pdf
