def get_number_of_words(book_text):
    word_count = 0
    for word in book_text.split():
        word_count += 1
    return word_count

def get_char_count(book_text):
    char_count = {}
    for char in book_text:
        char = char.lower()
        if (char in char_count):
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["count"]

def get_sorted_dictlist(char_count):
    sorted_list = []
    for key in char_count:
        entry = {}
        entry["char"] = key
        entry["count"] = char_count[key]
        sorted_list.append(entry)
    sorted_list.sort(reverse = True, key = sort_on)
    return sorted_list
