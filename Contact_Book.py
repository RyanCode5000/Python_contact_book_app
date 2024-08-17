################################################################################
##      Fundamental Operations
################################################################################

##      The dictionary

contact_book = {}

##      Methods to request info

def get_fname():
    print('Enter contact first name:')
    fname = input()
    return fname

def get_lname():
    print('Enter contact last name:')
    lname = input()
    return lname

def get_number():
    print('Enter contact phone number:')
    number = input()
    return number

def get_email():
    print('Enter contact email:')
    email = input()
    return email

##       Printers

def print_dict(dict):
    for key in dict.keys():
        print(key + ': ' + dict[key])

def print_contact_book(dict):
    for key in dict.keys():
        print('Entry: ' + str(key))
        print_dict(dict[key])
        print(' ')

##      Create dictionary out of values

def make_dict(fname, lname, number, email):
    dict = {
        "First name":fname,
        "Last name":lname,
        "Phone number":number,
        "Email address":email
    }
    return dict

##      Search and return contact book of results

def contact_search(query):
    search_results = {}
    results_qty = 0
    for key in contact_book:
        for nest_key in contact_book[key]:
            if contact_book[key][nest_key] == query:
                results_qty = results_qty + 1
                search_results[results_qty] = contact_book[key]
    print('\n< Found ' + str(results_qty) + ' result(s) >\n')
    return search_results

################################################################################
##      1. Create contact
################################################################################

def create_contact():
    print('\n< Create new contact >')

    fname = get_fname()
    lname = get_lname()
    number = get_number()
    email = get_email()

    name = fname + ' ' + lname

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
    print('\n< Search for a contact >\nEnter search query:')

    query = input()

    results = contact_search(query)

    print_contact_book(results)

################################################################################
##      3. Update contact
################################################################################

def modify_contact(name, dict):
    print('Current first name = ' + dict["First name"] + '...')
    fname = get_fname()
    print('Current last name = ' + dict["Last name"] + '...')
    lname = get_lname()
    print('Current phone number = ' + dict["Phone number"] + '...')
    number = get_number()
    print('Current email address = ' + dict["Email address"] + '...')
    email = get_email()
    dict = make_dict(fname, lname, number, email)
    contact_book[name] = dict

def update_contact():
    print('\n< Search for a contact >\n<   update a contact   >\nEnter search query:')

    query = input()

    results = contact_search(query)

    print_contact_book(results)

    print('\n< Select a contact to update >\nEnter entry number:')
    selection = input()
    selection = int(selection)
    if selection in results.keys():
        dict = results[selection]
        name = dict['First name'] + ' ' + dict['Last name']
        modify_contact(name, dict)
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
    print('\n< Search for a contact >\n<   delete a contact   >\nEnter search query:')

    query = input()

    results = contact_search(query)

    print_contact_book(results)

    print('< Select a contact to delete >\nEnter entry number:')
    selection = input()
    selection = int(selection)
    if selection in results.keys():
        dict = results[selection]
        name = dict['First name'] + ' ' + dict['Last name']
        del contact_book[name]
        print('\n< Success! >\n')
    else:
        print('\n...Invalid selection...\n')

################################################################################
##      Front end
################################################################################

def front_end():
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
    selection = str(selection)
    if selection == '1':
        create_contact()
        front_end()
    elif selection == '2':
        search_contact()
        front_end()
    elif selection == '3':
        update_contact()
        front_end()
    elif selection == '4':
        view_all_contacts()
        front_end()
    elif selection == '5':
        delete_contact()
        front_end()
    elif selection == '6':
        print('< Thank you for using the contact app >')
    else:
        print('\n...Invalid selection...\n')
        front_end()
    
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

front_end()