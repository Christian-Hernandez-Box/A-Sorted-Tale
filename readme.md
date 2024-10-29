# Book Sorting Project

This project demonstrates sorting algorithms applied to a collection of books. The books are sorted based on different criteria such as title, author, and the total length of the title and author names.

## Project Structure

- `main.py`: The main script that loads books, defines sorting criteria, and prints sorted books.
- `sorts.py`: Contains the implementation of sorting algorithms (bubble sort and quicksort).
- `utils.py`: Utility functions for loading books from a CSV file.
- `test_sorts.py`: Unit tests for the sorting algorithms.
- `test_utils.py`: Unit tests for the utility functions.

## Requirements

- Python 3.x
- `pytest` for running unit tests

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required packages:
    ```bash
    pip install pytest
    ```

## Usage

1. Run the main script:
    ```bash
    python main.py
    ```

2. Run the tests:
    ```bash
    pytest
    ```

## Sorting Criteria

The project sorts books based on the following criteria:

1. **Title Ascending**: Sorts books by their titles in ascending order.
2. **Author Ascending**: Sorts books by their authors in ascending order.
3. **Total Length**: Sorts books by the total length of the title and author names.

## Functions

### main.py

- `print_books(books, key)`: Prints the specified key of each book in the list.
- `main()`: The main function that loads books, defines sorting criteria, and prints sorted books.

### sorts.py

- `bubble_sort(arr, comparison_function)`: Sorts an array using the bubble sort algorithm.
- `quicksort(arr, start, end, comparison_function)`: Sorts an array using the quicksort algorithm.

### utils.py

- `load_books(filename)`: Loads books from a CSV file and processes the author and title fields.

## Tests

### test_sorts.py

- `test_bubble_sort_by_title()`: Tests bubble sort by title.
- `test_quicksort_by_author()`: Tests quicksort by author.
- `test_bubble_sort_by_length()`: Tests bubble sort by total length.

### test_utils.py

- `test_load_books()`: Tests the `load_books` function.
