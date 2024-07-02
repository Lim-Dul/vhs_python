# from collections import Counter

def is_isogram(string):
    """
    Checks if string is an isogram (no duplicate letters)

    Arguments:
        string -- string to be checked

    Returns:
        True if string is isogram
    """
    for character in (" -"):
        string = string.replace(character,"")
    print(string, len(string))
    print(set(string), len(set(string)))
    return len(string) == len(set(string.lower()))


print(is_isogram("eleven")) # eleven sollte False liefern
