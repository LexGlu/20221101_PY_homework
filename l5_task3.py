import random

'''
TASK
Create a program that reads an input string
and then creates and prints 5 random strings
from characters of the input string.

For example, the program obtained the word ‘hello’, 
so it should print 5 random strings(words)
that combine characters 
'''


def words_combination():
    word = input('Enter your word: ')

    # loop that creates and prints 5 random strings
    i = 0
    while i < 5:
        # x is an empty string that will be added with random chars from the input
        # temp_word is used to delete already randomly used chars
        x = ''
        temp_word = word

        # this loop ensures that output consists of exact same chars as input
        # e.g. so that from 'hello' we will not get 'lllll', 'hheee' etc
        while temp_word != '':
            char = random.choice(temp_word)
            x += char
            temp_word = temp_word.replace(char, '', 1)

        i += 1
        print(x)


words_combination()
