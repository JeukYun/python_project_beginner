from art import logo, vs
from game_data import data
import random
from replit import clear


def choice_data(X):
  X = random.choice(data)
  return X


game = True
score = 0
A = choice_data(data)
print(logo)

while game:

  B = choice_data(data)

  while A == B:
    B = choice()

  print(f"Compare A : {A['name']}, {A['description']}, from {A['country']}")
  print(vs)
  print(f"Compare B : {B['name']}, {B['description']}, from {B['country']}")

  guess = input("\nWho has more followers? Type 'A' or 'B'").lower()
  count_A = int(A['follower_count'])
  count_B = int(B['follower_count'])

  if guess == 'a' and (count_A > count_B):
    guess = A
    score += 1
    clear()
    print("#####################")
    print("### You Right !!! ###")
    print(f"###### SOCRE {score} ######")
    print("#####################\n\n")

  elif guess == 'b' and (count_A < count_B):
    A = B
    guess = A
    score += 1
    clear()
    print("#####################")
    print("### You Right !!! ###")
    print(f"###### SOCRE {score} ######")
    print("#####################\n\n")

  else:
    clear()
    print("\n######## You Lose ########")
    print(f"Your Final Score is {score} !!")
    print(f"\n{A['name']} has {A['follower_count']} follower")
    print(f"{B['name']} has {B['follower_count']} follower")
    play_more = input("play one moer? : press 'y'").lower()

    if not play_more == 'y':
      game = False
      clear()
    else:
      clear()
