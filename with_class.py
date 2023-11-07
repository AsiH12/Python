import json

class TicTacToe:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.current_player = "X"
        self.winner = None

    def display_board(self):
        board_format = """
        A | B | C
        -----------
          |   |
     1| {} | {} | {}
          |   |
        -----------
          |   |
     2| {} | {} | {}
          |   |
        -----------
          |   |
     3| {} | {} | {}"""
        print(
            board_format.format(
                self.board[0][0],
                self.board[0][1],
                self.board[0][2],
                self.board[1][0],
                self.board[1][1],
                self.board[1][2],
                self.board[2][0],
                self.board[2][1],
                self.board[2][2],
            )
        )

    def check_win(self):
        x_wins = ["X", "X", "X"]
        o_wins = ["O", "O", "O"]

        for i in range(3):
            column = [self.board[0][i], self.board[1][i], self.board[2][i]]
            row = [self.board[i][0], self.board[i][1], self.board[i][2]]
            if column in [x_wins, o_wins] or row in [x_wins, o_wins]:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

    def check_tie(self):
        if not self.check_win() and " " not in self.board:
            return True
        else:
            return False

    def save_results(self):
        try:
            results_file = open("results.json", "r+")
        except FileNotFoundError:
            results_file = open("results.json", "w")
            if self.winner == "Tie":
                results = {"X": 0, "O": 0, "Tie": 1}
            elif self.winner == "X":
                results = {"X": 1, "O": 0, "Tie": 0}
            elif self.winner == "O":
                results = {"X": 0, "O": 1, "Tie": 0}
            json.dump(results, results_file)
            results_file.close()
        else:
            results = json.load(results_file)
            if self.winner == "Tie":
                results["Tie"] = results["Tie"] + 1
            elif self.winner == "X":
                results["X"] = results["X"] + 1
            elif self.winner == "O":
                results["O"] = results["O"] + 1
            results_file.seek(0)
            json.dump(results, results_file)
            results_file.close()
        print(
            "The current results are: X: {}, O: {}, Tie: {}".format(
                results["X"], results["O"], results["Tie"]
            )
        )

    def play(self):
        while not self.winner:
            self.display_board()
            print("It is {}'s turn.".format(self.current_player))
            move = input("Where would you like to move? ")
            move = move.lower()
            if move in ["exit", "quit", "q", "x"]:
                print("Stopping game... Goodbye!")
                exit()

            columns = {"a": 0, "b": 1, "c": 2}
            rows = {"1": 0, "2": 1, "3": 2}

            column, row = None, None
            for letter in move:
                if letter in columns.keys():
                    column = columns[letter]
                if letter in rows.keys():
                    row = rows[letter]

            try:
                if self.board[row][column] != " ":
                    print("That is not a valid move.")
                    continue
                self.board[row][column] = self.current_player
            except (TypeError, IndexError):
                print("That is not a valid move.")
                continue

            if self.check_win():
                self.winner = self.current_player

            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"

        self.display_board()
        if self.winner == "Tie":
            print("It's a tie!")
        else:
            print("Congratulations, {} wins!".format(self.winner))
        self.save_results()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
