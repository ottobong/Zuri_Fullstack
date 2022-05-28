# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from typing import Counter


def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        contents = f.read()
    
    return contents


def count_words():
    text = read_file_content('Reading-Text-Files\story.txt')
    # [assignment] Add your code here
    count = Counter(text.split()).items()
    print (count)
    return count



