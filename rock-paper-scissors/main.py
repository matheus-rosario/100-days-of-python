rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

computer = random.randint(0, 2)

if player == 0:
  if computer == 0:
    print(rock)
    print("Computer chose:\n" + rock + "\nDraw")
  elif computer == 1:
    print(rock)
    print("Computer chose:\n" + paper + "\nYou lose")
  else:
    print(rock)
    print("Computer chose:\n" + scissors + "\nYou win")

elif player == 1:
  if computer == 0:
    print(paper)
    print("Computer chose:\n" + rock + "\nYou win")
  elif computer == 1:
    print(paper)
    print("Computer chose:\n" + paper + "\nDraw")
  else:
    print(paper)
    print("Computer chose:\n" + scissors + "\nYou lose")

elif player == 2:
  if computer == 0:
    print(scissors)
    print("Computer chose:\n" + rock + "\nYou lose")
  elif computer == 1:
    print(scissors)
    print("Computer chose:\n" + paper + "\nYou win")
  else:
    print(scissors)
    print("Computer chose:\n" + scissors + "\nDraw")

else:
  print("You typed an invalid number. You lose!")