from players.AI import AI
from players.Computer import Computer
from players.HumanPlayer import HumanPlayer


def player_factory(entry, players_mark, board):
    if entry == 1:
        return HumanPlayer(players_mark)
    elif entry == 2:
        return Computer(board, players_mark)
    elif entry == 3:
        return AI(board, players_mark)
    else:
        return None
