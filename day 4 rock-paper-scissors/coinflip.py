import random

start = input("Type 'flip' to flip a coin! ").lower()
if start == "flip":
    flip = random.randint(1,2)
    if flip == 1:
        print("~heads~")
    else:
        print("~tails~")
else:
    print("Invalid response!")