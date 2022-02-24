import json
import sys
from commands import add_contact, search_for_contact, delete_contact, list_contacts
from support_functions import read_contacts

CONTACT_FILE_PATH = "contacts.json"
WELCOME_MESSAGE = """Welcome to your contact list!\nThe following is a list of useable commands:\n"add": Adds a contact.\n"delete": Deletes a contact.\n"list": Lists all contacts.\n"search": Searches for a contact by name.\n"q": Quits the program and saves the contact list."""
CONTACTS = read_contacts(CONTACT_FILE_PATH)

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
    

