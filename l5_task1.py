import random


def guessing_game():
    res = random.randint(1, 10)
    x = input('Enter number between 1 and 10\n')
    # input should be converted to an int type before comparing with random int
    print(f'Wow, you guessed it! It was really {res}!') if res == int(x) else print(f'Nope, it was {res}.')


guessing_game()
