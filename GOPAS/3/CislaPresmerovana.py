# Program cte i data z presmerovaneho vstupu (souboru)
# Napr.: Python CislaPresmerovana.py < Cisla.txt

count = 0
total = 0

while True:
    try:
        line = input()
        if line != "":
            number = int(line)
            total += number
            count += 1
        else:
            break
    except ValueError as err:
        print("Chyba:",err)
        continue
    except EOFError:    # konec souboru - ukoncit cyklus
        print("Konec souboru")
        break

if count != 0:          
    print("Pocet=",count,"Soucet=",total,"Prumer=",total/count)
else:
    print("Nebylo zadano zadne platne cislo")
