from SelectionScreen import SelectionScreen
from TicTacToe import TicTacToe

if __name__ == "__main__":
    # SelectionScreen().ascii_art()
    TicTacToe()
    input_str = input("Another game? ")
    while input_str.lower() != "n":
        input_str = input("Another game? ")
        if input_str.lower() not in ["y", "n"]:
            input_str = input("Y or N? ")