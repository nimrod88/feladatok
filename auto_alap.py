class Híres_auto:
    def __init__(self, marka_név, henger_térfogat, nemzetiseg):
        self.név = None
        self. henger_térfogat = henger_térfogat
        self.nemzetiseg = nemzetiseg
    def elotag(self):
        if self.nemzetiseg == 'n':
            return 'német'
        else:
            return 'japán'

híres_autok = []
for _ in range(3):
    marka_név = input('Adja meg a márka nevét')
    henger_térfogat = int(input('Adja meg a henger térfogatát'))
    nemzetiseg = input=('Adja meg a márkát gyártó nemzetiségét')
    hires_auto=Híres_auto(marka_név, henger_térfogat, nemzetiseg)
    híres_autok.append(hires_auto)

for híres_auto in híres_autok:
    print(f' A {hires_auto.marka_név},egy hires ,{hires_auto.elotag()} márka {hires_auto.henger_térfogat}')