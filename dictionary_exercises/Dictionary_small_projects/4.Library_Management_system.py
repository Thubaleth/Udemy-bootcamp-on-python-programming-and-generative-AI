"""Create a library system:

library = {
    "B101": {"title": "Python Basics", "copies": 5},
    "B102": {"title": "Data Science", "copies": 3}
}

Requirements:
- Function to add books
- Function to issue a book (reduce copies)
- Function to return a book (increase copies)
- Function to search for a book
- Function to display available books
- Use loops for menu navigation
"""

library = {
    "B101": {"title": "Python Basics", "copies": 5},
    "B102": {"title": "Data Science", "copies": 3}
}

def add_books():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    copies = int(input("Enter book copies: "))

    library[book_id] ={"title":title,"copies":copies}

-#Function to issue a book (reduce copies)
def reduce_copies():
    book_id = input("Enter book Id: ")
    if book_id in library:
        if library[book_id]["copies"] > 0:
            library[book_id]["copies"] =- -1
            print("copies reduced successfully")

        else:
            print("invalid number")
    else:
        print("book not found")
    

#Function to return a book (increase copies)
def increase_copies():
    book_id = input("Enter book Id: ")
    if book_id in library:
        if library[book_id]["copies"] > 0:
            library[book_id]["copies"] =+1
            print("copies increased successfully")

        else:
            print("invalid number")
    else:
        print("book not found")
    


#Function to search for a book
def book_search():
    book_id = input("Enter book ID: ")
    if book_id in library:
        print("book found")
    
#Function to display available books
