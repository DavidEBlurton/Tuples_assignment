# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately (hint: do a membership check to see if the new book is already in the library).

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book():
    title = input("Please input your title.\n")
    author = input("please input the author.\n")
    book = (title, author)
    if is_duplicate(book, library):
        print(f"Book '{title}' by {author} already exists in the library.")
    else:
        library.append(book)
        print(f"Book '{title}' by {author} has been added to the library.")

def is_duplicate(book, library):
    return book in library

def main():
    while True:
        ans = input('''
Welcome to the Coding Temple Library
Enter the corresponding number for the action you'd like to take:
    1 - Add a book to the library.
    2 - Print out the library
    3 - Quit
''')
        if ans == '1':
            add_book()
        elif ans == '2':
            print(library)
        else:
            print("Thanks for using our library")

main()