phonebook = {}

while True:
    contact_info = input()

    if contact_info.isdigit():
        for _ in range(int(contact_info)):
            contact = input()
            if contact in phonebook:
                print(f'{contact} -> {phonebook[contact]}')
            else:
                print(f'Contact {contact} does not exist.')
        break
    
    contact_name, contact_number = contact_info.split("-")

    phonebook[contact_name] = contact_number #creates or updates phone number
