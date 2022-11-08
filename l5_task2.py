def birthday_greeting():
    name = input('Enter your name: ')
    # age should be converted to an int type in order not to
    age = int(input('Enter your age: '))
    print(f'Hello {name}, on your next birthday you\'ll be {age + 1} years')


birthday_greeting()
