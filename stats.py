def get_book_text(filepath):
    book = ''
    with open(filepath) as f:
        book = f.read()
    return book

def count_words(book_text):
    list_of_words = book_text.split()
    number_of_words = 0
    eder = 0
    for word in list_of_words:
        word = word.lower()
        number_of_words += 1
        if word == 'victor':
            eder += 1 
    #print(f"Number of times that 'Frankenstein' appears: {eder}")
    return number_of_words

def count_characters(book_text):
    #Characters that will be counted
    allowed_characters = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()æâêëô'
    dict_of_characters = {}
    #Creating dictionary of characters
    for char in allowed_characters:
        dict_of_characters[char]= 0
    #Counting characters from the string of the book
    for letter in book_text:
        letter = letter.lower()
        if letter in dict_of_characters:
            dict_of_characters[letter] += 1
    return dict_of_characters

def sort_on(items):
    return items[1]
def pretty_print(dict_char, number_of_words, filepath):
    #Ordening by the number of times the char appears in the book
    list_of_char = list(dict_char.items())
    list_of_char.sort(reverse=True,key=sort_on)

    #Printing info
    print(f'============ BOOKBOT ============\n\nAnalyzing book found at {filepath}')
    print(f'----------- Word Count ----------\nFound {number_of_words} total words')
    print('--------- Character Count -------')
    #Printing pretty the characters
    for char, count in list_of_char:
        print(f"{char}: {count}")
    print('============= END ===============')