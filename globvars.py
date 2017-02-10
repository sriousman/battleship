SHIP_INFO = [
    # ("Aircraft Carrier", 5)
    # ("Battleship", 4),
    # ("Submarine", 3),
    # ("Cruiser", 3),
    ("Patrol Boat", 2)
]

BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'


def clear_screen():
    print("\033c", end="")
