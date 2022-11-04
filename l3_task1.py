import datetime


def greeting():
    name = 'Oleksandr'
    day = datetime.datetime.today().weekday()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(f'Good day {name}! {days[day]} is a perfect day to learn some python.')


greeting()
