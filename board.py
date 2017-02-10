import globvars as g


class Board:
    def __init__(self):
        self.board = [{'fill': 'O', 'ship': None} for _ in range(100)]

    # Place the ship in board and also to the player's fleet list
    # for tracking the ship name
    # Validates the ship placement and returns the coordinates
    def place_ship(self, start, step, size, name):
        coordinates = []
        new_fill = g.HORIZONTAL_SHIP

        if step == 10:
            new_fill = g.VERTICAL_SHIP
            if start + step * size < 100:
                coordinates = [i*step+start for i in range(size)]
            else:
                return(
                    0,
                    ", your {} needs at least {} spaces to fit!\n"
                    "Choose another location."
                    )

        elif (10 - (start % 10)) >= size:
            coordinates = [i*(step)+start for i in range(size)]
        else:
            return(
                0,
                ", your {} needs at least {} spaces to fit!\n"
                "Choose another location."
                )

        for c in coordinates:
            if self.board[c]['fill'] != g.EMPTY:
                return(
                    0,
                    ", your {} is in the way!".format(self.board[c]['ship'])
                    )

        for c in coordinates:
            self.board[c]['fill'] = new_fill
            self.board[c]['ship'] = name
        self.print_board()

        return(
            coordinates,
            ", your {} has been deployed!"
            )

    def print_board_heading(self):
        print("\n"+"_" * 40+"\n")
        columns = [chr(c) for c in range(ord('A'), ord('A') + g.BOARD_SIZE)]
        print(" "*11 + " ".join(columns))

    def print_board(self):
        self.print_board_heading()

        row_num = 0
        while row_num <= 90:
            print(
                " "*8 +
                str(int(row_num/10) + 1).rjust(2) + " " + (" ".join([
                    self.board[i]['fill'] for i in range(row_num, row_num+10)
                            ]
                        )
                    )
                )
            row_num += 10
        print("_" * 40)
