# This code asks a user to guess the value of 
# a dice roll, simulates the roll them 
# determines if the user guess equals the 
# simulated roll
# Kaylen 2022

#Import functions to use later
from random import randint
from time import sleep

# Function gets users guess
def get_user_guess():
  guess=int(raw_input("Enter Guess: "))
  return guess

# Function that simulates dice roll
def roll_dice(number_of_sides):
  roll_1=randint(1,number_of_sides)
  roll_2=randint(1,number_of_sides)
  max_val=number_of_sides*2
  print "The maximun value is %d" % max_val
  guess=get_user_guess()
  if guess > max_val:
    print "Invalid Input"
  else: 
    print "Rolling..."
    sleep(2)
    print "The first roll is: %d" % roll_1
    print "The second roll is: %d" % roll_2
    sleep(1)
    # Determine Winner 
    total_roll=roll_1+roll_2
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "You Win!"
    else:
      print "You Lose :("
#Test function
roll_dice(6)
