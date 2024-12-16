'''
    @Author:Ankitha
    @Date: 12-12-2024
    @Last Modified by: Ankitha
    @Last Modified time: 12-12-2024
    @Title : Address Book problem
'''
import re
import log
log = log.logger_init("Address Book")

class Contact:
    
    def __init__(self,first_name,last_name,address,city,state,zip,phone_num,email):
        """
            Description:
                Initializes an Contact object with persons details
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone_num
        self.email = email
        
    def __str__(self):
        """
        Description:
            Display Object in string representation
        """
        return (f"{self.first_name} {self.last_name},{self.address},{self.city},{self.state},{self.zip},{self.phone},{self.email}")


class AddressBook:
    def __init__(self):
        """
            Description:
                Initializes an Contact list 
        """
        self.contacts = {}
        
    def add_contacts(self,contact):
        """
            Description:
                Function to add new contact to contact book
            Parameters:
                contact = contact to add
            Return:
                It returns contact is added or not
        """
        contact_key = f"{contact.first_name,contact.last_name}"

        if contact_key not in self.contacts:
            self.contacts[contact_key] = contact
            log.info(self.contacts.keys())
            log.info(f"Contact {contact_key} added successfully.")
        else:
            log.info(f"Contact {contact_key} already exists in the address book.")

    
class AddressBookMain:
    def __init__(self):
        """
            Description:
                Initializes address book for list of contacts
        """
        self.address_book = AddressBook()

    def dispaly(self):
        """
            Description:
                Function is used to display welcome message 
        """
        print("Welcome to Address Book program in AddressBookMain class")
    
    def details_from_console(self):
        """
            Description:
                Function is used to get the details from the user
            Return:
                It returns contact object
        """
        self.first_name = input("Enter First Name :")
        try:
            match = re.search(r'^[A-Z][A-Za-z]{4,}$',self.first_name)
        except Exception:
            log.error("Please Enter correct first name..")
        
        self.last_name = input("Enter Last name :")
        try:
            match = re.search(r'^[A-Z]\s?[A-Za-z]{2,}$',self.last_name)
        except Exception:
            log.error("Please Enter correct last name..")
            
        self.address = input("Enter your Address :")
        try:
            match = re.search(r'^\w*$',self.address)
        except Exception:
            log.error("Please Enter correct Address..")
            
        self.city = input("Enter your city :")
        try:
            match = re.search(r'^[A-Za-z]{4,}$',self.city)
        except Exception:
            log.error("Please Enter correct city..")
        
        self.state = input("Enter your state :")
        try:
            match = re.search(r'^[A-Za-z]{3,}$',self.state)
        except Exception:
            log.error("Please Enter correct State..")
        self.zip = input("Enter your pin code :")
        try:
            match = re.search(r'^[1-9][0-9]{5}$',self.zip)
        except Exception:
            log.error("Please Enter correct pincode..")
            
        self.phone_num = input("Enter phone number :")
        try:
            match = re.search(r'^[0-9]{10}$',self.phone_num)
        except Exception:
            log.error("Please Enter correct pincode..")
            
        self.email = input("Enter your email address :")
        try:
            match = re.search('^\[a-zA-Z0-9. _%+-]+@\[a-zA-Z0-9. -]+\. \[a-zA-Z\]{2,}$',self.email)
        except Exception:
            log.error("Please enter correct email Id")
            
        contact = Contact(self.first_name,self.last_name,self.address,self.city,self.state,self.zip,self.phone_num,self.email)
        self.address_book.add_contacts(contact)
        
    def run(self):
        n=1
        while n<5:
            print("------Address Book------")
            print("1.Add New contact")
            
            choice =  int(input("Input your choice: "))
            
            if choice == 1:
                self.details_from_console()
            else:
                print("Invalid choice..")
        n += 1        
if __name__=="__main__":
    address_main = AddressBookMain()
    address_main.dispaly()
    address_main.run()