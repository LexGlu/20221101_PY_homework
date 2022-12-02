"""
Task 1
Write a Python program to detect the number of local variables declared in a function.
"""


def loc_var_num(func):
    return func.__code__.co_nlocals


# random func
def sqr_sum(x, y):
    x *= x
    y *= y
    res = x + y
    return res


print(f'Number of local vars in {sqr_sum}: {loc_var_num(sqr_sum)}')

"""
Task 2
Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""


def outer_func(x):
    print(f"Hello, i'm outer func {outer_func}! Param 'x' in outer func = {x}")

    def inner_func(y):
        nonlocal x

        print(f"Hello, i'm inner func {inner_func}! Param 'y' in outer func = {y}")
        x **= 2
        y **= 2
        print(f"x**2 + y**2 = {x + y}")

    return inner_func


func = outer_func(5)  # returns inner_func as object
func(10)  # call inner_function with param y = 10


"""
Task 3

Write a function called `choose_func` which takes a list of nums and 2 callback functions. If all nums inside the list
are positive, execute the first function on that list and return the result of it.
Otherwise, return the result of the second one


def choose_func(nums: list, func1, func2):
    pass

# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]
    

def remove_negatives(nums):
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
"""
