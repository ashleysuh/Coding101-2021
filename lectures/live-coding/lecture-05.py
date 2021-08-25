import random

###########################################################################################
# RPS(botChoice, userChoice): Determines if the bot or user has won the RPS game.
# - INPUT: botChoice and userChoice are characters, where 'r'=rock, 'p'=paper, 's'=scissors
# - OUTPUT: Who won the RPS game!
###########################################################################################
def RPS(botChoice, userChoice):
  # Bot has chosen rock
  if botChoice == "r":
    print("Bot chose Rock.")
    if userChoice == "r":
      print("You tie with Rock!")
    elif userChoice == "p":
      print("You win with Paper! Ow, paper cut!")
    else:
      print("You lose with Scissors!")

  # Bot has chosen paper
  elif botChoice == "p":
    print("Bot chose Paper.")
    if userChoice == "r":
      print("You lose with Rock!")
    elif userChoice == "p":
      print("You tie with Paper!")
    else:
      print("You win with Scissors! Snip snip!")

  # Bot has chosen scissors
  else:
    print("Bot chose Scissors.")
    if userChoice == "r":
      print("You win with Rock! I have a headache...")
    elif userChoice == "p":
      print("You lose with Paper!")
    else:
      print("You tie with Scissors!")

rpsChoices = ["r", "p", "s"]
playGame = True

while playGame:
  robotChoice = random.choice(rpsChoices)
  userChoice = input("Bot has chosen. Will you pick (r)ock, (p)aper, (s)cissors, or e(x)it? ")
  # If the user inputs "x", break out of the loop
  if userChoice == "x":
    break
  # If the user hasn't input "x", then call RPS()
  RPS(robotChoice, userChoice)
  print("\n")

print("Thanks for playing!")


###############  
# The remainder of the code in this project is code that was shown in our slides for the day. Feel free to uncomment code and edit it to see what's really happening.
#
# NOTE: Functions should be defined at the top of your program, so if you have a function you want to write or uncomment, put it at the top of this page!
###############


# myList = [1, 2, 3, 4]

# # first way with range():
# for i in range(0, len(myList)):
#   print(f"The element is: {myList[i]}")

# # alt. way without starting at 0 in range():
# print("Only using len(myList): ")
# for i in range(len(myList)):
#   print(f"The element is: {myList[i]}")

# # another way by iterating over elements directly:
# for elem in myList:
#   print(f"The element is: {elem}")

# def multiply_two_numbers(x, y):
#   z = x * y
#   print(f"{x} times {y} equals {z}")
#   return z

# firstVal = int(input("Enter a value for x: "))
# secondVal = int(input("Enter a value for y: "))
# finalVal = multiply_two_numbers(firstVal, secondVal)
# print(f"The z-value returned from our function is: {finalVal}")

# def multiply_two_numbers(x, y):
#   z = x * y
#   print(f"{x} times {y} equals {z}")

# firstVal = int(input("Enter a value for x: "))
# secondVal = int(input("Enter a value for y: "))
# multiply_two_numbers(firstVal, secondVal)

# def print_user_input(message):
#   print("You said: " + message)

# x = input("Enter something you want me to repeat: ")
# print_user_input(x)

# def m2():
#   print("the")

# def m3():
#   print("sat on")
#   m2()

# def m1():
#   m2()
#   print("cat")
#   m3()
#   print("mat")

# m1()

######### ORIGINAL LAB 4 SOLUTION (before a function was made)
# import random

# # imports to be used later
# import numpy as np
# import matplotlib.pyplot as plt

# print("Welcome to Rock Paper Scissors!\n Press x at any time to stop playing the game")

# playGame = True

# while playGame:
#     robot_choice = random.randint(0, 2)
#     user_choice = input("Rock (r), paper (p), scissors (s), or quit (x) ")

#     if user_choice == "x":
#         break
#     elif user_choice != "r" and user_choice != "s" and user_choice != "p":
#         continue

#     # 0 == rock for robot
#     if robot_choice == 0:
#         if user_choice == "r":
#             print("Robot also selected rock, you tie!")
#             results = np.append(results, [1])
#         elif user_choice == "p":
#             print("Robot selected rock, you win!")
#             results = np.append(results, [2])
#         elif user_choice == "s":
#             print("Robot selected rock, you lose!")
#             results = np.append(results, [0])

#     # 1 == paper for robot
#     elif robot_choice == 1:
#         if user_choice == "r":
#             print("Robot selected paper, you lose!")
#             results = np.append(results, [0])
#         elif user_choice == "p":
#             print("Robot also selected paper, you tie!")
#             results = np.append(results, [1])
#         elif user_choice == "s":
#             print("Robot selected paper, you win!")
#             results = np.append(results, [2])

#     # 2 == scissors for robot
#     elif robot_choice == 2:
#         if user_choice == "r":
#             print("Robot selected scissors, you win!")
#             results = np.append(results, [2])
#         elif user_choice == "p":
#             print("Robot selected scissors, you lose!")
#             results = np.append(results, [0])
#         elif user_choice == "s":
#             print("Robot also selected scissors, you tie!")
#             results = np.append(results, [1])
