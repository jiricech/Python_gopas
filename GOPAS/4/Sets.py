Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Typ mnozina (set)
>>> 
>>> s = {5, "Franta",3,("a","b"),"Eva"}
>>> s
{3, 5, 'Franta', 'Eva', ('a', 'b')}
>>> # Set NENI USPORADANY!!
>>> 
>>> # Prazdna mnozina
>>> emptyset = set()
>>> len(emptyset)
0
>>> type(emptyset)
<class 'set'>
>>> 
>>> # K dispozici je sada mnozinovych operaci (ukazka nekterych):
>>> s2 = {3,"Eva",7,"Karel"}
>>> rozdil = s.difference(s2)
>>> rozdil
{('a', 'b'), 5, 'Franta'}
>>> prunik = s.intersection(s2)
>>> prunik
{'Eva', 3}
>>> sjednoceni = s.union(s2)
>>> sjednoceni
{3, 5, 'Franta', 'Karel', 7, 'Eva', ('a', 'b')}
>>> 
>>> # Pridavani do mnoziny
>>> s.add("Vera")
>>> s
{3, 'Vera', 5, 'Franta', 'Eva', ('a', 'b')}
>>> s.add("Franta")
>>> s
{3, 'Vera', 5, 'Franta', 'Eva', ('a', 'b')}
>>> # mnozina NEPRIDA DUPLICITNI HODNOTU (ale nevyvola chybu)
>>> 
>>> # cyklus pres mnozinu
>>> for p in s:
	print(p)

	
3
Vera
5
Franta
Eva
('a', 'b')
>>> 
