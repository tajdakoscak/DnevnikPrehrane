def BMR(spol, teza, visina, starost):
    if spol == "ženska":
        return 655.1 + (9.563 * int(teza)) + (1.850 * int(visina)) - (4.676 * int(starost))
    elif spol == "moški":
        return 66.47 + (13.75 * int(teza)) + (5.003 * int(visina)) - (6.755 * int(starost))
        
def AMR(aktivnost, spol, teza, visina, starost):
    if aktivnost == "nič":
        return BMR(spol, teza, visina, starost) * 1.2
    elif aktivnost == "malo":
        return BMR(spol, teza, visina, starost) * 1.375
    elif aktivnost == "srednje":
        return BMR(spol, teza, visina, starost) * 1.55
    elif aktivnost == "zelo":
        return BMR(spol, teza, visina, starost) * 1.725



def priporocen_dnevni_vnos(cilj, aktivnost, spol, teza, visina, starost):
    if cilj == "pridobiti":
        return AMR(aktivnost, spol, teza, visina, starost) + 500
    elif cilj == "Ohraniti":
        return AMR(aktivnost, spol, teza, visina, starost)
    elif cilj == "Izgubiti":
        return AMR(aktivnost, spol, teza, visina, starost) - 500


priporocen_dnevni_vnos("Izgubiti", "zelo", "moški", 50, 166, 15)