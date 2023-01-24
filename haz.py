def oldal(hazszam):
    if hazszam % 2 == 0:
        print('A ház a jobb oldalon van.')
    else:
        print('A ház a bal oldalon van.')

utca=input('Adja meg az utca nevét! ')
while utca != '':
    utca=input('Adja meg az utca nevét! ')
    hazszam=int(input('Adja meg a házszámát! '))
    oldal(hazszam)