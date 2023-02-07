import random

from players.Player import Player


class Computer(Player):

    def init(self, board, playersMark):
        super().init("Random", playersMark)
        self.board = board
        print(self.getPlayerName() + " will play as " + self.getPlayersMark())

    def pickASpace(self):
        pick = random.randint(1, 9)
        if self.board.spaceOccupied(self.board.spaceToBoardCoordinates(pick)):
            return self.pickASpace()
        print("The computer is randomly picking...")
        return pick
