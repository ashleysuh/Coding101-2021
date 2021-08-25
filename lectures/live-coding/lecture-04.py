### Recall our lab from yesterday:

# userIsShopping = True
# shoppingList = []

# while userIsShopping:
#   print("Shopping list menu: \n" +
#         "(1) Print your shopping list\n" +
#         "(2) Add an item to your shopping list\n" +
#         "(3) Remove an item from your shopping list\n" +
#         "(4) Quit")

#   userInput = int(input("Enter your choice, 1-4: "))
#   if userInput == 1:
#     print("\nYour shopping list is: ")
#     print(f"{shoppingList}\n")

#   elif userInput == 2:
#     print("Type an item to add to your shopping list: ")
#     newItem = input()
#     shoppingList.append(newItem)
#     print("Added the item " + newItem + " to your shopping list.\n")

#   elif userInput == 3:
#     print("Type an item you would like to remove from your shopping list: ")
#     removedItem = input()

#     # First, check if the item is on the list
#     if removedItem in shoppingList:
#       shoppingList.remove(removedItem)
#       print("Successfully removed the item from your list.\n")
#     else:
#       print("Couldn't remove the item because it is not on your list!\n") 
  
#   elif userInput == 4:
#     userIsShopping = False
  
# print("Thank you for using this program.")
########################################################################################

### What if we wanted to modify our code above to keep letting the user add items to their shopping list?

# keepAddingItems = True
newList = []

# while keepAddingItems:
#   newItem = input("Type an item to add it to your list: ")
#   newList.append(newItem)
#   choice = input("Add another item? (Y)es or (N)o: ")

#   if choice == "N":
#     keepAddingItems = False

# print(f"Your shopping list is: {newList}\n")

# ### Next, let's modify the code so the user doesn't need to say Y or N to exit

# keepAddingItems = True

# while keepAddingItems:
#   print("Type an item to add it to your list, or hit Enter to be done: ")
#   newItem = input()

#   if newItem == "":
#     keepAddingItems = False
#   else:
#     newList.append(newItem)

# print(f"Your shopping list is: {newList}")


### In general, loops let us continually do something until we want to stop

# answer = input("What is the capital of France? Type it here: ")
 
# while answer != "Paris":
#  print("Incorrect! Try again.")
#  answer = input("What is the capital of France? Type it here: ")
 
# print("Correct!")

### The format for a while loop is:
# while <condition>:
#   <do something>

### The condition isn't always dependent on the user's input. For example, we may want to use a while loop for a countdown:

### EXAMPLE CODE FOR A 5-SECOND TIMER
# import time

# start = 5
# end = 0
# print(f"Setting a timer for {start} seconds:")

# while start != end:
#   print(f"{start}...")
#   # "sleep" for 1 second to look like a timer
#   time.sleep(1)
#   start = start - 1

# print("Time's up!")

### Remember our guessing game?
# import random
# secretNumber = random.randint(1, 10)
# userGuess = int(input("Guess a number between 1-10: "))

# while userGuess != secretNumber:
#   userGuess = int(input("Wrong guess! Try again: "))

# print(f"Correct! The answer was the secret number {secretNumber} :)")

### There's another very popular method for looping, they're called "for loops". These types of loops are good for iterating through a lot of data, like lists!

### If I wanted to print every word in my list, one on each line, I could do something like this...
shoppingList = ["Apples", "Oranges", "Eggs"]
# print("My shopping list is: ")
# print(shoppingList[0])
# print(shoppingList[1])
# print(shoppingList[2])

### But that can get tiresome if the list is too long:
# moonQuote = ["That’s", "one", "small", "step", "for", "man", "...", "One", "giant", "leap", "for", "mankind"]

# ### We can use for loops for something like this:
# for w in moonQuote:
#   print(f"The word is: {w}")

# index = 0
# print("While version: ")

# while index < len(moonQuote):
#   print(moonQuote[index])
#   index = index + 1

### The format for a for loop is:
## for <variable> in <items>:
##   <do something>
### 
### Note that <variable> is should not have been declared yet. It is a fresh variable being used ONLY FOR OUR for loop. <variable> will keep the value that it ended with. 

### This may seem strange to you, but the structure of a for loop can be translated in English:
### - For each item in all of my items,
###     - Do something with that item

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

### Let's look at what we can do with 'n' in our for loop:
for n in numbers:
  print(f"Number: {n}")
  # print(f"Number * 2: {n*2}")
  ### We can break in our loops
  if n==8:
    continue
  else:
    break

### We can also use a for loop to loop, or iterate, a certain number of times

# for count in range(1, 10):
#   print(count)

### Note that range(a, b) will start the loop at 'a' (inclusive) and then end at 'b' (exclusive)
# for count in range(1, 5):
#   print(count)

### I want to print a list of numbers from 0-20 and indicate whether the number is even or odd
# for num in range(0, 21):
#   if num % 2 == 0:
#     print(f"The number {num} is even.")
#   if num % 2 == 1:
#     print(f"The number {num} is odd.")


#######
# Bonus if we have time: reading files
#
# GENERAL FORMAT:
# with open('filename.filetype') as <variableName>:
#   # do something with file  
#
#######

### This line opens a file from within Python and reads it right here
# with open('greeting.txt') as fileObject:
#   ### We use a for loop to iterate over all the lines of text in our file
#    for textLine in fileObject:
#        print(textLine)

#######
# Extra Bonus if we have time: reading and saving data from files
#######

### create an empty list to store a shopping list of items
# shoppingList = [] 

# with open('shoppingList.txt') as f:
#   ### Each line in our file is an item we want to add to our shoppingList
#   for line in f:
#     ### Add this item to our list
#     shoppingList.append(line)

# ### Now check that we have our list of shopping items
# print("My shopping list: ")
# for item in shoppingList:
#   print(item)

# ### Notice how each item in the list has a large break between the next one? Look what happens when we print the entire list, instead of item by item: 
# print(f"My shopping list: {shoppingList}")

### Do you see how there's a '\n' at the end of each item in the list? The way we were reading the code in, line by line, meant that Python was also capturing the new line. The below code fixes this problem by removing the newline character using .rstrip('\n')

### First, reset our shopping list to display the difference
# shoppingList = []

# with open('shoppingList.txt') as f:
#   ### Each line in our file is an item we want to add to our shoppingList
#   for line in f:
#     ### Add this item to our list
#     l = line.rstrip('\n')
#     shoppingList.append(l)

# ### Now check that we have our list of shopping items
# print("My shopping list: ")
# for item in shoppingList:
#   print(item)