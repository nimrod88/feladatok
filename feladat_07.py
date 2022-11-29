#1
print('1. feladat')
import random
szám1=int(input('Adjon meg egy számot. '))
szám2=random.randint(10,50)
szám3=12

#2
print('2. feladat')
if szám2 % 2 == 0:
    szám2+=1
print(szám2)

#3
print('3. feladat')
if szám1 % 2:
    print("A megadott szám páratlan.")
else:
    print("A megadott szám páros.")

#4
print('4. feladat')
számok=[szám1, szám2, szám3]
print(számok)

számok.append(76)
print(számok)

számok.reverse()
print(számok)

számok.remove(76)
print(számok)

számok.insert(2, 45)
print(számok)

számok.pop(2)
print(számok)

#5
print('5. feladat')
halmaz = {szám1, szám2, szám3}
halmaz2 = {23, 54, 67, 12}

halmaz.add(67)
print(halmaz)

halmaz.remove(szám2)
print(halmaz)

kulonb=halmaz.difference(halmaz2)
print(kulonb)

uni=halmaz.union(halmaz2)
print(uni)

subs=halmaz.issubset(halmaz2)
print(subs)

#6
with open("MucsiNimród.txt",'w') as file:
    file.write(str(számok))
    file.close

#7
re=open('MucsiNimród.txt','r')
line=re.readline()
print(line)
re.close