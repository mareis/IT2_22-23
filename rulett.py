from random import randint
import matplotlib.pyplot as plt 

tot = 0
antant = 1000
sim = []
for i in range(1, antant+1):
    person1 = 0
    ant = 100_000
    for rulett in range(ant):
        gønner = [0 for x in range(6)]
        gønner[randint(0, 5)] = 1

        if gønner.index(1)%2 == 0:
            person1 += 1

    sim.append(tot/i)

    print(i, person1/ant, tot/i) 
    if person1/ant > 0.5:
        tot+=1 

print(tot/antant)

plt.plot(sim)
plt.show()


