"""
Lesson 17. Homework.
"""

"""
Task 1. Method overloading.
Create a base class named Animal with a method called talk and then create two subclasses:
Dog and Cat, and make their own implementation of the method talk be different.
For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
Also, create a simple generic function, which takes as input instance of a Cat or Dog classes
and performs talk method on input parameter.  
"""


def talk(animal):
    return animal.talk()


class Animal:

    def talk(self):
        pass


class Dog(Animal):

    def talk(self):
        print('Woof woof!')


class Cat(Animal):

    def talk(self):
        print('Meow!')


cat1 = Cat()
dog1 = Dog()

# talk(cat1)
# talk(dog1)
# cat1.talk()
# dog1.talk()


"""
Task 2. Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []
Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books
list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year
All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books
"""


class Library:

    def __init__(self, name: str, books: list = [], authors: list = []):
        self.name = name
        self.books = books
        self.authors = authors

    def __str__(self):
        return f'Library name: {self.name}\n' \
               f'Books: {", ".join(book.name for book in self.books)}\n' \
               f'Authors: {", ".join(author.name for author in self.authors)}'

    def __repr__(self):
        return f'Library name: {self.name}\nBooks: {self.books}\nAuthors: {self.authors}'

    def new_book(self, book):
        if book not in self.books:
            self.books.append(book)
        if book.author not in self.authors:
            self.authors.append(book.author)
        return book

    # added to create multiple new books within one func
    def new_books(self, *books):
        for book in books:
            if book not in self.books:
                self.books.append(book)
            if book.author not in self.authors:
                self.authors.append(book.author)
        return books

    def group_by_author(self, author):
        books_list = []
        for book in self.books:
            if book.author == author:
                books_list.append(book)
        return books_list

    def group_by_year(self, year: int):
        books_list = []
        for book in self.books:
            if book.year == year:
                books_list.append(book)
        return books_list


class Book:
    number_of_books = 0

    def __init__(self, name: str, year: int, author):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.number_of_books += 1

    def __str__(self):
        return f'"{self.name}" by {self.author.name} ({self.year})'

    def __repr__(self):
        return f'{self.name}'


class Author:

    def __init__(self, name, country, birthday, books: list = []):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f'{self.name} from {self.country}, born on {self.birthday}. ' \
               f'Books: {", ".join([f"{i.name} ({i.year})" for i in self.books])}'

    def __repr__(self):
        return f'{self.name}'


lib1 = Library('My home library')

author1 = Author('Charlotte Bronte', 'UK', '21.04.1816')
author2 = Author('J.D. Salinger', 'USA', '11.11.1911')
author3 = Author('F.S. Fitzgerald', 'USA', '12.12.1912')
book1 = Book('Jane Eyre', 1847, author1)
book2 = Book('Shirley', 1849, author1)
book3 = Book('The Catcher in the Rye', 1917, author2)
book4 = Book('The Great Gatsby', 1847, author2)
book5 = Book('Tender is the night', 1849, author2)  # book not added to lib1

# lib1.new_book(book1)
# lib1.new_book(book2)
# lib1.new_book(book3)
# lib1.new_book(book4)
lib1.new_books(book1, book2, book3, book4)

print(lib1.group_by_author(author1))
print(lib1.group_by_year(1847))

print(lib1)
print(f'Number of all books: {Book.number_of_books}')

"""
Task 3. Fraction
Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *)
з належною перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій
та операції порівняння між об'єктами класу Fraction
"""


class Fraction:

    def __init__(self, number1, number2):
        if number2 == 0:
            raise ZeroDivisionError("You cannot divide by zero!")
        self.result = number1 / number2

    def check_class(self, other):
        if self.__class__ != other.__class__:
            raise AttributeError(f'{other.__class__.__name__} object is not of type {Fraction.__name__}')
        return True

    def __str__(self):
        return f'{self.result}'

    def __add__(self, other):
        if self.check_class(other):
            return self.result + other.result

    def __sub__(self, other):
        if self.check_class(other):
            return self.result - other.result

    def __mul__(self, other):
        if self.check_class(other):
            return self.result * other.result

    def __truediv__(self, other):
        if self.check_class(other) and other.result != 0:
            return self.result / other.result
        raise ZeroDivisionError("You cannot divide by zero!")

    def __eq__(self, other):
        return self.result == other

    def __ne__(self, other):
        return self.result != other

    def __lt__(self, other):
        return self.result < other

    def __le__(self, other):
        return self.result <= other

    def __gt__(self, other):
        return self.result > other

    def __ge__(self, other):
        return self.result >= other


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))
