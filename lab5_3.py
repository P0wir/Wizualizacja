class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)

class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

class Menadzer(Pracownik):
    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

jozek = Pracownik('Józef', 'Bajka', 2000)
adrian = Menadzer('Adrian', 'Mikulski', 12000)

print(jozek.przedstaw_sie())
print(adrian.przedstaw_sie())
