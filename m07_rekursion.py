"""
Modul 07: Rekursion
"""

# 1) Fibonacci-Zahlen:
# Die nächste Zahl der Folge ist die Summe der beiden vorhergehenden Zahlen der Folge
# fib(n) 0 1 1 2 3 5 8 13 21 34
# n      0 1 2 3 4 5 6 7  8  9

# a b | a + b
# - 0 | 0       n = 0
# 0 1 |
# 0 1 | 1       n = 1
# 1 1 | 2       n = 2
# 1 2 | 3       n = 3
# 2 3 | 5       n = 4
# 3 5 | 8       n = 5
# ...


def fib(n):
    """
    _summary_

    Arguments:
        n -- Positiver Integer, welche Zahl ausgegeben werden soll

    Returns:
        Gibt 0 bei 0 zurück und n-te Fibonacci-Zahl bei n > 0
    """
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a

print(fib(9))

# Rekursive Lösung (Rekursion: Eine Funktion, die sich selbst aufruft)
# Die nächste Zahl der Folge ist die Summe der beiden vorhergehenden Zahlen der Folge.
# fib(n) = fib(n - 1) + fib(n -2) für n >= 2 # rekursive Definition
# fib(0) = 0
# fib(1) = 1
# fib(2) = 1
def fib_rekursiv(n):
    """
    Ruft sich selbst rekursiv auf, um Fibonacci-Zahlen zurückzugeben, ist aber ineffizient
    (berechnet immer wieder neu)

    Arguments:
        n -- Positiver Integer, welche Zahl ausgegeben werden soll

    Returns:
        Gibt 0 bei 0 zurück und n-te Fibonacci-Zahl bei n > 0
    """
    if n >= 3:
        return fib_rekursiv(n - 1) + fib_rekursiv(n - 2)
    if n == 0:
        return 0
    return 1

print(fib_rekursiv(9))

d = {}
def fib_rekursiv_memo(n):
    """
    Ruft sich selbst rekursiv auf, um Fibonacci-Zahlen zurückzugeben, 
    speichert aber die Zwischenergebnisse in einer Dictionary

    Arguments:
        n -- Positiver Integer, welche Zahl ausgegeben werden soll

    Returns:
        Gibt 0 bei 0 zurück und n-te Fibonacci-Zahl bei n > 0
    """
    if n in d: # Haben wir den Wert für n schon einmal berechnet?
        return d[n] # Wenn ja: Gib diesen einfach zurück, indem du ihn im Wörterbuch nachschlägst.
    if n >= 2:
        d[n] = fib_rekursiv_memo(n - 1) + fib_rekursiv_memo(n - 2)
        return d[n]
    return 1
