# Zapis dat na disk, ve formatu vhodnem pro cteni Pythonem

import sys,pickle

seznam = [dict(id=1,krestni="Franta",prijmeni="Novak"),
          dict(id=2,krestni="Venca",prijmeni="Vopicka")]

fh = None

try:
    fh = open("Vystup.dat","wb")   # wb - write binary
    pickle.dump(seznam,fh,pickle.HIGHEST_PROTOCOL)
    # pickle.dump se obvykle pouziva opakovane
except (EnvironmentError,pickle.PicklingError) as err:
    print(err)
finally:
    if fh:   # totez jako fh not is null (podarilo se otevrit soubor?)
        fh.close()
    print("Hotovo!")
