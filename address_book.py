'''
    @Author:Ankitha
    @Date: 12-12-2024
    @Last Modified by: Ankitha
    @Last Modified time: 17-12-2024
    @Title : Address Book problem
'''
import log
import os
log = log.logger_init("Address Book")

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.address},{self.city},{self.state},{self.zip_code},{self.phone},{self.email}"

    @staticmethod
    def from_string(data):
        details = data.strip().split(',')
        if len(details) == 8:
            return Contact(details[0], details[1], details[2], details[3], details[4], details[5], details[6],details[7])
        else:
            print(f"Skipping malformed line: {data.strip()}")
            log.info(f"Skipping malformed line: {data.strip()}")
            return None

class AddressBook:
    def __init__(self):
        self.contacts = {}
        self.city_dict = {}
        self.state_dict = {}

    def add_contact(self, contact):
        key = f"{contact.first_name} {contact.last_name}".lower()
        if key not in self.contacts:
            self.contacts[key] = contact
            log.info(f"Contact {key} added successfully.")
            print(f"Contact {contact.first_name} {contact.last_name} added successfully.")

            if contact.city.lower() not in self.city_dict:
                self.city_dict[contact.city.lower()] = []
            self.city_dict[contact.city.lower()].append(contact)

            if contact.state.lower() not in self.state_dict:
                self.state_dict[contact.state.lower()] = []
            self.state_dict[contact.state.lower()].append(contact)

        else:
            log.info(f"Contact {key} already exists in the address book.")
            print(f"Contact {contact.first_name} {contact.last_name} already exists in the address book.")

    def edit_contact(self, f_name, l_name):
        key = f"{f_name} {l_name}".lower()
        if key not in self.contacts:
            log.info(f"{key} not found in Contacts")
            print(f"Contact {f_name} {l_name} not found in the address book.")
        else:
            print("Enter the new details for the contact:")
            self.contacts[key].address = input("Enter new address: ")
            self.contacts[key].city = input("Enter new city: ")
            self.contacts[key].state = input("Enter new state: ")
            self.contacts[key].zip_code = input("Enter new zipcode: ")
            self.contacts[key].phone = input("Enter new phone number: ")
            self.contacts[key].email = input("Enter new email: ")
            log.info(f"Contact {key} updated successfully.")
            print(f"Contact {f_name} {l_name} updated successfully.")

    def delete_contact(self, first_name, last_name):
        key = f"{first_name} {last_name}".lower()
        if key in self.contacts:
            contact = self.contacts[key]
            del self.contacts[key]
            log.info(f"Contact {key} deleted successfully.")
            print(f"Contact {first_name} {last_name} deleted successfully.")

            if contact.city.lower() in self.city_dict:
                self.city_dict[contact.city.lower()].remove(contact)
                if not self.city_dict[contact.city.lower()]:
                    del self.city_dict[contact.city.lower()]

            if contact.state.lower() in self.state_dict:
                self.state_dict[contact.state.lower()].remove(contact)
                if not self.state_dict[contact.state.lower()]:
                    del self.state_dict[contact.state.lower()]
        else:
            log.info(f"Contact {key} not found in the address book.")
            print(f"Contact {first_name} {last_name} not found in the address book.")

    def search_by_city_or_state(self, city_name=None, state_name=None):
        found_contacts = []
        if city_name:
            city_name = city_name.lower()
            if city_name in self.city_dict:
                found_contacts = self.city_dict[city_name]
        
        if state_name:
            state_name = state_name.lower()
            if state_name in self.state_dict:
                found_contacts += self.state_dict[state_name]
        
        return found_contacts
    
    def number_of_persons(self, city_name=None, state_name=None):
        city_count = 0
        state_count = 0

        if city_name:
            city_name = city_name.lower()
            if city_name in self.city_dict:
                city_count = len(self.city_dict[city_name])
        
        if state_name:
            state_name = state_name.lower()
            if state_name in self.state_dict:
                state_count = len(self.state_dict[state_name])

        print(f"Number of contacts in city '{city_name}': {city_count}")
        print(f"Number of contacts in state '{state_name}': {state_count}")
        
    def sort_names(self):
        if not self.contacts:
            log.info("No contacts to sort in the address book.")
            print("No contacts to sort.")
            return
            
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: (c.first_name.lower(), c.last_name.lower()))

        log.info("Contacts sorted successfully.")
        print("\nContacts sorted alphabetically by name:")
        for contact in sorted_contacts:
            print(contact)
                
    def sort_contacts(self, sort_by):
        if not self.contacts:
            log.info("No contacts to sort.")
            print("No contacts to sort.")
            return

        if sort_by == "city":
            sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.city.lower())
            log.info("Contacts sorted by City.")
            print("\nContacts Sorted by City:")
        elif sort_by == "state":
            sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.state.lower())
            log.info("Contacts sorted by State.")
            print("\nContacts Sorted by State:")
        elif sort_by == "zip":
            sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.zip_code)
            log.info("Contacts sorted by Zip Code.")
            print("\nContacts Sorted by Zip Code:")
        else:
            print("Invalid sorting parameter. Choose city, state, or zip.")
            return

        for contact in sorted_contacts:
            print(contact)
            
    def save_to_file(self, file_name):
        with open(file_name, 'a') as file:
            for contact in self.contacts.values():
                file.write(str(contact) + '\n')
        print(f"All contacts have been saved to {file_name}")
        log.info(f"Contacts saved to file {file_name}.")

    def load_from_file(self, file_name):
        if not os.path.exists(file_name):
            print(f"File '{file_name}' does not exist.")
            return
        with open(file_name, 'r') as file:
            for line in file:
                contact = Contact.from_string(line)
                if contact:  
                    self.add_contact(contact)
        log.info(f"Contacts loaded from file {file_name}.")

        
    def display_contacts(self):
        if self.contacts:
            print("\nContacts in Address Book:")
            for contact in self.contacts.values():
                log.info(contact)
                print(contact)
        else:
            log.info("No contacts in the address book.")
            print("No contacts in the address book.")

