# Ukazka vytvoreni modulu (casto lze pouzit i jako samostatny program)

pi = 3.14

_tajne = "Zcela tajne"

# Pridano pro variantu 3 importu
__all__ = ["pi","soucet"]

def soucet(p1,p2):
    """
    Scitanymi cisly jsou parametry funkce

    >>> soucet(2,3)
    5
    """
    
    return p1 + p2

def rozdil(p1,p2):
    """
    Odecitanymi cisly jsou parametry funkce

    >>> rozdil(2,3)
    -1
    """
    
    return p1 - p2

# Samostatne spusteni moduly jako programu: v tom pripade je vnitrni promenna
# __name__ nastavena na hodnotu "__main__". Je-li modul importovan, je __name__
# nastavena na jmeno programu (zde "Matika")

# if __name__ == "__main__":
#     print("Modul Matika spusten jako program")
    
# Samostane spusteni modulu jako programu lze pouzit i pro
# spusteni testu z dokumentacnich retezcu:

if __name__ == "__main__":
    import doctest
    # doctest.testmod()             # vyvolani testu (neni-li chyba, nenapise nic)
    doctest.testmod(verbose=True)   # podrobnejsi vypisy

# Testy lze spoustet z prikazoveho radku:
# python -m doctest -v Matika.py    # -v - verbose
