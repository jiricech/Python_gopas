Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Seznamy (list)
>>> 
>>> seznam = [1,3,5,7,9]
>>> seznam
[1, 3, 5, 7, 9]
>>> # Pristup k prvkum seznamu je pres index (zacinaji nulou)
>>> seznam[1]  # druhy prvek
3
>>> len(seznam) # urceni delky (i u jinych typu) - funkce len
5
>>> # Pripojovani hodnot k seznamu - metoda append
>>> seznam.append(11)
>>> seznam
[1, 3, 5, 7, 9, 11]
>>> 
>>> # vymazavani prvku ze seznamu (podle hodnoty)
>>> s = [1,3,5,7,5,3]
>>> s.remove(5)
>>> s
[1, 3, 7, 5, 3]
>>> # vymazal prvni petku
>>> 
>>> # Operator +  pro seznamy
>>> seznam = [1,3,5,7,9]
>>> seznam2 = ["Alfa","Beta","Gama"]
>>> treti = seznam + seznam2
>>> treti
[1, 3, 5, 7, 9, 'Alfa', 'Beta', 'Gama']
>>> 
>>> chyba = seznam + 5   # chyba - nelze "pricist cislo k seznamu"
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    chyba = seznam + 5   # chyba - nelze "pricist cislo k seznamu"
TypeError: can only concatenate list (not "int") to list
>>> 
>>> ok = seznam + [5]
>>> ok
[1, 3, 5, 7, 9, 5]
>>> 
>>> chyba = seznam + "ABCD"  # retezec take nelze "pricist" k seznamu
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    chyba = seznam + "ABCD"  # retezec take nelze "pricist" k seznamu
TypeError: can only concatenate list (not "str") to list
>>> 
>>> # Rezy (ziskavani casti seznamu)
>>> seznam = [1,3,5,7,9]
>>> cast = seznam[2:4]     # vrati seznam s indexy 2,3 (4 jiz ne!!)
>>> cast
[5, 7]
>>> zacatek = seznam[:4]
>>> zacatek
[1, 3, 5, 7]
>>> konec = seznam[4:]     # do konce
>>> konec
[9]
>>> # Zaporne indexy
>>> # -1 = posledni, -2 - predposledni, ...
>>> seznam[-1]
9
>>> # lze pouzivat i v rezech:
>>> seznam[-3:-1]
[5, 7]
>>> 
>>> # Seznamy jsou MENITELNE typy
>>> seznam = [1,3,5,7,9]
>>> seznam[2] = 13
>>> seznam
[1, 3, 13, 7, 9]
>>> seznam = [1,3,5,7,9]
>>> s2 = seznam
>>> s2[2] = 19
>>> s2
[1, 3, 19, 7, 9]
>>> seznam
[1, 3, 19, 7, 9]
>>> seznam = [1,3,5,7,9]
>>> # Prikazem s2 = seznam jsem priradil do s2 pointer na STEJNA data!!
>>> # Tedy "zmena v jednom" provede i "zmenu ve druhem" (spolecna data)
>>> 
>>> # Rez PREKOPIRUJI data rezu na jine misto pameti (a na to nasmeruji rez)
>>> s2 = seznam[:]  # kopie celeho seznamu
>>> s2[2] = 19
>>> s2
[1, 3, 19, 7, 9]
>>> seznam
[1, 3, 5, 7, 9]
>>> # Dalsi pouziti rezu
>>> c = seznam[:]
>>> c[1:3] = [21,22,23]
>>> # nahradi prvky v rezu VLEVO seznamem VPRAVO
>>> c
[1, 21, 22, 23, 7, 9]
>>> 
>>> # ciste vlozeni BEZ vymazani
>>> c = seznam[:]
>>> c[1:1] = ['a','b']
>>> c
[1, 'a', 'b', 3, 5, 7, 9]
>>> # c[1:1] - rez nulove sirky
>>> 
>>> # Ciste vymazani bez vlozeni
>>> c = seznam[:]
>>> c[1:3] = []  # [] - prazdny seznam
>>> c
[1, 7, 9]
>>> 
>>> # index mimo rozsah vyvola chybu
>>> seznam[4]
9
>>> seznam[5] # chyba
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    seznam[5] # chyba
IndexError: list index out of range
>>> seznam[-5]
1
>>> seznam[-6] # chyba
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    seznam[-6] # chyba
IndexError: list index out of range
>>> 
>>> # Nektere datove typy lze tridit:
>>> cisla = [5,7,11,2]
>>> cisla.sort()
>>> cisla
[2, 5, 7, 11]
>>> 
