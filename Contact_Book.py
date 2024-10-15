################################################################################
##      Fundamental Operations
################################################################################

##      The dictionary

contact_book = {}

##      Methods to request info

def get_fname():
    return input('Enter contact first name: ')

def get_lname():
    return input('Enter contact last name: ')

def get_number():
    return input('Enter contact phone number: ')

def get_email():
    return input('Enter contact email: ')

##       Printers

def print_dict(dict):
    for key in dict.keys():
        print(f'{key}: {dict[key]}')

def print_contact_book(dict):
    for key in dict.keys():
        print(f'Entry: {key}')
        print_dict(dict[key])
        print(' ')

##      Create dictionary out of values

def make_dict(fname, lname, number, email):
    return {
        "First name":fname,
        "Last name":lname,
        "Phone number":number,
        "Email address":email
    }

##      Search and return contact book of results

def contact_search(query):
    search_results = {}
    results_qty = 0
    query = query.lower()
    for key, nested_dict in contact_book.items():
        if any(query in value.lower() for value in nested_dict.values()):
            results_qty += 1
            search_results[results_qty] = nested_dict
    print(f'\n< Found {results_qty} result(s) >\n')
    return search_results

def search_and_select_contact():
    query = input('Enter search query: ')
    results = contact_search(query)

    if not results:
        print('\n...No results found...\n')
        return None

    print_contact_book(results)

    try:
        selection = input('Enter contact number: ')
        selected_contact = results.get(int(selection))
        if selected_contact:
            return selected_contact
        else:
            print('\n...Invalid selection...\n')
            return None
    except ValueError:
        print('\n...Invalid input, please enter a number...\n')
        return None

################################################################################
##      1. Create contact
################################################################################

def create_contact():
    print('\n< Create new contact >')

    fname = get_fname()
    lname = get_lname()
    number = get_number()
    email = get_email()

    name = f'{fname} {lname}'

    dict = make_dict(fname, lname, number, email)

    if name not in contact_book.keys():
        contact_book[name] = dict
        print('\n< Contact created successfully! >\n')
        print_dict(dict)

    else:
        print('\n...Contact already exists...\n')

        print('Existing contact:')
        print_dict(contact_book[name])

        print('\nNew contact:')
        print_dict(dict)

        print('\nWould you like to update the existing contact?\n1 = yes\nAny key = no\n')

        choice = input()

        if choice == '1':
            contact_book[name] = dict
            print('\n< Success! >\n')

        else:
            print('\n...Returning to main menu...\n')

################################################################################
##      2. Search contact
################################################################################

def search_contact():
    query = input('\n< Search for a contact >\nEnter search query: ')

    print_contact_book(contact_search(query))

################################################################################
##      3. Update contact
################################################################################

def edit_contact(dict):
    print(f'Current first name = {dict["First name"]}...')
    fname = get_fname()
    print(f'Current last name = {dict["Last name"]}...')
    lname = get_lname()
    print(f'Current phone number = {dict["Phone number"]}...')
    number = get_number()
    print(f'Current email address = {dict["Email address"]}...')
    email = get_email()
    dict = make_dict(fname, lname, number, email)
    return dict
    

def modify_contact(old, new):
    name = f'{old['First name']} {old['Last name']}'
    del contact_book[name]
    new_name = f'{new['First name']} {new['Last name']}'
    contact_book[new_name] = new

def update_contact():
    print('\n< Search for a contact >\n<   update a contact   >\n')

    results = search_and_select_contact()

    if isinstance(results, dict):
        modified_contact = edit_contact(results)
        modify_contact(results, modified_contact)
        print('\n< Success! >\n')

    else:
        print('\n...Invalid selection...\n')

################################################################################
##      4. View all contacts
################################################################################

def view_all_contacts():
        print('\n< Current contact book entries >\n')
        print_contact_book(contact_book)

################################################################################
##      5. Delete contact
################################################################################

def delete_contact():
    print('\n< Search for a contact >\n<   delete a contact   >\n')

    results = search_and_select_contact()
    if isinstance(results, dict):
        name = f'{results['First name']} {results['Last name']}'
        del contact_book[name]
        print('\n< Success! >\n')
    else:
        print('\n...Invalid selection...\n')

################################################################################
##      Front end
################################################################################

def main_menu():
    options = {

        '1': create_contact,
        '2': search_contact,
        '3': update_contact,
        '4': view_all_contacts,
        '5': delete_contact,
        '6': lambda: print('...Thank you for using the contact book app...\n')
    }

    while True:

        print('''
        Please make a selection from the following:
        < 1 > Create a new contact
        < 2 > Search for a contact
        < 3 > Update an existing contact
        < 4 > View all contacts
        < 5 > Delete a contact
        < 6 > Exit contact app
        ''')
        selection = input()
        if selection in options:
            options[selection]()
            if selection == '6':
                break
        else:
            print('\n...Invalid selection...\n')

print('''
##############################################
##                                          ##
##                < Welcome >               ##
##                                          ##
##                  (>'-')>                 ##
##                                          ##
##          Contact book application        ##
##        Premium contact storage and       ##
##       management at your fingertips      ##
##                                          ##
##############################################''')

################################################################################
##      Initialize front end
################################################################################

main_menu()
