from players.Player import Player


class HumanPlayer(Player):

    def __init__(self, players_mark):
        super().__init__("name", players_mark)
        players_name = input("Give player " + str(Player.playerNumber) + " a name: ")
        self.set_player_name(players_name)
        print(self.get_player_name() + " will play as " + self.get_players_mark())

    def get_player_name(self):
        return super().get_player_name()

    def get_players_mark(self):
        return super().get_players_mark()

    def pick_a_space(self):
        pick = int(input("It is " + self.get_player_name() + "'s turn: "))
        if 9 >= pick > 0:
            return pick
        print("Not a valid space. Try again.")
        return self.pick_a_space()
