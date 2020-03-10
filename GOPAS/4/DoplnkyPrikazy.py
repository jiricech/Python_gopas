Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Doplnky prikazy
>>> 
>>> # Zruseni objektu (promenne):
>>> i = 5
>>> i
5
>>> del(i)
>>> i   # chyba - i jiz neexistuje
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    i   # chyba - i jiz neexistuje
NameError: name 'i' is not defined
>>> 
>>> # del se seznamem
>>> seznam = [1,2,3,4,5,6]
>>> del(seznam[3])
>>> seznam
[1, 2, 3, 5, 6]
>>> del(seznam[1:3])
>>> seznam
[1, 5, 6]
>>> 
>>> # Prirazeni nekolika promennym najednou
>>> a,b = 1,2
>>> a,b
(1, 2)
>>> # prohozeni obsahu promennych
>>> a,b = b,a
>>> a,b
(2, 1)
>>> seznam = [1,2,3,4,5,6]
>>> prvni,*zbytek = seznam
>>> prvni
1
>>> zbytek
[2, 3, 4, 5, 6]
>>> prvni,*prostredni,posledni = seznam
>>> prvni,posledni
(1, 6)
>>> prostredni
[2, 3, 4, 5]
>>> 
>>> # "Vyraz" if
>>> import sys
>>> sys.platform
'win32'
>>> typ = "Windows" if sys.platfom.startswith("win") else "Linux"
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    typ = "Windows" if sys.platfom.startswith("win") else "Linux"
AttributeError: module 'sys' has no attribute 'platfom'
>>> typ = "Windows" if sys.platform.startswith("win") else "Linux"
>>> typ
'Windows'
>>> 
>>> i = 5
>>> while i > 0:
	i -= 1
else:	# kod za else se vykona POUZE po standardnim ukonceni cyklu
	# (ne po break a exception)
	print("Hotovo")

	
Hotovo
>>> while i > 0:
	i -= 1
	if (i == 2):
		break
else:	# kod za else se vykona POUZE po standardnim ukonceni cyklu
	# (ne po break a exception)
	print("Hotovo")

	
Hotovo
>>> i = 5
>>> while i > 0:
	i -= 1
	if (i == 2):
		break
else:	# kod za else se vykona POUZE po standardnim ukonceni cyklu
	# (ne po break a exception)
	print("Hotovo")

	
>>> # else u exception (plus finally)
>>> try:
	cislo = int(input("Cislo: "))
	print(cislo)
except ValueError as err
SyntaxError: invalid syntax
>>> try:
	cislo = int(input("Cislo: "))
	print(cislo)
except ValueError as err:
	print(err)
else:   # vykona POUZE, pokud NEBYLO EXCEPTION
	print("Provedeno bez chyby")
finally: # Provede VZDY - pri chybe i pro OK
	print("Provedeno finally")

	
Cislo: 123
123
Provedeno bez chyby
Provedeno finally
>>> try:
	cislo = int(input("Cislo: "))
	print(cislo)
except ValueError as err:
	print(err)
else:   # vykona POUZE, pokud NEBYLO EXCEPTION
	print("Provedeno bez chyby")
finally: # Provede VZDY - pri chybe i pro OK
	print("Provedeno finally")

	
Cislo: xyz
invalid literal for int() with base 10: 'xyz'
Provedeno finally
>>> 
>>> # "Jednoradkove" verze prikazu:
>>> i = 5
>>> if i > 0: print("Kuk!")

Kuk!
>>> if i > 0: print("Kuk!"); print("Mnau!")  # zdestredniky vytvareji blok

Kuk!
Mnau!
>>> # lze dokonce pridat i elif a else
>>> 
>>> # podobne pro whilw a for:
>>> for i in range(1,10): k = 2*i; print(k,k*k)

2 4
4 16
6 36
8 64
10 100
12 144
14 196
16 256
18 324
>>> if i > 0: print("Kuk!"); print("Mnau!") else: print("Haf!");print("Huu")
SyntaxError: invalid syntax
>>> if i > 0: print("Kuk!"); print("Mnau!"); else: print("Haf!");print("Huu")
SyntaxError: invalid syntax
>>> if i > 0: print("Kuk!"); print("Mnau!") else: print("Haf!");print("Huu")
SyntaxError: invalid syntax
>>> if i > 0: print("Kuk!"); print("Mnau!") else: print("Haf!");print("Huu")
SyntaxError: invalid syntax
>>> 
======================= RESTART: C:/MyPython/Smazat.py =======================
Kuk!
Mnau!
>>> 
======================= RESTART: C:/MyPython/Smazat.py =======================
Haf!
Huu
>>> 
