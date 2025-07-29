import sys
print("Usage: python3 main.py <path_to_book>")
sys.exit(1)

def get_book_texts(text):
    with open(text) as book:
        output = book.read()
    return output

from stats import count_words

from stats import count_characters

from stats import sorted_characters

def main():
    book_path = sys.argv(1)
    book_content = (get_book_texts(book_path))
    total_words = count_words(book_content)
    book_char_counts = count_characters(book_content)
    book_sorted = sorted_characters(book_char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for char in book_sorted:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
main()
print(sys.argv)