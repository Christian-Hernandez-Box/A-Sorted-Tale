import utils
import sorts

def print_books(books, key):
    for book in books:
        print(book[key])

def main():
    bookshelf = utils.load_books('books_small.csv')
    print_books(bookshelf, 'title')

    print(ord('a'))
    print(ord(' '))
    print(ord('A'))

    def by_title_ascending(book_a, book_b):
        return book_a['title_lower'] > book_b['title_lower']

    sorted_by_title = sorts.bubble_sort(bookshelf, by_title_ascending)
    print_books(sorted_by_title, 'title')

    def by_author_ascending(book_a, book_b):
        return book_a['author_lower'] > book_b['author_lower']

    bookshelf_copy = bookshelf.copy()
    sorted_by_author = sorts.bubble_sort(bookshelf_copy, by_author_ascending)
    print_books(sorted_by_author, 'author')

    bookshelf_copy = bookshelf.copy()
    sorts.quicksort(bookshelf_copy, 0, len(bookshelf_copy) - 1, by_author_ascending)
    print_books(bookshelf_copy, 'author')

    def by_total_length(book_a, book_b):
        length_a = len(book_a['author_lower']) + len(book_a['title_lower'])
        length_b = len(book_b['author_lower']) + len(book_b['title_lower'])
        return length_a > length_b

    long_bookshelf = utils.load_books('books_large.csv')
    sorted_by_length = sorts.bubble_sort(long_bookshelf, by_total_length)
    print_books(sorted_by_length, 'title')

    sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)
    print_books(long_bookshelf, 'title')

if __name__ == "__main__":
    main()