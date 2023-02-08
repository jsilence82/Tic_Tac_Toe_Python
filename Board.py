
class Board:
    def __init__(self):
        self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    def get_board(self):
        return self.board

    def place_players_mark(self, players_pick, player_mark):
        self.board[players_pick[0]][players_pick[1]] = player_mark

    def board_coordinates_to_space(self, row, col):
        return int(self.board[row][col])

    def print_board(self):
        print()
        for i in range(3):
            print(" | ".join(self.board[i]))
            if i < 2:
                print("- + - + -")
        print()

    @staticmethod
    def space_to_board_coordinates(space):
        if space == 1:
            return [0, 0]
        elif space == 2:
            return [0, 1]
        elif space == 3:
            return [0, 2]
        elif space == 4:
            return [1, 0]
        elif space == 5:
            return [1, 1]
        elif space == 6:
            return [1, 2]
        elif space == 7:
            return [2, 0]
        elif space == 8:
            return [2, 1]
        elif space == 9:
            return [2, 2]

    def space_occupied(self, space):
        return self.board[space[0]][space[1]] == "X" or self.board[space[0]][space[1]] == "O"

    def board_is_full(self):
        for row in self.board:
            for s in row:
                if s in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    return False
        return True

    def check_winner(self, player_mark):
        rows = [all(cell == player_mark for cell in row) for row in self.board]
        cols = [all(self.board[i][j] == player_mark for i in range(3)) for j in range(3)]
        diagonal1 = all(self.board[i][i] == player_mark for i in range(3))
        diagonal2 = all(self.board[i][ 2 -i] == player_mark for i in range(3))
        return any(rows + cols + [diagonal1, diagonal2])
