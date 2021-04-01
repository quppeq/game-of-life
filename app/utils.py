import logging
from typing import List, Tuple, Sequence

GAME_SYMBOL = "x."
LIVE = 'x'
DEAD = '.'
logger = logging.getLogger(__name__)


def read_file(file_path: str) -> Tuple[int, int, int, List[str]]:
    """

    :param file_path:
    :returns:
    :returns: generation, width, height, board


    """
    with open(file_path) as read:
        generation = read.readline()
        width, height = read.readline().split()
        board = read.read().splitlines()
    generation = int(generation)
    width = int(width)
    height = int(height)

    return generation, width, height, board


def board_validation(width: int, height: int, board: List[str]) -> bool:
    # check len(board) == height
    if len(board) != height:
        logger.debug('Bad height')
        return False
    for line in board:
        # check len(line) == width and all symbol in whitelist
        if len(line) != width:
            logger.debug('Bad width')
            return False
        for symbol in line:
            if symbol not in GAME_SYMBOL:
                logger.debug('Bad symbols')
                return False
    return True


def get_neighborhood_coord(row: int, col: int, width: int, height: int) -> Tuple[Tuple[int, int]]:

    cols = (col - 1) % width, col, (col + 1) % width
    rows = (row - 1) % height, row, (row + 1) % height
    pairs = tuple((i, j) for i in rows for j in cols if (i != row or j != col))

    return pairs


def is_alive(old_board: List[str], row: int, col: int, old_symbol):
    height = len(old_board)
    width = len(old_board[0])
    live = True
    pairs = get_neighborhood_coord(row, col, width, height)
    neighbors = map(lambda coord: old_board[coord[0]][coord[1]], pairs)
    alives = tuple(filter(lambda x: x == LIVE, neighbors))

    if old_symbol == DEAD:
        if len(alives) == 3:
            return LIVE
        return DEAD
    if len(alives) in (2, 3):
        return LIVE
    return DEAD


def clock(board: List[str]) -> List[str]:
    new_board = [""] * len(board)
    for row, line in enumerate(board):
        for col, symbol in enumerate(line):
            new_board[row] += is_alive(board, row, col, symbol)
    for line in new_board:
        print(line)
    print('')
    return new_board
