def letszam(iskola):
    if pontszam >= 1000:
        print(iskola, 'nagy létszámú iskola.')
    elif pontszam < 1000:
        print(iskola, 'kis létszámú iskola.')
iskola=input('Add meg az iskola nevét.')
pontszam=int(input('Add meg a pontszámát! '))
letszam(iskola)