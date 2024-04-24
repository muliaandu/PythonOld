# Welcome message.
print(f"Welcome to The Secret Auction program.")

# Module.
import os
# Variable.
auction = {}
bidding_finished = False
# Function
def bid_auction():
    auction[name] = bid

def win_auction():
    winner_bid = 0
    winner = ""
    for name in auction:
        win_bid = auction[name]
        if win_bid > winner_bid:
            winner_bid = win_bid
            winner = name
    print(f"The Winner is {winner} with a bid of ${winner_bid}")

another_bidders = ""
while not bidding_finished:
    # Ask name.
    name = input(f"What is your name : ")
    # Ask how much bid.
    bid = int(input(f"What is your bid : $"))
    # Ask another bidders
    bid_auction()
    another_bidders = ""
    while another_bidders != "yes" or another_bidders != "no":
        another_bidders = input(f"Are there any other bidders? Type 'yes' or 'no'. ").lower()
        if another_bidders == "no":
            print(auction)
            win_auction()
            bidding_finished = True
        elif another_bidders == "yes":
            os.system('cls')
            break