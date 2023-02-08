class SelectionScreen:
    def __init__(self):
        self.input = input

    def select_player(self, player_number):
        print(f"\nSelect from the following for Player {player_number}...")
        print(f"{' ' * 6}1: Human player.")
        print(f"{' ' * 6}2: Computer picking randomly (Easy).")
        print(f"{' ' * 6}3: Computer AI (Hard).")
        player_type = self._validate_input(f"\nPlayer {player_number}: ")
        return player_type

    def _validate_input(self, prompt):
        player_type = int(input(prompt))
        if player_type in [1, 2, 3]:
            return player_type
        else:
            return self._validate_input("Select 1, 2, or 3: ")
