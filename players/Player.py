
class Player:
    playerNumber = 0

    def __init__(self, player_name, players_mark):
        self.playersMark = players_mark
        self.playerName = player_name
        Player.playerNumber += 1

    def get_player_name(self):
        return self.playerName

    def set_player_name(self, player_name):
        self.playerName = player_name

    def get_players_mark(self):
        return self.playersMark

    @staticmethod
    def dispose():
        Player.playerNumber -= 1

    def pick_a_space(self):
        pass
