# Module 4: Mini-Project | Library Management System
# Project Requirements
# In this project, you will apply Object-Oriented Programming (OOP) principles in Python to develop an advanced Library Management System. This command-line-based application is designed to streamline the management of books and resources within a library. Your mission is to create a robust system that allows users to browse, borrow, return, and explore a collection of books while demonstrating your proficiency in OOP principles and the use of modules.
# Enhanced User Interface (UI) and Menu:
# Create an improved, user-friendly command-line interface (CLI) for the Library Management System with separate menus for each class of the system.
# Welcome to the Library Management System!
# Main Menu:
# 1. Book Operations
# 2. User Operations
# 3. Author Operations
# 4. Quit
# Book Operations:
#         Book Operations:
#         1. Add a new book
#         2. Borrow a book
#         3. Return a book
#         4. Search for a book
#         5. Display all books
# User Operations: Highly Recommend Tracking a Current User
#         User Operations:
#         1. Add a new user
#         2. View user details
#         3. Display all users
# Author Operations: BONUS add this object as the Author Attribute of your books (check if author in author list, if not create author, add to list, and add as the author of the book
#         Author Operations:
#         1. Add a new author
#         2. View author details
#         3. Display all authors
# Class Structure:
# Implement a class structure that represents key entities in the library management system, including:
# Book: A class representing individual books with attributes such as title, author, ISBN, genre, publication date, and availability status.
# User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
# Author: A class representing book authors with attributes like name and biography.
# Encapsulation:
# Apply encapsulation principles by defining private attributes and using getters and setters for necessary data access. private __credit_card attribute
# Modules:
# Organize your code into modules to promote code organization and maintainability. Create separate modules for classes, user interactions, and error handling.
# Menu Actions:
# Implement the following actions in response to menu selections using the classes you've created:
# - Adding a new book with all relevant details.
# - Allowing users to borrow a book, marking it as "Borrowed."
# - Allowing users to return a book, marking it as "Available."
# - Searching for a book by its unique identifier (title) and displaying its details.
# - Displaying a list of all books with their unique identifiers.
# - Adding a new user with user details.
# - Viewing user details.
# - Displaying a list of all users.
# - Adding a new author with author details.
# - Viewing author details.
# - Displaying a list of all authors.
# - Quitting the application.
# User Interaction:
# Utilize the input() function within the appropriate menus to enable users to interact with the CLI and select menu options.
# Implement input validation using regular expressions (regex) to ensure the correct formatting of user input. (Bonus)
# Error Handling:
# Implement error handling using try, except, else, and finally blocks to manage potential issues gracefully, such as incorrect user input or file operations.



class Book: 

    # the __init__ method, which initilizes an object 'Book' class with the specified attributes.

    def __init__(self, title, author,isbn, genre, publication_date, availability=True):
        
    # Assigning th passed values to the attributes of the 'Book' class object.
        
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.availability = availability

    # Definition of the 'borrow_book' method, which changes the availaility status of the book to 'unavaiable'
    # if the book is availble for borrowing and prints a corresponding message   
    # And checking the availbility status of the book
    # Setting the availbility status of the bool to 'unavailble'
    # Printing the message that the book has been barrowed
    # REturning True to indicate a successful borrowing the book
    # Else: handling the case when the book is not available to borrowing
    # Printing a message that the book is not avaiable for borrowing
    # Returning False to indicate an unccessful borroeing of the book.
     
    def borrow_book(self):
        if self.availability: 
            self.availability = False 
            print(f"The book '{self.title}' has been borrowed.")
            return True
        else:
            print(f"The book '{self.title}' is not avaiable for borrowing.")
            return False

    # Defenition of the 'return_book' method, which changes the availbility status of the book to 'avaiable' if the book is return an prints a corresponding message.
    # Setting the availbility of the book to 'available'.
    # Printing a message that the book has been returned.

    def return_book(self):
        self.availability = True
        print(f"The book '{self.title}' has been returnend.")

# Definitionof the __init__ method, witch initilizes an object of the 'User" class with specified attrubutes.
# Assigning the paased values to the attributes of thee 'User' class object.
# [] in self.borrowed_books are used to create an empty list. 
# So we are creating a list that will store all the books borrowed by this user.
# After executing self.borrowed_books = [], each object of the 'User' class will have the 'borrowed_books' attribute, which will initially be an empty list.
 
class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []

# Defenition of the 'borrow_book' method, which allows the user to borrow a book and adds it to the user's list of borrowed books.
# Calling the 'borrow_book' method of the book object to check the availbility of the book and borrow it.
# Printning a message that the book has been borrowes by the user nad returning True.
# Printing a message that the user cou;dn't borrow the book and returning False

    def borrow_book(self, book):
        if book.borrow_book():
            self.borrowed_books.append(book)
            print(f"{self.name} has been borrowed the book '{book.title}'.")
            return True
        else:
            print(f"{self.name} couldn't borrow the book '{book.title}'.")
            return False

# Definition of the 'return_book' method, which allows the user to return a book and removes it from the user;s lsit of borrowed books.
# Cheking if the book is in the user;s list of borrowed books.
# Calling the 'return_book' method of the book object to mark the book as returned.
# Printning a message that the user has returned the book.
# Else: printning a message that the user doesn't have the book to return.

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned the book '{book.title}'.")
        else:
            print(f"{self.name} doesn't have the book '{book.title}' to return.")

# Definition of the __init__ method, which initilizes an object of the 'Author' class with the specified attributes.
# Assighing the paased values to the attributes of the 'Author' class object.

class Author:
    def __init__(self, name, biography):
        self.name = name 
        self.biography = biography

# Defintion of the __str__ method, which returns a dtring represantation of the 'Author' class object.
# REturning a string representation of the 'Author' class object.

    def __str__(self):
        return f"Author: {self.name}\nBiography: {self.biography}"
    
# Сhecking if the script is run directly& If the condition is True, th code inside this block will be executed.
# Creating an object 'book1' of the 'Book' class with the specified attributes.
# The same 'user1' of the 'User' class
# Calling the 'borrow_book' method of the 'user1' object to borrow the bookk.
# Calling the ;return_book' method of the 'user1' object to the return the book.
# Creating an object 'author1' of the 'Author' class with the specified attributes.

if __name__ == "__main__":
    book1 = Book("Around the World in Eighty days", "Jules Verne", "123456789", "Adventure Novel", "1872-01-01")        
    user1 = User("Rostovskaia K.", "ID005")
    user1.borrow_book(book1)
    user1.return_book(book1)
    author1 = Author("Jules Verne", "Jules Verne was a French novelist, poet, and playwright")