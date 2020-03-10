# Pouziti modulu Matika

# Varianta 1
##import Matika
##
### print(pi)  # chyba - ma byt Matika.pi
##
##print(Matika.pi)
##
##print(Matika._tajne)
##
##print(Matika.soucet(4,7))
##
##print(Matika.rozdil(4,7))

# Varianta 2
##from Matika import *
##
##print(pi)
##
### print(_tajne) # chyba - promenne zacinajici _ NEIMPORTUJE!!
##
##print(soucet(4,7))
##
##print(rozdil(4,7))

# Varianta 3
from Matika import *  # importuje POUZE to, co je uvedeno v __all__

print(pi)

print(soucet(4,7))

# print(rozdil(4,7))    # chyba - neni uvedeno v __all__


