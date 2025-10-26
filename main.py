def get_book_text(filepath):
    """Takes a filepath as input and returns the contents of the file as a string."""
    with open(filepath, 'r') as file:
        return file.read()

def count_words(text):
    """Accepts text as a string and returns the number of words in the string."""
    words = text.split()
    return len(words)

def main():
    """Counts and displays the number of words in the book."""
    book_text = get_book_text('books/frankenstein.txt')
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

if __name__ == '__main__':
    main()
