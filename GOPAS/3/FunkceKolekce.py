Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Funkce pro "kolekce" ("posloupnosti")
>>> 
>>> def addif(x):
	if x > 4:
		return x + 10
	else:
		return x

	
>>> addif(3)
3
>>> sddif(5)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sddif(5)
NameError: name 'sddif' is not defined
>>> addif(5)
15
>>> 
>>> seznam = [1,3,5,7,9]
>>> map(addif,seznam)
<map object at 0x0000000002F58F60>
>>> # vrati "spatny typ" - ne seznam. Proto konvertuji:
>>> list(map(addif,seznam))
[1, 3, 15, 17, 19]
>>> 
>>> # map lze pouzit i na mnoziny
>>> mnozina = {0,2,4,6,8}
>>> mnozina2 = set(map(addif,mnozina))
>>> mnozina2
{0, 2, 4, 16, 18}
>>> 
>>> # funkce lze vytvorit "na miste" pomoci lambda vyrazu:
>>> seznam2 = list(map(lambda x: x if x <= 4 else x + 10,seznam))
>>> seznam2
[1, 3, 15, 17, 19]
>>> 
>>> # map lze pouzit na vice poslupnosti
>>> a = [1,2,3,4]
>>> b = [6,7,8,9]
>>> list(map(lambda x,y: x + y,a,b))
[7, 9, 11, 13]
>>> c = [1,1,1,1]
>>> list(map(lambda z,y,z: x + y + z, a,b,c))
SyntaxError: duplicate argument 'z' in function definition
>>> list(map(lambda x,y,z: x + y + z, a,b,c))
[8, 10, 12, 14]
>>> 
>>> # Filtrovani: pouzijeme funkci, jejiz vysledky interpretujeme jako Tru/False
>>> # Do vystupu se zahrnuji ty prvky puvodni kolekce, pro ktere funkce vraci True
>>> fib = [0,1,1,2,3,5,8,13,21,34,55]
>>> result = list(filter(lambda x: x % 2,fib))
>>> result
[1, 1, 3, 5, 13, 21, 55]
>>> 
>>> # Redukce: pouzijeme funkci o 2 parametrech; ta je nejprve volana na prvni dva
>>> # prvky posloupnosti. Dale vzdy pouzijeme predchozi vysledek teto funkce jako
>>> # jeji 1. prametre a dalsi prvek posloupnosti jako druhy. Redukce vrati JEDNU
>>> # HODNOTU, nikoli posloupnost.
>>> 
>>> import functools  # pro Python 3.x
>>> functools.reduce(lambda x,y: x + y, range(1,101))
5050
>>> 
