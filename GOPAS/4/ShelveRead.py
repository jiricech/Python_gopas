# Cteni dat (podle klice) pomoci shelve

import shelve

adresar = shelve.open("adresy")

print(adresar["hasici"]) # prime nacteni polozky podle klice

adresar.close()
