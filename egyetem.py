class HíresEgyetem:
    def __init__(self, név, város, nemzetiség):
        self.név = név
        self.város = város
        self.nemzetiség = nemzetiség
    def elotag(self):
        if nemzetiség == "a":
            return "University"
        elif nemzetiség == "n":
            return "Universität"
    def utotag(self):
        if nemzetiség == "a":
            return "angol"
        if nemzetiség == "n":
            return "német"

egyetemek = []
for i in range(3):
    név=input('Add meg egy egyetem nevét! ')
    város=input('Add meg az egyetem városát! ')
    nemzetiség=input('Add meg a nemzetiségét (a/n)! ')
    egyetem = HíresEgyetem(név, város, nemzetiség)
    egyetemek.append(egyetem)

for iskola in egyetemek:
    print(f'{egyetem.elotag()}. {egyetem.név()} egy híres {egyetem.utotag()} egyetem.')