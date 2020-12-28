books = []


def add_book(name, author):
    books.append({'name': name, "author": author, "read" : False})

def get_books():
    return books

def read_books(name):
    for book in books:
        if book["name"] == name:
            book["read"] = True

def delete_books(name):
    global books
    books = [book for book in books if book["name"]!= name]


#def delete_books(name):
#    for book in books:
#        if book["name"] == name:
#            books.remove(book)