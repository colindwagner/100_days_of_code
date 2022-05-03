
#HINT: You can call clear() to clear the output in the console.
from art import logo
import os
clear = lambda: os.system('clear')

auction_dict= {}
def add_to_auction(name, bid):
    auction_dict[name] = bid

def determine_winner(dict_to_win):
    highest_bid = 0
    winner = ''
    for bidder in dict_to_win:
        bid_amount = dict_to_win[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with ${highest_bid}")


print(logo)
print("Welcome to the secret auction program")

stay_on = True
while stay_on:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    add_to_auction(name, bid)
    cont = input("Are there any other bidders? Type 'yes' or 'no'")
    if cont == 'no':
        stay_on = False
    elif cont == 'yes':
        clear()
    determine_winner(auction_dict)


