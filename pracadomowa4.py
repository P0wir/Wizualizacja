import random

#zadanie 1

plik = open("plik.txt", "a")
for x in range(0, 31):
    x = x * 2
    x = str(x)
    plik.write(x)
    plik.write(' ')

#zadanie 2

k=open("plik.txt", "r")
print(k.read())

#zadanie 3

with open("plik.txt", "a") as plik:
    plik.write("123\n")
with open("plik.txt", "r") as plik:
    for linia in plik:
        print(plik.read())

#zadanie 4

class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu)
        print(self.ilosc)
        print(self.jednostka_miary)
        print(self.cena_jed)
    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)
    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed
chleb=NaZakupy("jajka", 3, "Szt", 1)
chleb.wyswietl_produkt()
chleb.ile_produktu()
print(chleb.ile_kosztuje())

#zadanie 5

class ciagArytmetyczny:
    def __init__(self, a1, r, n):
        self.a1=a1
        self.r=r
        self.n=n
    def wyswietl_dane(self):
        wyraz=self.a1
        for x in range(self.n):
            print(wyraz)
            wyraz = wyraz + self.r
    def pobierz_elementy(self, x, roz, y):
        self.a1=x
        self.r=roz
        self.n=y
    def policz_sume(self):
        an=self.a1+(self.n-1)*self.r
        suma=((self.a1+an)/2)*self.n
        return suma
ciag=ciagArytmetyczny(5,3,3)
ciag.wyswietl_dane()
ciag.pobierz_elementy(10,2,5)
ciag.wyswietl_dane()
print(ciag.policz_sume())

#zadanie 6

class Robaczek:
    def __init__(self, x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def idz_w_gore(self, ile_krokow):
        self.y=self.y+(self.krok*ile_krokow)
    def idz_w_dol(self, ile_krokow):
        self.y=self.y-(self.krok*ile_krokow)
    def idz_w_lewo(self, ile_krokow):
        self.x=self.x-(self.krok*ile_krokow)
    def idz_w_prawo(self, ile_krokow):
        self.x=self.x+(self.krok*ile_krokow)
    def pokaz_gdzie_jestes(self):
        print(self.x, self.y)
robak=Robaczek(0,0,2)
robak.idz_w_dol(5)
robak.idz_w_gore(3)
robak.idz_w_lewo(2)
robak.idz_w_prawo(6)
robak.pokaz_gdzie_jestes()

