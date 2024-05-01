def main():
    print("--- Begin report of books/frankenstein.txt ---")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text) 
    char_dict = get_chars_dict(text)
    chars_sorted_list = dict_to_sorted_list(char_dict)
    print(f"{num_words} words found in the document")
    letter_count =  character_count(text)
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def count_words(text):
    word_count = len(text.split())
    return word_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_count(text):
    counted = {}
    lower_text = text.lower()
    for i in lower_text:
        if i not in counted:
            counted[i]=1
        else:
            counted[i] += 1
    return counted

def dict_to_sorted_list(char_dict):
    sorted_list = []
    for k in char_dict:
        sorted_list.append({"char": k, "num":char_dict[k]})
    return sorted_list

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()

