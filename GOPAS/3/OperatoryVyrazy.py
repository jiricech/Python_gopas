Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Vyrazy a operatory
>>> # Operatory aritmeticke + - * / - VZDY DESETINNE!!, // - celociselne deleni
>>> # Modulo (zbytek po deleni) %
>>> # Mocnine **
>>> 5 / 2
2.5
>>> 5 // 2
2
>>> 5 % 2
1
>>> 2 ** 3
8
>>> # Prirazeni NEVRACI hodnotu!!
>>> a = 5
>>> 
>>> # slozene (zkracene) operatory: += -= *= ...
>>> i = 1
>>> i += 2  # i = i + 2  - totez
>>> i
3
>>> # Operator + lze pouzit mezi retezci (retezi)
>>> "ABC" + "xyz"
'ABCxyz'
>>> "Cislo = " + 5  # chyba - Python NEkoonvertuje cislo na retezec pro + !!
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    "Cislo = " + 5  # chyba - Python NEkoonvertuje cislo na retezec pro + !!
TypeError: can only concatenate str (not "int") to str
>>> 
>>> "Cislo = " + str(5)  # str(...) - konverze na string (podobne int a dalsi typy)
'Cislo = 5'
>>> 
>>> # operatory relacni < <= > >= != (nerovno) == (rovno!!)
>>> 
>>> # Operator identity is - porovnava POINTERY (adresy), NIKOLI hodnoty!!
>>> a = 5
>>> b = 5
>>> a is b  # NEMUSI byt True!!
True
>>> # Dalsi priklad:
>>> s1 = [1,2,3]
>>> s2 = [1,2,3]
>>> s1 is s2
False
>>> 
>>> # pro porovnani hodnot pouzit ==
>>> 
>>> # is se obvykle pouziva pro testovani specielni hodnoty None
>>> # None - preddefinovana hodnota - nezname, neplatne, nedefinovane, ...
>>> c = None
>>> c is None
True
>>> # Priority operatoru - viz help
>>> 
>>> # Logicke operatory not and or
>>> 
>>> # Zkracene vyhodnocovani logickych vyrazu
>>> i = 5
>>> (i < 0) and (b - 3 != 7) # vyhodnocuje zleva a konci, je-li vysledek jasny
False
>>>                          # zrychli; pozor na funkce s vedlejsimi efekty!!
                         
>>> 1 < b < 7                # kompaktni zapis podminek (bez and)
True
>>> # Relacni operatory lze pouzit i pro seznamy a dalsi viceprvkove typy:
>>> [1,2,"Ahoj!",4] == [1,2,"Ahoj!",5]  # porovnava zleva
False
>>> 
>>> # Zkracene prirazeni retezce k seznamu
>>> seznam = [1,2,3,4]
>>> seznam = seznam + "Ahoj!" # chyba
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    seznam = seznam + "Ahoj!" # chyba
TypeError: can only concatenate list (not "str") to list
>>> 
>>> seznam += "Ahoj!"  # OK, ALE!!
>>> seznam
[1, 2, 3, 4, 'A', 'h', 'o', 'j', '!']
>>> seznam = [1,2,3,4]
>>> seznam += ["Ahoj!"]
>>> seznam
[1, 2, 3, 4, 'Ahoj!']
>>> 
