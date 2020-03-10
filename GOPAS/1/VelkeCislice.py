import sys   # zpristupneni modulu sys (kvuli cteni parametru prikazove radky)

Zero = ["   ***   ",
        " *     * ",
        "*       *",
        "*       *",
        "*       *",
        " *     * ",
        "   ***   "]
One = [" * ",
       "** ",
       " * ",
       " * ",
       " * ",
       " * ",
       "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero,One,Two,Three,Four,Five,Six,Seven,Eight,Nine]

try:
    cislo = sys.argv[1]
    # print(cislo)

    for indexHvezdicek in range(0,len(Zero)):   # cyklus pres vsechny radky hvezdicek
        line = ""   # budouci radek hvezdicek
        for cislice in cislo:  # cyklus pres cislice nacteneho cisla
            indexCislice = int(cislice)
            velkaCislice = Digits[indexCislice]
            line += velkaCislice[indexHvezdicek] + " "  # " " - odsazeni mezi cislicemi
        print(line)

except IndexError:  # nezadal argument (cislo); argv ma delku 1 (pouze index 0)
    print("Pouziti:",sys.argv[0],"<cislo>") # argv[0] - jmeno programu
except ValueError:
    print("Chybne zadane cislo:",cislo)
