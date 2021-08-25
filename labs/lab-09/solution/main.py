import time

#set up global variables and basic node
global blackboard

# dictionary
blackboard = {
    "BATTERY_LEVEL": 100,
    "PLAY_FETCH": 1,
    "FETCH_COUNT": -1,
}

class task_status(object):
    FAILURE = 0
    SUCCESS = 1
    RUNNING = 2

class node:
    pass

#################################################################
#The following are 3 types of nodes                          ####
#################################################################
class task(node):
    pass

class condition(node):
    pass

class composite(node):
    def __init__(self, children):
        self.children = children

#################################################################
#The following contain implementations for 3 types of composites#
#################################################################

# children run following order of input, fail/running as soon as one child fails/running
class sequence(composite):
    def run(self):
        print("inside composite node")
        for n in self.children:
            result = n.run()
            if result == task_status.FAILURE:
                return task_status.FAILURE
            elif result == task_status.RUNNING:
                return task_status.RUNNING
        return task_status.SUCCESS

# children following order, success/running as soon as one child success/running
class selection(composite):
    def run(self):
        print("inside selection node")
        for n in self.children:
            result = n.run()
            if result == task_status.RUNNING:
                return task_status.RUNNING
            elif result == task_status.SUCCESS:
                return task_status.SUCCESS
        return task_status.FAILURE

#################################################################
#The following contain implementations for conditions           #
#################################################################

#check_battery condition
#check_battery returns SUCCESS if the BATTERY_LEVEL is lower than 30
class check_battery(condition):
    def run(self):
        if blackboard["BATTERY_LEVEL"] < 30:
            print ("LOW BATTERY_LEVEL: ", blackboard["BATTERY_LEVEL"], "%")

            return task_status.SUCCESS
        else:
            print ("ENOUGH BATTERY_LEVEL: ", blackboard["BATTERY_LEVEL"], "%")
            return task_status.FAILURE

#play_fetch condition
#return SUCCESS if user choose to execute PLAY_FETCH
class play_fetch(condition):
    def run(self):
        if blackboard["PLAY_FETCH"] == 1:
            return task_status.SUCCESS
        else:
            return task_status.FAILURE

#################################################################
#####The following contain implementations of the tasks        ##
#################################################################

#go_home task
#print, sleep 1 tracks time, return SUCCESS
class go_home(task):
  def run(self):
    print("start go_home")
    time.sleep(1)
    return task_status.SUCCESS

#rest task
#print, recharge that change BATTERY_LEVEL on blackboard, return SUCCESS
class rest(task):
  def run(self):
    print("start resting")
    time.sleep(3)
    blackboard["BATTERY_LEVEL"] = 100
    print ("RECHARGED BATTERY_LEVEL: ", blackboard["BATTERY_LEVEL"], "%")
    return task_status.SUCCESS

#done_fetch task
#print, change PLAY_FETCH in blackboard, return SUCCESS
class done_fetch(task):
  def run(self):
    blackboard["PLAY_FETCH"] = 0
    print("done PLAY_FETCH")
    return task_status.SUCCESS

#fetch task
#print, takes 1 second, use 1 battery level per fetch
#return SUCCESS if fetch count is 0, return RUNNING otherwise
class fetch(task):
    def __init__(self, cycle):
      self.cycle = cycle
    def run(self):
        print("doing fetch")
        time.sleep(1)
        if blackboard["FETCH_COUNT"] == -1:
            blackboard["FETCH_COUNT"] = self.cycle

        if blackboard["FETCH_COUNT"] == 0:
            blackboard["PLAY_FETCH"] = 0
            return task_status.SUCCESS

        else:
            print("DO PLAY_FETCH ON ROUND #", blackboard["FETCH_COUNT"])
            blackboard["FETCH_COUNT"] -=1
            time.sleep(1)
            blackboard["BATTERY_LEVEL"] -= 1
            return task_status.RUNNING
        return task_status.RUNNING

#do_nothing task
#print, takes 1 second, no battery decrease, return SUCCESS
class do_nothing(task):
    def run(self):
        print("start do_nothing")
        time.sleep(1)
        return task_status.SUCCESS

################################################
#      build behavior tree and main           ##
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
                            ])

# print information on the blackboard
def print_info():
      print("")
      print("**********blackboard values **********")
      print(blackboard)
      print("**********blackboard values **********")
      print("")

# main function that takes in user input, and run the behavior tree
def main():
    CONTINUE_RUNNING = 0
    BATTERY_LEVEL = 0
    PLAY_FETCH = 0

    CONTINUE_RUNNING = int(input("Would you want to start the stimulation: (0 for no, 1 for yes)"))

    while (CONTINUE_RUNNING == 1):
        BATTERY_LEVEL = int(input("Current battery level (please input value from 0 to 100): "))
        PLAY_FETCH = int(input("Do you want your pet to play fetch: (0 for no, 1 for yes)"))

        blackboard["BATTERY_LEVEL"] = BATTERY_LEVEL
        blackboard["PLAY_FETCH"] = PLAY_FETCH
        blackboard["FETCH_COUNT"] = -1

        print_info()

        running_success = root.run()

        while (running_success != 1 or blackboard["PLAY_FETCH"] == 1):
            running_success = root.run()

        if (running_success == 1):
            print("All tasks complete!")
            CONTINUE_RUNNING = 0

    print_info()
    print("Thank you :)")

# run main
if __name__ == "__main__":
	main()

#################################################
#### if we want to limit user input         #####
#################################################
    # while True:
    #   try:
    #       CONTINUE_RUNNING = int(input("Would you want to start the stimulation: (0 for no, 1 for yes)"))
    #   except ValueError:
    #       print("Sorry, please input 0 for no, 1 for yes.")
    #       continue
    #   if CONTINUE_RUNNING == 1:
    #       break
    #   if CONTINUE_RUNNING == 0:
    #       break
    #   else:
    #       print("Sorry, please input 0 for no, 1 for yes.")
    #       continue

      # while True:
      #     try:
      #         BATTERY_LEVEL = int(input("Current battery level: "))
      #     except ValueError:
      #         print("Sorry, battery level has to be a number between 0 and 100.")
      #         continue
      #     if BATTERY_LEVEL > 100:
      #         print("Sorry, battery level has to be a number between 0 and 100.")
      #         continue
      #     if BATTERY_LEVEL < 0:
      #         print("Sorry, battery level has to be a number between 0 and 100.")
      #         continue
      #     else:
      #         break
      #
      # while True:
      #     try:
      #         PLAY_FETCH = int(input("Do you want your pet to play fetch: (0 for no, 1 for yes)"))
      #     except ValueError:
      #         print("Sorry, please input 0 for no fetch, 1 for yes fetch.")
      #         continue
      #     if PLAY_FETCH == 1:
      #         break
      #     if PLAY_FETCH == 0:
      #         break
      #     else:
      #         print("Sorry, please input 0 for no, 1 for yes.")
      #         continue