# Zapis textoveho souboru po radcich

import io

clovek = [1,"Franta","Novak"]

fh = None

try:
    fh = open("Clovek.txt","w",encoding="utf8") # otevrit soubor pro zapis - vytvorit (w)
    for polozka in clovek:
        fh.write(str(polozka) + "\n")  # \n - odradkovat (chci samostatny radek pro
                                       # kazdou polozku; str(...): 1 -> string

except IOError as err:
    print(err)
finally:
    if fh:          # if not fh is None - totez; podarilo se vytvorit soubor?
        fh.close()  # zavreni souboru
    print("Hotovo!")
