def get_book_text(filepath):
    """Takes a filepath as input and returns the contents of the file as a string."""
    with open(filepath, 'r') as file:
        return file.read()

def main():
    """Uses get_book_text to read and print the entire contents of frankenstein.txt"""
    book_text = get_book_text('books/frankenstein.txt')
    print(book_text)

# Call main at the bottom
if __name__ == '__main__':
    main()
