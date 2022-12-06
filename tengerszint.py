'''
Írjon programot tengerszint néven!
Kérjen be addig földrajzi hely nevét és tengerszint feletti magasságát, 
amíg üres karaktert nem üt a felhasználó!

Írjon függvényt!
a tengerszintek néven, amely alföldet,"dombságot,"középhegység" és "magashegység" különböztet meg!
200m alatt alföldet,
200m és 500m között dombságot
500m és 1500m között középhegység
1500m magashegység


# Fájl írása tenger.txt néven az amelyben az összes eredmény szerepel!

Beadandó

A program forráskódja .py kiterjesztéssel a Githubra!
A program forráskódja .txt kiterjesztéssel dkt-ra!
'''
lista=[]
wr=open('tengerszint.txt','a')
def tengerszint():
    if magassag < 200:
        print(hely, 'az egy alföld.')
        lista.append('Alföld')
    elif magassag > 200 and magassag < 500:
        print(hely, 'az egy dombság.')
        lista.append('Dombság')
    elif magassag > 500 and magassag < 1500:
        print(hely, 'az egy középhegység.')
        lista.append('Középhegység')
    else:
        print(hely, 'az egy magashegység.')
        lista.append('Magashegység')

hely=None
magassag=None
while hely != " ":
    hely=input("Kérem írja be egy földrajzi hely nevét. ")
    magassag=int(input("Kérem adja meg a hely tengerszint fölötti magasságát. "))
    tengerszint()