szam=int(input('Adjon meg egy számot! '))
if szam > 0 and szam % 2 == 0:
    print('A szám pozitív és páros')
elif szam < 0 and szam % 2 == 1:
    print('A szám negatív és páratlan.')
else:
    print('A szám egyik sem.')