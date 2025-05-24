def get_num_words(whole_book):
    each_word = whole_book.split()
    word_count = len(each_word)
    print(f"Found {word_count} total words")

def count_letters(whole_book):
    print("--------- Character Count -------")
    alphabet_dict = {}

    no_upper_book = whole_book.lower()
    for letter in no_upper_book:
        if letter not in alphabet_dict:
            alphabet_dict[letter] = 1
        else:
            alphabet_dict[letter] += 1
    
    return alphabet_dict

def sort_dict(unsorted_dict):
    list_dict = list(unsorted_dict.items())
    
    sorted_list = sorted(list_dict, key=lambda x: x[1], reverse=True)

    for entry in sorted_list:
        if entry[0].isalpha():
            print(f"{entry[0]}: {entry[1]}")
    
    print("============= END ===============")
