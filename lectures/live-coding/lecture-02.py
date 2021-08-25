# Day 2: Lecture 2 (conditionals)

### SHELL
# Assign variables True or False
# Compare variables using math
# See how you can do wacky things with !'s
# What happens if you set something as
# x = !True
# What is x?
# You can think of "!" as a negation... like multipling a number by a negative sign turns it negative. Using a '!' on a boolean negates it and flips the sign: True becomes False, False becomes True

# Talk about how 1 == True, 0 == False
# what happens when we do if(1) ?
# What about if(0) ?
# What about if(1 == True) ?
# What about if(0 == True) ?


### CONDITIONALS

print("Is it True or False?")

if (True):
  print("It's true!")

if (False):
  print("It's false!")

print("Python has spoken.")

##########################################
# Entering two values and comparing them
##########################################

print("Enter two values and I will compare them for you.")
x = input("Value #1: ")
y = input("Value #2: ")

print(f"You chose {x} and {y}. Here's how they stack up: ")

if (x > y):
  print(f"{x} is greater than {y}.")

if (x < y):
  print(f"{x} is less than {y}.")

if (x == y):
  print(f"{x} is equal to {y}.")

# Add >=
# Add <=
# Add !=
# Add else statements - what happens when something is not True?

print("That's all we know.")