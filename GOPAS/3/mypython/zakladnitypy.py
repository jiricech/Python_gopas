Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> prvni\ndruhy\treti
SyntaxError: unexpected character after line continuation character
>>> "prvni\ndruhy\treti"
'prvni\ndruhy\treti'
>>> print("prvni\ndruhy\treti"0
      
SyntaxError: invalid syntax
>>> print("prvni\ndruhy\treti")
prvni
druhy	reti
>>> print("prvni\ndruhy\ntreti")
prvni
druhy
treti
>>> cislo=5
>>> print(cislo)
5
>>> list=[0,1,2]
>>> print[list]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print[list]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> list
[0, 1, 2]
>>> list[0]
0
>>> len[list]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    len[list]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> len(list)
3
>>> 
