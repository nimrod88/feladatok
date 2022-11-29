import random
# 1 A kitermelés 50 és 100 m3 között lehetséges naponta októberben!
print('1.feladat')
okt=[]
rand=0
for i in range(31):
    okt.append(random.randint(50, 100))
print(okt)
# 2 A legnagyobb fakitermelés mennyiségét a tervszerint 
print('2.feladat')
legnagyobb=None
legnagyobb=okt[0]
for elem in okt:
    if elem > legnagyobb:
        legnagyobb=elem
print('A legnagyobb fakitermelés mennyisége:', legnagyobb)

# 3 A legkisebb fakitermelés mennyiségét a tervszerint 
print('3.feladat')
legkisebb=None
legkisebb=okt[0]
for elem in okt:
    if elem < legkisebb:
        legkisebb=elem
print('A legkisebb fakitermelés mennyisége:', legkisebb)
        
# 4 Hány alkalommal volt a fakitermelés mennyiségé 82 m3 felett?
print('4.feladat')
hanyszor=0
for elem in okt:
    if elem > 82:
        hanyszor+=1
print('Ennyiszer volt a fakitermelés mennyisége 82 m3 fölött:', hanyszor)

# 5 mekkora volt a fakitermelés mennyisége októberi 20.-án?
print('5.feladat')
print('Október 20.-án', okt[19], 'volt a fakitermelés mennyisége.')

# 6 mekkora volt a fakitermelés átlag mennyisége?
print('6.feladat')
print('A fakitermelés átlag mennyisége', sum(okt) / len(okt), 'volt.')

# Fájl írása fa.txt néven az amelyben az összes eredmény szerepel!
wr=open('fakitermeles.txt','w')
wr.write(f'Terv:, {okt}\n')
wr.write(f'A legnagyobb kitermelés: {legnagyobb}\n')
wr.write(f'A legkisebb kitermelés: {legkisebb}\n')
wr.write(f'Ennyiszer volt a kitermelés mennyisége 82 m3 fölött: {hanyszor}\n')
wr.write(f'Október 20.-án a fakitermelés mennyisége {okt[19]} volt\n')
wr.write(f'A fakitermelés átlag mennyisége {sum(okt) / len(okt)} volt\n')