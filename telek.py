def red(t, w, l):
    if l<=25 or w<=15:
        t = 0.8 * t
    return t

def hetnapja(honap, nap):
    napnev=["vasarnap","hetfo","kedd","szerda","csutortok","pentek","szombat"]
    napszam=[0, 31, 59, 90 ,120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam=(honap[honap-1]+nap) % 7
    hetnapja=napnev[napsorszam]
    return napnev[napsorszam]
print(hetnapja(1,8))

tax=int(input("Kérem a kedvezmény nélküli adót: "))
length = int(input("Kérem a telek hosszát: "))
width = int(input("Kérem a telek szélességét: "))
print("A kedvezményes adó: ", red(tax,width,length))