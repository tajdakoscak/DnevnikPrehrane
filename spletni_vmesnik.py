import bottle
import os
from model import Stanje, Dan, Obrok


def nalozi_uporabnikovo_stanje():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime")
    if uporabnisko_ime:
        return Stanje.preberi_iz_datoteke(uporabnisko_ime)
    else:
        bottle.redirect("/prijava/")


def shrani_uporabnikovo_stanje(stanje):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime")
    stanje.shrani_v_datoteko(uporabnisko_ime)


@bottle.get("/")
def osnovna_stran():
    stanje = nalozi_uporabnikovo_stanje()
    return bottle.template(
        "osnovna_stran.html",
        obroki=stanje.aktualni_dan.obroki if stanje.aktualni_dan else [],
        dnevi=stanje.dnevi,
        aktualni_dan=stanje.aktualni_dan,
        uporabnisko_ime=bottle.request.get_cookie("uporabnisko_ime"),
    )


@bottle.get("/registracija/")
def registracija_get():
    return bottle.template("registracija.html", napake={}, polja={}, uporabnisko_ime=None)


@bottle.post("/registracija/")
def registracija_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    if os.path.exists(uporabnisko_ime):
        napake = {"uporabnisko_ime": "Uporabniško ime že obstaja."}
        return bottle.template("registracija.html", napake=napake, polja={"uporabnisko_ime": uporabnisko_ime}, uporabnisko_ime=None)
    else:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/")
        Stanje().shrani_v_datoteko(uporabnisko_ime)
        bottle.redirect("/")

@bottle.get("/prijava/")
def prijava_get():
    return bottle.template("prijava.html", napake={}, polja={}, uporabnisko_ime=None)


@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    if not os.path.exists(uporabnisko_ime):
        napake = {"uporabnisko_ime": "Uporabniško ime ne obstaja."}
        return bottle.template("prijava.html", napake=napake, polja={"uporabnisko_ime": uporabnisko_ime}, uporabnisko_ime=None)
    else:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/")
        bottle.redirect("/")


@bottle.post("/odjava/")
def odjava_post():
    bottle.response.delete_cookie("uporabnisko_ime", path="/")
    print("piškotek uspešno pobrisan")
    bottle.redirect("/")


@bottle.post("/dodaj/")
def dodaj_obrok():
    hrana = bottle.request.forms.getunicode("hrana")
    kalorije = bottle.request.forms.getunicode("kalorije")
    obrok = Obrok(hrana,kalorije)
    stanje = nalozi_uporabnikovo_stanje()
    stanje.dodaj_obrok(obrok)
    shrani_uporabnikovo_stanje(stanje)
    bottle.redirect("/")


@bottle.get("/dodaj-dan/")
def dodaj_dan_get():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    return bottle.template("dodaj_dan.html", napake={}, polja={}, uporabnisko_ime=uporabnisko_ime)


@bottle.post("/dodaj-dan/")
def dodaj_dan_post():
    ime = bottle.request.forms.getunicode("ime")
    polja = {"ime": ime}
    stanje = nalozi_uporabnikovo_stanje()
    napake = stanje.preveri_podatke_novega_dneva(ime)
    if napake:
        return bottle.template("dodaj_dan.html", napake=napake, polja=polja)
    else:
        dan = Dan(ime)
        stanje.dodaj_dan(dan)
        shrani_uporabnikovo_stanje(stanje)
        bottle.redirect("/")




@bottle.post("/zamenjaj-aktualni-dan/")
def zamenjaj_aktualni_dan():
    print(dict(bottle.request.forms))
    indeks = bottle.request.forms.getunicode("indeks")
    stanje = nalozi_uporabnikovo_stanje()
    dan = stanje.dnevi[int(indeks)]
    stanje.aktualni_dan = dan
    shrani_uporabnikovo_stanje(stanje)
    bottle.redirect("/")


@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"


bottle.run(reloader=True, debug=True)