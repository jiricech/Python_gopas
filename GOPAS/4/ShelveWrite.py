# Zapis dat typu klic/hodnota pomoci shelve

import shelve

adresar = shelve.open("adresy") # v praxi try/except

adresar["policie"] = ["Policie CR","158"]
adresar["hasici"] = ["Hasicsky sbor","150"]
# ...

adresar.close()

print("Hotovo!")
