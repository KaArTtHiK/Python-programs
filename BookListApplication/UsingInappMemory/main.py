from utils import database

User_Choice = """
a to add book
l to list all books
d to delete book from list
r to mark the book as read
Enter your choice: 
"""


def menu():
    user_input = input(User_Choice)
    while user_input != "q":
        if user_input == 'a':
            add_book()
        elif user_input == 'r':
            mark_read()
        elif user_input == 'd':
            delete_book()
        elif user_input == 'l':
            list_books()
        else:
            print("Enter the correct option")
        user_input = input(User_Choice)


def add_book():
    name = input("Enter the book name:")
    author = input("Enter the author name:")
    database.add_book(name, author)


def mark_read():
    name = input("Enter the name of the book you finished reading:")
    database.read_books(name)


def delete_book():
    name = input("Enter the name of the book you want to delete")
    database.delete_books(name)


def list_books():
    books = database.get_books()
    for book in books:
        read = "Yes" if book["read"] == True else "No"
        print("{} by {}, read : {}".format(book["name"],book["author"],read))


menu()