import logging
from app.game_of_life import run_game

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


if __name__ == '__main__':
    run_game()
