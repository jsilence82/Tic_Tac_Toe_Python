from players.Player import Player


class AI(Player):
    def __init__(self, board, players_mark):
        super().__init__("AI Computer", players_mark)
        self.board = board
        self.computer = players_mark
        self.opponent = "O" if players_mark == "X" else "X"
        self.mapped = {i: str(i) for i in range(1, 10)}
        print(f"{self.get_player_name()} will play as {self.get_players_mark()}")

    def pick_a_space(self):
        print("The AI evaluates and is picking...")
        update_map = self.update_mapped()
        return self.findBestMove(update_map)

    def update_mapped(self):
        count = 1
        for i in range(3):
            for j in range(3):
                self.mapped[count] = self.board.get_board()[i][j]
                count += 1
        return self.mapped

    def evaluate(self, mapped):
        winning_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for numbers in winning_conditions:
            if mapped[numbers[0]] == mapped[numbers[1]] == mapped[numbers[2]]:
                if mapped[numbers[0]] == self.computer:
                    return 10
                elif mapped[numbers[0]] == self.opponent:
                    return -10
        return 0

    @staticmethod
    def map_is_full(mapped):
        for value in mapped.values():
            if value in [str(i) for i in range(1, 10)]:
                return False
        return True

    def findBestMove(self, mapped):
        best_value = -1000
        best_move = -1

        for move, space in mapped.items():
            if space not in [self.computer, self.opponent]:
                temp = space
                mapped[move] = self.computer
                move_value = self.minMax(mapped, 0, False)
                mapped[move] = temp

                if move_value > best_value:
                    best_move = move
                    best_value = move_value
        return best_move

    def minMax(self, mapped, depth, is_max):
        score = self.evaluate(mapped)
        if score == 10:
            return score
        if score == -10:
            return score
        if self.map_is_full(mapped):
            return 0
        if is_max:
            best = -1000
            for move, space in mapped.items():
                if space not in [self.computer, self.opponent]:
                    temp = space
                    mapped[move] = self.computer
                    best = max(best, self.minMax(mapped, depth + 1, False))
                    mapped[move] = temp
            return best
        else:
            best = 1000
            for move, space in mapped.items():
                if space not in [self.computer, self.opponent]:
                    temp = space
                    mapped[move] = self.opponent
                    best = min(best, self.minMax(mapped, depth + 1, True))
                    mapped[move] = temp
            return best
