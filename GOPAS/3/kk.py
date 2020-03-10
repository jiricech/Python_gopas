# movies =["slunce","seno","erotika"]
#
# for item in movies:
#     print (item)
#
# print(movies[2])
#
# count=0
# while count<len(movies):
#     print(movies[count])
#     count+=1
# jiri=["2-18","2:19","2.20"]
#
# def sanitize(time_string):
#         if "-" in time_string:
#             (min,sec)=time_string.split("-")
#             return min+"."+sec
#
#         elif ":" in time_string:
#             (min,sec)=time_string.split(":")
#             return min + "." + sec
#         else:
#             return time_string
#
# for each in jiri:
#     print(sanitize(each))
#
# clean = [sanitize(t) for t in jiri]
# print(clean)
#
# mins = [1, 2, 3]
# secs = [m * 60 for m in mins] #comprehension - one line short zapis
# print(secs)
#
# lower = ["I", "don't", "like", "spam"]
# upper = [s.upper() for s in lower]
# print(upper)
#
# my_set = {1,2,3,4,3,2}
# print(my_set)
#
# # class NamedList(list):
# #     def __init__(self, a_name):
# #     list.__init__([])
# #     self.name = a_name
#
# print('hello')
# print("hello")
# print('"hello"')
# cislo=6//2
# print(cislo)
# a="All"
# b="work"
# c="and"
# print(a+" "+b+" "+c)
#
# P=10000
# r=0.08
# n=12
# t=10
# A=P*(1+(r/n))**(n*t)
# print(A)
#
# def soucin(*a):
#     vysledek = 1
#     for arg in a:	# chape argumenty, definovane pomoci * jako kolekci
#         vysledek *= arg
#     return vysledek
#
# print(soucin(2,6,9))
#
# def sum_of_powers(*args,power=1):
#     vysledek = 0
#     for arg in args:
#         vysledek += arg ** power
#     return vysledek
#
# print(sum_of_powers(5,power=2))
#
# def add_person_details(id,prijmeni,**dalsi_udaje):
# 	print("id:",id)
# 	print("prijmeni:",prijmeni)  # dalsi udaje (pro **) pri VOLANI NUTNO ZADAT
# 	for key in dalsi_udaje:      # ve tvaru POJMENOVANYCH PARAMETRU!!
# 		print("{}: {}".format(key,dalsi_udaje[key]))  # Bere jako slovnik!!
#
#
# def compare(x,y):
#     if x<y:
#         print(x,"je mensi nez",y)
#     elif x>y:
#         print(x,"je vetsi nez",y)
#     else:
#         print("x a y jsou stejne")
#
# print(compare(5,6))
# print(compare(6,5))
# print(compare(5,5))
#
# def triradky():
#     return 3*5
# #    return print("\n\n\n")
#
# #print(triradky())
#
# def ninelines(n):
#     res=n* triradky()
#     return res
#
# print(ninelines(3))
#
# def slope(x1, y1, x2, y2):
#     """
#         >>> slope(5, 3, 4, 2)
#         1.0
#         >>> slope(1, 2, 3, 2)
#         0.0
#         >>> slope(1, 2, 3, 3)
#         0.5
#         >>> slope(2, 4, 1, 2)
#         2.0
#     """
#     if (x2-x1)==0:
#         print("deleni nulou nepripustne")
#     else:
#         return float(y2 - y1)/(x2 - x1)
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
#
#
# print(slope(1,4,1,2))
#
# def intercept(x1, y1, x2, y2):
#     """
#         >>> intercept(1, 6, 3, 12)
#         3.0
#         >>> intercept(6, 1, 1, 6)
#         7.0
#         >>> intercept(4, 6, 12, 8)
#         5.0
#     """
#     m = slope(x1, y1, x2, y2)
#     print(m)
#     return float(y1 - m*x1)
#
# print(intercept(6,1,1,6))
# print(intercept(5,3,4,2))
#
# def iseven(n):
#     if n%2==0:
#         return True
#     else:
#         return False
#
# def isodd(n):
#     return iseven(n)
#
# print(isodd(9))
#
# print(30250%10)
#
#
# def sqrt(n):
#    approx = n/2.0
#    better = (approx + n/approx)/2.0
#    while better != approx:
#        print(better)
#        approx = better
#        better = (approx + n/approx)/2.0
#
#    return approx
#
# sqrt(25)
#
# def triang(x):
#     i=1
#     while i<x:
#         print(i,"\t",i*(i+1)//2)
#         i+=1
# triang(6)
#
#
#
# def is_prime(n):
#     """
#         >>> is_prime(2)
#         True
#         >>> is_prime(3)
#         True
#         >>> is_prime(4)
#         False
#         >>> is_prime(41)
#         True
#         >>> is_prime(42)
#         False
#     """
#     count = 2
#     #so counting starts at 2
#     #as all numbers can be divided by 1 and remainder = 0; and because nothing can be divided by 0
#     while count <= n:
#         if n % count == 0 and count != n:
#             #if when n divided by count remainder is 0
#             #for example when 4 is divided by 2
#             #and to make sure count != n because any number divided by itself then remainder = 0;
#             #then return False
#             return False
#         #if above is not applicable then return true for doctest to pass
#         elif count == n:
#             return True
#         #to make sure it doesnt exit after one try, and it counts
#         elif n % count != 0:
#             count = count + 1
#
# def is_prime(n):
#     """
#         >>> is_prime(2)
#         True
#         >>> is_prime(3)
#         True
#         >>> is_prime(4)
#         False
#         >>> is_prime(41)
#         True
#         >>> is_prime(42)
#         False
#     """
#     count = 2
#     while count <= n:
#         if n % count == 0 and count != n:
#             return False
#         else:
#             count = count + 1
#     return True
#
# print(is_prime(3))
#
# def sum_of_squares_of_digits(n):
#     """
#       >>> sum_of_squares_of_digits(1)
#       1
#       >>> sum_of_squares_of_digits(9)
#       81
#       >>> sum_of_squares_of_digits(11)
#       2
#       >>> sum_of_squares_of_digits(121)
#       6
#       >>> sum_of_squares_of_digits(987)
#       194
#     """
#     sumof = 0
#     while n != 0:
#         sumof += (n % 10)**2
#         print(sumof)
#         n = n//10
#         print(n)
#     return sumof
#
# print(sum_of_squares_of_digits(72))
# print(7%10)

