# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# zad 1
from typing import List
import math

lista1 = ["siatkowka", "koszykowka", "MMA", "pilka nozna", "pilka reczna"]
lista1.reverse()
lista1.append("kajakarstwo")
lista1.append("boks")
print(lista1)

# zad 2

slownik1 = {'FAQ': 'Frequenly Asked Questions', 'DIY': 'Do It Yourself', 'BTW': 'But The Way'}

print(slownik1)

# zad 3

slownik1 = {'LoL': 'League Of Legends', 'WoW': 'World of Warcraft', 'PoE':'Path of Exile'}
print(len(slownik1))

# zad 4

print('Napisz zdanie:')
x = input()
print(x.count('a'))

# zad 5

a = int(input("liczba1: "))
b = int(input("liczba2: "))
c = int(input("liczba3: "))

print(pow(a,b)+c)

# zad 6
x = int(input("liczba1: "))
y = int(input("liczba2: "))
z = int(input("liczba3: "))

if (x > y and x > z):
    print('liczba x jest najwieksza')
elif (y > x and y > z):
    print('liczba y jest najwieksza')
else:
    print('liczba z jest najwieksza')

# zad 7

a1 = 5
a2 = 3.14
b1=1
b2=1
for n in range(2):
    b1 = b1*a1

for n in range(2):
    b2 = b2*a2

print(b1)
print(b2)

# zad 8
a_list = []

i = 1
while (i < 10):
    i += 1
    if(i % 2 == 0):
        a_list.append(i)

print(a_list)

# zad 9
x3=input("Podaj liczbe")
x3=int(x3)
try:
    if (x3<1):
        raise ValueError
    pierwiastek=math.sqrt(x3)
    print(pierwiastek)
except ValueError:
    print("nieobslugiwana liczba")









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
