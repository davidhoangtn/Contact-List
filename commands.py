from support_functions import verify_email_address, verify_phone_number, read_contacts, write_contacts
ERROR_MESSAGE = "You entered invalid information, this contact was not added."
CONTACT_FILE_PATH = "contacts.json"

def add_contact(contacts):
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    if contacts:
        for contact in contacts:
            if contact['first_name'] == first_name and contact['last_name'] == last_name:
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
    if not email:
        pass 
    elif not verify_email_address(email):
        print("Invalid email address.")
        print(ERROR_MESSAGE)
        return 

    address = input("Address: ")
    print("Contact Added!")
    contacts.append({'first_name': first_name, "last_name": last_name, "mobile": mobile_num, "home": home_num, "email": email, "address": address})
    write_contacts(CONTACT_FILE_PATH, contacts)


def search_for_contact(contacts):    
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    matches = []
    for contact in contacts:
        if first_name in contact["first_name"].lower() or not first_name and last_name in contact["last_name"].lower() or not last_name:
            matches.append(contact)
    print(f"Found {len(matches)} matching contacts")            
    for idx, match in enumerate(matches):
            idx += 1
            first_name = match["first_name"]
            last_name = match["last_name"]
            mobile = match["mobile"]
            email = match["email"]
            address = match["address"]
            print(f"{idx}. {first_name} {last_name}")
            if mobile:
                print(f"\tMobile: {mobile}")
            
            if email:
                print(f"\tEmail: {email}")
            
            if address:
                print(f"\tAddress: {address}.")


def delete_contact(contacts):
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    for contact in contacts:
        if first_name.strip() == contact["first_name"] and last_name.strip() == contact["last_name"]:
            confirm_del = input("Are you sure you would like to delete this contact (y/n)? ")
            if confirm_del == "y":
                contacts.remove(contact)
                write_contacts(CONTACT_FILE_PATH, contacts)
                print("Contact deleted!")
                return
            else:
                return
        else:
            continue
    print("No contact with this name exists")
    return


def list_contacts(contacts):   
    if not contacts:
        print("There is no saved contacts")
    else:
        for idx, contact in enumerate(contacts):
            idx += 1
            first_name = contact["first_name"]
            last_name = contact["last_name"]
            mobile = contact["mobile"]
            email = contact["email"]
            print(f"{idx}. {first_name} {last_name}\n\tMobile: {mobile}\n\tEmail: {email}")
