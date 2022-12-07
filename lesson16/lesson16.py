"""
Lesson 16 (Inheritance). Homework
"""

"""
Task 1. School
Make a class structure in python representing people at school.Make a base class called Person,
a class called Student, and another one called Teacher.
Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example, the name should be a Person attribute,
while salary should only be available to the teacher.
"""


class Person(object):

    persons_count = 0

    def __init__(self, name: str, age: int, sex: str, city: str):
        self.name = name
        self.age = age
        self.sex = sex
        self.city = city
        Person.persons_count += 1

    def say_hi(self) -> None:
        print(f"Hello, my name is {self.name} and I'm {self.age} years old. I was born in {self.city}.")


class Teacher(Person):

    teachers_count = 0

    def __init__(self, name: str, age: int, sex: str, city: str, salary: int, discipline: str, title: str = ''):
        super().__init__(name, age, sex, city)
        self.salary = salary
        self.discipline = discipline
        self.title = title
        Teacher.teachers_count += 1

    def greet(self) -> None:
        if self.sex == 'female':
            self.title = 'Mrs.'
        elif self.sex == 'male':
            self.title = 'Mr.'
        else:
            self.title = 'combat helicopter'
        print(f"Hi, students! You can call me {self.title} {self.name}. I'll be teaching you {self.discipline}.")

    def reveal_salary(self) -> None:
        print(f"My salary is {self.salary} UAH per month.")


class Student(Person):

    students_count = 0

    def __init__(self, name: str, age: int, sex: str, city: str, academic_year: int, major: str):
        super().__init__(name, age, sex, city)
        self.academic_year = academic_year
        self.major = major
        Student.students_count += 1

    def speak_up(self) -> None:
        print(f'I study {self.major} and currently at academic year {self.academic_year}.')


student1 = Student('Jake', 20, 'male', 'Kyiv', 2, 'Computer Science')
student1.say_hi()
student1.speak_up()
print(f"Number of persons: {Person.persons_count}")
print(f"Number of students: {Student.students_count}", "\n")

teacher1 = Teacher('Antolini', 36, 'male', 'New York', 35000, 'English')
teacher1.say_hi()
teacher1.greet()
teacher1.reveal_salary()
print(f"Number of persons: {Person.persons_count}")
print(f"Number of teachers: {Teacher.teachers_count}", "\n")

teacher2 = Teacher('McGonagall', 72, 'female', 'Hogwarts', 50000, 'Transfiguration')
teacher2.say_hi()
teacher2.greet()
teacher2.reveal_salary()
print(f"Number of persons: {Person.persons_count}")
print(f"Number of teachers: {Teacher.teachers_count}", "\n")

teacher3 = Teacher('Trelawney', 42, 'None', 'Far far away', 20000, 'Divination')
teacher3.say_hi()
teacher3.greet()
teacher3.reveal_salary()
print(f"Number of persons: {Person.persons_count}")
print(f"Number of teachers: {Teacher.teachers_count}", "\n")


"""
Task 2. Mathematician
Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:
* square_nums (takes a list of integers and returns the list of squares)
* remove_positives (takes a list of integers and returns it without positive numbers
* filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
"""


class Mathematician:

    def square_nums(self, lst: list[int]) -> list:
        return [i**2 for i in lst]

    def remove_positives(self, lst: list[int]) -> list:
        return [i for i in lst if i < 0]

    def filter_leaps(self, lst: list[int]) -> list:
        return [i for i in lst if not i % 4]


m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


"""
Task 3. Product Store
Write a class Product that has three attributes:
* type
* name
* price
Then create a class ProductStore, which will have some Products and will operate with all products in the store.
All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional
classes to operate on a certain type of product, etc.
Also, the ProductStore class must have the following methods:
* add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your
store(30 percent)
* set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input
identifiers (type or name). The discount must be specified in percentage
* sell_product(product_name, amount) - removes a particular amount of products from the store if available,
in other case raises an error. It also increments income if the sell_product method succeeds.
* get_income() - returns amount of money earned by ProductStore instance.
* get_all_products() - returns information about all available products in the store.
* get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
"""


