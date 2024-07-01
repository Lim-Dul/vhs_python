""" 
Benchmark stuff
"""
from collections import Counter
import cProfile
from wonderwords import RandomWord

text = []


def GenText():
    """ Generate ONE MILLION words """
    while len(text) < 1000000:
        text.extend(RandomWord().random_words(1000))
    print(len(text))


def StrichlisteCounter():
    """ Strichliste mit Counter """
    strichliste = Counter("".join(text).lower())
    print(strichliste)
    

def LoopCount():
    """ Loop mit Count """
    text_lower = "".join(text).lower()
    text_unique = set(text_lower)
    char_list = []

    for character in text_unique:
        char_list.append([character, text_lower.count(character)])
    char_list_sorted = sorted(char_list, key=lambda x: x[1], reverse=True)
    print(char_list_sorted)

cProfile.run("GenText()")
cProfile.run("StrichlisteCounter()")
cProfile.run("LoopCount()")
