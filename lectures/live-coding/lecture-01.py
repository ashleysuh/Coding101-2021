# Coding 101 - Day 1 - July 12, 2021
# Author: Ashley Suh
# 
# Lecture 1 will cover the basics of Python
# We will work through this file together by using the Console and the Shell, shown on the right of this screen

################################
# USING THE PYTHON SHELL
# - Show the Python shell
# - Show how you can practice Python in the terminal

################################
# WORKING WITH NUMBERS

# You can do arithmetic in the shell in general!
# Try doing 5+2, 20/10, 100*3, 3.33 * 9, ()'s, etc.

# If we want to update certain numbers, we'll need to store them appropriately in variables that we "declare" - so Python will remember them

################################
# WORKING WITH VARIABLES
# - Assigning values to variables
# - Viewing variable values from the shell
# - Updating variable values

# Assign the value 0 to a variable called 'total'
total = 0
# What does the shell say when you type in 'total'?

# Add 2 to total in the shell - the output should be 2
# Does the value of total change?
# How do we update the value of total?
total = total + 2

# Re-assign the value for 'total' to 10
total = 10
# What is 'total' equal to now?

# We can have multiple variables, and they don't need to be whole numbers
# Assign the value 5.5 to a variable called 'newTotal'
newTotal = 5.5
# What does the shell say when you type in 'newTotal'?

# We can add two variables together
newTotal = newTotal + total
# What is 'newTotal' equal to now? What about 'total'?
# Multiple newTotal by 52.37. Divide by 10.2. 

################################
# WORKING WITH STRINGS

# Variables can be assigned other value types besides numbers
message = "Welcome to Coding 101!"

# You can add strings together
message = message + " It is Day 1."
# What is 'message' now?

# You can repeat strings together
message = message * 3
# What is 'message' now?

# Note that strings are taken very literally. Look at when you do "Hello" + "World"
# Note that strings can have spaces between them, but not variable names

###############################
# WORKING WITH PRINT STATEMENTS

# We can also use print(...) to print to the Console, or the shell
print("Hello World!")

# Notice how printing prints a message, where as inputting a string to the shell outputs a string surrounded by 's
# Hello World vs. 'Hello World'

# You can print anything you want
print(5)
print(10.3456)
print("5")
print("My favorite number is 7.")

# You can also print variables!
message = "New message"
print(message)

x = 10
print(x)

# And you can print variables WITH text!
print("My total is: ", total)

# If you add an 'f' before the first ", you can add variables in the middle of print statements:
print(f"My total is {total} and my newTotal is {newTotal}")

###############################
# INPUT FROM CONSOLE

# The last thing we'll cover today is getting input from the shell or console
print("Type something: ")
x = input()

# Now, x will be whatever you put into the console
# You can also put text into an input statement to ask the user for input in the same line, instead of starting a new line like in the above example
userName = input("Enter your name: ")
# And print it:
print(f"You entered {x}, {userName}")

# Whenever we get input from the user through the console, Python will automatically interpret it was a STRING. Like so:
testValue = input("Enter any value: ")
print("The variable 'testValue' has the type: ", type(testValue))
# Even when the variable entered was a number, like 2 or 3.41

# You can convert one value to another, in most cases, Python will let you if it's a valid conversion:
testValue = int(testValue)
# print("The variable 'testValue' now has the type: ", type(testValue))

# This may seem abstract, but the main purpose I'm trying to highlight to you is that there are different types of data that Python is interpreting "behind the scenes". Depending on if the data is a number (integer, float) or text (string) or perhaps a list of numbers (list / array), you may get an error in your code if you try to use a data type in a way that Python doesn't allow you to use it. 

# Whenever you run into an error, read it, and Google it if you're confused. Try sites like stackoverflow for community help, and most importantly - try reading the Python documentation. 

################################
# WHAT YOU LEARNED:

# - Variables can store information for us
# - Variables can be updated
# - Variables can be assigned as whole numbers (Integers)
# - Variables can be assigned as decimals (Floats)
# - Variables can be assigned as text (Strings)
# - You can do math in Python!
# - You can use print() to print a message to the Python console / terminal
# - You can get user input using input()
# - Variables can be remembered by Python, and accessed / read any time after they've been declared
# - Variables have types, depending on the data that's being assigned to it (e.g., '5' is an int type, "Hello" is a str type)
# - You can convert one type to another in Python, using functions like int() - but also str(), float(), etc. Check out the Python documentation if you're interested to learn more

# SPECIAL HINTS
# When you're coding in the Python shell, if you forget to assign your variable to a new value, you can do the following:
# EXAMPLE
# >>> message = "Hello"
# >>> message + " World!"
# 'Hello World!'
# >>> message = _
# >>> message
# 'Hello World!'
# END EXAMPLE
#
# The '_' character will tell Python to assign the variable with the value that came directly before the line. Test it out in the shell!