class AddressBookMain:
    def __init__(self):
        self.address_books = {}

    def display(self):
        print("Welcome to Address Book Problem")
        
    def create_address_book(self):
        book_name = input("Enter the name for the new Address Book: ")
        if book_name.lower() not in self.address_books:
            self.address_books[book_name.lower()] = AddressBook()
            log.info(f"New Address Book '{book_name}' created successfully.")
            print(f"New Address Book '{book_name}' created successfully.")
        else:
            log.info(f"Address Book '{book_name}' already exists.")
            print(f"Address Book '{book_name}' already exists.")

    def select_address_book(self):
        print("\nAvailable Address Books:")
        for name in self.address_books:
            print(f"{name}")
        book_name = input("Enter the name of the Address Book you want to manage: ").lower()
        if book_name in self.address_books:
            return self.address_books[book_name]
        else:
            log.info(f"Address Book '{book_name}' does not exist.")
            print(f"Address Book '{book_name}' does not exist.")
            return None

    def add_contact_from_console(self, address_book):
        print("Enter the following contact details:")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        zip_code = input("Zip Code: ")
        phone = input("Phone Number: ")
        email = input("Email: ")

        contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        address_book.add_contact(contact)

    def edit_contact_from_console(self, address_book):
        print("Enter the following details to edit a contact: ")
        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        address_book.edit_contact(f_name, l_name)

    def delete_contact_main(self, address_book):
        f_name = input("Enter First Name: ")
        l_name = input("Enter Last Name: ")
        address_book.delete_contact(f_name, l_name)
        
    def city_or_state_search(self, address_book):
        print("Search by: ")
        print("1. City")
        print("2. State")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            city_name = input("Enter City Name to search: ")
            found_contacts = address_book.search_by_city_or_state(city_name=city_name)
            if found_contacts:
                print(f"\n{len(found_contacts)} Contacts found in the city '{city_name}':")
                for contact in found_contacts:
                    print(contact)
            else:
                print(f"No contacts found in city {city_name}.")
                
        elif choice == "2":
            state_name = input("Enter State Name to search: ")
            found_contacts = address_book.search_by_city_or_state(state_name=state_name)
            if found_contacts:
                print(f"\n{len(found_contacts)} Contacts found in the state '{state_name}':")
                for contact in found_contacts:
                    print(contact)
            else:
                print(f"No contacts found in state {state_name}.")
        else:
            print("Invalid choice.")
            
    def count_city_or_states(self, address_book):
        print("1. Count by City")
        print("2. Count by State")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            city_name = input("Enter city name to count: ")
            address_book.number_of_persons(city_name=city_name)
        elif choice == "2":
            state_name = input("Enter state name to count: ")
            address_book.number_of_persons(state_name=state_name)
        else:
            print("Invalid choice.")
            
    def sort_contacts_menu(self, address_book):
        print("\nSort Contacts By:")
        print("1. City")
        print("2. State")
        print("3. Zip Code")
        choice = input("Enter your choice : ")

        if choice == "1":
            address_book.sort_contacts("city")
        elif choice == "2":
            address_book.sort_contacts("state")
        elif choice == "3":
            address_book.sort_contacts("zip")
        else:
            print("Invalid choice. Please try again.")
            
    def run(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Create New Address Book")
            print("2. Select Address Book")
            print("3. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_address_book()
            elif choice == "2":
                selected_address_book = self.select_address_book()
                if selected_address_book:
                    self.manage_address_book(selected_address_book)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_address_book(self, address_book):
        while True:
            print("\n--- Address Book Menu ---")
            print("1. Add New Contact")
            print("2. Edit Contact")
            print("3. Delete Contact")
            print("4. Search by City or State")
            print("5. Count Contacts by City or State")
            print("6. Sort Contacts by Name")
            print("7. sort by city or state or zip")
            print("8. Save Contacts to File")
            print("9. Load Contacts from File")
            print("10. Display Contacts")
            print("11. Exit to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact_from_console(address_book)
            elif choice == "2":
                self.edit_contact_from_console(address_book)
            elif choice == "3":
                self.delete_contact_main(address_book)
            elif choice == "4":
                self.city_or_state_search(address_book)
            elif choice == "5":
                self.count_city_or_states(address_book)
            elif choice == "6":
                address_book.sort_names() 
            elif choice == "7":
                self.sort_contacts_menu(address_book)
            elif choice == "8":
                file_name = input("Enter the file name to save contacts: ")
                address_book.save_to_file(file_name)
            elif choice == "9":
                file_name = input("Enter the file name to load contacts: ")
                address_book.load_from_file(file_name)
            elif choice == "10":
                address_book.display_contacts() 
            elif choice == "11":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    address_main = AddressBookMain()
    address_main.display()
    address_main.run()
