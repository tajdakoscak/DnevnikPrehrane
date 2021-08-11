DODAJ_DAN = 1
IZBRISI_DAN = 2
DODAJ_OBROK = 3
IZBRISI_OBROK = 4
IZHOD = 5



def tekstovni_vmesnik():
    print("Pozdravljen v dnevniku prehrane")
    while True:
        prikaz_danasnjih_obrokov()
        ukaz = izberi_moznost([
            (DODAJ_DAN, "dodaj nov don"),
            (IZBRISI_DAN, "izbrisi dan"),
            (DODAJ_OBROK, "dodoaj obrok"),
            (IZBRISI_OBROK, "izbrisi obrok"),
            (IZHOD, "zapri program")
        ])

        if ukaz == DODAJ_DAN:
            dodaj_dan()
        elif ukaz == IZBRISI_DAN():
            izbrisi_danasnji_dan()
        elif ukaz == DODAJ_OBROK():
            dodaj_obrok()
        elif IZBRISI_OBROK():
            ukaz == izbrisi.obrok()
        elif ukaz == IZHOD():
            print ("Nasvidenje!")
            break

def prikazi_pozdravno_sporocilo():
    print("POZDRAVLJENI!")

def prikazi_aktualni_dan():
    pass
