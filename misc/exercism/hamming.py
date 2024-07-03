"""
Lösung für Exercism Hamming-Abstand-Berechnung
"""

def distance(dna_strang_a, dna_strang_b):
    """
    _summary_

    Arguments:
        dna_strang_a -- String: DNA-Strang (nur Buchstaben A, C, G, T erlaubt)
        dna_strang_b -- String: DNA-Strang (nur Buchstaben A, C, G, T erlaubt)

    Raises:
        ValueError:
            - Wenn Stränge unterschiedliche Länge haben.
            - Wenn Stränge sich nicht aus den Buchstaben A, C, G, T zusammensetzen.

    Returns:
        Hamming-Abstand der DNA-Stränge
    """
    if len(dna_strang_a) != len(dna_strang_b):
        raise ValueError("DNA-Stränge müssen die gleiche Länge haben.")
    nukleinbasen = {"A", "C", "G", "T"}
    if set(dna_strang_a) > nukleinbasen or set(dna_strang_b) > nukleinbasen:
        raise ValueError("DNA-Stränge dürfen sich nur aus den Buchstaben "
                        "A, C, G, T zusammensetzen.")
    hamming_abstand = 0
    for nukleinbase_a, nukleinbase_b in zip(dna_strang_a, dna_strang_b):
        if nukleinbase_a != nukleinbase_b:
            hamming_abstand += 1
    return hamming_abstand

# print(distance("GATTACA", "TAGCCTA"))