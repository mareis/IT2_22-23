class Rose():
    def __init__(self, navn, pris, høyde, farge):
        self.navn = navn
        self.pris = pris
        self.høyde = høyde
        self.farge = farge

    def beskrivelse(self):
        print(self.navn)
        print(f'Pris: {self.pris} kr')
        print(f'Høyde: {self.høyde} cm')
        print(f'Farge: {self.farge}')

class Stilkrose(Rose):
    def __init__(self, navn, pris, høyde, farge, stilklengde):
        self.stilklengde = stilklengde
        self.type = 'Stilkrose'
        super().__init__(navn, pris, høyde, farge)

    def beskrivelse(self):
        super().beskrivelse()
        print(f'Stilklengde: {self.stilklengde} cm')

class Butikk():
    def __init__(self, navn):
        self.navn = navn
        self.utvalg = {'Stilkrose':[], 'Buskrose':[], 'Klatrerose':[]}
        self.kunder = []

    def leggTilRose(self, rose):
        self.utvalg[rose.type].append(rose)

    def skrivUtUtvalg(self):
        print(self.utvalg)

    def skrivUtBestemt(self, type):
        liste = self.utvalg[type]
        for rose in liste:
            rose.beskrivelse()
            print(' ')

    def skrivUtEtterFarge(self, farge):
        for kategori, roser in self.utvalg.items():
            print(kategori, end='\n-----------\n')
            for rose in roser:
                if farge.lower() in rose.farge.lower():
                    rose.beskrivelse()
                    print(" ")

class Kunde():
    def __init__(self, navn):
        self.navn = navn
        self.handlevogn = Handlevogn()

class Handlevogn():
    def __init__(self):
        self.handlevogn = []

    def legg_til_rose(self, antall:int, rose):
        self.handlevogn.append({'antall': antall, 'rose':rose})

    def skriv_ut(self):
        tot = 0
        print(f"{'Rose':25}{'Antall':10}{'Pris':6}")
        print(f"{'-'*40}") 
        for roser in self.handlevogn:
            tot += roser['antall']*roser['rose'].pris
            print(f"{roser['rose'].navn:20}{roser['antall']:12}{roser['rose'].pris:6} kr")
        print(f"{'-'*40}") 
        print(f"Sum:     {tot} kr")

    def tom(self):
        self.handlevogn = []


coopX = Butikk('Coop Extra')
link = Stilkrose('Mr. Link', 154.00, 120, 'Rød', 110)

#link.beskrivelse()

coopX.leggTilRose(link)
coopX.leggTilRose(Stilkrose('Queen Lizz', 196.00, 70, 'Rosa', 55))
coopX.leggTilRose(Stilkrose('Queen Lizzi', 196.00, 70, 'Rødlilla', 55))

#coopX.skrivUtUtvalg()

#coopX.skrivUtBestemt('Stilkrose')

#coopX.skrivUtEtterFarge('Rød')

coopX.kunder.append(Kunde("Felix"))
coopX.kunder[0].handlevogn.legg_til_rose(2, coopX.utvalg['Stilkrose'][0])
coopX.kunder[0].handlevogn.legg_til_rose(1, coopX.utvalg['Stilkrose'][1])
coopX.kunder[0].handlevogn.legg_til_rose(10, coopX.utvalg['Stilkrose'][2])
coopX.kunder[0].handlevogn.skriv_ut()
coopX.kunder[0].handlevogn.tom()
coopX.kunder[0].handlevogn.skriv_ut()
coopX.kunder[0].handlevogn.legg_til_rose(200, coopX.utvalg['Stilkrose'][1])
coopX.kunder[0].handlevogn.legg_til_rose(5, coopX.utvalg['Stilkrose'][2])
coopX.kunder[0].handlevogn.skriv_ut()
