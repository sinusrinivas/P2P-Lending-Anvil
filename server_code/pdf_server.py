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
    try:
        # Your PDF creation logic here
        print(f"Creating PDF for {name} with image {image_source}")
        pdf = anvil.pdf.render_form("bank_users.main_form.about_main_form",name, image_source)  # Replace with your actual PDF creation code
        return pdf
    except Exception as e:
        print(f"Error creating PDF: {e}")
        raise

