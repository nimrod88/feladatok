def gyujto(konyv):
    if mennyiseg > 800:
        return nev, 'ügyes gyűjtő címet kap.'
    elif mennyiseg < 800:
        return nev, 'kevésbé szorgalmas címet kap.'

nev=None
while nev != "":
    nev = input('Add meg a könyvtár nevét! ')
    mennyiseg = int(input('Add meg a gyűjtött kötetek mennyiségét (ezer). '))
    print(gyujto)