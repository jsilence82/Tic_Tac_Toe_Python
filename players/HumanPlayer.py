from players.Player import Player


class HumanPlayer(Player):

    def __init__(self, playersMark):
        super().__init__("name", playersMark)
        playersName = input("Give player " + str(Player.playerNumber) + " a name: ")
        self.set_player_name(playersName)
        print(self.get_player_name() + " will play as " + self.get_players_mark())

    def get_player_name(self):
        return super().get_player_name()

    def get_players_mark(self):
        return super().get_players_mark()

    def pick_a_space(self):
        pick = int(input("It is " + self.get_player_name() + "'s turn: "))
        if pick <= 9 and pick > 0:
            return pick
        print("Not a valid space. Try again.")
        return self.pick_a_space()
