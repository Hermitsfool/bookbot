from stats import get_num_words, get_letter, sort_dict
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
    else:
        path_to_book = sys.argv[1]
        

def main():
    book_path = path_to_book            #path of book ?? is this overwritten if we add it to the call function?
    text = get_book_text(book_path)                 #get the book with f.read in get_book_text funct.
    lower_text = text.lower()                       #lowercase the text
    num_words = get_num_words(lower_text)                 #call func from stats.py with text var-- see stats.py
    sum_letter = get_letter(lower_text)
    sorted = sort_dict(sum_letter)
    print_report(book_path, num_words, sorted)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, sorted):
    print("================BOOKBOT===============")
    print(f"Analyzing book found at {book_path}...")
    print("-------------- Word Count -------------")
    print(f"Found {num_words} total words")
    print("--------------Character Count----------")
    for item in sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("=============END===============")

main()
