# This program allows the user to  calculate 
# the area of a circle or square based on the
# dimensions of that shape they input
import math
# Informs the user the program is running
print("The Area Calculator is now running.")

#Gets user input for shape name
option = raw_input("Enter a C for Circle or T for Triangle: ")

# Selects the right calculation type, then 
# prompts user for input and calculates area
if option == "C":
  radius = float(raw_input("Enter the radius: "))
  area = 3.14159 *(radius**2)
  print "Area: %f" % area
elif option == "T":
  base = float(raw_input("The base of the triangle is: "))
  height=float(raw_input("The height of the triangle is: "))
  area = .5*base*height
  print "Area: %f" % area
# Handle invaild inputs by user
else:
  print "Invalid shape entered, try again."

# Inform user you are exiting program
print "You are now exiting the program"
