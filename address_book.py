'''
    @Author:Ankitha
    @Date: 12-12-2024
    @Last Modified by: Ankitha
    @Last Modified time: 12-12-2024
    @Title : Address Book problem
'''
import log
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
        return (f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone}, {self.email}")

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        key = f"{contact.first_name} {contact.last_name}"
        if key not in self.contacts:
            self.contacts[key] = contact
            log.info(self.contacts.items())
            log.info(f"Contact {key} added successfully.")
        else:
            log.info(f"Contact {key} already exists in the address book.")
    
    def edit_contact(self, f_name, l_name):
        key = f"{f_name} {l_name}"
        if key not in self.contacts:
            log.info(f"{key} not found in Contacts")
        else:
            self.contacts[key].address = input("Enter new address: ")
            self.contacts[key].city = input("Enter new city: ")
            self.contacts[key].state = input("Enter new state: ")
            self.contacts[key].zip_code = input("Enter new zipcode: ")
            self.contacts[key].phone = input("Enter new phone number: ")
            self.contacts[key].email = input("Enter new email: ")
            
    def delete_contact(self,first_name,last_name):
        key = f"{first_name} {last_name}"
        if key in self.contacts:
            del self.contacts[key]
        else:
            print(f"{key} is not present in contact book ")

    def display_contacts(self):
        if self.contacts:
            for contact in self.contacts.values():
                log.info(contact)
        else:
            log.info("No contacts in the address book.")

    
class AddressBookMain:
    def __init__(self):
        self.address_book = AddressBook()
        
    def diaply(self):
        print("Welcome to Address Book Problem")

    def add_contact_from_console(self):
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
        self.address_book.add_contact(contact)

    def edit_contact_from_console(self):
        print("Enter the Following Details: ")

        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")

        self.address_book.edit_contact(f_name,l_name)
        
    def delete_contact_main(self):
        f_name = input("Enter First Name:")
        l_name  = input("Enter Last Name:")
        
        self.address_book.delete_contact(f_name,l_name)
        
    def run(self):
        n = int(input("Enter Number of Contacts to Add :"))
        i = 1
        while i <= n:
            print("\n--- Address Book ---")
            print("1. Add New Contact")
            print("2. Edit Contact")
            print("3. Delete Contact")
            print("6. Display Contact")
            print("7.Exit")
    
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact_from_console()
            elif choice == "2":
                self.edit_contact_from_console()
            elif choice == "3":
                self.delete_contact_main()
            elif choice == "6":
                self.address_book.display_contacts()
            elif choice =="7":
                break
            else:
                print("Invalid choice. Please try again.")
            i += 1

if __name__=="__main__":
    address_main = AddressBookMain()
    address_main.run()