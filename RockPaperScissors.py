# This program simulates a game of rock, 
# paper, scissors, shot between the user and 
# the program.

from random import randint

#String with options for the game
options = ["ROCK", "PAPER", 'SCISSORS']
message = {"tie":"Yawn it's a tie!", 
"won":"Yay you won!", "lost":"Aww you lost!"}

# Function that decides winner
def decide_winner(user_choice, computer_choice):
  print "User selected %s" % user_choice
  print "Computer selected %s" % computer_choice
#Control flow to determine outcome of game
  if user_choice==computer_choice:
      print message["tie"]
  #User rock, comp scissors
  elif user_choice==options[0] and computer_choice==options[2]:
      print message["won"]
  #User paper, comp rock
  elif user_choice==options[1] and computer_choice==options[0]:
      print message["won"]
  #user scissors, comp paper
  elif user_choice==options[2] and computer_choice==options[1]:
      print message["won"]
  else:
      print message["lost"]

#Function to prompt user for their selection
def play_RPS():
  user_choice=raw_input("Enter Rock, Paper, or Scissors: ")
  user_choice=user_choice.upper()
  computer_choice=options[randint(0,2)]
  decide_winner(user_choice,computer_choice)

play_RPS()
