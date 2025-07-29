# python3 week-1/dictionaries-and-nesting-day9/secret-auction.py

import time
import os 

def clear():
  if os.name == 'nt': # windows
    os.system('cls')
  else:
    os.system('clear') # linux/mac


def print_message(message, pause=None):
  message_length = len(message)

  for index in range(message_length + 1):
    clear()
    print(message[:index], flush=True)

    if (pause == None):
      time.sleep(0.03)
    else:
      if (index < message_length):
        time.sleep(0.03)
      else:
        time.sleep(pause)  


def is_int(num):
  try:
    int(num)
    return True
  except ValueError:
    return False



print_message("Welcome bidding will start shortly.", 1)  

bidders = {}
num_of_bidders = 0

while (1):
  valid_name = False

  
  total_message = f"Total bidders: {num_of_bidders}\n\n"
  print_message(total_message + "Enter your name,\nor (stop) to end the bid.")  
  name = input("\n")

  if (name == "stop"):
    if (num_of_bidders == 0):
      print_message("Goodbye :)", 1)
      break
    else:
      highest_bid = 0
      winner = ""
      for name in bidders:
        if (bidders[name] > highest_bid):
          highest_bid = bidders[name]
          winner = name
  
      print_message(f"{winner} wins, with a bet of {highest_bid}", 2)
      print_message("Goodbye :)", 1)
      break
  
  if name in bidders:
    print_message("Name already taken, try again :(", 1)
    continue # jump back to the top of the while loop

  while (1):
    print_message("Enter your bet.\n")
    bet = input()
      
    if (is_int(bet)):
      bidders[name] = int(bet)
      break
    else:
      print_message("Invalid bet, please enter a hole number :(", 1)

  

  num_of_bidders += 1

