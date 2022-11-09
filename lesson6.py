import random

"""
Task 1. The greatest number
Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
"""


def greatest_number():
    random_list = []
    i = 0
    while i < 10:
        random_list.append(random.randint(0, 100))
        i += 1
    print(f"""
TASK 1 
Randomly generated list: {random_list} with length {len(random_list)}
Largest number in this list is {max(random_list)}
    """)


"""
Task 2. Exclusive common numbers
Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common
integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
"""


def exclusive_common_nums():
    lst1 = []
    lst2 = []

    i = 0
    while i < 10:
        lst1.append(random.randint(1, 10))
        lst2.append(random.randint(1, 10))
        i += 1

    # lists ==> sets in order to remove duplicates and perform intersection method (or use ampersand operator)
    lst3 = set(lst1) & set(lst2)

    print(f"""
TASK 2
Randomly generated list1: {lst1}
Randomly generated list2: {lst2}
List with exclusive common numbers: {list(lst3)}
""")


"""
Task3. Extracting numbers
Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
but not a multiple of 5, and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration
"""


def extract_nums():
    lst1 = list(range(1, 101))
    lst1_length = len(lst1)
    res = []
    i = 0
    while lst1_length - i > 0:
        if lst1[i] % 7 == 0 and lst1[i] % 5 != 0:
            res.append(lst1[i])
        i += 1

    print(f"""
TASK 3
List with numbers divisible by 7 but not a multiple of 5: {res}
""")


greatest_number()
exclusive_common_nums()
extract_nums()
