def oops():
    raise IndexError


def catcher():
    try:
        oops()
    except:  # if we indicated 'except IndexError:' won't catch KeyError
        print('We caught some error')

    # except IndexError:
    #     print('We caught IndexError')


"""
If we change oops() to raise KeyError instead of IndexError, then catcher() will also capture the KeyError
"""

catcher()


def task2():
    values = input('Enter 2 numbers separated by space: ').split()
    try:
        a, b = values
        try:
            a, b = int(a), int(b)
            print(a ** a / b)
        except ValueError:
            print(f'Please indicate numbers! You have entered: a = {a}, b = {b}')
        except ZeroDivisionError:
            print('You cannot divide by zero!')
    except ValueError:
        print(f'You have indicated {len(values)} values. Please enter exactly 2 numbers!')


task2()
