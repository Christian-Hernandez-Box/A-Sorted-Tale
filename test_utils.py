import utils

def test_load_books():
    books = utils.load_books('books_small.csv')
    assert len(books) > 0
    assert 'author_lower' in books[0]
    assert 'title_lower' in books[0]