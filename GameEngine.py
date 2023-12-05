import random
import os
from Captain import Captain
from Rabbit import Rabbit
from Veggie import Veggie


class GameEngine:
    __NUMBEROFVEGGIES = 30  # Private constant for initial number of vegetables
    __NUMBEROFRABBITS = 5  # Private constant for number of rabbits
    __HIGHSCOREFILE = "highscore.data"  # Private constant for the name of the high score file

    def __init__(self):
        self.field = []  # List to represent the field
        self.rabbits = []  # List to represent the rabbits in the field
        self.captain = None  # To store the captain object
        self.possible_veggies = []  # List to represent all possible vegetables in the game
        self.score = 0  # To store the score

    def initVeggies(self):
        while True:
            try:
                # Prompt user for the veggie file name
                veggie_file_name = input("Please enter the name of the vegetable point file: ")
                # if os.path.exists(veggie_file_name):
                #     break
                # print(f"{veggie_file_name} does not exist! Please enter the name of the vegetable point file: ")

                # Open the veggie file
                with open(veggie_file_name, 'r') as file:
                    # Read the first line to initialize the field size
                    field_size = file.readline().strip().split(',')

                    rows = int(field_size[1])
                    cols = int(field_size[2])
                    self.field = [[None for _ in range(cols)] for _ in range(rows)]

                    # Read the remaining lines to create a new Veggie object
                    for line in file:
                        veggie_info = line.strip().split(',')
                        veggie_name = veggie_info[0]
                        veggie_symbol = veggie_info[1]
                        veggie_points = int(veggie_info[2])

                        # create new Veggie object that are added to the List of possible vegetables
                        new_veggie = Veggie(veggie_name, veggie_symbol, veggie_points)
                        self.possible_veggies.append(new_veggie)

                        # Place the Veggie object at a random location in the field
                        for _ in range(self.__NUMBEROFVEGGIES):
                            x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
                            if self.field[x][y] is None:
                                x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)

                            self.field[x][y] = random.choice(self.possible_veggies)

                break  # Exit the loop if file reading is successful
            except FileNotFoundError:
                print(f"{veggie_file_name} does not exist! Please enter the name of the vegetable point file: ")
            except Exception as e:
                print(f"An error occurred: {e}")

    def initCaptain(self):
        rows = len(self.field)
        cols = len(self.field[0])

        while True:
            # Choose a random location for the Captain object
            x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)

            # Check if the location is empty
            if self.field[x][y] is None:
                # Create a new Captain object using the random location
                new_captain = Captain(x, y)
                # Store the Captain object in the appropriate member variable - captain
                self.captain = new_captain
                # Assign the Captain object to the random location in the field
                self.field[x][y] = new_captain
                break  # Exit the loop if a valid location is found

    def initRabbits(self):
        rows, cols = len(self.field), len(self.field[0])

        for _ in range(self.__NUMBEROFRABBITS):
            while True:
                # Choose a random location for a Rabbit object
                x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)

                # Check if the location is empty
                if self.field[x][y] is None:
                    # Create a new Rabbit object using the random location
                    new_rabbit = Rabbit(x, y)
                    # Add the Rabbit object to the member variable List of rabbits
                    self.rabbits.append(new_rabbit)
                    # Assign the Rabbit object to the random location in the field
                    self.field[x][y] = new_rabbit
                    break  # Exit the loop if a valid location is found

    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

