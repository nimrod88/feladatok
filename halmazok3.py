#1
print("1.feladat")
tárgyak = {'ceruza', 'szék', 'toll', 'könyv'}
tárgyak.clear()
print(tárgyak)

#2
print("2.feladat")
halmaz1 = {'a', 'b', 'c', 'd'}
halmaz2 = {1, 2, 3, 4}
print(halmaz1 | halmaz2)

#3
print("3.feladat")
diff = halmaz1.difference(halmaz2)
print(diff)

#4
print("4.feladat")
halmaz3 = {'a', 6, 'j', 'h', 4, 'y'}
halmaz4 = {6, 'h', 3, 'n', 7, 'm'}
halmaz3.difference_update(halmaz4)
print(halmaz3)

#5
print("5.feladat")
inter = halmaz3.intersection(halmaz4)
print(inter)

#6
print("6.feladat")
halmaz3.intersection_update(halmaz4)
print(halmaz3)

#7
print("7.feladat")
isdis = halmaz3.isdisjoint(halmaz4)
print(isdis)
#akkor true hogyha nincs a két halmazban ugyan az az elem

#8
print("8.feladat")
halmaz5={'a', 'b', 'c'}
halmaz6={'f', 'e', 'd', 'c', 'b', 'a'}
subs=halmaz5.issubset(halmaz6)
print(subs)
#akkor true hogyha az első halmaz minden eleme benne van a második halmazban

#9
print("9.feladat")
issuper = halmaz6.issuperset(halmaz5)
print(issuper)
#akkor true hogyha a második halmaz minden eleme benne van az első halmazban

#10
print("10. feladat")
symdif = halmaz4.symmetric_difference(halmaz3)
print(symdif)
#a két halmaz összes elemét belerakja egy halmazba, csak azokat nem ami mid a két halmazba benne van

#11
print('11.feladat')

print("1.metódus")
halmaz1.pop()
print(halmaz1)
#egy véletlenszerű elemet kitöröl a halmazból

print("2.metódus")
uni=halmaz3.union(halmaz4)
print(uni)
#a két halmaz minden elemét kiírja, ami mind a kettő halmazban megvan azt csak egyszer írja ki

print("3.metódus")
halmaz5.remove('b')
print(halmaz5)
#egy kiválaszott elemet kitöröl a halmazból