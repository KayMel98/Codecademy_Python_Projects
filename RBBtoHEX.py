""" Program converts RGB values to Hex values and vice versa """

# Converts RGB to Hex
def rgb_hex():
  invalid_msg="Invalid Value Entered"

  #User inputs color values and validity check
  red=int(raw_input("Enter Red value: "))
  if (red < 0 or red > 255):
    print invalid_msg
    return
  green=int(raw_input("Enter Green value: "))
  if (green < 0 or green > 255):
    print invalid_msg
    return
  blue=int(raw_input("Enter Blue value: "))
  if (blue < 0 or blue > 255):
    print invalid_msg
    return
  
  val=(red << 16) + (green << 8) + blue
  print "%s" % (hex(val)[2:]).upper()

# Convert Hex to RGB
def hex_rgb():
   # Get and check user input for hex value
   hex_val=raw_input("Enter Color's Hex Value: ")
   if len(hex_val) != 6:
     print "Invalid Input. Try Again"
     return
   else: 
     hex_val=int(hex_val)

   # Calculate RGB Values
   two_hex_digits = 2 ** 8
   blue = hex_val % two_hex_digits
   hex_val = hex_val >> 8
   green = hex_val % two_hex_digits
   hex_val = hex_val >> 8
   red = hex_val % two_hex_digits
   hex_val = hex_val >> 8

   # print out RGB Values
   print "Red: %s Green: %s Blue: %s" % (red, green, blue)

def convert():
  while True:
    option=raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == "1":
      print "RGB to Hex..."
      rgb_hex()
    elif option == "2":
      print "Hex to RGB..."
      hex_rgb()
    elif option == "x" or option == "X":
      break
    else:
      print "ERROR"

convert()      
