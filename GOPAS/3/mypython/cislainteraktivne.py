#program cte data ze vstupu a zpracovava
count=0
total=0
while True:     #nekonecny cyklus
    line=input("Cislo:")
    if line: #neni li prazdny retezec line
        try:
               number=int(line)
        except VauleError as err:
               print("chyba:",err)
               continue
        total+=number
        count+=1
    else:
        break
if count:
    print ("Pocet=",count,"Soucet=",total,"Prumer=",total/count)
else:
    print ("Nebylo zadano zadne platne cislo")
    
