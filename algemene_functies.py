def mijn_functie_1(argument):
    tabel = {
        2: 4,
        4: 16,
        10: 100,
        12: 144
    
    }

    return tabel.get(argument, None)

def mijn_functie_2(argument):
    tabel = {
        12: 3,
        2: 10,
        5: 100,
        20: None

    }

    return tabel.get(argument, None)