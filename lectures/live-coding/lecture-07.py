### LECTURE 7 - Python collections 

## Dictionaries ##

# # Creating a dictionary using the dict() constructor
# players_ages_dict = dict()
# print(f"The type of players_ages_dict is: {type(players_ages_dict)}")

# # Creating a dictionary in-place 
players_ages_dict2 = {"Mario": 45, "Peach": 40, "Yoshi": 100, "Luigi": 43}
# print(f"The players_ages_dict2 is: {players_ages_dict2}")

# # Accessing the values in our dictionary
# # Generally, we use dictionaries to grab the value associated to the key
# marios_age = players_ages_dict2["Mario"]
# print(f"Mario's age is {marios_age}")

# yoshis_age = players_ages_dict2["Yoshi"]
# print(f"Yoshi's age is {yoshis_age}... wow")

# ## Looping (or iterating) through dictionaries
# ## METHOD 1: Looping through the keys
# for elem in players_ages_dict2:
#   print(f"The element (or key) I'm looping on is: {elem}")

# ## METHOD 1 extra tip: You will often see people call it a key in the for loop when looping over the keys of the dictionary (Note how this results in the same print as above)
# for key in players_ages_dict2:
#   print(f"The element (or key) I'm looping on is: {key}")

# ## METHOD 1 cont: You can also just use .keys to loop over:
# for key in players_ages_dict2.keys():
#   print(f"The element (or key) I'm looping on is: {key}")

# ## METHOD 2: Looping over the values of a dictionary 
# for val in players_ages_dict2.values():
#   print(f"The value I'm looping on is: {val}")

# ## METHOD 3: Looping through each item in the dictionary 
# ## Note that this returns they key, value as a pair
# for item in players_ages_dict2.items():
#   print(f"The item I'm looping on is: {item}")
## Fun fact: the above 'item' is a Tuple!

# ## Look at how we could do the same loop above by changing Method 3:
# for item in players_ages_dict2.items():
#   print(f"The item at index 0 is: {item[0]} and the item at index 1 is: {item[1]}")
# ## Above is an illustrative example of how any item, or key-value pair, in a dictionary can be accessed as a tuple

# ## METHOD 4: Looping over the keys AND values 
# for key, value in players_ages_dict2.items():
#   print(f"The key I'm looping on is: {key}, and its value is {value}")
## Fun fact: we are "unpacking" the tuple above

###### Example of using a dictionary ######

# Dictionary to hold the inventory of grocery items
itemInventory = {
  "Apples": 5,
  "Oranges": 4,
  "Peaches": 10,
  "Yogurt": 1
}
## Dictionary for our user's shopping cart
# shoppingCart = {}

is_shopping = True 

while is_shopping:
  print("Add an item to your shopping cart\n")
  print(f"Here is what you can buy:")

  # Loop through the grocery items (key) and their inventory stock (values) from our dictionary
  for key, value in itemInventory.items():
    print(f"{key}: {value} in stock")

  itemToAdd = input("\nEnter an item to add to your cart, or x to quit: ")
  
  # Check if the user has entered x to quit
  if itemToAdd == "x":
    is_shopping = False
    break
  # If they didn't enter x, the program will continue 

  # First, grab the current inventory for this item 
  newInventoryCount = itemInventory[itemToAdd]

  # Now, set the inventory to one fewer than its current inventory
  itemInventory[itemToAdd] = newInventoryCount - 1

  # Print our current inventory for that item now
  print(f"Thank you for adding {itemToAdd} to your cart. There are now {itemInventory[itemToAdd]} {itemToAdd} left in our inventory.")

## If time - what can we do if an item has 0 stock?

## Lists ##
# players_list = ["Mario", "Mario", "Luigi", "Yoshi", "Peach"]
# print(f"The players_list is: {players_list}")
# print(f"The type of players_list is: {type(players_list)}")

## CAN WE CHANGE THE VALUES IN OUR LIST?
# players_list[0] = "Wario" 

## Sets ##
# players_set1 = {"Mario", "Yoshi", "Peach"}
# print(f"The players_set1 is: {players_set1}")
# print(f"The type of players_set1 is: {type(players_set1)}")

# # Trying to add a duplicate Mario
# players_set1.add("Mario")
# print(f"The players_set is: {players_set1}")

# # Trying to create a set with duplicate values
# players_set2 = {"Mario", "Yoshi", "Peach", "Peach", "Peeach"}
# print(f"The players_set2 is: {players_set2}")

## CAN WE CHANGE THE VALUES IN OUR SET?
# players_set2[0] = "Wario"

## IF THERE'S TIME: Tuples ##
# players_tuple = ("Mario", "Mario", "Luigi", "Yoshi", "Peach")
# print(f"The players_tuple is: {players_tuple}")
# print(f"The type of players_tuple is: {type(players_tuple)}")

## CAN WE CHANGE THE VALUES IN OUR TUPLE?
# players_tuple[0] = "Wario" 

# ## How do I add elements to tuples? show in the shell
# players_tuple.add("Mario")
# ## Are there duplicates in my tuple?
# print(f"The players_tuple is: {players_tuple}")

