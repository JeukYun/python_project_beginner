import random
from art import logo
from replit import clear

ans = random.randint(1, 100)


def guess_game():
    print(logo)
    print('welecome to number guessing game')
    print('number : 1~100')
    difficulty = input("difficulty. 'easy' or 'hard' : ")
    chance = 0

    if difficulty == 'easy':
        chance = 8
    elif difficulty == 'hard':
        chance = 5

    while not chance == 0:
        print(f"\nyou have [{chance}] chance to guess number!")
        guess_num = int(input("guess number : "))

        if guess_num == ans:
            print("\nYou Win !!")
            chance = 0
        elif guess_num > ans:
            print(f"Too high... under {guess_num}!!")
            chance -= 1
        elif guess_num < ans:
            print(f"Too low... upper {guess_num}!!")
            chance -= 1
    print(f"--game end-- number is [{ans}]!!")

    re = input("\none more? type 'y' or 'n' : ")
    if re == 'y':
        clear()
        guess_game()


guess_game()
