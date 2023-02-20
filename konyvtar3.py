class Konyvtar:
    def __init__(self, könyvtárnev, város, mennyiség):
        self.könyvtárnev = könyvtárnev
        self.város = város
        self.mennyiség = mennyiség
    def elotag(self):
        if mennyiség > 50:
            return 'ügyes gyűjtő'
        elif mennyiség < 50:
            return 'kevésbé szorgalmas'

konyvtarak = []
for _ in range(3):
    könyvtárnév = input('Add meg egy könyvtár nevét!')
    város = input('Add meg a az könyvtár városát! ')
    mennyiség = int(input('Add meg az könyvtár gyűjtött kötetek mennyiségét (millió)!' ))
    konyvt = Konyvtar(könyvtárnév, város, mennyiség)
    konyvtarak.append(konyvt)
for konyvtar in konyvtarak:
    print(f'A(z) {konyvt.elotag()} címet kapott {konyvt.könyvtárnev()} {konyvt.mennyiség()} millió gyűjtött kötettel')