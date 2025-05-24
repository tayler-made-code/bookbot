def get_num_words(whole_book):
    each_word = whole_book.split()
    word_count = len(each_word)
    print(f"{word_count} words found in the document")


def count_letters(whole_book):
    print("entered count_letters")
    alphabet_dict = {}

    no_upper_book = whole_book.lower()
    for letter in no_upper_book:
        if letter not in alphabet_dict:
            alphabet_dict[letter] = 1
        else:
            alphabet_dict[letter] += 1

    print(alphabet_dict)
