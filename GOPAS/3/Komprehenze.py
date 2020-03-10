Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Komprehenze
>>> 
>>> prestupne = []
>>> for rok in range(2000,2050):
	if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
		prestupne.append(rok)

		
>>> prestupne
[2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]
>>> # zjednodusene
>>> prestupne = []
>>> for rok in range(2000,2050):
	if rok % 4 == 0:
		prestupne.append(rok)

		
>>> prestupne
[2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]
>>> 
>>> del(prestupne)
>>> 
>>> # Komprehenze - vyraz, ktery "generuje posloupnost" (napr. seznam)
>>> prestupne = [y for y in range(2000,2050) if y % 4 == 0]
>>> prestupne
[2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]
>>> del(prestupne)
>>> 
>>> prestupne = [y for y in range(2000,2050) if y % 4 == 0]
>>> # Lze pouzivat i jednotlive prvky
>>> prestupne[3] = 19
>>> prestupne
[2000, 2004, 2008, 19, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]
>>> 
