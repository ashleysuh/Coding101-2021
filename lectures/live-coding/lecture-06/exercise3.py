'''
The purpose of this exercise is to draw a pattern of letters to the screen by allowing the user to enter a letter/character they'd like to repeat, and a number of times to repeat that character. For example,
---------------------------------
Enter a character: x
Enter a number: 3

Output:
xxx
xx
x
xx
xxx
---------------------------------
We may need to use the Python print() function without adding a newline at the end of the sentence. We can do this by adding an optional keyword parameter end = "" to the function:
print("Hello, ", end = "")
print("world.") 
'''
# TO DO
# pattern(x, y): repeats the letter x y times, then y-1 times, then y-2... until y=1. Then, repeats +1 times until reaching the number y again.
# INPUT: the letter to be repeated, with the number of times to repeat
# OUTPUT: the printed pattern specified
def pattern(letter, numRepeats):
  # First, we want to print the letter 'numRepeats' number of times
  # Then print it one less time, and then one less time, until we reach 1
  # Once we reach 1, we want to print it again 2 times, then 3 times... until numRepeats

  for i in range(numRepeats, 0, -1):
    print(letter * i)

  for i in range(2, numRepeats+1):
    print(letter * i)


# Provided to initiate the program
def run_exercise2():
  print("Complete exercise 2")

  # Ask the user to enter a single character, represent it as a string
  letter = input("Enter a single letter: ")
  # Do we need to convert anything?

  # Ask the user to enter a number
  num = input("Enter a whole number: ")
  # Convert the number to an int
  num = int(num)

  # Call the pattern function
  pattern(letter, num)