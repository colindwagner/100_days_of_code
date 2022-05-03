
import os
from art import logo
import random


def dealcard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def determine_score(list_of_cards):
    score = 0
    for card in list_of_cards:
        score += card
    return score

def determine_winner(user_score, computer_score):
      #Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and computer_score > 21:
      return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def blackjack2():
    print(logo)
    users_cards = []
    cpu_cards = []
    users_cards.append(dealcard())
    users_cards.append(dealcard())
    cpu_cards.append(dealcard())
    print(f"Your cards: {users_cards}")
    print(f"Computer's first card: {cpu_cards}")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while another_card == 'y':
        users_cards.append(dealcard())
        print(users_cards)
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    
    user_score = determine_score(users_cards)
    dealer_score = determine_score(cpu_cards)

    while (dealer_score) < 21 and (dealer_score < user_score):
        cpu_cards.append(dealcard())
        dealer_score = determine_score(cpu_cards)

    print(f"Computer's final hand: {cpu_cards}")

    determine_winner(user_score=user_score, computer_score=dealer_score)


    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game == 'y':
        blackjack2()


play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play_game == 'y':
    blackjack2()
else:
    print("You're no fun")