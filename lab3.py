# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

a = []
for x in range(0, 10):
    a.append(x**2)
print(a)
b = []
for x in range(0,6):
    b.append(3**x)
print(b)
b2 = [3**x for x in range(0, 6)]
print(b2)

a2 = []
for x in a:
    if(x % 2 != 0):
        a2.append(x)
print(a2)

a3 = [x for x in a if(x % 2 != 0)]
print(a3)


lista = []
for a in [1, 2, 3]:
    for b in [4, 5, 6]:
        lista.append((a,b))
print(lista)
lista2 = [(a,b) for a in [1, 2, 3] for b in [4, 5, 6]]
print(lista2)

slownik = {'PZU': 'Państwowy zakład ubezpieczeń',
           'ZUS': 'Zakład ubezpieczeń społecznych',
           'Wysocki': 'Drakul'}
slownik_odwrocony = {}
for key, value in slownik.items():
    slownik_odwrocony[value] = key
print(slownik_odwrocony)
print(slownik)
slownik2 = {value: key for key, value in slownik.items()}
print(slownik2)

def row_kwadratowe(a, b, c):
    delta = b**2-(4*a*c)
    if delta < 0:
        print('Mniejsze wieksze')
        return -1
    elif delta == 0:
        print('jedno rozwiazanie')
        x = (-b)/(2*a)
        return x
    else:
        print('dwa rozwiazania')
        x1 = ((-b) - math.sqrt(delta))/(2*a)
        x2 = ((-b) + math.sqrt(delta))/(2*a)
        return x1,x2


print(row_kwadratowe(6,1,3))
print(row_kwadratowe(1,2,1))
print(row_kwadratowe(1,4,1))

def parzysta(a):
    if(a % 2 == 0):
        return 'liczba jest parzysta'
    else:
        return 'liczba jest nieparzysta'
print(parzysta(5))

def dlugosc_odcinka(x1=1, y1=2, x2=3, y2=4):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(dlugosc_odcinka())
print(dlugosc_odcinka(2,1,3,7))
print(dlugosc_odcinka(1, 1, y2=8, x2=7))
print(dlugosc_odcinka(y2=3, x1=5, y1=6, x2=0))
print(dlugosc_odcinka(y2=1, x2=6))

def ciag(* liczba):
    if len(liczba) == 0:
        return 0
    else:
        suma = 0
        for i in liczba:
            suma += i
        return suma

print(ciag())
print(ciag(1, 2, 3, 4, 5, 6, 7, 8, 9))

def co_lubie(** rzeczy):
    for cos in rzeczy:
        print('lubie')
        print(cos)
        print('co lubie')
        print(rzeczy[cos])

co_lubie(gry=['planszowe', 'komputerowe'])
