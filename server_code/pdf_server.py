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

# @anvil.server.callable
# def create_pdf(name, image_source,selected_row):
    
#     # Your PDF creation logic here
#     pdf = anvil.pdf.PDFRenderer(page_size='A4', orientation='landscape').render_form("lendor.dashboard.lender_portfolio",selected_row = selected_row)  
#     return pdf

@anvil.server.callable
def create_pdf(name, image_source, selected_row):
    # A4 size in points (width, height) is (595, 842), for landscape swap to (842, 595)
    landscape_a4 = (842, 595)
    
    # Create the PDF in landscape mode by specifying the size
    pdf = anvil.pdf.PDFRenderer(page_size=landscape_a4).render_form("lendor.dashboard.lender_portfolio", selected_row=selected_row)
    
    return pdf


@anvil.server.callable
def create_pdf1(name, image_source, selected_row):
    
    # Your PDF creation logic here
    pdf = anvil.pdf.PDFRenderer(page_size='A4', orientation='landscape').render_form("borrower.dashboard.borrower_portfolio", selected_row=selected_row)  
    return pdf

