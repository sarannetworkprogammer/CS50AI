import nltk

import sys
from nltk.tokenize import word_tokenize

s = "Holmes chuckled to HIMSELF 1234."

def preprocess(s):
    words = []
    words1 = word_tokenize(s.lower())
    for each in words1:
        if each.isalpha():
            words.append(each)
    return words


words = preprocess(s)
print(words)
