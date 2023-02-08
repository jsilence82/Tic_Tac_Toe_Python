from TicTacToe import TicTacToe

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    print()
    while True:
        TicTacToe()
        input_str = input("Another game? ")
        replay_flag = True
        while True:
            if input_str.lower() not in ["y", "n"]:
                input_str = input("Y or N? ")
            if input_str.lower() == "y":
                break
            if input_str.lower() == "n":
                replay_flag = False
                break
        if replay_flag is False:
            break
