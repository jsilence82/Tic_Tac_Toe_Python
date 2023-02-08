import random

from players.Player import Player


class Computer(Player):

    def __init__(self, board, players_mark):
        super().__init__("Random", players_mark)
        self.board = board
        print(self.get_player_name() + " will play as " + self.get_players_mark())

    def pick_a_space(self):
        pick = random.randint(1, 9)
        if self.board.space_occupied(self.board.space_to_board_coordinates(pick)):
            return self.pick_a_space()
        print("The computer is randomly picking...")
        return pick
