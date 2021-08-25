##########################################################################
class ShoppingCart:
  # When we create a new instance of our ShoppingCart class,
  # we create an empty dictionary to represent the shopping list
  def __init__(self):
    self.shoppingCart = {}

  def destroy_cart(self):
    self.shoppingCart = {}

  # Add the item to our shoppingList dictionary 
  # Where the name is its key, and the item's quantity is its value
  def add_item(self, item, quantity):
    self.shoppingCart[item] = quantity

  # Function to remove our item from our dictionary 
  # If the item doesn't exist, we return -1
  def remove_item(self, item):
    removed = self.shoppingCart.pop(item, False)

    if removed:
      print(f"Successfully removed {item} from the cart.")
    else:
      print(f"{item} was not in your cart, couldn't remove it.")

  # This is a built-in method of all classes
  # Which lets us overwrite how the class object is printed
  def print_cart(self):
    # This if-statement checks if our shopping cart is empty
    if not self.shoppingCart:
      print("Your shopping cart is empty.")
    # If it's not, then print each item and its quantity
    else:
      print("Your shopping cart is:\n------------------------")
      for key, val in self.shoppingCart.items():
        print(f"{key}: {val}")
      print("------------------------")
##########################################################################
## BEGIN THE ACTUAL PROGRAM 

# First, let's create an instance of a shoppingCart 
# using an empty dictionary as input
shoppingCart = ShoppingCart()

# Now, let's have users create new items to add to their list
is_shopping = True

while is_shopping:
  print("Shopping cart menu: \n" +
      "(1) Print your shopping cart\n" +
      "(2) Add an item to your shopping cart\n" +
      "(3) Remove an item from your shopping cart\n" +
      "(4) Destroy your shopping cart\n" +
      "(5) Quit")

  userInput = int(input("Enter your choice, 1-4: "))
  print()

  if userInput == 1:
    # Call the print_cart() method from my shoppingCart object
    shoppingCart.print_cart()

  elif userInput == 2:
    itemName = input("Enter the item to add to your cart: ")
    itemAmt = int(input(f"How many {itemName}s do you want to add? "))
    # What do I do here?
    shoppingCart.add_item(itemName, itemAmt)

  elif userInput == 3:
    itemName = input("Enter an item to remove it from your shopping cart: ")
    shoppingCart.remove_item(itemName)

  elif userInput == 4:
    areYouSure = input("Are you sure? (y)es, (n)o: ") 

    if areYouSure == 'y':
      shoppingCart.destroy_cart()
      print("Cart was destroyed.")
    else:
      print("Cart was not destroyed.")

  else:
    is_shopping = False
  
  print("\n")

# Program ending
print(f"Thank you for using our shopping cart program!")
  