"""
Exercism: Leap Year
"""


def leap_year(year):
    """
    Prüft, ob ein Jahr ein Schaltjahr ist.

    Arguments:
        year -- integer: Jahr

    Returns:
        Wahr, wenn Jahr ein Mehrfaches von 4,
        außer wenn Mehrfaches von 100, außer wenn auch ein Mehrfaches von 400
    """
    if year % 400 == 0: # spezifischster Check zuerst
        return True
    if year % 100 == 0: # 100 als Sonderfall von 400
        return False
    if year % 4 == 0: # 4 als generischster Check
        return True
    return False
