import logging
from utils import read_file, board_validation, clock, get_neighborhood_coord
from pprint import pprint

logger = logging.getLogger(__name__)


def run_game():
    generation, width, height, board = read_file("input_data.txt")
    ok = board_validation(width, height, board)
    if not ok:
        logger.error("Bad board!")
        return False
    logger.info(board)

    for iteration in range(generation):
        board = clock(board)
    logger.info("End Game!")
    logger.info(board)
