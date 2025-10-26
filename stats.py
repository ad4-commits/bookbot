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

def get_sorted_char_counts(char_count_dict):
    """Takes a dictionary of characters and their counts, returns a sorted list of dictionaries"""
    
    # Create a list of dictionaries for alphabetical characters only
    char_list = []
    for char, count in char_count_dict.items():
        if char.isalpha():  # Only include alphabetical characters
            char_list.append({"char": char, "count": count})  # Changed to "count"
    
    # Define helper function for sorting
    def sort_by_count(dict_item):
        return dict_item["count"]  # Changed to "count"
    
    # Sort from greatest to least
    char_list.sort(key=sort_by_count, reverse=True)
    
    return char_list
