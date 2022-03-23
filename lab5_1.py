class Kształty():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.opis = "To jest klasa dla ogólnych kształtów"
    def pole(self):
        return self.x*self.y
    def obwod(self):
        return 2*self.x+2*self.y
    def dodaj_opis(self,text):
        self.opis = text
    def skalowanie(self,czynnik):
        self.x *= czynnik
        self.y *= czynnik
class Kwadrat(Kształty):
    def __init__(self,x):
        self.x = x
        self.y = x
class KwadratAleToLiteraL(Kwadrat):
    def obwod(self):
        return 8 * self.x
    def pole(self):
        return 3*self.x*self.y

kwadrat = Kwadrat(5)
print(kwadrat.obwod())
print(kwadrat.pole())
kwadrat.dodaj_opis("Nasza figura to kwadrat")
print(kwadrat.opis)
kwadrat.skalowanie(0.3)
print(kwadrat.obwod())
print("")

litera_l = KwadratAleToLiteraL(5)
print(litera_l.obwod())
print(litera_l.pole())
litera_l.dodaj_opis("Litera L")
print(litera_l.opis)
litera_l.skalowanie(0.5)
print(litera_l.obwod())


