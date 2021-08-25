# import our libraries to be used

# random allows us to generate pseudo-random numbers to be used
import random

# imports to be used later
import numpy as np
import matplotlib.pyplot as plt

print("Welcome to Rock Paper Scissors!\n Press x at any time to stop playing the game")

playGame = True

# create numpy array to hold results
results = np.array([])

while playGame:
    robot_choice = random.randint(0, 2)
    user_choice = input("Rock (r), paper (p), scissors (s), or quit (x) ")

    if user_choice == "x":
        break
    elif user_choice != "r" and user_choice != "s" and user_choice != "p":
        continue

    # 0 == rock for robot
    if robot_choice == 0:
        if user_choice == "r":
            print("Robot also selected rock, you tie!")
            results = np.append(results, [1])
        elif user_choice == "p":
            print("Robot selected rock, you win!")
            results = np.append(results, [2])
        elif user_choice == "s":
            print("Robot selected rock, you lose!")
            results = np.append(results, [0])

    # 1 == paper for robot
    elif robot_choice == 1:
        if user_choice == "r":
            print("Robot selected paper, you lose!")
            results = np.append(results, [0])
        elif user_choice == "p":
            print("Robot also selected paper, you tie!")
            results = np.append(results, [1])
        elif user_choice == "s":
            print("Robot selected paper, you win!")
            results = np.append(results, [2])

    # 2 == scissors for robot
    elif robot_choice == 2:
        if user_choice == "r":
            print("Robot selected scissors, you win!")
            results = np.append(results, [2])
        elif user_choice == "p":
            print("Robot selected scissors, you lose!")
            results = np.append(results, [0])
        elif user_choice == "s":
            print("Robot also selected scissors, you tie!")
            results = np.append(results, [1])

# represent our x-axis as the number of rounds we played RPS 
# we can use numpy's to create an array from [0, 1, ..., n], where n is the size of our 'results' numpy array
x = np.arange(len(results))
# add a line chart with our game rounds as the x-values and our game results as the y-values
plt.plot(x, results, 'o-b')
# the x-axis tick marks should start at 0 and end at the number of RPS rounds, we tell matplotlib this explicitly 
plt.xticks(range(0, len(results)))
# the y-axis tick marks should be labeled as 'Loss' when the result is 0, 'Tie' when the result is 1, and 'Win' when the result is 2
plt.yticks([0, 1, 2], ['Loss', 'Tie', 'Win'])
# label our x-axis
plt.xlabel('Game Round')
# label our y-axis
plt.ylabel('Game Result')
# label our plot
plt.title("Rock-Paper-Scissors Results Per Round")
plt.show()

### Read more about plotting simple line charts here: https://datascienceparichay.com/article/plot-a-line-chart-in-python-with-matplotlib/ ###