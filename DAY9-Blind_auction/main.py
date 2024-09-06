from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program.")
bidders = {}
end_code = False
while not end_code:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: Rs."))
  bidders[name] = bid
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  if other_bidders == "yes":
    clear()
  else:
    end_code = True
highest_bid = 0
winner = ""
for bidder_name in bidders:
    if bidders[bidder_name] > highest_bid:
        highest_bid = bidders[bidder_name]
        winner = bidder_name
print(f"The winner is {winner} with a bid of Rs.{highest_bid}.")
