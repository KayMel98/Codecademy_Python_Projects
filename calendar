""" This program builds a calendar the user can interact with including viewing the calendar, adding events, and editing existing the calendar """

# Import required functions
from time import sleep, strftime

# User's name
user_name = "Kaylen"
calendar ={}

#Function for welcome message
def welcome():
  print "Welcome, " + user_name + "."
  print "Your Calendar is now opening..."
  sleep(1)
  print "Today is: " + strftime("%A %B %d %Y")
  print "The time is: " + strftime("%X")
  print "What would you like to do?"

#Function to start calendar
def start_calendar():
  welcome()
  #while loop
  start = True
  while start:
    #Start making calendar w/ user choice
    user_choice = raw_input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit")
    user_choice = user_choice.upper()
    # If statement ptocesses user input
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "The calendar is empty" 
      else:
        print calendar
    elif user_choice="U":
      date=raw_input("What date? ")
      update=raw_input("Enter the Update: ")
      calendar[date]=update
      print "Update Successful"
      print calendar
    elif user_choice="A":
      event=raw_input("Enter Event: ")
      date=raw_input("Enter Date (MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[6:]) < int(strftine("%Y"))):
        print "Incorrect date format"

