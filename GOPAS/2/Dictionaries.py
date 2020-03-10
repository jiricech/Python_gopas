Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Datovy typ dictionary
>>> 
>>> d = {"id":1,"krestni":"Franta","prijmeni":"Novak"}
>>> d
{'id': 1, 'krestni': 'Franta', 'prijmeni': 'Novak'}
>>> # pristup k polozkam:
>>> d["krestni"]
'Franta'
>>> # cyklus "pres" dictionary:
>>> for key in d:
	print(key,d[key])

	
id 1
krestni Franta
prijmeni Novak
>>> 
>>> d.values()
dict_values([1, 'Franta', 'Novak'])
>>> d.keys()
dict_keys(['id', 'krestni', 'prijmeni'])
>>> d.items()
dict_items([('id', 1), ('krestni', 'Franta'), ('prijmeni', 'Novak')])
>>> 
>>> # chyba neexistujiciho klice:
>>> d["name"]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d["name"]
KeyError: 'name'
>>> 
>>> # metoda get
>>> d.get("krestni")
'Franta'
>>> d.get("name")
>>> # pro neexistujici vrati None
>>> d.get("name","!!! NEEXISTUJE !!!")
'!!! NEEXISTUJE !!!'
>>> 
>>> # Nekolik zpusobu vytvoreni dictionary:
>>> d1 = {"id":1,"krestni":"Franta","prijmeni":"Novak"}
>>> d1
{'id': 1, 'krestni': 'Franta', 'prijmeni': 'Novak'}
>>> d2 = dict(id=1,krestni="Franta",prijmeni="Novak")
>>> d2
{'id': 1, 'krestni': 'Franta', 'prijmeni': 'Novak'}
>>> d3 = dict([("id",1),("krestni","Franta"),("prjmeni","Novak")])
>>> d3
{'id': 1, 'krestni': 'Franta', 'prjmeni': 'Novak'}
>>> d4 = dict(zip(("id","krestni","prijmeni"),(1,"Franta","Novak")))
>>> d4
{'id': 1, 'krestni': 'Franta', 'prijmeni': 'Novak'}
>>> 
>>> # Vytvoreni melke (shallow) kopie
>>> dkopie = d.copy()
>>> dkopie
{'id': 1, 'krestni': 'Franta', 'prijmeni': 'Novak'}
>>> dkopie["krestni"] = "Frantisek"
>>> dkopie
{'id': 1, 'krestni': 'Frantisek', 'prijmeni': 'Novak'}
>>> d
{'id': 1, 'krestni': 'Franta', 'prijmeni': 'Novak'}
>>> 
>>> # Problemy melke kopie - pro jednoduchost ukazano na seznamech
>>> s = [['a','b'],'r','s']
>>> s[0]
['a', 'b']
>>> s[1]
'r'
>>> c = s.copy()  # totez jako c = s[:]
>>> c
[['a', 'b'], 'r', 's']
>>> c[1] = 't'
>>> c
[['a', 'b'], 't', 's']
>>> s
[['a', 'b'], 'r', 's']
>>> 
>>> c[0][1] = 'x'
>>> c
[['a', 'x'], 't', 's']
>>> s
[['a', 'x'], 'r', 's']
>>> # Dusledek shallow copy (zmeni "oba") - shallow copy kopiruje je 1. uroven dat!
>>> 
>>> # deepcopy - hluboka kopie - popiruje data do libovolne urovne
>>> s = [['a','b'],'r','s']
>>> import copy
>>> hluboka = copy.deepcopy(s)
>>> s
[['a', 'b'], 'r', 's']
>>> hluboka
[['a', 'b'], 'r', 's']
>>> hluboka[0][1] = 'x'
>>> hluboka
[['a', 'x'], 'r', 's']
>>> s
[['a', 'b'], 'r', 's']
>>> 
