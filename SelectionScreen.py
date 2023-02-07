import sys
import random

class SelectionScreen:
    def __init__(self):
        self.input = input

    def ascii_art(self):
        image = [[" " for x in range(144)] for y in range(32)]
        for i, row in enumerate(image):
            for j, char in enumerate(row):
                if i == 24 and 6 <= j < 6 + len("TicTacToe"):
                    image[i][j] = "TicTacToe"[j-6]
                else:
                    image[i][j] = "#" if char == " " else "*"

        for row in image:
            print("".join(row))

    def select_player(self, player_number):
        print(f"\nSelect from the following for Player {player_number}...")
        print(f"{' '*6}1: Human player.")
        print(f"{' '*6}2: Computer picking randomly (Easy).")
        print(f"{' '*6}3: Computer AI (Hard).")
        player_type = self._validate_input(f"\nPlayer {player_number}: ")
        return player_type

    def _validate_input(self, prompt):
        player_type = int(input(prompt))
        if player_type in [1, 2, 3]:
            return player_type
        else:
            return self._validate_input("Select 1, 2, or 3: ")
