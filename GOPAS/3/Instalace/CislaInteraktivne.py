# Program cte data ze vstupu a zpracovava

count = 0
total = 0

while True:         # nekonecny cyklus
    line = input("Cislo: ")
    if line:        # neni-li prazdny retezec line (totez jako: if line != "": )
        try:
            number = int(line)
        except ValueError as err:
            print("Chyba:",err)
            continue # pokracovat - zacit dalsi cyklus

        total += number
        count += 1
        
    else:           # zmackl jen Enter - konec
        break       # break opusti cyklus (ukonci jej)

if count:           # totez jako count != 0 (zadal alespon 1 cislo?)
    print("Pocet=",count,"Soucet=",total,"Prumer=",total/count)
else:
    print("Nebylo zadano zadne platne cislo")
