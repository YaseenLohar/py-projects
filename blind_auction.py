from art import logo
from replit import clear
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the blind auction")

details = {}

while True:
  state = input("do you want to bid? Y or N : ").lower()
  if state == "y":
    name = input("Enter your name :")
    bid = int(input("How much do you bid?"))
    details[name] = bid
    clear()
  if state == "n":
    break
bids = []
for x in details:
  bids.append(details[x])

win = max(bids)
pos = bids.index(win)

key = list(details.keys())

print(f"The winner is {key[pos]} with a bid of {win} dollars.")
