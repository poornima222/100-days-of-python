import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

user = int(input())
if user == 0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif user == 1:
    print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
elif user == 2:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
else:
    print("Invalid response!")

computer = random.randint(0,2)
print("Computer chose:")
if computer == 0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif computer == 1:
    print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
else:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

if user == computer:
    print("It's a draw")
elif user == 0 and computer == 1:
    print("You lose")
elif user == 0 and computer == 2:
    print("You win")
elif user == 1 and computer == 0:
    print("You win")
elif user == 1 and computer == 2:
    print("You lose")
elif user == 2 and computer == 0:
    print("You lose")
elif user == 2 and computer == 1:
    print("You win")
else:
    print("Error")