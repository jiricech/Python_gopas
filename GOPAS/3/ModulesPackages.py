Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> # Importovani modules and packages
>>> 
>>> os.path.basename(r"c:\data\texty\dopisy\dopis.txt")  # chyba - neni import!
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    os.path.basename(r"c:\data\texty\dopisy\dopis.txt")  # chyba - neni import!
NameError: name 'os' is not defined
>>> 
>>> import os
>>> os.path.basename(r"c:\data\texty\dopisy\dopis.txt")  # OK
'dopis.txt'
>>> 
>>> # V jednom importu lze uvest vice modules a packages
>>> # import m1,m2,m3
>>> 
>>> # Je mozne pojmenovat importovane - MUZE nastat kolize se jmenem promenne!!
>>> import os.path as cesta
>>> cesta.basename(r"c:\data\texty\dopisy\dopis.txt")
'dopis.txt'
>>> cesta = 5
>>> cesta.basename(r"c:\data\texty\dopisy\dopis.txt") # chyba - prepsano!!
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    cesta.basename(r"c:\data\texty\dopisy\dopis.txt") # chyba - prepsano!!
AttributeError: 'int' object has no attribute 'basename'
>>> 
>>> # Import vklada IMPORTOVANE JMENO do tabulky promennych interpretu!!
>>> # Tabulka jmen je dictionary, ke ktere se dostanu takto:
>>> locals()["os"]
<module 'os' from 'C:\\Program Files\\Python37\\lib\\os.py'>
>>> 
>>> import os.path as cesta
>>> locals()["cesta"]
<module 'ntpath' from 'C:\\Program Files\\Python37\\lib\\ntpath.py'>
>>> 
>>> # lze importovat i jednotlive funkce, promenne, ...
>>> from os.path import basename
>>> basename(r"c:\data\texty\dopisy\dopis.txt")
'dopis.txt'
>>> locals()["basename"]
<function basename at 0x0000000001D41EA0>
>>> # opet lze importovat vice polozek
>>> # from importovatelne import f1,f2,f3
>>> # lze opet prejmenovat
>>> # pro jednotlive funkce a promenne je jeste vetsi riziko prepsani
>>> 
>>> # lze importovat "vse" z modulu/package:
>>> # from importovatelne import *
>>> 
>>> # Pri importu pomoci * importuji "vse co neni soukrome".
>>> # Importuji tedy vse, co nezacina znakem _ ("soukrome" promenne)
>>> # Je-li definovana promenna __all__ potom * importuje POUZE to,
>>> # co je uvedeno v __all__ (coz je seznam)
>>> 
>>> # Modul je obycejny soubor s Pythonovskym kodem (a pripadnym __all__).
>>> # Package je adresar, ve kterem jsou soubory (moduly) a soubor __init__.py
>>> # V tom je opet promenna __all__ = ["Bmp","Jpg","Png"] (mame-li napr.
>>> # moduly Bmp.py, Jmg.py a Png.py ... v danem adresari a budu-li chtit
>>> # importovat pomoci * (opet importuji pouze to, co je v __all__ v __init__.py)
>>> 
>>> # Packages lze vnorovat (jsou to adresare). Oddelovace packages, modulu
>>> # (ale i funkci a promennych, ...) je tecka
>>> 
>>> # Cesta, odkud Python nacita modules a packages: jednak adresar, kde je importujici
>>> # soubor (program).  Dale lze pouzit environment promennou PYTHONPATH (do te napiseme
>>> # jmena adresaru, ktere se maji prohledavat)
>>> 
>>> # Standardne pouzite cesty jsou v sys.path
>>> 
>>> import sys
>>> sys.path
['', 'C:\\Program Files\\Python37\\Lib\\idlelib', 'C:\\Program Files\\Python37\\python37.zip', 'C:\\Program Files\\Python37\\DLLs', 'C:\\Program Files\\Python37\\lib', 'C:\\Program Files\\Python37', 'C:\\Program Files\\Python37\\lib\\site-packages']
>>> 
