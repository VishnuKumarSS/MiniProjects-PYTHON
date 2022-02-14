# the below program used lists with dictionary.

from clear import clear # importing own function to clear the screen
from bid_logo import logo
print(logo) # to print the bid logo

all_bids=[]
end="yes"
while end!="no":
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    bidder={name:bid}
    all_bids.append(bidder)
    end=input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    clear() # this is the module , used to clear the screen for next bidder. ( Own module )
# print(all_bids)
max=0
winner_name=""
winner_bid=0
for items in all_bids:
    for name in items:
        #print(items[name]) # this returns the corresponding value of that name.
        if items[name] > max:
            max = items[name]
            winner_name=name
            winner_bid=max
print(f"The winner is {winner_name} with a bid of ${winner_bid}.")









# or 
# The below program used only dictionaries ( without list )


# from clear import clear
# from bid_logo import logo
# print(logo)

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()
  