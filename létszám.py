isk1=int(input('Adj meg az egyik iskolai számot! '))
isk2=int(input('Adjon meg egy másik iskolai számot! '))
if isk1 > isk2:
    print('A létszám érték az egyik isolában több,', isk1)
elif isk2 > isk1:
    print('A létszám érték a másik isolában több,', isk2)
else:
    print('A két létszám egyenlő.')