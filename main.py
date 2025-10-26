from stats import get_num_words, get_character_counts, get_sorted_char_counts

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

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_character_counts(text)  # This matches your function name
    
    # Get sorted character counts
    sorted_chars = get_sorted_char_counts(chars_dict)
    
    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Print each character and count
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['num']}")
    
    print("============= END ===============")
