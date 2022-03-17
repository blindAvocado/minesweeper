from game import Game
from config import boardSize, bombCount


def main():
    game = Game(boardSize, bombCount)
    game.run()


if __name__ == "__main__":
    main()
