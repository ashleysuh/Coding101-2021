''''
Lab #1: Python Basics pt.1 

Assigned: 7/12/21
Due:      7/13/21 10:30AM EST

To complete this lab, look for any "TO DO:" statements in this file and follow the instructions. Please ask the CAs for help when needed. Submit your file through replit when you are done.
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

''' TO DO: Answer the short answer questions. When you're done with the short answer questions, check your answers with the CAs.

1. Type in 'type(5)', without the apostrophes, into the shell. What does the output say?
ANSWER:

2. Type in 'type(3.14)', without the apostrophes, into the shell. What does the output say?
ANSWER:

3. Type in 'type("Hello World!")', without the outside apostrophes, into the shell. What does the output say?
ANSWER:

4. What do you think 'type(10)' would output? Check your answer in the shell.
ANSWER:

5. What do you think 'type("5.1")' would output? Check your answer in the shell.
ANSWER:

6. Why do you think the output is different when you type 'type(...)' into the console, depending on what the '...' is inside of the parentheses? 

7. Type in 'type(int)', 'type(float)', 'type(str)', each on a new line without the apostrophes, into the shell. What do the outputs say?
ANSWER:

8. Consider your answers to questions 6 and 7. What do you think 'type(...)' does in Python?
ANSWER:

9. Type in the following line into the Python shell, like so:
    >>> "Welcome to Coding " + 101
When you hit enter, you will get an error:
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can only concatenate str (not "int") to str
Based on the above error, plus your answer to #8, what do you think a "TypeError" is?
ANSWER:

10. Type in the following line into the Python shell, like so:
    >>> "Welcome to Coding " + str(101)
When you hit enter, the Python shell will output the following:
    'Welcome to Coding 101'
Now, type in the following line into the Python shell, like so:
    >>> type(str(101))
Notice what the output says. Why do you think the code works now, without any errors?
ANSWER:

'''

##################################################################
# Begin part 2 of Lab 1
# For the remainder of the lab, you will be writing code to 
# implement a calculator. Follow the instructions in the comments 
# (which are labeled with the character '#' at the start of the line), 
# and try running your code using the [ Run > ] button at the top of 
# this page. The output to the code you write here will appear in the 
# "Console" tab on the right of the page.
##################################################################

# Introduces the user to what the program does
print("CALCULATOR MENU - Here are your options: ")

# Print the calculator menu
print('''
          1. Add two numbers: (x + y)
          2. Subtract two numbers: (x - y)
          3. Multiply two numbers: (x * y)
          4. Divide two numbers: (x / y)
          5. Raise to a power: (x ^ y)
