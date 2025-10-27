import sys
from stats import (
    get_num_words,
    get_character_count,
    get_sorted_character_list
)

def get_text(path):
    with open(path) as f:
        return f.read()

def get_report(path,num_words,character_count_list):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for i in character_count_list:
        if i['char'].isalpha():
            print(f'{i['char']}: {i['num']}')
    print('============= END ===============')


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]
    text = get_text(path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    sorted_character_list = get_sorted_character_list(character_count)
    report = get_report(path,num_words,sorted_character_list)

main()