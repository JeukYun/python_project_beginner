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

#Write your code below this line 👇
import random

list = [rock, paper, scissors]

me = int(input("What do you choose?\nType [0 for Rock], [1 for Paper] or [2 for Scissors]."))

if me < 3:
  print("\nYour choose\n", list[me])
  computer = random.randint(0,2)
  print("\nComputer choose\n", list[computer])
  if me == computer:
    print("Draw")
  elif me == 0 and computer == 1:
    print("You lose")
  elif me == 0 and computer == 2:
    print("You Win")
  elif me == 1 and computer == 0:
    print("You Win")
  elif me == 1 and computer == 2:
    print("You lose")
  elif me == 2 and computer == 0:
    print("You lose")
  elif me == 2 and computer == 1:
    print("You Win")
else:
  print("You type an invalid number, you lose!")



