from stats import count_words, get_book_text, count_characters, pretty_print

def test():
    #filepath = input('Type the filepath of the book:\n')
    book = get_book_text("books/frankenstein.txt")
    number_of_words = count_words(book)
    dict_of_char = count_characters(book)
    pretty_prin_1 = pretty_print(dict_of_char, number_of_words, "books/frankenstein.txt")


def main():
    test()

main()