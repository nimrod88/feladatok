ora = int(input('Hány óra van most? '))
if ora >= 8 and ora <= 16:
    print('A bolt nyitva van.')
    ennyit_nyitva = 16 - ora
    print('Ennyi órád van odaérni:', ennyit_nyitva)
else:
    print('A bolt zárva van.')