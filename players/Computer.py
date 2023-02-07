import random

from players.Player import Player


class Computer(Player):

    def init(self, board, playersMark):
        super().init("Random", playersMark)
        self.board = board
        print(self.get_player_name() + " will play as " + self.get_players_mark())

    def pick_a_space(self):
        pick = random.randint(1, 9)
        if self.board.spaceOccupied(self.board.spaceToBoardCoordinates(pick)):
            return self.pick_a_space()
        print("The computer is randomly picking...")
        return pick
