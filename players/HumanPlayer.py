from players.Player import Player


class HumanPlayer(Player):

    def init(self, playersMark):
        super().init("name", playersMark)
        playersName = input("Give player " + str(Player.playerNumber) + " a name: ")
        self.setPlayerName(playersName)
        print(self.getPlayerName() + " will play as " + self.getPlayersMark())

    def getPlayerName(self):
        return super().getPlayerName()

    def getPlayersMark(self):
        return super().getPlayersMark()

    def pickASpace(self):
        pick = int(input("It is " + self.getPlayerName() + "'s turn: "))
        if pick <= 9 and pick > 0:
            return pick
        print("Not a valid space. Try again.")
        return self.pickASpace()
