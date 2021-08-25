'''
The purpose of this program is to convert feet and inches to meters and centimeters. The user can specify the feet and inches as integers, and we should write a function that will convert those values to meters and centimeters.
'''

# TO DO
# feet_to_meters(x): converts feet to meters
# INPUT: the metric feet the user wants to convert to meters
# OUTPUT: the metric meters converted from the user's feet
def feet_to_meters(feet):
  # Special note: 1 meter = 1 ft / 3.2808
  meters = feet / 3.2808
  return meters

# TO DO
# inches_to_centimeters(x): converts inches to centimeters
# INPUT: the metric inches the user wants to convert to centimeters
# OUTPUT: the metric centimeters converted from the user's inches
def inches_to_centimeters(inches):
  # Special note: 1 inch = 2.54 centimeters
  centimeters = inches * 2.54
  return centimeters


# Provided to initiate the program
def run_exercise1():
  # print("Complete exercise 1")
  
  # Ask the user to input feet
  feet = input("How many feet? ")
  # Convert feet to an int
  feet = int(feet)

  # Ask the user to input inches
  inches = input("How many inches? ")
  # Convert inches to an int
  inches = int(inches)

  # Now do the conversion
  meters = feet_to_meters(feet)
  centimeters = inches_to_centimeters(inches)

  print(f"{feet} feet is {meters} meters.")
  print(f"{inches} inches is {centimeters} centimeters.")


  # TASK:
  # How can we handle negative inputs?
  # Could we keep asking the user to try entering a number again until it's positive?
  # How can we round our conversions to 2 decimal places? Try round(val, precision)