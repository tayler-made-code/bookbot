from stats import get_num_words
from stats import count_letters
from stats import sort_dict

def get_book_text(path_to_file):
    message_path = path_to_file[2:]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {message_path}...")
    print("----------- Word Count ----------")
    with open(path_to_file) as f:
        file_contents = f.read()
        get_num_words(file_contents)
        unsorted_dict = count_letters(file_contents)
        sort_dict(unsorted_dict)

def main():
    path = "./books/frankenstein.txt"    
    get_book_text(path)

main()
