def valid_number():
    phone_number = input('Please, enter your phone number\n')
    digit_error = not phone_number.isdigit()
    length_error = len(phone_number) != 10
    if not digit_error and not length_error:
        print('Congratulations, your phone number is VALID!')
    else:
        print(f'Oopsie, your phone number is INVALID!')
        valid_number()


valid_number()
