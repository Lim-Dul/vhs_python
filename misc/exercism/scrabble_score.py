"""
Übung Scrabble aus Exercism
"""
punkte = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
        }

def score(wort):
    """
    Bewertet wort anhand der obigen Punktetabelle (Wörterbuch)

    Arguments:
        wort -- String: Wort

    Returns:
        Scrabble-Bewertung des Wortes
    """
    # Loop über zeichen in wort (Großbuchstaben), Lookup des von zeichen in Wörterbuch, dann Summe
    return sum(punkte[zeichen] for zeichen in wort.upper())

print(score("Eggplant"))
