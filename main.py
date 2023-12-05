from GameEngine import GameEngine


def main():
    game_engine = GameEngine()  # Instantiate the GameEngine object
    game_engine.initializeGame()
    game_engine.intro()

    remaining_veggies = game_engine.remainingVeggies()

    # print(f"{remaining_veggies} veggies remaining. Current score: {game_engine.getScore()}")

    # game_engine.printField()  # I am calling it here just to check the output. It should only be called inside While
    # loop, below. Please remove this when below While loop is defined properly

    while remaining_veggies > 0:
        print(f"\n{remaining_veggies} veggies remaining. \nPlayer's score: {game_engine.getScore()}")
        # calls the function that prints the field
        game_engine.printField()

        # Moves the rabbits in 8 directions randomly
        game_engine.moveRabbits()

        # Moves captain in as per user input( up(W), down(S), left(A), right(D))
        game_engine.moveCaptain()

        # Updates remaining veggies
        remaining_veggies = game_engine.remainingVeggies()

    # Informs user that the game is over
    game_engine.gameOver()

    # Function to keep track of highscore
    game_engine.highScore()


if __name__ == "__main__":
    main()
