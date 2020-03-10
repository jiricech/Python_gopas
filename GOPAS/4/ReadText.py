# Cteni textoveho souboru po radcich

import io

fh = None

try:
    fh = open("Clovek.txt",encoding="utf8") # neuvadim rezim (r - read - je default)

    while True:
        line = fh.readline()
        if line == "":  # cteni za koncem souboru vrati prazdny retezec
            break       # .readline() v Pythonu "neoholuje" \n -> i v
                        # "opticky prazdnych" radcich je obsazen alespon \n (neni to "")
        print(line,end='')  # end - neodradkovavat po print (\n je obsazen v nactenych datech)

except IOError as err:
    print(err)
finally:
    if fh:
        fh.close()

            