def print_multiples(n, high):

   i = 1
   while i <= high:
       print (n*i, '\t',end="")
       i += 1
   print()

def print_mult_table(high):
    i = 1
    while i <= high:
        print_multiples(i, high)
        i += 1

print(print_multiples(5,5))
print(print_mult_table(5))


    # """
    #   >>> print_digits(13789)
    #   9 8 7 3 1
    #   >>> print_digits(39874613)
    #   3 1 6 4 7 8 9 3
    #   >>> print_digits(213141)
    #   1 4 1 3 1 2
    # """

def print_digits(n):
    new = []
    index = ""
    number = str(n)
    for char in reversed(number):
        new.append(char)
    print(new)

    for w in new:
         index = index + w
    return int(index)

print(print_digits(13789))
# fruit="banana"
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print (letter,end="")
#     index += 1
# for char in fruit:
#     print (char,end="")


#s=len("happy")
#print(s)
# def reverse(s):
#     x = 1
#     while x <= len(s):
#         length = len(s)
#         #print(length)                             h,a,p,p,y
#         lastoutput = s[length - x] #length 5-1 =4 (0,1,2,3,4) =y, length 5-2 =3 =p,....
#         print (lastoutput,end="")
#         x += 1

def reverse(s):
    last = ""
    x = 1
    while x <= len(s):
        lastoutput = s[-x]
        last += lastoutput
        x += 1
    return last
print(reverse("happy"))


#################################################################################################################
# colors=["red","blue","yellow","pink","green"]
# names=["jiri","paja","josef","petr"]

# for i in range(len(colors)):
#     print (i,"-->",colors[i])
# print (len(colors))
# print (range(5))

# for i,color in enumerate(colors):
#     print (i,"-->",colors[i])
#
#print (list(enumerate(colors)))
#
# n=min(len(names),len(colors))
# for i in range(n):
#     print (names[i],"-->",colors[i])
#
# for name,color in zip(names,colors):   #vytvari treti list v pameti, ktera obsahuje tuples a zabira tak mnoho pameti, proto je lepsi pouzit izip funkci.
#     print (name,"-->",color)
#
# for name,color in izip(names,colors):   #You can convert any iterable into a list with the list function, i.e. n = list(zip(names, colors)), V python 3 dela zip to "same" jako izip.
#     print (name,"-->",color)
# print(n)
# print(len(colors))
#
# x=min(4,5)
# print (x)

# for color in sorted(colors): #seradi podle pocatecniho indexu abecedy
#     print (color)
#
# for color in sorted(colors,reverse=True): #seradi podle pocatecniho indexu abecedy nazpet
#     print (color)
#
#
# print (sorted(colors,key=len)) #seradi dle delky klice v seznamu colors,tj. "red" je prvni a "yellow" je posledni.
# # ( plati to i pro ostatni collection jako je tuples (),dict{key:value},list[],set{}.

