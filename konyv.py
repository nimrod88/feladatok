def nagyobb(oldal):
    if oldal1 > oldal2:
        return 'A könyv oldalszáma az egyik könyvben több,', oldal1
    elif oldal2 > oldal1:
        return 'A könyv oldalszáma a másik könyvben több,', oldal2
    elif oldal2 == oldal1:
        return 'A két könyv egyenlő oldalszámú.'

oldal1 = int(input('Adj meg az egyik könyv oldalszámát! '))
oldal2 = int(input('Adjon meg egy másik könyv oldalszámát! '))
print(nagyobb)
