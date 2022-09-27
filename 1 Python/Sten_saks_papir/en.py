import random 
data = random.randint(1,3)
print(data)
player = int(input("Ditt tall mellom 1 og 3"))
if player == data:
    print("uavgjort")
elif player == 1 and data == 2 or player == 2 and data == 3 or player == 3 and data == 1:
        print("ditt vatn")
else:
        print("din tapet")