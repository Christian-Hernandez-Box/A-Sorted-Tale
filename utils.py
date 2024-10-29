import csv

def load_books(filename):
    bookshelf = []
    try:
        with open(filename) as file:
            shelf = csv.DictReader(file)
            for book in shelf:
                book['author_lower'] = book['author'].lower()
                book['title_lower'] = book['title'].lower()
                bookshelf.append(book)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return bookshelf