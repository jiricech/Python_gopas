Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Datovy typ tuple (n-tice)
>>> 
>>> jmena = ("Franta","Eva","Karel")
>>> jmena
('Franta', 'Eva', 'Karel')
>>> tpe
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tpe
NameError: name 'tpe' is not defined
>>> type(jmena)
<class 'tuple'>
>>> # pristup ke 2. prvku pres index:
>>> jmena[1]
'Eva'
>>> 
>>> jmena[0] = "Jirka"  # chyba - tuple je NEMENITELNY!!
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    jmena[0] = "Jirka"  # chyba - tuple je NEMENITELNY!!
TypeError: 'tuple' object does not support item assignment
>>> # Tuple je efektivnejsi nez seznam pro nepromenna data
>>> 
>>> # Tuples lze scitat
>>> jmena2 = ("Tonda","Dana")
>>> jmena3 = jmena + jmena2
>>> jmena3
('Franta', 'Eva', 'Karel', 'Tonda', 'Dana')
>>> # Vnorovani
>>> vnorene = (jmena,jmena2)
>>> vnorene
(('Franta', 'Eva', 'Karel'), ('Tonda', 'Dana'))
>>> vnorene[1]
('Tonda', 'Dana')
>>> vnorene[1][1]
'Dana'
>>> # Vnorovat lze i seznamy a dalsi typy
>>> 
