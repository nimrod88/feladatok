import random

fejviras=('Fej vagy írás?')
feldob = random.randint(1,2)
if fejviras == 'fej' and feldob == 1:
    print('Eltaláltad.')
elif fejviras == 'írás' and feldob == 2:
    print('Eltaláltad')
else:
    print('Nem találtad el.')