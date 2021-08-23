
from model import Stanje, Dan, Opravilo

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
IZHOD = 6


def preberi_stevilo():
    while True:
        vnos = input("> ")
        try:
            return int(vnos)
        except ValueError:
            print("Vnesti morate število.")


def izberi_moznost(moznosti):
    """Uporabniku našteje možnosti ter vrne izbrano."""
    for i, (_moznost, opis) in enumerate(moznosti, 1):
        print(f"{i}) {opis}")
    while True:
        i = preberi_stevilo()
        if 1 <= i <= len(moznosti):
            moznost, _opis = moznosti[i - 1]
            return moznost
        else:
            print(f"Vnesti morate število med 1 in {len(moznosti)}.")


def prikaz_spiska(dan):
    vsa = dan.stevilo_vseh()
    return f"{dan.ime} ({vsa})"


def prikaz_dneva(obrok):
    if obrok.rok:
        return f"{obrok.ime} ({obrok.rok})"
    else:
        return f"{obrok.ime}"


def izberi_dan(model):
    return izberi_moznost([(dan, prikaz_spiska(dan)) for dan in model.dnevi])


def izberi_obrok(model):
    return izberi_moznost(
        [
            (obrok, prikaz_dneva(obrok))
            for obrok in model.aktualni_dan.obroki
        ]
    )


def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    print("Niste še vnesli nobenega dneva.")
    while True:
        prikazi_aktualne_dneve()
        ukaz = izberi_moznost(
            [
                (DODAJ_DAN, "dodaj nov dan"),
                (POBRISI_DAN, "pobriši dan"),
                (ZAMENJAJ_DAN, "prikaži drug dan"),
                (DODAJ_OBROK, "dodaj nov obrok"),
                (POBRISI_OBROK, "pobriši obrok"),
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
        elif ukaz == IZHOD:
            moj_model.shrani_v_datoteko(IME_DATOTEKE)
            print("Nasvidenje!")
            break


def prikazi_pozdravno_sporocilo():
    print("Pozdravljeni!")


def prikazi_aktualne_dneve():
    if moj_model.aktualni_dan:
        for obrok in moj_model.aktualni_dan.obroki:
            if not obrok.opravljeno:
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
    print("Vnesite podatke novega obroki.")
    ime = input("Ime> ")
    opis = input("Opis> ")
    rok = None
    novo_obrok = Opravilo(ime, opis, rok)
    moj_model.dodaj_obrok(novo_obrok)


def pobrisi_obrok():
    obrok = izberi_obrok(moj_model)
    moj_model.pobrisi_obrok(obrok)



tekstovni_vmesnik()
