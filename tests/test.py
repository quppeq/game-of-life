import pytest
from app.utils import board_validation, read_file, get_neighborhood_coord


@pytest.fixture(scope='function')
def setup_test_file():
    with open('test', 'w') as write:
        write.write(
            "3\n"
            "8 5\n"
            "........\n"
            "..x.....\n"
            "..x.....\n"
            "..x.....\n"
            "........"
        )


def test_one_equal_one():
    assert 1 == 1


def test_false_board_validation():
    # setup
    width = 3
    height = 3
    board = [
        "",
        "",
    ]
    assert board_validation(width, height, board) is False


def test_true_board_validation():
    # setup
    width = 2
    height = 2
    board = [
        ".x",
        "..",
    ]
    assert board_validation(width, height, board) is True


def test_read_file(setup_test_file):
    generation, width, height, board = read_file('test')
    val = board_validation(width, height, board)
    assert generation == 3
    assert val is True


def test_get_neighbor_cord():
    coord = get_neighborhood_coord(5, 5, 8, 8)
    pairs = (
        (4, 4), (4, 5), (4, 6),
        (5, 4), (5, 6),
        (6, 4), (6, 5), (6, 6),
    )
    assert set(coord) == set(pairs)


def test_get_neighbor_cord_on_edge():
    coord = get_neighborhood_coord(5, 0, 8, 8)
    pairs = (
        (4, 7), (5, 7), (6, 7),
        (4, 0), (6, 0),
        (4, 1), (5, 1), (6, 1),
    )
    assert set(coord) == set(pairs)
