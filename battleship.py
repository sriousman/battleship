from playerclass import Player
import globvars as g
from sys import exit
import pdb


class Game:
    def __init__(self):
        self.welcome()
        self.p = [Player(), Player()]
        print("Let the battle commence!")
        self.run()

    def welcome(self):
        g.clear_screen()
        print("\n"+"_" * 40+"\n")
        print("        Welcome to BATTLESHIP!!")
        print("_" * 40+"\n")

    def run(self):
        turn = 1
        while True:
            g.clear_screen()
            # Set Attacker and Defender
            defender = self.p[turn % 2]
            attacker = self.p[(turn+1) % 2]

            attacker.command_center()
            # pdb.set_trace()
            attacker.attack(defender)

            if self.game_over():
                print("Game is over!")
                exit(0)
            turn += 1
            input(
                "{}, please give the console to the other player.\n\n"
                "Hit Enter when you are ready {}.".format(
                                                        attacker.name,
                                                        defender.name)
                )

    def game_over(self):
        if self.p[0].ship_count > 0 and self.p[1].ship_count > 0:
            return False
        return True

        # exit
Game()
