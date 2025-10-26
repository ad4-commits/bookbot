def get_num_words(text):
    """Accepts text as a string and returns the number of words in the string."""
    words = text.split()
    return len(words)

def get_character_counts(text):
    """Returns the number of times each character appears in the string."""
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
