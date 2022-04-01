import os
from art import logo

print(logo)
print("Welcome to the Secret Auction")
list_of_bids = []
secret_auction = True

while secret_auction:
    bids = {}
    name = input("What is your name:\n")
    bid = int(input("What is your bid:\n$"))
    bids[name] = bid
    list_of_bids.append(bids)
    other_bidder = input("Are there any other bidders? Yes or No\n").lower()
    if other_bidder == 'no':
        secret_auction = False
    elif other_bidder == 'yes':
        os.system('cls')
    
highest = 0
for bidding in list_of_bids:
    for bidder in bidding:
        if bidding[bidder] > highest:
            highest = bidding[bidder]
print(f"The highest bid was of {highest}$ and it was made by {bidder}!")

