Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Formatovani (Python 2.x a 3.x vyrazne odlisne)
>>> 
>>> "Kamarad {0} se narodil v roce {1}".format("Jirka",1980)
'Kamarad Jirka se narodil v roce 1980'
>>> "Kamarad {jmeno} se narodil v roce {rok}".format(jmeno="Jirka",rok=1980)
'Kamarad Jirka se narodil v roce 1980'
>>> # Prametrem metody format je seznam
>>> sklad = ["pocitac","notebook","tablet","mobil"]
>>> "Na skladu mame {0[0]} a {0[3]}".format(sklad)
'Na skladu mame pocitac a mobil'
>>> # Parametrem je dictionary
>>> d = dict(zvire="pes",vaha=40)
>>> "Nas {0[zvire]} vazi {0[vaha]}kg.".format(d)
'Nas pes vazi 40kg.'
>>> # Parametr promenna
>>> prvek = "Vodik"
>>> cislo = 1
>>> "Prvek {prvek} je elementem c. {cislo}".format(**locals())
'Prvek Vodik je elementem c. 1'
>>> # Parametr je modul
>>> import math,sys
>>> "pi={0.pi}; platform={1.platform}".format(math,sys)
'pi=3.141592653589793; platform=win32'
>>> 
>>> # zjednoduseni
>>> i = 1
>>> k = 3
>>> "Prvni cislo {}, druhe cislo {}".format(i,k)
'Prvni cislo 1, druhe cislo 3'
>>> # dosadil  do svorek podle poradi
>>> # "f stringy"
>>> jmeno = "Franta"
>>> f"Muj kamarad se jmenuje {jmeno}"
'Muj kamarad se jmenuje Franta'
>>> # uvnit svorek {} za dvojteckou mohu uvadet dalsi informace (pocet des. mist apod.)
>>> 
>>> # Nektere moznosti:
>>> # zarovnani: < - vlevo, ^ - na stred, > - vpravo
>>> # znamenko:  + - vynucene (vzdy), - jen, je-li potreba
>>> # pred cele cislo lze vypsat prefix: 0b, 0x (hexa), ...
>>> # 0 - vyplnit do dane sirky nulami (nebo jinym znakem)
>>> # , - oddelovac tisicu
>>> # lze zadat presnost pro float, typ pro int: b, x (hexa), ...
>>> 
>>> s = "Krasny den"
>>> "{0}".format(s)
'Krasny den'
>>> "{0:25}".format(s)		' 25 - sirka pole
SyntaxError: EOL while scanning string literal
>>> "{0:25}".format(s)		# 25 - sirka pole
'Krasny den               '
\
>>> "{0:>25}".format(s)		# 25 - sirka pole; zarovnani vpravo
'               Krasny den'
>>> "{0:^25}".format(s)		# 25 - sirka pole; zarovnani na stred
'       Krasny den        '
>>> "{0:-^25}".format(s)	# 25 - sirka pole; zarovnani na stred + vyplnit znakem -
'-------Krasny den--------'
>>> "0:0=3".format(7)
'0:0=3'
>>> "{0:0=3}".format(7)
'007'
>>> 
>>> # Konverze znakovych sad
>>> text = "žluťoučký"
>>> text.encode("utf-16")
b'\xff\xfe~\x01l\x00u\x00e\x01o\x00u\x00\r\x01k\x00\xfd\x00'
>>> 