class Product:

    def __init__(self, product_type, name, price):
        self.product_type = product_type
        self.name = name
        self.price = price
        self.premium = 0.3 * self.price


class ProductStore:

    def __init__(self):
        self.product_type = []
        self.product_name = []
        self.price = []
        self.premium = []
        self.amount = []
        self.income = 0

    def error(self, text='oops!'):
        raise ValueError(text)

    def product_index(self, name) -> int:
        return self.product_name.index(name)

    def product_is_available(self, name, amount=0) -> bool:
        if name in self.product_name and self.amount[self.product_index(name)] >= amount:
            return True
        return False

    def add(self, name, amount):
        if not self.product_is_available(name):
            self.product_type.append(name.product_type)
            self.product_name.append(name.name)
            self.price.append(name.price)
            self.premium.append(name.premium)
            self.amount.append(amount)
        else:
            self.amount[self.product_index(name)] += amount

    def sell(self, name, amount):
        if self.product_is_available(name, amount):
            self.amount[self.product_index(name)] -= amount
            self.income += amount * self.premium[self.product_index(name)]
        else:
            self.error(f'There is no such product as "{name}" in the store or the amount of products is insufficient!')

    def set_discount(self, identifier, discount, identifier_type='name'):

        if identifier_type == 'name':
            if self.product_is_available(identifier):
                i = self.product_index(identifier)
                delta = self.price[i] * discount
                self.premium[i] -= delta
                self.price[i] -= delta
            else:
                self.error(f'Store does not have "{identifier}"!')
        elif identifier_type == 'type':
            if identifier in self.product_type:
                for i, store_identifier in enumerate(self.product_type):
                    if store_identifier == identifier:
                        delta = self.price[i] * discount
                        self.premium[i] -= delta
                        self.price[i] -= delta
            else:
                self.error(f'Store does not have "{identifier}"!')
        else:
            self.error(f'Store does not have "{identifier}"!')

    def get_income(self) -> int or float:
        return self.income

    def get_product_info(self, name):
        if self.product_is_available(name):
            i = self.product_index(name)
            return self.product_name[i], self.amount[i]
        else:
            self.error(f'Store does not have "{name}"!')

    def get_all_products(self) -> str:
        output = f""
        for i in range(len(self.product_name)):
            output += f'{i+1}) product type: {self.product_type[i]}, product name: {self.product_name[i]}, ' \
                      f'amount: {self.amount[i]}, price: {self.price[i]} USD, premium per unit: {self.premium[i]} USD' \
                      f' \n'
        return output


# basic tests
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 100)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)

# extra tests:
# print('Before discount on ramen: ', s.get_all_products(), sep='\n')
# s.set_discount('Ramen', 0.1)
# print('After discount on ramen: ', s.get_all_products(), sep='\n')
#
# print('Income before selling 1 discounted Ramen: ', s.get_income())
# print(s.get_product_info('Ramen'))
# s.sell('Ramen', 1)
# print('Income after selling 1 discounted Ramen: ', s.get_income())
# print(s.get_product_info('Ramen'))
#
# p3 = Product('Food', 'Borsch', 200)
# p4 = Product('Food', 'Sushi', 150)
#
# s.add(p3, 50)
# s.add(p4, 20)
#
#
# print('Before discount on Food type: ', s.get_all_products(), sep='\n')
# s.set_discount('Food', 0.1, 'type')
# print('After discount on Food type: ', s.get_all_products(), sep='\n')


"""
Task 4. Custom exception
Create your custom exception named `CustomException`, you can inherit from base Exception class, but extend its
functionality to log every error message to a file named `logs.txt`.
Tips: Use __init__ method to extend functionality for saving messages to file
"""


class CustomException(Exception):

    def __init__(self, msg: str):
        self.msg = msg
        with open('logs.txt', 'a+') as log:
            log.write(msg)


number_of_errors = 10
for i in range(number_of_errors, -1, -1):
    if i != 0:
        CustomException(f'...Critical error! Your PC will be self destroyed in {i} second{(i != 1) * "s"}!\n')
    else:
        CustomException(f'...Boom!\n')
