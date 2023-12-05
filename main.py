from GameEngine import GameEngine


def main():
    game_engine = GameEngine()  # Instantiate the GameEngine object
    game_engine.initializeGame()
    game_engine.intro()

    remaining_veggies = game_engine.remainingVeggies()

    print(f"{remaining_veggies} veggies remaining. Current score: {game_engine.getScore()}")

    game_engine.printField()  # I am calling it here just to check the output. It should only be called inside While
    # loop, below. Please remove this when below While loop is defined properly

    # while remaining_veggies > 0:
    #     print(f"{remaining_veggies} veggies remaining. Current score: {game_engine.getScore()}")
    #     game_engine.printField()

    # rest of the function calls


if __name__ == "__main__":
    main()
