Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Regularni vyrazy v Pythonu
>>> 
>>> import re
>>> p = re.compile('[a-z]+')	# "kompilace" regularniho vyrazu
>>> m = p.match('xyz123')
>>> m.group()
'xyz'
>>> m.start()			# pocatek shody (match VZDY 0 - hleda jen na zacatku!!)
0
>>> m.end()			# konec (pozice z koncem)
3
>>> m.span()
(0, 3)
>>> # Nenajde-li shodu (match na zacatku), vrati None!!
>>> # Standardni pouziti match ( i dalsi vyhledavaci metody):
>>> m = p.match('123abc')
>>> if m:  # pri neshode None (=False)
	print("Shoda nalezena:",m.group(),"od:",m.start(),"do:",m.end())
else:
	print("Neshoduje se (na zacatku)")

	
Neshoduje se (na zacatku)
>>> 
>>> # Nalezeni shody kdekoli:
>>> m = p.search('123xyz567')
>>> m.group()
'xyz'
>>> m.start()
3
>>> # vyhledani vsech shod v retezci:
>>> p = re.compile(r'\d+') # cislice
>>> matches = p.findall('11 je prvocislo, i 13 a take 19')
>>> matches
['11', '13', '19']
>>> 

>>> # Iterator - nevytvori cely seznam shod, vraci prvky postupne:
>>> iterator = p.finiter('11 je prvocislo, i 13 a take 19')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    iterator = p.finiter('11 je prvocislo, i 13 a take 19')
AttributeError: 're.Pattern' object has no attribute 'finiter'
>>> iterator = p.finditer('11 je prvocislo, i 13 a take 19')
>>> for match in iterator:
	print(match.group())

	
11
13
19
>>> 
>>> # Module-level functions: match, search, findall, finditer
>>> re.match('[a-z]+','abc123').group()
'abc'
>>> # Case senzitivity:
>>> p = re.compile('[a-z]+')
>>> m = p.match('ABC123')    # nepozna velka
>>> print(m)
None
>>> # Compile flags - nastaveni vlstnosti vyhledavani
>>> p = re.compile('[a-z]+',re.IGNORECASE) # nerozlisovat mala/velka
>>> m = p.match('ABC123')
>>> m.group()
'ABC'
>>> 
>>> # Grouping (subpatterns - podvzory) - podvzory jsou urceny zavorkami v re:
>>> p = re.compile('(a(b)c)d')
>>> p = re.compile('(a(b)c)d')
>>> m = p.match('abcd')
>>> m.group()
'abcd'
>>> m.group(0) 		# opet cela shoda
'abcd'
>>> m.group(1) 		# retezec, odpovidajici 1. podvzoru
'abc'
>>> m.group(2) 		# 2. podvzor
'b'
>>> # Upravy stringu pomoci regularnich vyrazu:
>>> # split - rozdeli retezec podle oddelovace (re)
>>> p = re.compile(r'\W+') # oddelovace jsou skupiny znaku, ktere
>>>                        # NEpatri do "word" - [^A-Za-z0-9_]
                       
>>> p.split("Slova,jeste   slova  a dalsi   slova")
['Slova', 'jeste', 'slova', 'a', 'dalsi', 'slova']
>>> 
>>> # Tato a dalsi metody existuji i ve forme module level
>>> 
>>> # Search and replace
>>> p = re.compile('(Franta|Eva|Karel)')
>>> p.sub('zamestnanec','U nas pracuje Franta, Eva, Karel a Jirka')
'U nas pracuje zamestnanec, zamestnanec, zamestnanec a Jirka'
>>> p.sub('zamestnanec','U nas pracuje Franta, Eva, Karel a Jirka',count=2)
'U nas pracuje zamestnanec, zamestnanec, Karel a Jirka'
>>> # # count - max. pocet nahrazeni
>>> p.subn('zamestnanec','U nas pracuje Franta, Eva, Karel a Jirka')
('U nas pracuje zamestnanec, zamestnanec, zamestnanec a Jirka', 3)
>>> # ve vracenem tuple je 2. polozka pocet nahrazeni
>>> 
