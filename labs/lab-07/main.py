######################################################################################
######################################################################################
######################################################################################
#PLEASE SEE THE ALGORITHMSHANDOUTWRITEUP.DOCX ON CANVAS BEFORE STARTING THE ASSIGNMENT
######################################################################################
######################################################################################

# Creates the poplist and statelist to be used in the program
def getData():
  # opens the file
  infile = open("states.txt", 'r')

  # creates the lists
  stateList = []
  popList = []

  # reads each line, separting the data when it sees a ','; Stores the left as a
  # state, and the right as a population into the accroding list
  line = infile.readline()
  while line != "":
      line = line.strip()
      states, pop = line.split(',')
      stateList = stateList + [states]
      popList = popList + [pop]
      line = infile.readline()

  # closes the file and sends the finished statelist and poplist
  infile.close()
  return stateList, popList

# TODO: Conducts a linear search for the state and keeps track of the number of comparisions made at each step
def getPopLinear(stateList, popList, state):
  # Use comps to keep track of the number of comparisions 
  # **Feel free to change it if you want**
  comps = 0
  #If the state is not in the list return -1 
  population = -1

  # *******Put your solution here********
  # Hint: loop through the statelist, and once you find the state you are looking for, return the population at that same index

  print("Linear Search: comps = ", comps)
  return population

# TODO: Conducts a Binary search for the state and keep track of the number of comparisions made at each step
def getPopBinary(stateList, popList, state):
  # Use comps to keep track of the number of comparisions 
  # **Feel free to change it if you want**
  comps = 0
  #If the state is not in the list return -1 
  population = -1

  #*******Put your solution here********
    #Hint: start at the middle of the state list and compare the state you are looking for with the state you found, if it is less than: iterate on the lower part of the list, if greater than: iterate on the higher part

    #Hint In python you can compare strings by using less than or greater than
    #Example: a > b = False, AL < MA = True, AL > AK = True
    #Use this to compare if the current state you are searching for is greater/less than the one you get in the middle index 

  #Print the number of comparisions at the end
  print("Binary Search: comps = ", comps)

  return population

def getPopFaster(statelist, popList, state):
  #Use comps to keep track of the number of comparisions 
  # **Feel free to change it if you want**
  comps = 0
  # If the state is not in the list return -1
  population = -1

  #*******Put your solution here********
  #Hint look at the different data structures in the python docs (link in last questions below) One of them does all the work for you!

  #Print the number of comparisions at the end 
  print("Faster Search: comps = ", comps)
  return population


#creates lists, and runs other searchses for the proper poulation
def main():
  stateList, popList = getData()

  #asks the user for a state they want to use
  state = input("Enter a state abbreviation: ")

  #Uses functions to get populations
  populationBinary = int(getPopBinary(stateList, popList, state))
  populationLinear = int(getPopLinear(stateList, popList, state))
  populationFaster = int(getPopFaster(stateList, popList, state))

  #if the popluation isnt found, prints invalid abbrevaition
  if populationLinear == -1:
      print("No population provided by getPopLinear()")

  #if it is found, prints the state and the population
  else:
      print("Linear: The population of ", state, " is ", populationLinear)

          #if the popluation isnt found, prints invalid 
  if populationBinary == -1:
      print("No population provided by getPopBinary()")

  #if it is found, prints the state and the population
  else:
      print("Binary: The population of ", state, " is ", populationBinary)

              #if the popluation isnt found, prints invalid 
  if populationFaster == -1:
      print("No population provided by getPopBinary()")

  #if it is found, prints the state and the population
  else:
      print("Faster: The population of ", state, " is ", populationFaster)

#DO NOT TOUCH
if __name__ == "__main__":
    main()
        
#Explain the process of Linear Search. When is it better than Binary Search? What is the runtime of it? How does the number of comparisions differ from binary search (Not just greater than or less than, but in terms of mathematical relations)?

#Explain the process of Binary Search. When can you use binary search? What could you do to the state.txt file to break this function? What is the runtime of it? Explain why this runtime makes sense? (Hint: Think of what binary search is doing at every step)

#Can you think of solution that is faster than binary search? Implement it! Explain why it is faster, and provide its runtime! (Hint: The solution that I though of changes getData() so feel free to change anything but make sure your other functions work too
#This link may be helpful https://docs.python.org/3/tutorial/datastructures.html