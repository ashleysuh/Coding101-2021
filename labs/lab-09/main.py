''''
Lab #9: Amy's Lab

Assigned: 7/22/21
Due:      7/24/21 10:30AM EST

To watch Amy describe the lab, please watch this video:
https://www.youtube.com/watch?v=qQlZdQTgrp4 
'''

################################################
# import packages and set up global variables  #
################################################

#this package enables you to simulate wait in terminal
import time

''''
Here we create a global variable 'blackboard'
Which is basically our robot pet's mainframe 
'''
#set up global variables and basic node
global blackboard

## Our blackboard stores information needed by the robotic pet
blackboard = {
    "BATTERY_LEVEL": 100,
    "PLAY_FETCH": 1,
    "FETCH_COUNT": -1,
}

# This function prints information from the blackboard
def print_info():
    print("")
    print("**********blackboard values **********")
    print(blackboard)
    print("**********blackboard values **********")
    print("")

# This class allows assigning numbers to represent statuses
# 0 is considered failure, 1 is success, 2 means running
class task_status(object):
    FAILURE = 0
    SUCCESS = 1
    RUNNING = 2

################################################
# LEVEL 0: raw node                           ##
################################################
class node:
    pass

################################################
# LEVEL 1: The following are 3 types of nodes  #
################################################

class task(node):
    pass

class condition(node):
    pass

#composite is the only type of node that has children nodes
class composite(node):
    def __init__(self, children):
        self.children = children


'''
The following two classes represent sequence and selection nodes
These nodes return running or failure depending on if
the current child is running or not
'''
######################################################
# LEVEL 2: implementations for 3 types of composites #
######################################################

# children will be run following order of input, fail/running as soon as one child fails/running
class sequence(composite):
    def run(self):
        for n in self.children:
            result = n.run()
            if result == task_status.FAILURE:
                return task_status.FAILURE
            elif result == task_status.RUNNING:
                return task_status.RUNNING
        return task_status.SUCCESS

# children will be run following order of input, success/running as soon as one child success/running
class selection(composite):
    def run(self):
        for n in self.children:
            result = n.run()
            if result == task_status.RUNNING:
                return task_status.RUNNING
            elif result == task_status.SUCCESS:
                return task_status.SUCCESS
        return task_status.FAILURE

'''
The following two classes represent condition nodes
These nodes return success or failure depending on
if the robot meets the condition required.
'''
################################################
# LEVEL 2: implementations for conditions      #
################################################

# check_battery returns SUCCESS if the BATTERY_LEVEL is lower than 30
class check_battery(condition):
    def run(self):
        if blackboard["BATTERY_LEVEL"] < 30:
            print ("LOW BATTERY_LEVEL: ", blackboard["BATTERY_LEVEL"], "%")

            return task_status.SUCCESS
        else:
            print ("ENOUGH BATTERY_LEVEL: ", blackboard["BATTERY_LEVEL"], "%")
            return task_status.FAILURE

# return SUCCESS if user choose to execute PLAY_FETCH
class play_fetch(condition):
    def run(self):
        if blackboard["PLAY_FETCH"] == 1:
            return task_status.SUCCESS
        else:
            return task_status.FAILURE

'''
TO DO: complete the run function for the following 5 tasks nodes
'''
################################################
# LEVEL 2: implementations of the pet's tasks  #
# For the 5 task nodes you must complete, you  #
# will be returning the success or running of  #
# a task's status, from the class 'task_status'#
################################################

#go_home task, print something indicating going home, (optional: sleep 1 second), return the task status's SUCCESS if the task has succeeded
class go_home(task):
  # THIS FUNCTION IS GIVEN TO YOU AS A HINT FOR THE REMAINING FUNCTIONS
  def run(self):
    # 1. Print that we're going home 
    print("start go_home")
    # 2. Sleep for 1 second 
    time.sleep(1)
    # 3. Return the task status' success
    return task_status.SUCCESS

#rest task, print that we're resting, put the program to sleep for 3 seconds, recharge that change BATTERY_LEVEL on blackboard, (optional: sleep 10 second), return the task's SUCCESS if the task has succeeded
class rest(task):
  def run(self):
    # TO DO  #
    # 1. Print that we're resting 
    # 2. Sleep for 3 seconds
    # 3. "Recharge" (i.e., update) our blackboard's battery level to be 100
    # 4. Print the new battery level for our pet 
    # 5. Return the task_status' success 
    return -1

