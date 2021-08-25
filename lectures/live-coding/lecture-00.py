# Hello, and welcome to Coding 101!
# If you're viewing this Replit, congratulations! 
# You've successfully signed up for a replit account and you've managed to find our Coding 101 teams page. Every day, we will release a new replit project for our coding lectures and our coding labs. Before Monday, 7/12/21, this is the only replit project available for you to view.

# When we start class on Monday, 7/12/21, I will walk you through the features of replit, and I will show you how you will be able to "fork" your own version of the projects and work on them yourselves, and in groups. For now, just make sure you have your login credentials available to you so we can use replit together smoothly on the first day of class.

# Feel free to play around in this file and see what the code is doing that I've included below. If you've never coded before, don't fret! We will be covering the basics of programming in Python during the first week of classes.  

# You may be asking yourself, why are we using "replit"?
# Replit is a browser-based IDE that allows you to code in many different programming languages without installing any packages or dependencies. If you've ever tried installing programming tools on your PC before, you know it can be a bit difficult. To avoid problems with Windows vs. Mac OS vs. Linux, we will use replit for the Coding 101 program. Another great feature of replit is that it also allows us to collaborate on projects together in real time! If you already have Python installed, or you already have an IDE you prefer, that's also okay! But please note that you will still need to turn in all of the coding projects and assignments over Replit.
#################################

# I will provide some styling suggestions, and basic things to know about Python here

# Note that any line that starts with a '#' is a COMMENT
# If you delete the '#' character at the start of any line, the text will no longer be interpreted by the Python compiler as a comment, and instead as a line of Python code. You can also make comments by including 3 apostrophes at start and end of a comment message, like so:

'''
This is a comment `block'. Everything between these two sets of apostrophes will be interpreted as a comment by the Python compiler. Using apostrophes is generally preferred when you intend to have a long comment block - in other words, a lot of text. You're free to either the '#' character to start a comment line, or the three apostrophes.

If you're wondering what a Python "compiler" is, please check out these guides:

WHAT IS A COMPILER? Basically, a compiler converts a high-level programming language (like Python) into machine code that a computer can read and execute (like with bits and bytes - 0001110000 etc.) Read more here:
- https://www.eejournal.com/article/what-is-a-compiler-anyway/
- https://www.techopedia.com/definition/3912/compiler
- https://www.thoughtco.com/definition-of-compiler-958198

DOES PYTHON USE A COMPILER? Yes, but Python is also interpreted. This is a very nuanced topic that you do not need to know about if you are still a beginner. However, if you're interested in the difference between a Compiler and an Interpreter, or you'd like to understand how Python compiles/interprets code, then you can watch these videos:
- https://www.youtube.com/watch?v=0BhSWyDEDC4
- https://www.youtube.com/watch?v=civYDSPIIPI
- https://www.youtube.com/watch?v=AisW8ZhqUuc
'''

# How to style your code is typically very subjective. Some people are deadset in how they write code.
# For best practices, please refer to the official Python syntax guide (although it's a bit advanced):
# - https://www.python.org/dev/peps/pep-0008/
# - https://docs.python-guide.org/writing/style/

# In general, code should be written in a way that is EASIEST to read. Look at the difference here:
x = 5 
y=4
# You should always include spaces when assigning a value to a variable. Line 40 is preferable to line 41.

# Do you know what a 'variable' is? 
# A good way to think of a variable is as a container that holds information
# A variable has a name, and it also has a value that can be assigned to it using the '=' character.
# When you write a variable out in your code, you are *declaring* it. Giving it existence, like so:
pi = 3.14

# In this case, I've assigned the decimal value 3.14 to the variable I've named 'pi'
# Variables can be assigned almost any value, like a line of text:
myStringVariable = "This is a string, as opposed to a decimal value like 3.14"

# myStringVariable contains text surrounded by quotation marks ("), which means it's considered a *string* by Python

# When naming variables, you should be as descriptive as reasonably possible (as in, the variable name typically shouldn't be more than a few words max). There are a few choices for syntax when writing variable names, like so:
myVariableName = "This variable is named myVariableName"
my_variable_name = "This variable is named my_variable_name"

# You'll notice that both variables, myVariableName and my_variable_name, contain no spaces.
# That's because NO variable names can contain spaces! Alas, all variable names must be written as a single word.
# In Python, camel case is usually preferred for styling your variables' names.
# Camel case looks like this:
camelCaseExample = "Camel case means the first letter of the first word is lowercase"
camelCaseExample2 = "And each new word that follows will start with a capital letter"

# In line 65, you'll notice that each new word is separated by the '_' character. This is referred to as snake case.
snake_case_example = "Snake case means each word is separated by the underscore character"
snake_case_example_2 = "This style convention is typically used in the C programming language"

# Now that we know how to style and declare variables, what can we do with them?
# One of the easiest things to do is *print* your variables!
# Here, I'll assign a string of text to the variable myGreeting:
myGreeting = "Hello World!"

# Now, I can print it using the print() built-in function in Python
print(myGreeting)
# Try pressing "Run >" at the top of this replit. On the right, you should see a black "console" that will have text printed out after you've hit "Run >". Does the first line say "Hello World!"?

# You can print almost anything you want! For example, you could print a number or decimal:
print(5.211118986)
# Does the second line in the console say 5.211118986?

# You can also print variables that have been declared anywhere else before the print line:
print(myVariableName)
# Does the third line in the console say This variable is named myVariableName? 
# Notice that the variable 'myVariableName' was declared on line 51, but our compiler didn't lose track of it!

# You can also print whatever text you want inside of a print function, like so:
print("This is new text that hasn't been assigned to a variable.")
# Notice that in the console, the line above doesn't have any quotations printed. 
# That's because a string is considered anything inside a pair of quotation marks 
# If you want to print quotation marks, you'll need to include a '\' character before each of them, AND include the outside quotation marks, like so:
print("\"This is new text that hasn't been assigned to a variable, but with QUOTATION MARKS!\"")
# Can you tell the difference between lines 90 and 94

# There is much, much more to learn about the basics of Python, including syntax/styling.
# We will do our best to cover as much as possible during our Coding 101 program.
# Please, never feel discouraged if you don't understand something or if you feel confused.
# Learning to code is like learning to speak a new language.
# You're not going to know all of the nuances of a new language when you start to learn it.
# You will need to practice, learn from others, do independent studying, etc. to improve.
# But with all things in life, the more you practice - the better you'll become!
