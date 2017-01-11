SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'

class BattleShip:

    def clear_screen():
        print("\033c", end="")


    def print_board_heading():
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))


    def print_board(board):
        print_board_heading()

        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def get_user_names(self):
        pass

    # prompt users to place ship
    # validate user input


    def update_board(self):
        pass

    def turn(self):
        pass

    # clear screen after each turn
    # Prompt new player (by name) to start turn and then print the board
    # Prompt player for guess
    # validate guess
    # Display results



    ## EXTRA CREDIT *******
    #  Clear screen after invalid entry
    #  Error messages are detailed and explicit.  Include the invalid guess information
    #  Display both the player's boards on the screen showing the ship positions
    if __name__ == "__main__":
