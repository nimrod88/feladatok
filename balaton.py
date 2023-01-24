class balaton:
    def __init__(self, település, fekvés, lakosság):
        self.település = település
        self.fekvés = fekvés
        self.lakosság = lakosság
    def part(fekvés):
        if fekvés == 'é':
            return 'északi'
        if fekvés == 'd':
            return 'déli'

telepulesek = []
for _ in range(3):
    település=input('Add meg egy település nevét! ')
    fekvés=input('Add meg a fekvését (é/d)! ')
    lakosság=input('Add meg a lakosság számát (o/n)!')
    telepules=balaton(település, fekvés, lakosság)
    telepulesek.append(telepules)

for varos in telepulesek:
    print(f'{telepules.település} egy {telepules.fekvés} parti város, {telepules.lakosság}')