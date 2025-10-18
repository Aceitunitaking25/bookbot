import sys
from stats import count_words, get_book_text, count_characters, pretty_print

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def test():
    try:
        book = get_book_text(sys.argv[1])
    except:
        print("Please, use a correct filepath. Example: 'books/frankenstein.txt' ")
        sys.exit(1)
    number_of_words = count_words(book)
    dict_of_char = count_characters(book)
    pretty_prin_1 = pretty_print(dict_of_char, number_of_words, sys.argv[1])

def main():
    test()

main()