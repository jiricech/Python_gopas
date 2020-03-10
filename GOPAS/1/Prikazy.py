Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Prikazy jazyka Python
>>> 
>>> # Prirazovaci prikaz (NEMA HODNOTU!!)
>>> a = 5
>>> 
>>> # Ridici prikazy:
>>> if a > 0:
	b = 1
	c = 2   # blok prikazu (suite) - stejne odsazene
	        # tvori jednoku (blok), ktery se vykona pri splnene podmince

	        
>>> b,c
(1, 2)
>>> if a > 0:
	b = 1
	c = 2
else:   # pokud podminka neni splnena
	b = 9
	c = 15
	d = 2

	
>>> # Prikazy if lze vnorovat (opet s odsazenim)
>>> 
>>> # Prikaz pass - nedela nic - prazdny prikaz
>>> if a > 0:
else:		# chyba - nelze nemit prikazy za if!!
	
SyntaxError: expected an indented block
>>> if a > 0:
	pass
else:
	b = 1

	
>>> # Vicenasobne vetveni
>>> teplota = 18
>>> if teplota > 25:
	print("Vedro")
elif teplota > 20:
	print("Teplo")
elif teplota > 16:
	print("Prijemne")
# ...
elif teplota > 0:
	print("Nemrzne")
else
SyntaxError: invalid syntax
>>> if teplota > 25:
	print("Vedro")
elif teplota > 20:
	print("Teplo")
elif teplota > 16:
	print("Prijemne")
# ...
elif teplota > 0:
	print("Nemrzne")
else:
	print("Zima jak v psirne")

	
Prijemne
>>> 
>>> # Cyklus while
>>> x = 1
>>> while x < 10:
	print(x,x*x)
	x += 1

	
1 1
2 4
3 9
4 16
5 25
6 36
7 49
8 64
9 81
>>> 
>>> # False: 0,"",None,False,prazdny seznam (a dalsi prazdne viceprvkove typy)
>>> # True: vse ostatni
>>> 
>>> # for ccyklus - pouzivan pro iterovatelne typy (list, string, ...)
>>> staty = ["Ceska republika","Slovensko","Rakousko","Nemecko","Anglie"]
>>> for stat in staty:  # projdde seznam a jeho prvky postupne vklada do stat
	print(stat)

	
Ceska republika
Slovensko
Rakousko
Nemecko
Anglie
>>> 
>>> # Dalsi priklad - retezec a znaky v nem:
>>> for znak in "ABCDEFGHIJKLMNOP":
	if znak in "AEIOUY":  # in zde - je dany prvek obsazen v list, string,
		print(znak,"je samohlaska")
	else:
		print(znak,"je souhlaska")

		
A je samohlaska
B je souhlaska
C je souhlaska
D je souhlaska
E je samohlaska
F je souhlaska
G je souhlaska
H je souhlaska
I je samohlaska
J je souhlaska
K je souhlaska
L je souhlaska
M je souhlaska
N je souhlaska
O je samohlaska
P je souhlaska
>>> 
>>> # "klasicky" cyklus for:
>>> for x in range(4,10):  # range vraci 4,5,6,7,8,9 (10 ne)
	print(x,x*x)

	
4 16
5 25
6 36
7 49
8 64
9 81
>>> # cyklus s krokem
>>> for x in range(1,10,2): # 3. param je krok
	print(x,x*x)

	
1 1
3 9
5 25
7 49
9 81
>>> 
>>> # funkce enum
>>> for polozka in enum(staty):
	polozka

	
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    for polozka in enum(staty):
NameError: name 'enum' is not defined
>>> # funkce enumerate
>>> for polozka in enumerate(staty):
	polozka

	
(0, 'Ceska republika')
(1, 'Slovensko')
(2, 'Rakousko')
(3, 'Nemecko')
(4, 'Anglie')
>>> 
>>> # Vstup z klavesnice
>>> data = input("Zadaej cislo: ")  # input - vstup z klavesnice + prompt
Zadaej cislo: 123
>>> data
'123'
>>> '12' + '34'
'1234'
>>> i = int(data)
>>> i
123
>>> data = int(input("Zadej cislo: "))
Zadej cislo: 123
>>> data
123
>>> data = int(input("Zadej cislo: "))
Zadej cislo: xyz
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    data = int(input("Zadej cislo: "))
ValueError: invalid literal for int() with base 10: 'xyz'
>>> # Vznikla chyba (exception - vyjimka) - xyz nelze konvertovat na cislo
>>> 
