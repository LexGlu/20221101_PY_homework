def valid_number():
    phone_number = input('Please, enter your phone number\n')
    if phone_number.isdigit() and len(phone_number) == 10:
        print('Congratulations, your phone number is VALID!')
    else:
        print(f'Oopsie, your phone number is INVALID!')
        valid_number()


valid_number()