#done_fetch task, print something indicating done_fetch, return the task's SUCCESS if the task has succeeded
class done_fetch(task):
  def run(self):
    # TO DO  #
    # 1. Update our blackboard to know that we aren't playing fetch anymore
    # 2. Print that we're done playing fetch 
    # 3. Return the task_status' success
    return -1

''' fetch task
each execution of the fetch task simulates 1 round of fetch
takes 1 second, uses 1 battery level per fetch, and decreases fetch count by 1
return SUCCESS if fetch count is 0, return RUNNING otherwise
'''
class fetch(task):
    def __init__(self, cycle):
      self.cycle = cycle

    def run(self):
      # TO DO  #
      # 1. Print that we're running fetch 
      # 2. Put the program to sleep for 1 second 
      
      # Check if FETCH_COUNT is equal to -1
      # If so, that means we havent played fetch yet, so cycle
      if blackboard["FETCH_COUNT"] == -1:
        blackboard["FETCH_COUNT"] = self.cycle 

      # 3. Check if FETCH_COUNT is equal to 0 
      # 3a. If it is, set PLAY_FETCH to 0 and return the task status' success
      
      # 4. If the two above if-statements don't pass, that means we've already played fetch at least once. Create an else-statement that does the following:
      # 4a. Print how many times we've played fetch now using FETCH_COUNT 
      # 4b. Subtract 1 from the FETCH_COUNT's value and update our blackboard 
      # 4c. Put the program to sleep for 1 second 
      # 4d. Subtract 1 from the BATTERY_LEVEL's value and update our blackboard
      # 4e. Return task_status.RUNNING (note it's not "success" here)

      return -1

'''
do_nothing task, print according message, (optional: sleep 1 second), no battery decrase, return SUCCESS if task succeeds
''' 
class do_nothing(task):
    def run(self):
        # TO DO  #
        # 1. Print that we're starting do_nothing 
        # 2. Put the program to sleep 
        # 3. Return the task_status' success 
        return -1

''''
Builds the behavior tree according to the behavior tree on the handout
'''
################################################
# build behavior tree and main function        #
################################################

# build behavior tree
root = selection(children = [sequence(children = [check_battery(),
                                                 go_home(),
                                                 rest()]),
                            selection(children = [sequence(children = [play_fetch(),
                                                                       fetch(20),
                                                                       done_fetch()
                                                                       ]),
                                                  do_nothing()]),
                            do_nothing()])

''''
Builds the the main function that ask the user to input battery level (0-100) and willingness to play fetch (0 for no, 1 for yes), and run the behavior tree until terminating condition
'''
# main function that takes in user input, and run the behavior tree
def main():
    print("you are in main function") #remove this line 

    CONTINUE_RUNNING = 0
    BATTERY_LEVEL = 0
    PLAY_FETCH = 0

    CONTINUE_RUNNING = int(input("Start the stimulation? (0 = no, 1 = yes)"))

    while (CONTINUE_RUNNING == 1):
        BATTERY_LEVEL = int(input("Current battery level: "))
        PLAY_FETCH = int(input("Play fetch? (0 = no, 1 = yes)"))

        blackboard["BATTERY_LEVEL"] = BATTERY_LEVEL
        blackboard["PLAY_FETCH"] = PLAY_FETCH
        blackboard["FETCH_COUNT"] = -1

        print_info()

        # run the tree starting from the root
        running_success = root.run()

        # TO DO: understand what this while loop does
        while (running_success != 1 or blackboard["PLAY_FETCH"] == 1):
            running_success = root.run()

        if (running_success == 1):
            print("All tasks complete!")
            CONTINUE_RUNNING = 0

    print_info()
    print("Thank you")

# run main
if __name__ == "__main__":
	  main()


'''
Some questions to answer:
1. Explain in your words, how class inheritance works.

2. Explain in your words, how behavior tree works? How does it relay information between nodes? What information is being passed between nodes?

3. What does the second while loop in main function do?

4. What does the "blackboard" do?

5. What is the difference between sequence and selection nodes?

6. EXTRA CREDIT: be creative and build on top of the finished tree with at least 2 new tasks or condition nodes. 
'''