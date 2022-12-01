"""
Functionality of Phonebook application:

Add new entries +
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program

The first argument to the application should be the name of the phonebook.
Application should load JSON data, if it is present in the folder with application, else raise an error.
After the user exits, all data should be saved to loaded JSON.
"""

import json


def phonebook(file_name):

    # try/except block will raise FileNotFoundError if file is not present in the folder with application
    try:
        with open(file_name) as read_file:
            content = read_file.read()
            # if json file is empty or type of data there is not dict => data_base will be assigned as empty dict
            if not content and content != '{}' and type(content) != dict:
                data_base = {}
            # if json file is non-empty dict => app will load its content (only once)
            else:
                read_file.seek(0)  # added to read file from beginning
                data_base = json.load(read_file)
    except FileNotFoundError:
        raise FileNotFoundError(f'{file_name} is not present in the folder with application')

    def add_record():
        while True:
            name = input('Enter full name: ')
            # app will take only first name and last name consisting of 1 word
            # 'cause code below will retrieve data using split method
            if len(name.split()) != 2:
                print('Please enter valid name. Like this - Ben Smith')
                add_record()
                break
            phone_number = input('Enter phone number: ')
            # title() will be used to unify data and for search to work no matter the case of input
            city = input('Enter city name: ').title()
            data_base[name.title()] = f'{phone_number} {city}'
            if input("Enter 'q' to exit to main menu or anything else to add new entry: ") == 'q':
                menu()
                break

    def exit_phonebook():
        # json file will be written once in the end of the app
        with open(file_name, 'w') as write_file:
            json.dump(data_base, write_file, indent=4, sort_keys=True)  # data will be sorted by keys
            print('Your phonebook was successfully updated. Goodbye!')

    def search_by_first_name():
        f_name = input('Enter first name: ').title()
        count = 0
        for k in data_base:
            if f_name == k.split()[0]:
                count += 1
                data = data_base[k].split()  # var 'data' added in order to split once per iteration
                phone = data[0]
                city = data[1]
                print(f'Full name: {k}, phone number: {phone}, city: {city}')
        if count == 0:
            print(f'First name {f_name} not found. Please try another one.')
        menu()

    def search_by_last_name():
        l_name = input('Enter last name: ').title()
        count = 0
        for k in data_base:
            if l_name == k.split()[1]:
                count += 1
                data = data_base[k].split()
                phone = data[0]
                city = data[1]
                print(f'Full name: {k}, phone number: {phone}, city: {city}')
        if count == 0:
            print(f'Last name {l_name} not found. Please try another one.')
        menu()

    def search_by_full_name():
        full_name = input('Enter full name: ').title()
        count = 0
        for k in data_base:
            if full_name == k:
                count += 1
                data = data_base[k].split()
                phone = data[0]
                city = data[1]
                print(f'Full name: {k}, phone number: {phone}, city: {city}')
        if count == 0:
            print(f'Name {full_name} not found. Please try another one.')
        menu()

    def search_by_phone_number():
        phone = input('Enter phone number: ')
        count = 0
        for k, v in data_base.items():
            if phone == v.split()[0]:
                count += 1
                city = data_base[k].split()[1]
                print(f'Full name: {k}, phone number: {phone}, city: {city}')
        if count == 0:
            print(f'Phone number {phone} not found. Please try another one.')
        menu()

    def search_by_city():
        city = input('Enter city: ').title()
        count = 0
        for k, v in data_base.items():
            if city == v.split()[1]:
                count += 1
                phone = data_base[k].split()[0]
                print(f'Full name: {k}, phone number: {phone}, city: {city}')
        if count == 0:
            print(f'City {city} not found. Please try another one.')
        menu()

    def del_by_phone():
        phone = input('Enter phone number to delete relevant record(s): ')
        records = []
        for k, v in data_base.items():
            if phone == v.split()[0]:
                records.append(k)
                print(f'Record of {k} with phone number {phone} was deleted from phonebook!')
        for record in records:
            del data_base[record]
        if not records:
            print(f'Phone number {phone} not found. Please try another one.')
        menu()

    def upd_by_phone():
        phone = input('Enter phone number to update relevant record(s): ')
        records = []
        for k, v in data_base.items():
            if phone == v.split()[0]:
                records.append(k)
        for record in records:
            info_upd = input(f'Enter new info about mr(s) {record} like "phone_number city": ').title()
            data_base[record] = info_upd
        if not records:
            print(f'Phone number {phone} not found. Please try another one.')
        menu()

    def print_phonebook():
        print('\n__full name: phone city__')
        for k, v in data_base.items():
            print(f'{k}: {v}')
        menu()

    def menu():

        action = input("""
Please choose what would you like to do. Enter 'help' to get all commands or 'exit' to stop this app.

Enter command here: """)

        # new solution wih dict
        actions = {'add': add_record,
                   'first': search_by_first_name,
                   'last': search_by_last_name,
                   'full': search_by_full_name,
                   's phone': search_by_phone_number,
                   'city': search_by_city,
                   'd phone': del_by_phone,
                   'print': print_phonebook,
                   'upd': upd_by_phone,
                   'help': menu_help,
                   'exit': exit_phonebook
                   }

        if action in actions:
            actions[action]()
        else:
            print(f'\n{action} is invalid! Please try again.')
            menu()

        # previous solution
        # if action == 'add':
        #     add_record()
        # elif action == 'first':
        #     search_by_first_name()
        # elif action == 'last':
        #     search_by_last_name()
        # elif action == 'full':
        #     search_by_full_name()
        # elif action == 's phone':
        #     search_by_phone_number()
        # elif action == 'city':
        #     search_by_city()
        # elif action == 'd phone':
        #     del_by_phone()
        # elif action == 'print':
        #     print_phonebook()
        # elif action == 'upd':
        #     upd_by_phone()
        # elif action == 'help':
        #     menu_help()
        # elif action == 'exit':
        #     exit_phonebook()
        # else:
        #     print(f'\n{action} is invalid! Please try again.')
        #     menu()

    def menu_help():
        print("""
    Enter:
    1) 'add' to add a new record;
    2) 'first' to search by first name; 
    3) 'last' to search by last name;
    4) 'full' to search by full name;
    5) 's phone' to search by phone number;
    6) 'city' to search by city; 
    7) 'd phone' to delete record by phone number;
    8) 'print' to print all current phonebook data;
    9) 'upd' to update a record for a given phone number;
    10) 'exit' to exit this app and save file.""")
        menu()

    menu_help()


phonebook(input('enter name of your phonebook: '))

