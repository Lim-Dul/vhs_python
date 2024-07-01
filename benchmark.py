""" 
Benchmark stuff
"""
from collections import Counter
import cProfile
from wonderwords import RandomWord


text = RandomWord().random_words(1000)

for i in range(1000):
    text.extend(RandomWord().random_words(1000))
print(len(text))

def test():
    """ Blah """
    strichliste = Counter("".join(text))
    print(strichliste)

def test2():
    """ Blah """
    # Meine Lösung 1
    text_lower = "".join(text).lower()
    text_unique = "".join(set(text_lower))
    print(text_unique)
    char_list = []
    for character in text_unique:
        char_list.append([character, text_lower.count(character)])
    # print(char_list)
    char_list_sorted = sorted(char_list, key=lambda x: x[1], reverse=True)
    # print(char_list_sorted)
    for char_count_pair in char_list_sorted:
        print(char_count_pair[0] + ":", char_count_pair[1])

cProfile.run("test()")
cProfile.run("test2()")
