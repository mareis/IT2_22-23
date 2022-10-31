import random

bruker = int(input("Velg stein('1'), saks('2') eller papir('3'): "))
data = random.randint(1, 3)

valg = ["stein", "saks", "papir"]
seier = [-1, 2]

s = bruker - data

def ut(a, b):
        print(f"{a}! {valg[bruker-1]} {b} {valg[data-1]}")

ut("Uavgjort", "er lik ") if s == 0 else ut("Seier", "slår") if s in seier else ut("Tap", "taper over")


