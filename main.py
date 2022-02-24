import json
import sys

from sympy import continued_fraction_convergents

def read_contacts(file_path):
    try:
        with open(file_path, 'r') as f:
            contacts = json.load(f)['contacts']
    except FileNotFoundError:
        contacts = []

    return contacts

def write_contacts(file_path, contacts):
    with open(file_path, 'w') as f:
        contacts = {"contacts": contacts}
        json.dump(contacts, f)


def verify_email_address(email):
    if "@" not in email:
        return False

    split_email = email.split("@")
    identifier = "".join(split_email[:-1])
    domain = split_email[-1]

    if len(identifier) < 1:
        return False

    if "." not in domain:
        return False

    split_domain = domain.split(".")

    for section in split_domain:
        if len(section) == 0:
            return False

    return True

def verify_phone_number(phone_number):
    test_phone_number = phone_number.replace('-', '').replace(" ", "").replace("(", '').replace(")", "")
    if len(test_phone_number) == 10:
        return True
    else: 
        return False


def add_contact(contacts):
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    if contacts:
        for contact in contacts:
            if contact['first name'] == first_name or contact['last_name'] == last_name:
                print("A contact with this name already exists.")
                print(ERROR_MESSAGE)
                return 
    mobile_num = input("Mobile Phone Number: ")
    if not verify_phone_number(mobile_num):
        print("Invalid mobile phone number.")
        print(ERROR_MESSAGE)
        return 
    home_num = input("Home Phone Number: ")
    email = input("Email Address: ")
    if not verify_email_address(email):
        print("Invalid email address.")
        print(ERROR_MESSAGE)
        return 
    address = input("Address: ")
    print("Contact Added!")
    contacts.append({'first_name': first_name, "last_name": last_name, "mobile": mobile_num, "home": home_num, "email": email, "address": address})
    write_contacts(CONTACT_FILE_PATH, contacts)

def search_for_contact(contacts):
    pass


def delete_contact(contacts):
    pass


def list_contacts(contacts):
    
    pass


CONTACT_FILE_PATH = "contacts.json"
WELCOME_MESSAGE = """Welcome to your contact list!\nThe following is a list of useable commands:\n"add": Adds a contact.\n"delete": Deletes a contact.\n"list": Lists all contacts.\n"search": Searches for a contact by name.\n"q": Quits the program and saves the contact list."""
CONTACTS = read_contacts(CONTACT_FILE_PATH)
ERROR_MESSAGE = "You entered invalid information, this contact was not added."

def main(contacts_path):
    print(WELCOME_MESSAGE)
    command = input("Type a command: ")
    while command != 'q':
        if command.lower() == "add":
            add_contact(CONTACTS)
            command = input("Type a command: ")
        elif command.lower() == "delete":         
            delete_contact(CONTACTS)
            command = input("Type a command: ")
        elif command.lower() == "list":
            list_contacts(CONTACTS)
            command = input("Type a command: ")
        elif command.lower() == "search":
            search_for_contact(CONTACTS) 
            command = input("Type a command: ")
        else:
            print(f'"{command}" is not a valid command. Please try again')
            command = input("Type a command: ")
    if command == 'q':
        print("Contacts were saved successfully.")
        sys.exit()

if __name__ == "__main__":
    main(CONTACT_FILE_PATH)
    

