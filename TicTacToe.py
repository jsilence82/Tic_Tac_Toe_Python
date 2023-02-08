from Board import Board
from SelectionScreen import SelectionScreen
from players import Factory


class TicTacToe:

    def __init__(self):
        self.game_loop()
        self.player1 = None
        self.player2 = None

    def player_create(self, board):
        select = SelectionScreen()
        player = select.select_player(1)
        opponent = select.select_player(2)
        self.player1 = Factory.player_factory(player, "X", board)
        self.player2 = Factory.player_factory(opponent, "O", board)

    def game_loop(self):
        board = Board()
        self.player_create(board)

        players = [self.player1, self.player2]
        turn = 0
        board.print_board()
        while True:
            if board.board_is_full():
                print("\nIt's a draw!")
                break
            else:
                players_pick = board.space_to_board_coordinates(players[turn].pick_a_space())
                if board.space_occupied(players_pick):
                    print("\nOops. That spot is taken. Try again.")
                    board.print_board()
                else:
                    board.place_players_mark(players_pick, players[turn].get_players_mark())
                    board.print_board()
                    if board.check_winner(players[turn].get_players_mark()):
                        print("\n" + players[turn].get_player_name() + " Wins!")
                        break
                    else:
                        turn = (turn + 1) % 2
        self.player1.dispose()
        self.player2.dispose()
