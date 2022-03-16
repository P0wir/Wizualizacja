import math
import random

#zad 1

a = []
for x in range(1, 11):
    a.append(1-x)
print(a)

b = []
for x in range(0,8):
    b.append(math.pow(4,x))
print(b)

c = []
for x in b:
    if(x % 2 == 0):
        c.append(x)
print(c)

#zad 2

lista1 = []

for x in range(0,10,1):
    lista1.append(random.randint(0, 100))

print(lista1)

lista2 = []
for x in lista1:
    if(x % 2 == 0):
        lista2.append(x)
print(lista2)

#zad 3

produkty={'szynka':"kg", "mleko":"litry", "Cukierki":"kg","jajka":"Sztuki"}
print(produkty)
produkty2={key:value for key, value in produkty.items() if value=="Sztuki"}
print(produkty2)

#zad 4

def trojkat_prostokatny(a, b, c):
    if(pow(a,2) + pow(b,2) == pow (c,2)):
        return 'trojkat jest prostakatny'
    else:
        return 'trojat nie jest prostokatny'
print(trojkat_prostokatny(3,4,6))


#zad 5

def Pole_trapezu(a=2, b=3, h=4):
    P = ((a+b)*h)/2
    return P
print(Pole_trapezu(2,3,4))

#zad 6

def ciag(a1=1,b=4,ile=10):
    for x in range(ile):
        a1=a1*b
    return a1
print(ciag())

