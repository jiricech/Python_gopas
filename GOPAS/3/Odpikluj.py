# Nacteni dat, zapsanych pomoci pickle

import sys,pickle

seznam = []

fh = None

try:
    fh = open("Vystup.dat","rb")  # rb - read binary
    seznam = pickle.load(fh)
    print(seznam)

except (EnvironmentError,pickle.PicklingError) as err:
    print(err)
finally:
    if fh:
        fh.close()
