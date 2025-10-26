from stats import get_num_words

def get_book_text(filepath):
    """Takes a filepath as input and returns the contents of the file as a string."""
    with open(filepath, 'r') as file:
        return file.read()

def main():
    """Counts and displays the number of words in the book."""
    book_text = get_book_text('books/frankenstein.txt')
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

if __name__ == '__main__':
    main()
