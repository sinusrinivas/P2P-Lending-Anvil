from ._anvil_designer import all_detailsTemplate
from anvil import *
import anvil.server
import anvil.http  # Importing anvil.http for making HTTP requests
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import math  # Importing math for distance calculations

class all_details(all_detailsTemplate):
    def __init__(self, selected_row, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.selected_row = selected_row

        # Populate form fields with selected_row data
        self.borrower_id.text = f"{selected_row['borrower_customer_id']}"
        self.loan_id.text = f"{selected_row['loan_id']}"
        self.borrower_full_name.text = f"{selected_row['borrower_full_name']}"
        self.borrower_email.text = f"{selected_row['borrower_email_id']}"
        self.customer_address.text = f"{selected_row['street_adress_1']}"
        self.product_name.text = f"{selected_row['product_name']}"
        self.relative_name.text = f"{selected_row['guarantor_name']}"
        self.relative_relation.text = f"{selected_row['another_person']}"
        self.relative_number.text = f"{selected_row['guarantor_mobile_no']}"
        self.another_email.text = f"{selected_row['another_email']}"
        self.relative_address.text = f"{selected_row['guarantor_address']}"
        self.emi_number.text = f"{selected_row['emi_number']}"
        self.remaining_amount.text = f"{selected_row['total_remaining_amount']}"
        self.status.text = f"{selected_row['status']}"
        self.customer_address_2.text = f"{selected_row['street_adress_2']}"

        # Print all details to the console
        print("Borrower ID:", self.borrower_id.text)
        print("Loan ID:", self.loan_id.text)
        print("Borrower Full Name:", self.borrower_full_name.text)
        print("Borrower Email:", self.borrower_email.text)
        print("Customer Address:", self.customer_address.text)
        print("Product Name:", self.product_name.text)
        print("Relative Name:", self.relative_name.text)
        print("Relative Relation:", self.relative_relation.text)
        print("Relative Number:", self.relative_number.text)
        print("Another Email:", self.another_email.text)
        print("Relative Address:", self.relative_address.text)
        print("EMI Number:", self.emi_number.text)
        print("Remaining Amount:", self.remaining_amount.text)
        print("Status:", self.status.text)
        print("Customer Address 2:", self.customer_address_2.text)

        # Find nearest field engineer and populate dropdown
        self.find_nearest_field_engineer()

        # # Set the event handler for the dropdown
        # self.nearest_engineer_dropdown.set_event_handler('change', self.dropdown_change)

    def get_coordinates(self, address):
        # Call Nominatim API to get coordinates
        response = anvil.http.request(
            f"https://nominatim.openstreetmap.org/search?format=json&q={address}",
            method="GET",
            json=True  # Ensures the response is parsed as JSON
        )
        if response:
            location = response[0]
            print(f"Address: {address}, Coordinates: ({location['lat']}, {location['lon']})")
            return (float(location['lat']), float(location['lon']))
        else:
            print(f"Address: {address}, Coordinates: Not Found")
            return (0, 0)  # Default to (0, 0) if no results found

    def calculate_distance(self, coord1, coord2):
        # Function to calculate distance between two coordinates using Haversine formula
        lat1, lon1 = coord1
        lat2, lon2 = coord2

        # Haversine formula
        R = 6371  # Radius of the Earth in kilometers
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c

        print(f"Distance between {coord1} and {coord2}: {distance} km")
        return distance

    def find_nearest_field_engineer(self):
        customer_address = self.selected_row['street_adress_1']
        customer_coordinates = self.get_coordinates(customer_address)

        field_engineers = app_tables.fin_field_engineers.search()
        nearest_engineer = None
        shortest_distance = float('inf')

        for engineer in field_engineers:
            engineer_address = engineer['address']
            engineer_coordinates = self.get_coordinates(engineer_address)

            distance = self.calculate_distance(customer_coordinates, engineer_coordinates)
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_engineer = engineer

        if nearest_engineer:
            print(f"Nearest Engineer: {nearest_engineer['full_name']}, Distance: {shortest_distance} km")
            self.nearest_engineer_dropdown.items = [(nearest_engineer['full_name'], nearest_engineer['field_engineer_id'])]

    # def nearest_engineer_dropdown_change(self, **event_args):
    #     """This method is called when the dropdown selection changes"""
    #     selected_id = self.nearest_engineer_dropdown.selected_value
    #     if selected_id:
    #         engineer = app_tables.fin_field_engineers.get_by_id(selected_id)
    #         if engineer:
    #             engineer_address = engineer['address']
    #             engineer_coordinates = self.get_coordinates(engineer_address)
    #             self.show_location_on_map(engineer_coordinates)

    # def show_location_on_map(self, coordinates):
    #     """Show the selected location on the map"""
    #     lat, lon = coordinates
    #     self.map_1.center = [lat, lon]
    #     self.map_1.zoom = 15  # Set appropriate zoom level
    #     self.map_1.add_component(MapMarker(lat, lon))

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('admin.dashboard.loan_servicing.handle_collection_process')

