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
        außer wenn gleichzeitig Mehrfaches von 100, dann Falsch
        außer wenn auch gleichzeitig ein Mehrfaches von 400, dann wieder Wahr.
    """
    if year % 400 == 0: # seltenster Fall zuerst
        return True
    if year % 100 == 0: # 100 als Sonderfall von 400
        return False
    if year % 4 == 0: # 4 als häufigster Fall
        return True
    return False
