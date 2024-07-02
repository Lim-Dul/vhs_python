"""
Modul 08: Dekorateur
"""
wunschzahl = 9


# Dekorateur zum "cachen" - wrappt eine Funktion und gibt die "schöner gemachte" zurück
def mach_schoener(funktion):
    """
    Gibt der eingegebenen Funktion einen "Cache" in Form einer "Dictionary"

    Arguments:
        funktion -- Funktion, die dekoriert werden soll

    Returns:
        Neue, dekorierte Funktion
    """
    ds = {}

    def schoenere_funktion(n):
        if n in ds:
            return ds[n]
        ds[n] = funktion(n)
        return ds[n]

    return schoenere_funktion


@mach_schoener # Dekoriere nächste Funktion mit der mach_schoener-Funktion
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
