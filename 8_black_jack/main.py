import random
from art import logo
from replit import clear


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "computer have black jack"
    elif user_score == 0:
        return "you have black jack"
    elif computer_score > 21:
        return "computer went over, you win"
    elif user_score > 21:
        return "you went over, computer win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\n  user_cards : {user_cards}, current score : {user_score}")
        print(f"  computer first cards : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("want more card? 'y' or 'n' : ")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\n  your final score : {user_score} and final card : {user_cards}")
    print(
        f"  computer final score : {computer_score} and final card : {computer_cards}\n"
    )

    print(compare(user_score, computer_score))

    while input("one more game? 'y'or 'n'") == 'y':
        clear()
        play_game()


if input("play black jack? 'y' or 'no'") == 'y':
    play_game()