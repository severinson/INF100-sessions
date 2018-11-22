import os
import math
import bisect # needed for 1b

def load_wordlist(filename):
    """Loads a file from the disk and returns the words as a list."""
    with open(filename) as f:
        return [word.strip() for word in f if (word[0] is not ";" and word.strip())]
    
def load_positive():
    """Returns a list of positive words."""
    return load_wordlist("./positive-words.txt")

def load_negative():
    """Returns a list of negative words."""
    return load_wordlist("./negative-words.txt")

def index(l_sorted, v):
    '''locate the leftmost value exactly equal to x in a using binary search.
    returns False if x is not in a.'''
    i = bisect.bisect_left(l_sorted, v)
    if i != len(l_sorted) and l_sorted[i] == v:
        return i
    return None

def in_list(words, word):
    """Return true if word is in words, False otherwise."""
    word = word.lower().strip()
    idx = index(words, word)
    return False if idx is None else True

def count_words(word_list, sentence):
    """Count the occurences of a word in a list of words."""
    result = 0
    for word in sentence.split(" "):
        result += 1 if in_list(word_list, word) else 0
    return result

def count_positive_negative(s):
    """Returns a tuple (npositive, nnegative) with the amount of negative
    and positive words in s."""
    positive_words = load_positive()
    negative_words = load_negative()
    npositive = count_words(positive_words, s)
    nnegative = count_words(negative_words, s)
    return npositive, nnegative

def positiveness(s):
    """Returns how positive a sentence is."""
    npositive, nnegative = count_positive_negative(s)
    return math.log((npositive + 1) / (nnegative + 1))