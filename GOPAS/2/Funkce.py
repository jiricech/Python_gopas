Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Funkce
>>> 
>>> # definice funkce
>>> def soucet(a,b):
	retun a + b
	
SyntaxError: invalid syntax
>>> def soucet(a,b):
	return a + b

>>> # volani funkce
>>> soucet(2,3)
5
>>> # return u ktereho neni hodnota - jen navrat z funkce (z "procedury" - C void)
>>> 
>>> # funkce jsou objekty - lze je prirazovat
>>> sum = soucet
>>> sum(4,8)
12
>>> # Funkce MUSI pri volani dodrzet definovany pocet parametru:
>>> soucet(1)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    soucet(1)
TypeError: soucet() missing 1 required positional argument: 'b'
>>> soucet(1,2,3)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    soucet(1,2,3)
TypeError: soucet() takes 2 positional arguments but 3 were given
>>> 
>>> # Funkce s defaultnimi (implicitnimi, preddefinovanymi) hodnotami parametru
>>> def letter_count(text,letters="abcdefghijklmnopqrstuvwxyz"):
	# 2. parametr ma preddefinovanou hodnou - nemusim ji pri volani zadavat (pouzije)
	count = 0
	for char in text:
		if char in letters:
			count += 1
	return count

>>> letter_count("Dobrý den!") # pouzije default 2. param
6
>>> letter_count("Dobrý den!","aeiouy")
2
>>> # Named (pojmenovane, klicovane) parametry
>>> def shorten(text,length=25,indicator=" ..."):
	if len(text) > length:
		text = text[:length - len(indicator)] + indicator
	return text

>>> shorten("Kratky text")
'Kratky text'
>>> shorten(length=10,text="Zkracovany text")
'Zkraco ...'
>>> # POJMENOVANE parametry (length=10) mohu zadat v LIBOVOLNEM poradi
>>> # (priradi spravne). Dale lze vynechat parametry s default hodnotami.
>>> 
>>> # Dokumentacni retezce u funkci (slouzi i pri ladeni)
>>> def shorten(text,length=25,indicator=" ..."):
	""" Vraci text nebo jeho orezanou kopii s pripojenym indicatorem

	    - text je libovolny retezec
	    - length je max. pripustna delka retezce
	      (vcetne pripojeneho indicatoru)
	    - indicator je retezec, pripojeny na konec, ktery signalizuje
	      zkraceni retezce text

	    Dale jsou priklady, ktere umoznuji "automaticky"
	    testovat funkci. Casti za >>> prave umoznuji automaticke testy

	    
	"""
	if len(text) > length:
		text = text[:length - len(indicator)] + indicator
	return text
KeyboardInterrupt
>>> def shorten(text,length=25,indicator=" ..."):
	""" Vraci text nebo jeho orezanou kopii s pripojenym indicatorem

	    - text je libovolny retezec
	    - length je max. pripustna delka retezce
	      (vcetne pripojeneho indicatoru)
	    - indicator je retezec, pripojeny na konec, ktery signalizuje
	      zkraceni retezce text

	    Dale jsou priklady, ktere umoznuji "automaticky"
	    testovat funkci. Casti za >>> prave umoznuji automaticke testy

	    >>> shorten("Kratky text")
	    'Kratky text'

            >>> shorten(length=10,text="Zkracovany text")
            'Zkraco ...'	    
	"""
	if len(text) > length:
		text = text[:length - len(indicator)] + indicator
	return text

>>> # Funkce s libolnym poctem parametru
>>> def soucin(*args):
	vysledek = 1
	for arg in args:	# chape argumenty, definovane pomoci * jako kolekci
		vysledek *= arg
	return vysledek

>>> soucin(2,3)
6
>>> soucin(2,3,4,5)
120
>>> # Kombinace *args a pojmenovanych parametru
>>> def sum_of_powers(*args,power=1):
	vysledek = 0
	for arg in args:
		vysledek += arg ** power
	return vysledek

>>> sum_od_powers(1,2,3)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    sum_od_powers(1,2,3)
NameError: name 'sum_od_powers' is not defined
>>> sum_of_powers(1,2,3)
6
>>> sum_of_powers(1,2,3,power=2)
14
>>> def sum_of_powers(power=1,*args):
	vysledek = 0
	for arg in args:
		vysledek += arg ** power
	return vysledek

>>> sum_of_powers(1,2,3,power=2)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    sum_of_powers(1,2,3,power=2)
TypeError: sum_of_powers() got multiple values for argument 'power'
>>> 
>>> # hvezdicka mezi parametry
>>> import math
>>> def heron(a,b,c,*,units="m2")
SyntaxError: invalid syntax
>>> def heron(a,b,c,*,units="m2"):
	s = (a + b + c)/2
	area = math.sqrt(s*(s-1)*(s-b)*(s-c))
	return "{} {}".format(area,units)

