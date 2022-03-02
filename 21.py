# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#a = 6
#b = 6
#
#if a > b:
#    print('liczba a jest wieksza od liczby b')
#elif a < b:
#    print('liczba a jest mniejsza od liczby b')
#else:
#    print('liczby sa rowne')
#
#a = input('wpisz liczbę: ')
#print(a)
#print(type(a))
#a = int(a)
#print(type(a))

#b = input('wpisz pierwsza liczbę: ')
#c = input('wpisz druga liczbę: ')
#d = input('wpisz trzecia liczbę: ')
#e = input('wpisz czwarta liczbę: ')
#b = int(b)
#c = int(c)
#d = int(d)
#e = int(e)
#if(b > c) & (d > e):
#    print('liczba b jest wieksza od liczby c i liczba d jest wieksza od liczby e')
#else:
#    print('licza b jest mniejsza od liczby c lub liczba d jest mniejsza od liczby e')

#for x in range(0,7,1):
#    print(x)
#
#lista = ['b',1,3,5,5.6, 'siema']
#for siema in lista:
#   print(siema)
#else:
#    print('wszystkie elementy listy')
#a=0
#while a < 11:
#    print(a)
#   a += 1
#
#lista = [4,6,9,5,7,2,3]
#liczba = input('podaj liczbe: ')
#licznik = 0
#while licznik < len(lista):
#   if int(liczba) - lista[licznik] == 0:
#        print('liczba' + str(liczba) + ' - ' + str(lista[licznik]) + ' = 0')
#        break
#    else:
#        licznik += 1
#else:
#    print('zadna z wartosci nie dala odpowiedniego wyniku')
#lista1 = [4,6,8,2,3,9]
#lista2 = [2,1,3,7]
#suma = []
#for a in lista1:
#    for b in lista2:
#        wynik = a+b
#        suma.append(wynik)
#    print(suma)
#
#a = input("wczytaj pierwsza liczbe: ")
#b = input("wczytaj drugą liczbę: ")
#try:
#    a = int(a)
#   b = int(b)
#    wynik = a/b
#    print(wynik)
#except ZeroDivisionError:
#    print('nie można dzielić przez 0')
#except ValueError:
#    print('nie wczytano liczby calkowitej')

lista = ['a',5, 5.5, [1,2,3]]
slownik = {5:40, 'a':'b'}
a = lista[0]
print(slownik[a])

print(lista)
lista.append(20)
print(lista)
slownik[20] = 50
b = lista[4]
print(slownik[b])
lista.reverse()
print(lista)
listaa = [1,3,5,2,6,4]
listaa.sort()
print(listaa)
listaa.pop(3)
print(listaa)
lista.extend(listaa)
print(lista)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
