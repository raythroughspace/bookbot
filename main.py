from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    char_count = get_char_count(book_text)
    sorted_list = get_sorted_dictlist(char_count)

    output = "============ BOOKBOT ============\n" \
    f"Analyzing book found at {book_path}...\n" \
    "----------- Word Count ----------\n" \
    f"Found {get_number_of_words(book_text)} total words\n" \
    "--------- Character Count -------\n"

    for entry in sorted_list:
        if (entry["char"].isalpha()):
            output += f"{entry['char']}: {entry['count']}\n"
    
    output += "============= END ==============="

    print(output)

main()