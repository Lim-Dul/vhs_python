""" 
Benchmark stuff
"""
from collections import Counter
from timeit_decorator import timeit
from wonderwords import RandomWord

text = []

@timeit
def GenText():
    """ Generate ONE MILLION words """
    while len(text) < 1000000:
        text.extend(RandomWord().random_words(1000))
    print(len(text))

@timeit
def StrichlisteCounter():
    """ Strichliste mit Counter """
    strichliste = Counter("".join(text).lower())
    print(strichliste)

@timeit
def LoopCount():
    """ Loop mit Count """
    text_lower = "".join(text).lower()
    text_unique = set(text_lower)
    char_list = []

    for character in text_unique:
        char_list.append([character, text_lower.count(character)])
    char_list_sorted = sorted(char_list, key=lambda x: x[1], reverse=True)
    print(char_list_sorted)

GenText()
StrichlisteCounter()
LoopCount()
