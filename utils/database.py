books = []


def add_book(name, author):

    books.append({
        "name": name,
        "author": author,
        "read": False
    })


def get_all_books():
    return books


def read_book(name):
    for item in books:
        if item["name"] == name:
            item["read"] = True
            return True
    return False


def delete_book(name):
    global books # here to tell python that we are using the global variable
    books = [book for book in books if(book["name"] != name)]





