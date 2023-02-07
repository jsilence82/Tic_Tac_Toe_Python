

class Player:
    playerNumber = 0

    def __init__(self, playerName, playersMark):
        self.playersMark = playersMark
        self.playerName = playerName
        Player.playerNumber += 1


    def getPlayerName(self):
        return self.playerName


    def setPlayerName(self, playerName):
        self.playerName = playerName


    def dispose(self):
        Player.playerNumber -= 1


    def getPlayersMark(self):
        return self.playersMark


    def pickASpace(self):
        pass
