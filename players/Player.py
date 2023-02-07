

class Player:
    playerNumber = 0

    def __init__(self, playerName, playersMark):
        self.playersMark = playersMark
        self.playerName = playerName
        Player.playerNumber += 1


    def get_player_name(self):
        return self.playerName


    def set_player_name(self, playerName):
        self.playerName = playerName


    def dispose(self):
        Player.playerNumber -= 1


    def get_players_mark(self):
        return self.playersMark


    def pick_a_space(self):
        pass
