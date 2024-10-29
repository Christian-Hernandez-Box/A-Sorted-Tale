import sorts

def test_bubble_sort_by_title():
    books = [
        {'title_lower': 'c', 'author_lower': 'author1'},
        {'title_lower': 'a', 'author_lower': 'author2'},
        {'title_lower': 'b', 'author_lower': 'author3'}
    ]
    def by_title_ascending(book_a, book_b):
        return book_a['title_lower'] > book_b['title_lower']
    
    sorted_books = sorts.bubble_sort(books, by_title_ascending)
    assert [book['title_lower'] for book in sorted_books] == ['a', 'b', 'c']

def test_quicksort_by_author():
    books = [
        {'title_lower': 'title1', 'author_lower': 'c'},
        {'title_lower': 'title2', 'author_lower': 'a'},
        {'title_lower': 'title3', 'author_lower': 'b'}
    ]
    def by_author_ascending(book_a, book_b):
        return book_a['author_lower'] > book_b['author_lower']
    
    sorts.quicksort(books, 0, len(books) - 1, by_author_ascending)
    assert [book['author_lower'] for book in books] == ['a', 'b', 'c']

def test_bubble_sort_by_length():
    books = [
        {'title_lower': 'title1', 'author_lower': 'author1'},
        {'title_lower': 'title2', 'author_lower': 'a'},
        {'title_lower': 'title3', 'author_lower': 'author3'}
    ]
    def by_total_length(book_a, book_b):
        length_a = len(book_a['author_lower']) + len(book_a['title_lower'])
        length_b = len(book_b['author_lower']) + len(book_b['title_lower'])
        return length_a > length_b
    
    sorted_books = sorts.bubble_sort(books, by_total_length)
    assert [book['title_lower'] for book in sorted_books] == ['title2', 'title1', 'title3']