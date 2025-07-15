

def get_num_words(text):                #called by main func in main.py
    words = text.split()                #splits the words
    return len(words)                   #returns the count to main func
   


def get_letter(letters):                
    char_count = {}                      #init new dictionary
    for letter in letters:                  #iterate over book
        if letter not in char_count:            #if the letter is in dict increment it. else create  
            char_count[letter] = 1                     #key/value pair starting at 1.
        else:
            char_count[letter] += 1
    return(char_count)                      #return dictionary to main.py

def sort_on(d):
    return d["num"]


def sort_dict(words):
    sorted_letters = []
    
    for letter in words:
        sorted_letters.append({"char": letter, "num": words[letter]})
    sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters