"""
Exercism Pangram
"""
import string

def is_pangram(sentence):
    """
    Schaut, ob in einem Satz jeder Buchstabe mindestens einmal vorkommt.

    Arguments:
        sentence -- String: Der Satz, der geprüft werden soll.

    Returns:
        Wahr, wenn Satz ein Pangramm ist, sonst Falsch
    """
    sentence = sentence.lower()

    checker = set()

    buchstaben = string.ascii_lowercase
    for buchstabe in buchstaben:
        if buchstabe in sentence:
            checker.add(buchstabe)
    if len(checker) == len(buchstaben):
        return True

    return False


is_pangram("The quick brown fox jumps over the lazy fox.")
