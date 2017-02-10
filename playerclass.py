from board import Board
import globvars as g
import pdb
# The Playerclass is designed to handle all the communication between players
# including attacking and reporting hits.
# Playerclass handles printing and management of board


class Player:
    def __init__(self):
        # list for keeping track of attacks, hit or miss
        self.guesses = list()
        self.defense_board = Board()
        self.attack_board = Board()
        self.fleet = []
        self.ship_count = 0
        # Get the player's name
        self.name = 'Commander ' + input(
                "Welcome to Battleship! What is your name: ").strip()
        print(
            "\nWelcome {}, we have new intel that a hostile force "
            "is advancing on our position!\n\n"
            "Our fate is in your hands!".format(self.name)
            )
        input(
            "\nPrepare to deploy the fleet!"
            " Press any key to open command center..."
            )
        g.clear_screen()

        # Deploy player fleet to the board
        self.deploy_fleet()

    def get_index(self):
        row = self.get_row()
        column = self.get_column()
        return row + (column - 65)

    def get_row(self):
        try:
            row = int(input("Row Number: "))
            if row in range(1, 11):
                return (row - 1)*10
            else:
                print(
                    "Invalid Row Number."
                    " Enter a number between 1 and 10"
                    )
                return self.get_row()
        except ValueError:
            g.clear_screen()
            self.defense_board.print_board()
            print("Opps... not a number. Enter a number from 1 to 10.")
            return self.get_row()

    def get_column(self):
        # pdb.set_trace()
        try:
            column = ord(input("Column Letter: ").upper())
            if column >= 65 and column <= 74:
                return column
            else:
                print("Invalid Column. Try again.")
                return self.get_column()
        except:
            print(
                "Invalid Column. Please enter a "
                "letter between A and J.")
            return self.get_column()

    # Prompt Player for the vert or horiz ship orientation
    # Returns the step for determining the ship coordinates
    def get_orientation(self):
        response = input(
                        "(H)orizontal or (V)ertical: ").lower()
        if response == "v":
            return g.BOARD_SIZE
        elif response == "h":
            return 1
        else:
            g.clear_screen()
            print("Invalid Response, you must enter 'h' or 'v'.")
            return self.get_orientation()

    def deploy_fleet(self):
        for ship in g.SHIP_INFO:
            ship_name = ship[0]
            ship_size = ship[1]

            while True:
                self.defense_board.print_board()
                print(
                    "\n{}, please choose a location".format(self.name) +
                    " for your {} (size = {}).\n".format(
                                                    ship_name.upper(),
                                                    ship_size)
                    )

                # Try to place
                # pdb.set_trace()
                placement = self.defense_board.place_ship(
                                                        self.get_index(),
                                                        self.get_orientation(),
                                                        ship_size,
                                                        ship_name
                                                        )
                # if not valid placement print out error message
                if not placement[0]:
                    g.clear_screen()
                    print(
                        self.name + ' ' +
                        placement[1].format(ship_name, ship_size)
                        )
                else:
                    g.clear_screen()
                    self.fleet.append([ship_name, placement[0], ship_size])
                    self.ship_count += 1
                    print(self.name + placement[1].format(ship_name))
                    break
        input(
            "Your fleet has been successfully deployed!"
            "It is now time for your opponent's turn."
            "\nPress Enter to clear the screen "
            "then give control to the other player"
            )
        g.clear_screen()

    def attack(self, enemy):
        print("Attack!")
        attack = self.get_index()
        if attack in self.guesses:
            g.clear_screen()
            print("{}, you have already attacked there.".format(self.name))
            self.command_center()
            return self.attack(enemy)
        else:
            report = enemy.take_fire(attack)
            self.guesses.append(attack)
            self.attack_board.board[attack]['fill'] = report[0]
            g.clear_screen()
            self.command_center()
            print(report[1])

    def take_fire(self, attack):
        for ship in self.fleet:
            if attack in ship[1]:
                ship[2] -= 1
                if ship[2] > 0:
                    self.defense_board.board[attack]['fill'] = g.HIT
                    return g.HIT, "You have hit the {}!".format(ship[0])
                else:
                    for i in ship[1]:
                        self.defense_board.board[i]['fill'] = g.SUNK
                    self.ship_count -= 1
                    return g.HIT, "You have sunk the {}".format(ship[0])
        return g.MISS, "You have missed!"

    def command_center(self):
        print("\n"+"_" * 40 + "\n")
        print(":: {}'s Fleet Positions".format(self.name), end='')
        self.defense_board.print_board()
        print("\n"+"*"*12 + " Enemy Positions " + "*"*12, end='')
        self.attack_board.print_board()
        print()
