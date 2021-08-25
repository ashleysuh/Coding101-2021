
# Week 1, Day 3: Wednesday
# Lecture 3: LISTS

### We can have lists of any type, including strings or integers or floats, etc. We can also have lists with a mix of types, like so:
randomList = ["Hello", 2, 3.14, True]
# print(f"The type of the above list is: {type(randomList)}\n")

### Let's go ahead and start working with lists now
### List of classroom assistants, in alphabetical order, for C101
classroomAssistants = ["Aaron", "Amy", "Brawner", "Brooks", "Emily", "Jackson"]

### List of odd numbers between 0-9
oddNumbers = [1, 3, 5, 7, 9]

### List of even numbers between 0-9
evenNumbers = [0, 2, 4, 6, 8]

### WHAT CAN WE DO WITH LISTS?
### First, we can print any list by passing it to the print() function 
print(f"List 1: {classroomAssistants}")
print(f"List 2: {oddNumbers}")
print(f"List 3: {evenNumbers}")

# print("My list is: " + str(oddNumbers))

### Show how to access the elements of the list
print(oddNumbers[0])
print(evenNumbers[0])
print(classroomAssistants[0])

### Notice how when we access the first element of our list, we use the index 0
print(oddNumbers[1])
print(evenNumbers[1])
print(classroomAssistants[1])

### That means the last element of the list will have the index (n-1), where n is the total number of elements in the list 
print(oddNumbers[4])
print(evenNumbers[4])
print(classroomAssistants[5])

### Is there a way to access the last element of the list automatically? You bet!
print(oddNumbers[-1])
print(evenNumbers[-1])
print(classroomAssistants[-1])
### In general, passing a negative index to access an element in your list will count backwards. It's a little weird to wrap your head around, so you don't need to worry about it.

### What happens if we try to access an element in the list that doesn't exist?
### Let's try it out
### We know that the last index of our list 'oddNumbers' is 4
### Let's try accessing the element at index 5:
# print(oddNumbers[5])
### What does the error mean?

### Sometimes, we may want to assign the values from a list to a variable
firstOdd = oddNumbers[0]
firstEven = evenNumbers[0]

print(f"\nThe very first odd number is {firstOdd} and the very first even number is {firstEven}\n")

# oddNumbers[0] = -10
# print(oddNumbers)
# print(firstOdd)

### We can do arithmetic again with our lists!
print("The sum of our odd numbers is...")
sumOfOdds = oddNumbers[0] + oddNumbers[1] + oddNumbers[2] + oddNumbers[3] + oddNumbers[4]
print(f"{sumOfOdds}.\n")

print("The sum of our even numbers is...")
sumOfEvens = evenNumbers[0] + evenNumbers[1] + evenNumbers[2] + evenNumbers[3] + evenNumbers[4]
print(f"{sumOfEvens}.\n")
###


### We can add elements to our lists by using .append(x), where x is the element you want to add to the list

### Add a few more odd and even numbers to our lists
oddNumbers.append(11)
oddNumbers.append(13)

### Check how the list looks now
print(f"List of odds: {oddNumbers}")

### We can also remove the last element that was added to a list using .pop()
oddNumbers.pop()

### Check how the list looks now
print(f"List of odds: {oddNumbers}")

### Can we remove an element from our list anywhere? Yes! Using .remove(x), where x is the element you want to remove from the list
oddNumbers.remove(5)

### Check how the list looks now
print(f"List of odds: {oddNumbers}")

### If we can remove an element anywhere from our list, can we also add an element anywhere into our list? Yes! Using .insert(newPosition, x), where newPosition is the index for WHERE you want to add the new element x to the list

### For example, let's add the number -1 to the start of the list (index 0)
oddNumbers.insert(0, -1)

### Check how the list looks now
print(f"List of odds: {oddNumbers}")

### Let's do one more example
oddNumbers.insert(2, 100)

### What will the list look like?
# print(oddNumbers)

### Remember this is how our list looks:
### [ _  _  _  _  _  _ ] 
###   0  1  2  3  4  5
### Where the bottom numbers are the index values for the positions of the elements in our list

### So where will 100 get inserted?
# print(f"List of odds: {oddNumbers}")

### What happens if we try to remove an element that doesn't exist?
### Let's try removing the number 200, which doesn't exist in our list:
# oddNumbers.remove(200)
### What does the error mean?

### Check if an element is in our list, let's try the element 100
if 200 in oddNumbers:
  print("Why is 200 in there??")
  oddNumbers.remove(200)
else:
  print("200 isn't an odd number, silly.")

### Now, we can make it a little more complex:
chosenNumber = int(input("Enter a whole number between 0-9: "))

# x = input()

### Determine if the user's input is an even or odd number
if chosenNumber in evenNumbers:
  print("The number you chose is even.")
else:
  print("The number you chose is odd.")
