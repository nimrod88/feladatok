ora = int(input('Hány órás visszaszámlálást tervezünk? '))
print('Visszaszámlálás:', ora)
felfugg = input('Fel kell függeszteni a visszaszámlálást(i/n)?')
while felfugg != 'i':
    print('Visszaszámlálás:', ora-1)
    felfugg = input('Fel kell függeszteni a visszaszámlálást(i/n)?')
if ora == 0:
    print('A rakéta a visszaszámlálást követően ennyi órával indult:', ora)