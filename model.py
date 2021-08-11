from datetime import date
#današnji datum date.today()

class Model:
    def __init__(self):
        self.dnevi = []
        aktualni_dan = None

    
    def dodaj_dan(self):
        self.dnevi.append(date.today())
        if not self.aktualni_dan:
            self.aktualni_dan = date.today()

    def izbrisi_danasnji_dan(self):
        self.dnevi.remove(date.today())
    
    def dodaj_obrok(self, obrok):
        self.aktualni_dan.dodaj_obrok(obrok)

    def pobrisi_obrok(self, obrok):
        self.aktualni_dan.pobrisi_obrok(obrok) 

class Datum:
    def __init__(self):
        self.datum = date.today()
        self.obroki = []

    def dodaj_obrok(self, obrok):
        self.obroki.append(obrok)
    
    def izbrisi_obrok(self, obrok):
        self.obroki.remove(obrok)

    def stevilo_obrokov(self):
        return len(self.obroki)


class obrok:
    def __init__(self, hrana, čas, kcal):
        self.hrana = hrana
        self.čas = čas
        self. kcal = kcal
    