#from functools import partial
# blocks=[]
# while True:
#     block=f.read(32)   #Call function until sentinel value, i.e sentinel value is "".
#     if block =="":
#         break
#     blocks.append(block)
#
# blocks=[]
# for block in iter(partial(f.read,32),""): #iter() method is used to convert an iterable to iterator. This presents another way to iterate the container i.e access its elements. iter() uses next() for accessing values.
#     blocks.append(block)                    #Partial functions allow us to fix a certain number of arguments of a function and generate a new function.
# #iter function can take two arguments,i.e. first argument is a function (f.read(32)) that you call over and over again and the second argument is a sentinel argument ("") and it says it will call read 32 over and over again looping one block at the time.

# # A normal function
# def f(a, b, c, x):
#     return 1000 * a + 100 * b + 10 * c + x
# # A partial function that calls f with
# # a as 3, b as 1 and c as 4.
# g = partial(f, 3, 1, 4)
# # Calling g()
# print(g(5))         #output is 3145
#
#
# # A normal function
# def add(a, b, c):
#     return 100 * a + 10 * b + c
# # A partial function with b = 1 and c = 2
# add_part = partial(add, c=2, b=1)
# # Calling partial function
# print(add_part(3))      #output is 312

#############################################looping over dictionary keys###################################
# d={"jirka":"green","josef":"blue","tatka":"orange","mamka":"pink"}


#
# for k in d.keys():  # d.keys() calls the keys arguments and makes a copy of all the keys and stores them in list.
#     if k.startedwith("j"):
#         del d[k]
#
# d={k:d[k] for k in d if not k.startswith("j")}  #jednoradkovy zapis...

#
# for k in d:
#      print(k,"-->",d[k])
#
# for k,v in d.items():
#     print(k, "-->", v)
# ###############################################Construct dictionary from pairs###################################
# colors=["red","blue","yellow","pink","green"]
# names=["jiri","paja","josef","petr"]
#
# d=dict(zip(colors,names))
# print(d)
#
# ###################################################Counting with dictionary#####################################
# colors=["red","blue","red","yellow","pink","green","green","red"]
# d={}
# for color in colors:
#     if color not in d:
#         d[color]=0
#         print(d)
#     d[color]+=1
# print(d)
#
# d={}
# for color in colors:               #syntaxe: Dict.get(key, default=None)
#         d[color]=d.get(color,0)+1  #returning 0,  get() method returns the value for the given key, if present in the dictionary.
#                                                 # If not, then it will return None (if get() is used with only one argument).
#
#
#
# from collections import defaultdict
#
# d=defaultdict(int)  #int argument can be called with no argument producing the value zero
# for color in colors:
#     d[color]+=1
#
# print(d)

#################################################Grouping with dictionaries##################################################

names=["jiri","paja","josef","petr","milan","oldrich","bedrich"]

# d={}
# for name in names:
#     key=len(name)
#     if key not in d:
#         d[key]=[]
#     d[key].append(name)
#
# d={}
# for name in names:
#     key=len(name)
#     d.setdefault(key,[]).append(name)

from collections import defaultdict
d=defaultdict(list)  #deafaultdict(list) will create new list and final output of this list is {4: ['jiri', 'paja', 'petr'], 5: ['josef', 'milan'], 7: ['oldrich', 'bedrich']}
for name in names:
    key=len(name)
    d[key].append(name)

print(d)

######################################################doctest.testmode() ############################################
#doctest.testmetod()
#(0,4)                                #samotny doctest navrati nicnevypovidajici hodnoty 0 a 4,
#doctest.testmetod()
#TestResult(failed=0,attempted=4)     # pokud budu chtit popis s vyznamem techto hodnot jako je napr.failed a attempted,pak
                                      # je to mozne pomoci funkce namedtuple, viz nize...
# from collections import namedtuple
#TestResults=namedtuple("TestResults",["failed","attempted"])

#######################################################FFFFFFIBONACI##########################################################
def fibonaci (n):
    x=0
    y=1
    for i in range(n): #0
        print(x)       #x=0         0   1   1   2   3   5   8...............
        t=y            #t=5y        1   1   2   3   5   8
        y=x+y          #5y=0+5y     1   2   3   5   8   13
        x=t            #0x=5y       1   1   2   3   5   8


print(fibonaci(8))  #vystupem je vzdy soucet prvnich dvou,tj. 0,1,1,2,3,5...

def fibonaci_2(n):
    x,y=0,1
    for i in range(n):
        print(x)            #0      1       1       2       3...............
        x,y=y,x+y           #1,1    1,2     2,3     3,5
print(fibonaci_2(8))

#####################################################################Conactenating Strings################################
names=["jiri","paja","josef","petr","milan","oldrich","bedrich"]

# s=names[0]
# for name in names[1:]:
#     s+=","+ name
#     print(s)

print(",".join(names))   #output is jiri,paja,josef,petr,milan,oldrich,bedrich
print("$".join(names))   #output is jiri$paja$josef$petr$milan$oldrich$bedrich







