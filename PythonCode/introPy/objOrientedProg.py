from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#This is how Object Oriented Programming using python
#This is a class named Book
class Book:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def titleBook(book):
        print(f"Book:{book.title}")

b1 = Book("Chessmen", "Peter May", 120, 31)

b1.titleBook()

#Create a popup dialog box
# messagebox.showinfo("Message", "This is my first pop up dialog box")

#This is how encapsulation works in the python programming language
#This is a class named anotherBook
class anotherBook:
    def __init__(self, title, author, quantity, price):
        self.title = title #This is the variable that enters the title
        self.author = author #This is the variable that enters the author
        self.quantity = quantity #This is the variable that enters the quantity
        self.__price = price #This is the variable that enters the price
        self.__bargain = None #This variable is empty
    
    def set_discount(self, bargain):
        self.__bargain = bargain #This is an object that stores the value of the discount

    def get_price(srp):
        if srp.__bargain:
            return srp.__price*(1-srp.__bargain)
        return srp.__price

bulk_books = anotherBook("Runaway", "Peter May", 5, 300)

bulk_books.set_discount(0.50)
print(f"Price with a discount: {bulk_books.get_price()}")

#This is how inheritance work in Python programming language
#This is a class named bookSeries
class bookSeries:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.__price = price
        self.__bargain = None
        self.quantity = quantity
    
    def set_discount(self, bargain):
        self.__bargain = bargain
    
    def get_price(self):
        if self.__bargain:
            return self.__price*(1-self.__bargain)
        return self.__price
    
    def __repr__(self):
        return f"Book: {self.title}, Author: {self.author}, Quantity: {self.quantity}, Price: {self.get_price()}"

class Novel(bookSeries):
    def __init__(self, title, author, price, quantity, pages):
        super().__init__(title, author, price, quantity)
        self.pages = pages

class Academic(bookSeries):
    def __init__(self, title, author, price, quantity, branch):
        super().__init__(title, author, price, quantity)
        self.branch = branch

book1 = bookSeries("Time Machine", "H.G Wells", 600, 2)
book2 = Novel("Blah Blah!", "Bladi", 450, 12, 101)
book3 = Academic("Python Prog.", "Python Community", 300, 10, "Developer")

book2.set_discount(0.10) #This line sets the discount using the object set_discount()

#This prints all the variables stored in the book2
print(book2)

#This prints all the variables stored in the book3
print(book3)