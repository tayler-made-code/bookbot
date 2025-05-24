from stats import get_num_words
from stats import count_letters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        get_num_words(file_contents)
        count_letters(file_contents)

def main():
    path = "./books/frankenstein.txt"    
    get_book_text(path)

main()
