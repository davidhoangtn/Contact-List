ERROR_MESSAGE = "You entered invalid information, this contact was not added."

def add_contact(contacts):
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    if contacts:
        for contact in contacts:
            if contact['first_name'] == first_name or contact['last_name'] == last_name:
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
    for idx, contact in enumerate(contacts):
        idx += 1
        first_name = contact["first_name"]
        last_name = contact["last_name"]
        mobile = contact["mobile"]
        email = contact["email"]
        print(f"{idx}. {first_name} {last_name}\n\tMobile: {mobile}\n\tEmail: {email}")
