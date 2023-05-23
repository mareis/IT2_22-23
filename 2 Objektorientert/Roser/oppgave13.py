class Hagesenter():
  """
  Klasse for å lage hagesenter-objekter.

  Parametre:
  butikk (str): Butikkens navn
  """
  def __init__(self,butikk):
    """
    Konstruktør
    """
    self.butikk = butikk

    # Definerer tomme objektlister til rosene i butikkens utvalg
    self.stilkRoser = []
    self.buskRoser = []
    self.klatreRoser = []

  def leggTilRose(self,rosetype,navn, pris, beskrivelse, farge, mål):
    # Legger til rose objekt i riktig liste 0-stilk, 1-busk, 2-klatre
    if rosetype == 0:
      self.stilkRoser.append(Stilkrose(navn, pris, beskrivelse, farge, mål))
    elif rosetype == 1:
      self.buskRoser.append(Buskrose(navn, pris, beskrivelse, farge, mål))
    elif rosetype == 2:
      self.klatreRoser.append(Klatrerose(navn, pris, beskrivelse, farge, mål))

  def visRoser(self,farge):
    """
    Metode som skriver ut informasjon om roser
    Farge: 0-alle farger, 1-rød, 2-rosa, 3-hvit, 4-gul, 5-andre
    """

    print(f"Hagesenteret '{self.butikk}' har disse rosene med farge '{fargeListe[farge]}':")
    print("Stilkroser:")
    for s in self.stilkRoser:
      if(farge == s.farge or farge == 0):
        s.visInfo()
    print("\nBuskroser:")
    for b in self.buskRoser:
      if(farge == b.farge or farge == 0):
        b.visInfo()
    print("\nKlatreroser:")
    for k in self.klatreRoser:
      if(farge == k.farge or farge == 0):
        k.visInfo()

class Rose():
  """
  Klasse for å lage rose-objekter.
  Parametre:
  navn (str):             Rosens navn
  pris (int):             Rosens pris
  beskrivelse (str):      Rosens beskrivelse
  farge (int):            Rosens farge
  """
  def __init__(self,navn,pris,beskrivelse,farge):
    """
    Konstruktør
    """
    self.navn = navn
    self.pris = pris
    self.beskrivelse = beskrivelse
    self.farge = farge

  # Skriver ut informasjon om rose objektet
  def visInfo(self):
    print(f"Rosen '{self.navn}' koster {self.pris}kr og har farge {fargeListe[self.farge]}.")
    print(f"Den beskrives som: {self.beskrivelse}.")

class Stilkrose(Rose):
  """
  Klasse for å lage stilkrose-objekter. Arver fra klasse Rose.
  Parametre:
  navn (str):             Rosens navn
  pris (int):             Rosens pris
  beskrivelse (str):      Rosens beskrivelse
  farge (int):            Rosens farge
  høyde (int):            Rosens høyde
  """
  def __init__(self,navn,pris,beskrivelse,farge,høyde):
    """
    Konstruktør
    """
    self.høyde = høyde

    """
    Super klassens konstruktør
    """
    super().__init__(navn,pris,beskrivelse,farge)

  def visInfo(self):
    """
    Metode som skriver ut informasjon fra et stilkrose objekt
    """
    super().visInfo();
    print(f"{self.navn} er en stilkrose som blir max {self.høyde} cm høy.")

class Buskrose(Rose):
  """
  Klasse for å lage buskrose-objekter. Arver fra klasse Rose.
  Parametre:
  navn (str):             Rosens navn
  pris (int):             Rosens pris
  beskrivelse (str):      Rosens beskrivelse
  farge (int):            Rosens farge
  bredde (int):           Rosens bredde
  """
  def __init__(self,navn,pris,beskrivelse,farge,bredde):
    """
    Konstruktør
    """
    self.bredde = bredde

    """
    Super klassens konstruktør
    """
    super().__init__(navn,pris,beskrivelse,farge)

  def visInfo(self):
    """
    Metode som skriver ut informasjon fra et buskkrose objekt
    """
    super().visInfo();
    print(f"{self.navn} er en buskrose som blir max {self.bredde} cm bred.")

class Klatrerose(Rose):
  """
  Klasse for å lage klatrerose-objekter. Arver fra klasse Rose.
  Parametre:
  navn (str):             Rosens navn
  pris (int):             Rosens pris
  beskrivelse (str):      Rosens beskrivelse
  farge (int):            Rosens farge
  lengde (int):           Rosens lengde
  """
  def __init__(self,navn,pris,beskrivelse,farge,lengde):
    """
    Konstruktør
    """
    self.lengde = lengde

    """
    Superklassens konstruktør
    """
    super().__init__(navn,pris,beskrivelse,farge)

  def visInfo(self):
    """
    Metode som skriver ut informasjon fra et klatrerose objekt
    """
    super().visInfo();
    print(f"{self.navn} er en klatrerose der grenene blir max {self.lengde} cm lange.")

# Legge til flere nye roser i utvalget
def leggTilRoser(butikk):
  # Legge til flere roser i listene til objektet butikk
  fler=input("Legge til flere roser (y/n)? ")
  if fler!="y" and fler!="Y":
    flere=False
  else:
    flere=True
  while(flere):
    navn=input("Navn på rose: ")
    pris=int(input("Pris (kr): "))
    beskrivelse=input("Beskrivelse: ")
    farge=int(input("Farge 1-Rød, 2-Rosa, 3-Hvit, 4-Gul, 5-Andre: "))

    rosetype = int(input("Type 0-Stilk, 1-Busk, 2-Klatre: "))

    if rosetype == 0:
      høyde = int(input("Høyde (cm): "))
      butikk.leggTilRose(rosetype,navn, pris, beskrivelse, farge, høyde)
    elif rosetype == 1:
      bredde = int(input("Bredde (cm): "))
      butikk.leggTilRose(rosetype,navn, pris, beskrivelse, farge, bredde)
    elif rosetype == 2:
      lengde = int(input("Lengde (cm): "))
      butikk.leggTilRose(rosetype,navn, pris, beskrivelse, farge, lengde)

    fler=input("Flere roser (y/n)? ")
    if fler!="y" and fler!="Y":
      flere=False

fargeListe = ["alle","rød","rosa","hvit","gul","andre"]

# Hovedprogram:
# ---------------------
# Lager en rosebutikk
roseHagen = Hagesenter("Rosehagen.no")

# Legger til roser i utvalget
leggTilRoser(roseHagen)

# Vise informasjon om rosene
farge = int(input("Hvilken farge roser vil du se 0-Alle 1-Rød 2-Rosa 3-Hvit 4-Gul 5-Andre: "))
roseHagen.visRoser(farge)

print(float(" 100.3"))