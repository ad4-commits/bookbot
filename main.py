from stats import get_num_words, get_character_counts, get_sorted_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_character_counts(text)
    
    # Get sorted character counts - THIS IS THE KEY PART YOU'RE MISSING
    sorted_chars = get_sorted_char_counts(chars_dict)
    
    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Print each character and count in sorted format
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['count']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()
