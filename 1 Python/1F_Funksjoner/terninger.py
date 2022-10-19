import random as rd
def terning(antallSider: int) -> int:
  """Returnerer et tilfeldig heltall i intervallet [1, antallSider], med begge endepunktente inkludert."""
  return rd.randint(1, antallSider)