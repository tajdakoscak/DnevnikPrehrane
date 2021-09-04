from datetime import date
import json


class Stanje:
    def __init__(self):
        self.dnevi = []
        self.aktualni_dan = None

    def dodaj_dan(self, dan):
        self.dnevi.append(dan)
        if not self.aktualni_dan:
            self.aktualni_dan = dan

    def pobrisi_dan(self, dan):
        self.dnevi.remove(dan)

    def zamenjaj_dan(self, dan):
        self.aktualni_dan = dan

    def dodaj_obrok(self, obrok):
        self.aktualni_dan.dodaj_obrok(obrok)

    def pobrisi_obrok(self, obrok):
        self.aktualni_dan.pobrisi_obrok(obrok)

    def stevilo_vseh(self):
        return sum([dan.stevilo_vseh() for dan in self.dnevi])

    def v_slovar(self):
        return {
            "dnevi": [dan.v_slovar() for dan in self.dnevi],
            "aktualni_dan": self.dnevi.index(self.aktualni_dan)
            if self.aktualni_dan
            else None,
        }

    @staticmethod
    def iz_slovarja(slovar):
        stanje = Stanje()
        stanje.dnevi = [
            Dan.iz_slovarja(sl_dneva) for sl_dneva in slovar["dnevi"]
        ]
        if slovar["aktualni_dan"] is not None:
            stanje.aktualni_dan = stanje.dnevi[slovar["aktualni_dan"]]
        return stanje

    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w") as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat)

    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Stanje.iz_slovarja(slovar)

    def preveri_podatke_novega_dneva(self, ime):
        napake = {}
        if not ime:
            napake["ime"] = "Ime mora biti neprazno."
        for dan in self.dnevi:
            if dan.ime == ime:
                napake["ime"] = "Ime je že zasedeno."
        return napake
class Dan :
    def __init__(self, ime):
        self.ime = ime
        self.obroki = []

    def dodaj_obrok(self, obrok):
        self.obroki.append(obrok)
    
    def pobrisi_obrok(self, obrok):
        self.obroki.remove(obrok)

    def v_slovar(self):
        return {
            "ime": self.ime,
            "obroki": [obrok.v_slovar() for obrok in self.obroki],
        }

    def stevilo_vseh(self):
        return len(self.obroki)

    def stevilo_kalorij(self):
        stevilo = 0
        for obrok in self.obroki:
            stevilo = stevilo + int(obrok.kalorije)
        return stevilo

    @staticmethod
    def iz_slovarja(slovar):
        dan = Dan(slovar["ime"])
        dan.obroki = [
            Obrok.iz_slovarja(sl_obroki) for sl_obroki in slovar["obroki"]
        ]
        return dan

class Obrok:
    def __init__(self, hrana, kalorije):
        self.hrana = hrana
        self.kalorije = kalorije

    def v_slovar(self):
        return {
            "hrana": self.hrana,
            "kalorije": self.kalorije,
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Obrok(
            slovar["hrana"],
            slovar["kalorije"],
        )