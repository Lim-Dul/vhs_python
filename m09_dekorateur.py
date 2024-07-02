"""
Modul 09: Built-in-Cache
"""
from functools import cache


wunschzahl = 9


@cache # Gib der nächsten Funktion einen Cache
def fib_rekursiv(n):
    """
    Ruft sich selbst rekursiv auf, um Fibonacci-Zahlen zurückzugeben, ist aber ineffizient
    (berechnet immer wieder neu)

    Arguments:
        n -- Positiver Integer, welche Zahl ausgegeben werden soll

    Returns:
        Gibt 0 bei 0 zurück und n-te Fibonacci-Zahl bei n > 0
    """
    if n >= 2:
        return fib_rekursiv(n - 1) + fib_rekursiv(n - 2)
    if n == 0:
        return 0
    return 1

print(fib_rekursiv(wunschzahl))
