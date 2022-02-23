import sys
import math

print(sys.version)

a = "inżynieria systemów informatycznych"
print(a)

b=5
print(b)

c = 5.25
print(c)

d= 2+3j
print(d)

print(type(d))

#nowa_zmienna

# del a
# print(a)

f = 'isi'
g = ' grupa 3'
print(f+g)

h = 7
i = 2
print(h**i)
print(2/4 ** 2)
print(math.pow(2/4, i))

h+=1
print(h)

a = 5
b = 3
c = a - b
print('wynik działania %(z1)d - %(z2)d = %(z3)d' %{'z1': a, 'z2':b, 'z3':c})
print("wynik działania {0:d} - {1:d} = {2:d}".format(a, b, c))
