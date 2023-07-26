from replit import clear
from art import logo

other_bidder = True
list = {}

while other_bidder:
  print(logo)
  print("Welcome to the secret auction program. ")
  name = input("What is your name? : ")
  bid = input("What's your bid? : $")
  list[name] = bid
  other_bidder = input("Are there any other bidders? Type 'yes' or 'no' ")

  clear()
  
  if other_bidder == 'no':
    other_bidder = False


prince = 0
w_name = []
w_bid = []

for key in list:
  if int(list[key]) > prince:
    prince = int(list[key])
    w_name = key
    w_bid = list[key]
  elif int(list[key]) == prince:
    w_name += " ," + key 
    w_bid += " " + ",$" + list[key]


print(f"The winner is {w_name} with a bid of ${w_bid}")