from model import Stanje, Dan, Obrok

IME_DATOTEKE = "stanje.json"
try:
    moj_model = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    moj_model = Stanje()

DODAJ_DAN = 1
POBRISI_DAN = 2
ZAMENJAJ_DAN = 3
DODAJ_OBROK = 4
POBRISI_OBROK = 5
POGLEJ_DAN = 6
POGLEJ_DANASNJE_KALORIJE = 7
IZHOD = 6

def preveri_stevilo():
    while True:
        vnos = input("> ")
        try:
            return int(vnos)
        except ValueError:
            print("Vnesti morate število.")

def izberi_moznost(moznosti):
    for i, (_moznost, opis) in enumerate(moznosti, 1):
        print(f"{i}) {opis}")
    while True:
        i = preveri_stevilo()
        if len(moznosti) == 0:
            print("Te možnosti žal ne morete izbrati.")
            return nazaj()
        elif 1 <= i <= len(moznosti):
            moznost, _opis = moznosti[i - 1]
            return moznost
        else:
            print(f"Vnesti morate število med 1 in {len(moznosti)}.")

def prikaz_spiska(dan):
    vsa = dan.stevilo_vseh()
    return f"{dan.ime} ({vsa})"

def prikaz_dneva(obrok):
    return f"{obrok.tip_obroka}: {obrok.hrana} ({obrok.kalorije} kcal)"

def sestej_kalorije(model):
    obroki=model.aktualni_dan.obroki if model.aktualni_dan else []
    dan = model.aktualni_dan
    skupaj = 0
    for obrok in obroki:
        skupaj = skupaj + int(obrok.kalorije)
    st_kalorij = skupaj
    print(f"Na dan {dan.ime} ste zaužili {st_kalorij} kcal")

def izberi_dan(model):
    return izberi_moznost([(dan, prikaz_spiska(dan)) for dan in model.dnevi])

def izberi_obrok(model):
    return izberi_moznost([(obrok, prikaz_dneva(obrok)) for obrok in model.aktualni_dan.obroki])

def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    while True:
        prikazi_aktualne_dneve()
        ukaz = izberi_moznost(
            [
                (DODAJ_DAN, "dodaj nov dan"),
                (POBRISI_DAN, "pobriši dan"),
                (ZAMENJAJ_DAN, "prikaži drug dan"),
                (DODAJ_OBROK, "dodaj nov obrok"),
                (POBRISI_OBROK, "pobriši obrok"),
                (POGLEJ_DAN, "poglej dan"),
                (POGLEJ_DANASNJE_KALORIJE, "poglej danasnje kalorije"),
                (IZHOD, "zapri program"),
            ]
        )
        if ukaz == DODAJ_DAN:
            dodaj_dan()
        elif ukaz == POBRISI_DAN:
            pobrisi_dan()
        elif ukaz == ZAMENJAJ_DAN:
            zamenjaj_dan()
        elif ukaz == DODAJ_OBROK:
            dodaj_obrok()
        elif ukaz == POBRISI_OBROK:
            pobrisi_obrok()
        elif ukaz == POGLEJ_DAN:
            poglej_dan()
        elif ukaz == POGLEJ_DANASNJE_KALORIJE:
            poglej_danasnje_kalorije()
        elif ukaz == IZHOD:
            moj_model.shrani_v_datoteko(IME_DATOTEKE)
            print("Nasvidenje!")
            break

def nazaj():
    while True:
        prikazi_aktualne_dneve()
        ukaz = izberi_moznost(
            [
                (DODAJ_DAN, "dodaj nov dan"),
                (POBRISI_DAN, "pobriši dan"),
                (ZAMENJAJ_DAN, "prikaži drug dan"),
                (DODAJ_OBROK, "dodaj nov obrok"),
                (POBRISI_OBROK, "pobriši obrok"),
                (POGLEJ_DAN, "poglej dan"),
                (POGLEJ_DANASNJE_KALORIJE, "poglej danasnje kalorije"),
                (IZHOD, "zapri program"),
            ]
        )
        if ukaz == DODAJ_DAN:
            dodaj_dan()
        elif ukaz == POBRISI_DAN:
            pobrisi_dan()
        elif ukaz == ZAMENJAJ_DAN:
            zamenjaj_dan()
        elif ukaz == DODAJ_OBROK:
            dodaj_obrok()
        elif ukaz == POBRISI_OBROK:
            pobrisi_obrok()
        elif ukaz == POGLEJ_DAN:
            poglej_dan()
        elif ukaz == POGLEJ_DANASNJE_KALORIJE:
            poglej_danasnje_kalorije()
        elif ukaz == IZHOD:
            moj_model.shrani_v_datoteko(IME_DATOTEKE)
            print("Nasvidenje!")
            break

def prikazi_pozdravno_sporocilo():
    print("Pozdravljeni v dnevniku prehrane!")
    print("Izberite kako želite nadaljevati:")

def prikazi_aktualne_dneve():
    if moj_model.aktualni_dan:
        for obrok in moj_model.aktualni_dan.obroki:
            print(f"- {prikaz_dneva(obrok)}")
    else:
        print("Niste še vnesli nobenega dneva.")
        dodaj_dan()

def dodaj_dan():
    print("Prosim, vnesite podatke novega dneva.")
    ime = input("Datum> ")
    nov_dan = Dan(ime)
    moj_model.dodaj_dan(nov_dan)

def pobrisi_dan():
    dan = izberi_dan(moj_model)
    moj_model.pobrisi_dan(dan)

def zamenjaj_dan():
    print("Izberite dan, na katerega bi preklopili.")
    dan = izberi_dan(moj_model)
    moj_model.zamenjaj_dan(dan)

def dodaj_obrok():
    print("Vnesite podatke novega obroka.")
    hrana = input("Hrana> ")
    kalorije = int(input("Kalorije> "))
    tip_obroka = input("Tip obroka(zajtrk/malica/kosilo/večerja)> ")
    nov_obrok = Obrok(hrana, kalorije,tip_obroka)
    moj_model.dodaj_obrok(nov_obrok)

def pobrisi_obrok():
    obrok = izberi_obrok(moj_model)
    moj_model.pobrisi_obrok(obrok)

def poglej_dan():
    print("Izberite dan, katerega si želite ogledati.")
    izberi_dan(moj_model)

def poglej_danasnje_kalorije():
    sestej_kalorije(moj_model)
    
tekstovni_vmesnik()