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
    def __init__(self,first_name,last_name,address,city,state,zip,phone_num,email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone_num
        self.email = email
        
    def __str__(self):
        return (f"{self.first_name} {self.last_name},{self.address},{self.city},{self.state},{self.zip},{self.phone},{self.email}")
        
class AddressBookMain:
    def dispaly(self):
        print("Welcome to Address Book program in AddressBookMain class")
    
    def details_from_console(self):
        self.first_name = input("Enter First Name :")
        self.last_name = input("Enter Last name :")
        self.address = input("Enter your Address :")
        self.city = input("Enter your city :")
        self.state = input("Enter your state :")
        self.zip = int(input("Enter your pin code :"))
        self.phone_num = int(input("Enter phone number :"))
        self.email = input("Enter your email address :")
        
        contact = Contact(self.first_name,self.last_name,self.address,self.city,self.state,self.zip,self.phone_num,self.email)
        print(contact)
        
address_book_obj = AddressBookMain()
address_book_obj.dispaly()
address_book_obj.details_from_console()