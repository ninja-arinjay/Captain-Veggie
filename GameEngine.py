import random
import os
import pickle
from Captain import Captain
from Rabbit import Rabbit
from Veggie import Veggie


class GameEngine:
    __NUMBEROFVEGGIES = 30  # Private constant for initial number of vegetables
    __NUMBEROFRABBITS = 5  # Private constant for number of rabbits
    __HIGHSCOREFILE = "highscore.data"  # Private constant for the name of the high score file

    def __init__(self):
        self.__field = []  # List to represent the field
        self.__rabbits = []  # List to represent the rabbits in the field
        self.__captain = None  # To store the captain object
        self.possible_veggies = []  # List to represent all possible vegetables in the game
        self.__score = 0  # To store the score
        self.__snake = None

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
            self.__field = [[None for _ in range(cols)] for _ in range(rows)]

            for line in file:
                veggie_name, veggie_symbol, veggie_points = line.strip().split(',')
                new_veggie = Veggie(veggie_name, veggie_symbol, veggie_points)
                self.possible_veggies.append(new_veggie)

        for _ in range(GameEngine.__NUMBEROFVEGGIES):
            while True:
                x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
                if self.__field[x][y] is None:
                    self.__field[x][y] = random.choice(self.possible_veggies)
                    break

    def initCaptain(self):
        """
        A random location is chosen for the Captain object
        """
        rows = len(self.__field)
        cols = len(self.__field[0])

        while True:
            # Choose a random location for the Captain object
            x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)

            # Check if the location is empty
            if self.__field[x][y] is None:
                # Create a new Captain object using the random location
                new_captain = Captain(x, y)
                # Store the Captain object in the appropriate member variable - captain
                self.__captain = new_captain
                # Assign the Captain object to the random location in the field
                self.__field[x][y] = new_captain
                break  # Exit the loop if a valid location is found

    def initRabbits(self):
        """
        For NUMBEROFRABBITS, a random location is chosen for a Rabbit object
        """
        rows, cols = len(self.__field), len(self.__field[0])

        for _ in range(self.__NUMBEROFRABBITS):
            while True:
                # Choose a random location for a Rabbit object
                x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)

                # Check if the location is empty
                if self.__field[x][y] is None:
                    # Create a new Rabbit object using the random location
                    new_rabbit = Rabbit(x, y)
                    # Add the Rabbit object to the member variable List of rabbits
                    self.__rabbits.append(new_rabbit)
                    # Assign the Rabbit object to the random location in the field
                    self.__field[x][y] = new_rabbit
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
        return sum(1 for row in self.__field for item in row if isinstance(item, Veggie))

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
        cols = len(self.__field[0])

        # Print top border
        print("#" * (cols * 2 + 3))

        for row in self.__field:
            # Start each row with a border character
            row_str = "# "

            # For each item in the row, if it is None, print a space; otherwise, print the item
            # print(f"field here is..")
            row_str += " ".join(str(item.get_symbol()) if item else " " for item in row) + " #"

            # Print the row
            print(row_str)

        # Print bottom border
        print("#" * (cols * 2 + 3))

    def getScore(self):
        """
        :return: The current score
        """
        return self.__score

    def moveRabbits(self):
        """
        Function to randomize the hopping pattern of 5 rabbits to eat more veggies
        
        """
        rabbit_hop = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # possible hopping pattern

        # Loop to parse through all the rabbits and update there position
        for rabbit in self.__rabbits:
            if rabbit is not None:
                row, col = random.choice(rabbit_hop)

                # Get new location for a rabbit
                new_x, new_y = rabbit.get_x() + row, rabbit.get_y() + col
                # print("Pos", new_x, new_y)
                # print(len(self.__field), len(self.__field[0]))

                # To check index bounds
                if new_x < 0 or new_x >= len(self.__field) or new_y < 0 or new_y >= len(self.__field[0]):
                    # print("Rabbit cannot move")
                    continue

                # Forfeit rabbit movement if a captain or a rabbit is already present at new location
                elif isinstance(self.__field[new_x][new_y], Rabbit) or isinstance(self.__field[new_x][new_y], Captain):
                    # print("Don't step on bunnies or captain")
                    pass

                # Update location of bunnies if new location is empty or the bunny eats the veggies
                else:
                    self.__field[new_x][new_y] = rabbit
                    self.__field[rabbit.get_x()][rabbit.get_y()] = None
                    rabbit.set_x(new_x)
                    rabbit.set_y(new_y)

    def moveCptVertical(self, movement):
        """
        Tracks the movement of captain veggie in the vertical axis
        """
        curr_x, curr_y = self.__captain.get_x(), self.__captain.get_y()  # get the current location of Captain

        # create new location  using the direction chosen by the user(W,A,S,D)
        new_x, new_y = curr_x + movement, curr_y
        # print(new_x, new_y)

        # Check whether captain can be moved to new location
        if not self.is_valid_move(new_x, new_y):
            print("Invalid move. Try another direction.")

        # Simply update new location of captain
        elif self.is_valid_move(new_x, new_y) and self.__field[new_x][new_y] is None:
            self.update_captain_veggie(new_x, new_y)

        # Harvest veggies, track score and update new location of captain veggie
        else:
            self.found_veggie(new_x, new_y)

    def moveCptHorizontal(self, movement):
        """
        Tracks the movement of captain veggie in the horizontal axis
        """
        curr_x, curr_y = self.__captain.get_x(), self.__captain.get_y()

        # create new location  using the direction chosen by the user(W,A,S,D)
        new_x, new_y = curr_x, curr_y + movement
        # print(new_x, new_y)

        # Check whether captain can be moved to new location
        if not self.is_valid_move(new_x, new_y):
            print("Invalid move. Try another direction.")

        # Simply update new location of captain
        elif self.is_valid_move(new_x, new_y) and self.__field[new_x][new_y] is None:
            self.update_captain_veggie(new_x, new_y)

        # Harvest veggies, track score and update new location of captain veggie
        else:
            self.found_veggie(new_x, new_y)

    def is_valid_move(self, x, y):
        """
        Function to check x,y lies within the field
        return: Boolean
        """
        rows, cols = len(self.__field), len(self.__field[0])
        return 0 <= x < rows and 0 <= y < cols

    def update_captain_veggie(self, x, y):
        """
        Function to keep track of Captain Veggie
        """
        curr_x, curr_y = self.__captain.get_x(), self.__captain.get_y()
        self.__field[curr_x][curr_y] = None
        self.__captain.set_x(x)
        self.__captain.set_y(y)
        self.__field[x][y] = self.__captain

    def found_veggie(self, x, y):
        """
        Function to harvest veggies, track score and update new location of captain veggie
        """
        if isinstance(self.__field[x][y], Veggie):
            veggie = self.__field[x][y]
            print(f"Yummy! A delicious {veggie.get_name()}")
            self.__captain.addVeggie(veggie)
            self.__score += int(veggie.get_points())
            self.update_captain_veggie(x, y)

        # Forfeits move if rabbit present at new location
        elif isinstance(self.__field[x][y], Rabbit):
            print("You should not step on the rabbits! Try another direction.")

    def moveCaptain(self):

        """
        Function that prompts user for a direction to move captain veggie
        """

        direction = input("\nWould you like to move up(W), down(S), left(A), or right(D): ").upper()

        if direction == 'W':
            self.moveCptVertical(-1)
        elif direction == 'S':
            self.moveCptVertical(1)
        elif direction == 'A':
            self.moveCptHorizontal(-1)
        elif direction == 'D':
            self.moveCptHorizontal(1)
        else:
            print("Invalid input. Please enter W, A, S, or D.")

    def gameOver(self):
        """
        Informs the player that the game is over
        """
        print("\nGAME OVER!")

        get_veggies = [veg.get_name() for veg in self.__captain.get_veggies_collected()]
        print(f"You managed to harvest the following vegetables: {', '.join(get_veggies)}")
        print(f"Your score was: {self.__score}")

    def highScore(self):
        """
        Function that stores the top three scores of the game
        """
        high_scores = []

        # check if the highscore.data file exists
        if os.path.exists(GameEngine.__HIGHSCOREFILE):
            with open(GameEngine.__HIGHSCOREFILE, 'rb') as file:
                high_scores = pickle.load(file)

        # ask user for their initials
        initials = input("Please enter your three initials to go on the scoreboard:").upper()[:3]

        # create a tuple with the player;s initials and score
        player_score = (initials, self.__score)

        # add player;s score to the high scores list
        high_scores.append(player_score)
        # sort the list in descending order
        high_scores.sort(key=lambda score: score[1], reverse=True)

        print("\nHIGH SCORES")
        print("\nName\t\tScore")
        for score in high_scores:
            print(f"{score[0]}\t\t\t{score[1]}")

        with open(GameEngine.__HIGHSCOREFILE, 'wb') as file:
            pickle.dump(high_scores, file)
