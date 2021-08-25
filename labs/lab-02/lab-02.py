''''
Lab #2: Python Basics pt. 2 - booleans & conditionals

Assigned: 7/13/21
Due:      7/14/21 10:30AM EST

To complete this lab, look for any "TO DO:" statements in this file and follow the instructions. Please ask the CAs for help when needed. Submit your file through replit when you are done.

If working in groups, feel free to check your answers with your classmates. However, do not simply tell someone the answer to any part of the labs! If you are unsure about anything regarding the lab or short answer questions, please talk to to a CA to get clarification.
'''

##################################################################
# Begin part 1 of Lab 1
# To answer the questions for part 1, you will need to run 
# code using the Python shell. The Python shell can be 
# found on the right side of this screen by clicking on the 
# "Shell" tab. Once you're in the Python shell, type 'python', 
# without the apostrophes, to open the Python terminal.
# Your Python shell will produce a new line that looks like this:
# >>> 
# You can type Python code after the ">>>" to produce an 
# output, or result. Record your responses below next to 
# "ANSWER:" for each question.
##################################################################
'''
TO DO: Answer the short answer questions. When you're done with the short answer questions, check your answers with your classmates and/or the CAs.

0. Please help me get to know you all.  For all of the members in your group, please write each group member's name & where they are from / located below:
EXAMPLE: Ashley Suh - Somerville, MA
ANSWER:

1. Type in 'not True', without the apostrophes, into the shell. What does the output say?
ANSWER:

2. Type in 'not False', without the apostrophes, into the shell. What does the output say?
ANSWER:

3. What do you think the keyword 'not' does in Python?
ANSWER: 

4. Type in 'True and True', without the apostrophes, into the shell. What does the output say?
ANSWER:

5. Type in 'True and False', without the apostrophes, into the shell. What does the output say?
ANSWER:

6. Type in 'False and False', without the apostrophes, into the shell. What does the output say?
ANSWER:

7. Why do you think your answers to 4, 5, and 6 are different?
ANSWER:

8. Type in 'True or True', without the apostrophes, into the shell. What does the output say?
ANSWER:

9. Type in 'True or False', without the apostrophes, into the shell. What does the output say?
ANSWER:

10. Type in 'False or False', without the apostrophes, into the shell. What does the output say?
ANSWER:

11. Why do you think your answers to 8, 9, and 10 are different?
ANSWER:

12. Based on your answers to 7 and 11, what do you think the difference is between the keyword 'and' and the keyword 'or'? Check your answer with the CAs.
'''

##################################################################
# Begin part 2 of Lab 2
# Number guessing game!
# Our program will randomly choose a number.
# The user can try guessing the number.
#
# For the remainder of the lab, you will be writing code to 
# implement a number guessing game. Follow the instructions in 
# the comments (look for the TO DO's), and try running your code 
# using the [ Run > ] button at the top of this page. The output 
# to the code you write here will appear in the "Console" tab on 
# the right of the page.
#
# Note that you may need to look for resources on "Python 
# Comparison Operators" online if you aren't sure where to start. 
##################################################################

# Import the library 'random' from Python
import random

print("Welcome to the number guessing game!\n")
print('''Select your difficulty: 
        1. Easy mode
        2. Medium mode
        3. Hard mode\n''')
difficultyLevel = int(input("Enter a difficulty choice, 1-3: "))

if (difficultyLevel == 1):
  secretNumber = random.randint(1, 5)
  print("\nI'm thinking of a number between 1 and 5.")

elif (difficultyLevel == 2):
  secretNumber = random.randint(1, 10)
  print("\nI'm thinking of a number between 1 and 10.")

else:
  secretNumber = random.randint(1, 20)
  print("\nI'm thinking of a number between 1 and 20.")

''' TO DO: In plain English, explain what the code is doing above using the if, elif, and else statements.
ANSWER: 

'''

# Ask the user to guess a number
print("What do you think the number is?")
guess = int(input())

''' TO DO: Write an if-statement to check if GUESS is larger than SECRETNUMBER '''
# if (...):
  # print("Your guess is too high!")

''' TO DO: Write an if-statement to check if GUESS is smaller than SECRETNUMBER '''
# if (...):
  # print("Your guess is too low!")

''' TO DO: Write an if-statement to check if GUESS is equal to SECRETNUMBER. '''
# if (...):
  # print("You guessed correctly!")

''' TO DO: Once you have finished completing the if-statements above, update your code so the program will tell the user what the secretNumber was whenever the user guesses the wrong number, like so:

"Your guess is too low! The correct answer was 4."

When the user guesses the correct number, the program should not tell the user what the correct answer was, as they already know!'''


''' TO DO: Once you have finished updating your code, answer the following question: 

Notice how the if-statements you wrote check if the number is greater than, less than, or equal to. However, you could write the same code using an if, elif, and else statements like I did earlier when checking what the difficultyLevel was that the user chose. How would you modify your code to use an if, elif, and else instead of 3 if-statements? Type your answer here, then check if you're correct with the CAs if you have time:

ANSWER:


'''