from stats import get_num_words, get_character_counts

def get_book_text(filepath):
    """Takes a filepath as input and returns the contents of the file as a string."""
    with open(filepath, 'r') as file:
        return file.read()

def main():
    """Counts words and characters in the book."""
    book_text = get_book_text('books/frankenstein.txt')
    num_words = get_num_words(book_text)
    character_counts = get_character_counts(book_text)
    
    print(f"Found {num_words} total words")
    print(character_counts)

if __name__ == '__main__':
    main()
