Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Zakladni datove typy
>>> 
>>> 2 + 3
5
>>> # Cela cisla
>>> # jsou "neomezena"
>>> 123456789012345678901234567890 + 35
123456789012345678901234567925
>>> 
>>> # Retezce
>>> "Ahoj!'
SyntaxError: EOL while scanning string literal
>>> "Ahoj!"
'Ahoj!'
>>> 'Nazdar!'
'Nazdar!'
>>> 'Rekl "Dobry den!"'
'Rekl "Dobry den!"'
>>> # netistitelne (pripadne nepripustne) znaky - escape sekvence (zacinaji \)
>>> "prvni\ndruhy\ntreti"
'prvni\ndruhy\ntreti'
>>> print("prvni\ndruhy\ntreti")
prvni
druhy
treti
>>> # Promenne
>>> cislo = 5  # vytvori promennou cislo a priradi ji hodnotu 5 typu int
>>> type(cislo)
<class 'int'>
>>> cislo = "Ahoj!"
>>> type(cislo)
<class 'str'>
>>> # Identifikatory promennych: pismena (Unicode), _ podtrzitko a cislice
>>> # Nesmi zacinat cislici!!
>>> _neprilisdoporucene = 3  # "systemove" promenne casto zacinaji _
>>> 3chyba = 1  # chyba - zacina cislici
SyntaxError: invalid syntax
>>> 
>>> x  # nelze vypsat neexistujici promennou
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x  # nelze vypsat neexistujici promennou
NameError: name 'x' is not defined
>>> cislo = x  # opet nelze priradit neexistujici ...
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    cislo = x  # opet nelze priradit neexistujici ...
NameError: name 'x' is not defined
>>> 
>>> # V Pythonu jsou VSECHNY TYPY REFERENCNI ("objekty")
>>> # Promenna obsahuje pointer ("adresu") mista, kde je vlastni hodnota
>>> 
>>> # Typy int a str jsou NEPROMENNE - pri kazde zmene se v pameti vytvori
>>> # nova hodnota a pointer se na ni nasmeruje (dosavadni hodnota se casem
>>> # zrusi, pokud na ni neodkazuje jiny pointer)
>>> 
