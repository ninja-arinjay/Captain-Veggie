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
        """
        The field 2D List is populated with NUMBEROFVEGGIES number of new Veggie objects,
        located at random locations in the field.
        """
        while True:
            file_name = input("Please enter the name of the vegetable point file: ")
            if os.path.exists(file_name):
                break
            print(f"{file_name} does not exist! Please enter the name of the vegetable point file: ")

        with open(file_name, 'r') as file:
            field_size = file.readline().strip().split(',')
            rows, cols = int(field_size[1]), int(field_size[2])
            self.field = [[None for _ in range(cols)]for _ in range(rows)]

            for line in file:
                veggie_name, veggie_symbol,veggie_points = line.strip().split(',')
                new_veggie = Veggie(veggie_name,veggie_symbol,veggie_points)
                self.possible_veggies.append(new_veggie)

        for _ in range(GameEngine.__NUMBEROFVEGGIES):
            while True:
                x,y = random.randint(0, rows - 1), random.randint(0, cols - 1)
                if self.field[x][y] is None:
                    self.field[x][y] = random.choice(self.possible_veggies)
                    break

    def initCaptain(self):
        """
        A random location is chosen for the Captain object
        """
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
        """
        For NUMBEROFRABBITS, a random location is chosen for a Rabbit object
        """
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
        """
        This calls the init functions for veggies, captain and rabbits
        """
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

    def remainingVeggies(self):
        """
        This function examines the 'field'
        :return: The number of vegetables still in the game
        """
        return sum(1 for row in self.field for item in row if isinstance(item, Veggie))

    def intro(self):
        """
        In this function, player is welcomed to the game, goal of game is explained, and lists out possible vegetables including
        vegetables name, symbol and points.
        """
        print("Welcome to Captain Veggie!")

        print("The rabbits have invaded your garden and you must harvest " +
              "as many vegetables as possible before the rabbits eat them " +
              "all! Each vegetable is worth a different number of points " +
              "so go for the high score!")

        print("\nThe vegetables are:")
        for veggie in self.possible_veggies:
            print(veggie)

        print("\nCaptain Veggie is V, and the rabbits are R's.")

        print("\nGood Luck!")

    def printField(self):
        """
        In this function,the contents of the field are output in a pleasing 2D grid format with a border around the
        entire grid
        """
        width = len(self.field[0])
        height = len(self.field)

        # Print top border
        print("#" * (width * 2 + 3))

        for row in self.field:
            # Start each row with a border character
            row_str = "# "

            # For each item in the row, if it is None, print a space; otherwise, print the item
            # print(f"field here is..")
            row_str += " ".join(str(item.get_symbol()) if item else " " for item in row) + " #"

            # Print the row
            print(row_str)

        # Print bottom border
        print("#" * (width * 2 + 3))

    def getScore(self):
        """
        :return: The current score
        """
        return self.score

