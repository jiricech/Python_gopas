Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Doplnky k datovym typum
>>> 
>>> # Retezce
>>> # Stringy lze indexovat
>>> jmeno = "Franta"
>>> jmeno[2]
'a'
>>> # lze pouzivat rezy
>>> pismena = "ABCDEFGHIJKLMNOP"
>>> pismena[3:10]
'DEFGHIJ'
>>> pismena[0:10:2] # treti "index" je krok
'ACEGI'
>>> 
>>> # Dlouhe retezce - obklopeny """ ... """ nebo ''' ... '''
>>> dlouhyText = """Ja pisi viceradkovy text.
Toto je druhy radek \
a toto je take na druhem radku\n(diky \ na konci predchoziho radku)."""
>>> print(dlouhyText)
Ja pisi viceradkovy text.
Toto je druhy radek a toto je take na druhem radku
(diky \ na konci predchoziho radku).
>>> dlouhyText
'Ja pisi viceradkovy text.\nToto je druhy radek a toto je take na druhem radku\n(diky \\ na konci predchoziho radku).'
>>> 
>>> textPsanyPoCastech = "Prvni cast " "druha cast " "treti cast."
>>> textPsanyPoCastech
'Prvni cast druha cast treti cast.'
>>> 
>>> str = "ABCDEF" +  # chyba - chybi 2. operand
SyntaxError: invalid syntax
>>> str = ("ABCDEF" +
           "GHIJKL" +
           "MNOPQR")  # prokaz v zavorkach - OK (stejne vzorce apod.)
>>> str
'ABCDEFGHIJKLMNOPQR'
>>> 
>>> # Druha moznost - potlaceni konce radku pomoci \
>>> str = "ABCDEF" + \
          "GHIJKL" + \
          "MNOPQR"
>>> str
'ABCDEFGHIJKLMNOPQR'
>>> 
>>> # Specielni znaky a jejich kody
>>> euros = "€ \u20AC \U000020AC \N{euro sign}"
>>> euros
'€ € € €'
>>> 
>>> # Nektere metody retezcu
>>> retezce = ["abc","def","ghi"]
>>> t = ", ".join(retezce)
>>> t
'abc, def, ghi'
>>> t = "".join(retezce)
>>> t
'abcdefghi'
>>> 
>>> # Vyhledavani
>>> t.find("de")
3
>>> t.find("x")
-1
>>> t += "dexy"
>>> t
'abcdefghidexy'
>>> t.find("de")
3
>>> t.find("de",4)
9
>>> # 2. param - odkud hledat
>>> # Nahrazovani v retezci
>>> t
'abcdefghidexy'
>>> t.replace("de","XYZ")
'abcXYZfghiXYZxy'
>>> 
>>> # Retezce se znakem \
>>> path = "c:\data\texty\dopisy\dopis.txt"
>>> print(path)
c:\data	exty\dopisy\dopis.txt
>>> path = "c:\\data\\texty\\dopisy\\dopis.txt"
>>> print(path)
c:\data\texty\dopisy\dopis.txt
>>> # raw strings - zacinaji r" ... " (zde \ NENI zacatek escape sekvence)
>>> path = r"c:\data\texty\dopisy\dopis.txt"
>>> print(path)
c:\data\texty\dopisy\dopis.txt
>>> 
>>> # Preklad pomoci tabulky
>>> table = "".maketrans("žščťúý","zsctuy")
>>> "žluťoučký".translate(table)
'zlutoucky'
>>> 
>>> # Specielni pripady kolekce
>>> emptyList = []
>>> len(emptyList)
0
>>> emptyDict = {}
>>> len(emptyDict)
0
>>> emptyTuple = ()
>>> len(emptyTuple)
0
>>> emtySet = set()
>>> len(emptySet)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    len(emptySet)
NameError: name 'emptySet' is not defined
>>> len(emtySet)
0
>>> # jednoprvkovy tuple
>>> jednoprvkovy = (3)
>>> type(jednoprvkovy)
<class 'int'>
>>> jednoprvkovy = (3,) # OK
>>> type(jednoprvkovy)
<class 'tuple'>
>>> 
>>> # Nahodna cisla
>>> import random
>>> random.randint(1,6)
3
>>> random.randint(1,6)
3
>>> random.randint(1,6)
4
>>> random.randint(1,6)
1
>>> random.choice(["Franta","Karel","Vera","Eva"])
'Karel'
>>> random.choice(["Franta","Karel","Vera","Eva"])
'Eva'
>>> random.choice(["Franta","Karel","Vera","Eva"])
'Karel'
>>> 
>>> # Nektere doplnky k celym cislum
>>> round(2.1776)
2
>>> round(2.1776,2)  # 2 des. mista
2.18
>>> round(1283.432,-2) # na cele stovky
1300.0
>>> 
>>> # funkce bin a hex
>>> i = 349
>>> bin(i),hex(i)
('0b101011101', '0x15d')
>>> 
>>> # konverzni funkce int
>>> k = int("101")
>>> k
101
>>> k = int("101",2)  # zaklad ciselne soustavy!! (zde dvojkova)
>>> k
5
>>> # cisla lze zadavat i hexadecimalne
>>> n = 0x1A0
>>> n
416
>>> # take binarne
>>> i 0b101
SyntaxError: invalid syntax
>>> i = 0b101
>>> i
5
>>> # take oktalove
>>> i = 0o77
>>> i
63
>>> i = 077  # chyba
SyntaxError: invalid token
>>> 
>>> # Bitove operace - operatory | - bitove or, & - bitove and,
>>> #                            ^ - bitove xor, ~ - bitove not
>>> i = 5   	# ...0 0101
>>> j = 3 	# ...0 0011
>>> k = i & j 	# ...0 0001
>>> k
1
>>> # Bitove posuny << vlevo >> vpravo
>>> i = 3 	# ...0 0011
>>> k = i << 2  # ...0 1100
>>> 
>>> k
12
>>> # Desetinna cisla
>>> x = 1.23
>>> y = 3.54
>>> x + y
4.77
>>> z = 123.456e4 # krat 10 na 4
>>> z
1234560.0
>>> 
>>> # funkce pro desetinna cisla
>>> import math
>>> math.floor(5.7)  # neblizsi nizsi nebo rovne cele
5
>>> math.ceil(5.1)   # nejblizsi vysi nebo rovne cele
6
>>> math.sqrt(9)     # druha odmocnina
3.0
>>> # Desitkova cisla "bez zaokrouhlovani"
>>> import decimal
>>> 
>>> # Komplexni cisla
>>> z = 2 + 3j
>>> u = 1 + 9j
>>> w = u + z
>>> w
(3+12j)
>>> # Komplexni funkce
>>> import cmath
>>> 