''')
print("Choose a number to proceed, 1-5:")
# Assign user's menu choice to a variable
userChoice = input()

'''
TO DO: Print the user's menu choice that we just assigned to userChoice to the console, with the following text:
"You chose choice number N", where N is the number that the user chose
Comment out the next line and fill it out appropriately '''
# print(...)

# Now, we have the user input their chosen values for x and y
print("Enter a whole number for x: ")
x = input()

''' TO DO: Ask the user to enter a numerical value for y, like what we've done above
Comment out the next two lines and fill them out appropriately '''
# print(...)
# y = ...

# Print the user's value for x
print(f"You chose the value {x} for x.")

''' TO DO: Print the user's choice for y, like what we've done above
If you get an error, read the error and think about why you might have gotten that error!
Comment out the next line and fill it out appropriately '''
# print(...)

# Next, we will convert the user's input values for x and y to ints. This way, we tell Python explicitly to treat those values as numbers so we can perform arithmetic on them.
x = int(x)

''' TO DO: Convert the variable y to an int, similarly to how we did for x above
Comment out the next line and fill it out appropriately '''
# y = ...

# Finally, we implement the different calculator functionalities
#############################
# CHOICE 1: Add two numbers (x + y)
# Fill out the code where you see TO DO's.
#############################
if (userChoice == "1"):
  ''' TO DO: Assign the appropriate value for this option to a variable called 'z'
  Comment out the next line and fill it out appropriately '''
  # z = ...

  ''' TO DO: Fix this print statement by replacing the values for 'x', 'y', and 'z' with the actual values of x, y, and z. 
  For example: "Adding 10 and 2 results in: 20" '''
  print(f"Adding x and y results in: z")

#############################
# CHOICE 2: Subtract two numbers (x - y)
# Fill out the code.
#############################
if (userChoice == "2"):
  ''' TO DO: Assign the appropriate value for this option to a variable called 'z'
  Comment out the next line and fill it out appropriately '''
  # z = ...

  ''' TO DO: Fix this print statement by replacing the values for 'x', 'y', and 'z' with the actual values of x, y, and z. 
  For example: "Subracting 2 from 10 results in: 8" '''
  print(f"Subtracting y from x results in: z")

#############################
# CHOICE 3: Multiply two numbers (x * y)
# Fill out the code.
#############################
if (userChoice == "3"):
  ''' TO DO: Assign the appropriate value for this option to a variable called 'z'
  Comment out the next line and fill it out appropriately '''
  # z = ...

  ''' TO DO: Fix this print statement by replacing the values for 'x', 'y', and 'z' with the actual values of x, y, and z. 
  For example: "Multiplying 10 and 2 results in: 20" '''
  print(f"Multiplying x and y results in: z")

#############################
# CHOICE 4: Divide two numbers (x / y)
# Fill out the code.
#############################
if (userChoice == "4"):
  ''' TO DO: Assign the appropriate value for this option to a variable called 'z'
  Comment out the next line and fill it out appropriately '''
  # z = ...

  ''' TO DO: Fix this print statement by replacing the values for 'x', 'y', and 'z' with the actual values of x, y, and z. For example: "Dividing 10 by 2 results in: 5" '''
  print(f"Dividing x by y results in: z")

#############################
# CHOICE 5: Raise to a power (x ^ y)
# Fill out the code.
#############################
if (userChoice == "5"):
  ''' TO DO: Assign the appropriate value for this option to a variable called 'z'
  Comment out the next line and fill it out appropriately '''
  # z = ...

  ''' TO DO: Fix this print statement by replacing the values for 'x', 'y', and 'z' with the actual values of x, y, and z. For example: "Raising 2 to a power of 5 results in: 32" '''
  print(f"Raising x to a power of y results in: z")

# Tell the user that the program is ending
print("Thank you for using the calculator! Goodbye.")
# END CALCULATOR CODE


# Begin part 3 of Lab 1
'''
# TO DO: Answer the following free-response questions, once you have finished:

9. Notice the repeated lines "if (userChoice == "1")", "if (userChoice == "2")", etc. What do you think this line of code is doing?
ANSWER: 

10. Notice how when we ask the user for their inputs to x and y, we ask them for whole numbers. Then, we convert the values for x and y into ints, like so: "int(x)", "int(y)". Recall from the beginning of this file that when we ran "type(3.14)" into the Python shell, that there was a specific type that was outputted. If we wanted our calculator to accept decimal numbers, similar to 3.14, what type do you think we would need to convert x and y to? 
ANSWER: 
'''

#######################################
# 
# EXTRA CREDIT (if you finish early)
#
# 11. Try updating the code to reflect the suggested change from short answer response #10. What changes in the output to your code?
# 12. Add another choice (#6) to the menu - "Modulo two numbers: (x % y)"
# 13. Implement code for when the user selects choice #6
#       - This will require another "if (userChoice...)" line
#       - Be careful with indentations. Any code inside of an 'if' statement needs a 'tab' first
#
# 14. Try changing the variable "userChoice" to an int after it's been declared, like so: 
#       - userChoice = input()
#       - userChoice = int(userChoice)
#    When you run the code again, you will get an error. Read the error and think about why you might be having that problem. Explain what you think the problem might be, and speculate as to how you might fix the problem. If you think you know the answer, try fixing it in the code! The CAs will be happy to help you with this too!
#######################################
