>>> heron(25,24,7)
'252.0 m2'
>>> # parametry za * (v definici) MUSEJI byt pri VOLANI pojmenovane!!
>>> heron(25,24,7,"cm2")  # chyba - "cm2" NENI pojmenovany!!
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    heron(25,24,7,"cm2")  # chyba - "cm2" NENI pojmenovany!!
TypeError: heron() takes 3 positional arguments but 4 were given
>>> heron(25,24,7,units="cm2")  # OK
'252.0 cm2'
>>> 
>>> # Pouziti ** pri VOLANI (pouziti slovniku - dictionary)
>>> def print_setup(paper="letter",copies=1,color=False):
	print(paper,copies,color)

	
>>> print_setup()
letter 1 False
>>> print_setup(paper="A4")
A4 1 False
>>> print_setup(paper="A4",copies=2,color=True)
A4 2 True
>>> # Parametry pripominaji dictionary
>>> 
>>> # Definujeme dictionary
>>> options = dict(paper="A4",copies=2,color=True)
>>> options
{'paper': 'A4', 'copies': 2, 'color': True}
>>> 
>>> # pouziti dictionary misto jednotlivych parametru - chybne!!
>>> print_setup(options)
{'paper': 'A4', 'copies': 2, 'color': True} 1 False
>>> 
>>> # Spravne pouziti dictionary - "rozbalenim" slovniku pomoci **
>>> print_setup(**options)
A4 2 True
>>> # jako parametry byl pouzit "vnitrek definice slovniku"
>>> 
>>> # Pouziti ** v DEFINICI funkce
>>> def add_person_details(id,prijmeni,**dalsi_udaje):
	print("id:",id)
	print("prijmeni:",prijmeni)  # dalsi udaje (pro **) pri VOLANI NUTNO ZADAT
	for key in dalsi_udaje:      # ve tvaru POJMENOVANYCH PARAMETRU!!
		print("{}: {}".format(key,dalsi_udaje[key]))  # Bere jako slovnik!!


		      
>>> add_person_details(123,"Novak",krestni="Franta",vek=25,pohlavi="muz")
id: 123
prijmeni: Novak
krestni: Franta
vek: 25
pohlavi: muz
>>> 
>>> 
>>> # Pristup ke globalnim promennym
>>> jazyk = "en"
>>> 
>>> # jazyk - globalni promenna
>>> 
>>> def zobraz_jazyk():
	if jazyk == "en":
		print("Anglictina")
	elif jazyk == "cz":
		print("Cestina")
	else:
		print("Jiny jazyk")

		
>>> zobraz_jazyk()
Anglictina
>>> jazyk = "cz"
>>> zobraz_jazyk()
Cestina
>>> # z funkce MOHU CIST globalni promenne (vytvorene pred volanim funkce)
>>> 
>>> # funkce, zevnitr ktere chci MENIT globalni promennou
>>> def nastav_jazyk(lang):
	jazyk = lang

	
>>> jazyk = "en"
>>> 
>>> nastav_jazyk("cz")
>>> jazyk
'en'
>>> # Prirazeni UVNITR funkce vytvorim NOVOU LOKALNI promennou ve funkci
>>> # (ta zakryje stejnojmennou globalni)
>>> 
>>> def nastav_jazyk(lang):
	global jazyk	# pracovat s GLOBALNI promennou jazyk, NEVYTVARET novou lokalni!!
	jazyk = lang

	
>>> jazyk
'en'
>>> nastav_jazyk("cz")
>>> jazyk
'cz'
>>> 
>>> # Lambda funkce (lambda vyrazy)
>>> # Nejprve klasicka funkce
>>> def koncovka(count):
	if count == 1:
		return ""
	else:
		return "s"

	
>>> koncovka(1)
''
>>> koncovka(3)
's'
>>> # Totez jako lambda vyraz
>>> lambda x: "" if x == 1 else "s"
<function <lambda> at 0x00000000030A89D8>
>>> s = lambda x: "" if x == 1 else "s"
>>> s(1)
''
>>> s(3)
's'
>>> # Realistictejsi priklad:
>>> def volej_funkce(f,arg): # f - funkce, arg - jeji parametr
	return f(arg)

>>> # Pouziti s klasickou funkci
>>> def mocnina(x):
	return x * x

>>> volej_funkci(mocnina,4)
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    volej_funkci(mocnina,4)
NameError: name 'volej_funkci' is not defined
>>> volej_funkce(mocnina,4)
16
>>> # Nyni s lambda funkci
>>> volej_funkce(lambda x: x*x,5)
25
>>> 
