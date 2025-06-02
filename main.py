import sys

from stats import word_count
from stats import char_count
from stats import format_report

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def get_book_text(filepath): #takes filepath as input
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main (): 
    
    filepath = sys.argv[1]
    content = get_book_text(filepath)
    num_words = word_count(content) 
    char_ct = char_count(content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    #print(char_ct)
    print("--------- Character Count -------")
    report = format_report(char_ct)
    for item in report:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main ()

