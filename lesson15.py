"""
Lesson 15. Homework
"""


"""
Task 1. A Person class
Make a class called Person.
Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes.
Make another method called talk() which makes prints a greeting from the person containing,
for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.
"""


class Person:

    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old")


person0 = Person('Jerome', 'Salinger', 91)
person0.talk()


"""
Task 2. Doggy age
Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age.
Then create a method `human_age` which returns the dog’s age in human equivalent.
"""


class Dog:

    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * Dog.age_factor


doge = Dog(5)
print(doge.human_age())


"""
Task 3. TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
exists in the list, or "No" - in the other case.

The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above.
"""


CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:

    def __init__(self, channels: list):
        self.channels = channels
        self.current_position = 0

    def number_of_channels(self):
        return len(self.channels)

    def first_channel(self):
        self.current_position = 0
        return self.channels[self.current_position]

    def last_channel(self):
        self.current_position = len(self.channels) - 1
        return self.channels[self.current_position]

    def turn_channel(self, channel_num: int):
        self.current_position = channel_num - 1
        return self.channels[self.current_position]

    def next_channel(self):
        if self.current_position == TVController.number_of_channels(self) - 1:
            return TVController.first_channel(self)
        else:
            self.current_position += 1
            return self.channels[self.current_position]

    def previous_channel(self):
        if self.current_position == 0:
            return TVController.last_channel(self)
        else:
            self.current_position -= 1
            return self.channels[self.current_position]

    def current_channel(self):
        return self.channels[self.current_position]

    def is_exist(self, n: int or str):
        if n in self.channels or n in range(TVController.number_of_channels(self)):
            return 'Yes'
        return 'No'


controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"
