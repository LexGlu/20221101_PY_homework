"""
LESSON 7
"""

"""
Task 1.
Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
and the number of occurrences as values. 
"""


def occurrences():
    sentence = input('Task 1. Enter your sentence: ').lower()

    # __code for unique SYMBOLS__
    # unique_symbols = set(sentence)
    # res = {i: sentence.count(i) for i in unique_symbols}

    # __code for unique WORDS__
    words = sentence.split()

    # __code for unique WORDS and to keep only letters and digits__
    # raw_words = sentence.split()
    # words = []
    # for word in raw_words:
    #     if not word.isalnum():
    #         word = "".join(i for i in word if i.isalnum())
    #     if word:  # won't add empty elements
    #         words.append(word)

    res = {i: words.count(i) for i in set(words)}

    print(f'Task 1. Dict containing all unique words as keys and the number of occurrences as values: {res}')


"""
Task 2.
Compute the total price of the stock where the total price is the sum of the price of an item multiplied
by the quantity of this exact item. 
"""


def stock_sum():

    #  input data
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15,
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    total_stock = 0

    for item, quantity in stock.items():
        if prices.get(item):  # checks if 2 dicts don't have different keys (in order not to crush)
            total_stock += quantity * prices[item]

    print(f'Task 2. Total price of the stock: {total_stock}')


"""
Task 3.
List comprehension exercise
Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j`
is corresponding to `i` squared.
"""


def lst_comprehension():
    res = [(i, i * i) for i in range(1, 11)]
    print(f'Task 3. Resulting list with tuples: {res}')


occurrences()
stock_sum()
lst_comprehension()
