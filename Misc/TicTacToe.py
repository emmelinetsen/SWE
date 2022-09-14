# tic tac toe
# implement board in memory
# have 1 player play . place x or o
# win detection - print statement when player has won
# support n x n board


# implement 2 bots

# _ _ x
# o X _
# x _ o
# create a board object that takes in 1 parameter -> size of the board
# create a method that takes in 2 parameters -> player # , location/coordinates
## assume -> player 1 == x, player 2 == o

# after every turn, want to check whether there is a win
# win -> every position either horizontally, veritically, or diag after adding the new X/O

print("hello")
class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.board = [ ["-"]*size for i in range(size)]


    # input -> player (player1, player2)
    # coorinate -> an array containing the row/col for the postion to move ([row, col])
    # output -> nothing. will update the board
    def move(self, player, coordinates):

        row = int(coordinates[0])
        col = int(coordinates[1])
        print("row: ", row, "col: ", col)
        player_mark = "X" if player == "player1" else "O"

        self.board[row][col] = player_mark
        print(self.board)

    # input - coordinates to start the check from
    # input - player_mark ("X", "O")
    # checks whether or not there's a win on theboard
    # output - T/F

    # _ _ x
    # o X _
    # x _ o

    # _ _ _ _
    # _ _ _ _
    # _ _ _ _
    # _ _ _ _
    def win(self, player_mark, coordinates):
        # print(player_mark, coordinates)
        row = int(coordinates[0])
        col = int(coordinates[1])
        count = 0
        # check if all horizontal from [row][0:board_size]
        for i in range(self.size):
            count +=1
            if self.board[row][i] != player_mark:
                return False

        if count == self.size:
            return True

        print("vert win method")
        if self.vertical_win():
            return True
        if self.diag_win():
            return True


    def vertical_win(self, player_mark, coordinates):
        row = int(coordinates[0])
        col = int(coordinates[1])
        # check if win from all vertical from [0:board_size][col]

        for i in range(self.size):
            print("i: ", i, "col: ", col)
            if self.board[i][col] != player_mark:
                return False

        return True

    def diag_win(self, player_mark, coordinates):
        row = int(coordinates[0])
        col = int(coordinates[1])
        count = 0
        # diagonal -> [row-1][col-1] all the way to [0][0], [row+1][col+1] --> [size-1][size-1]
        for r in range(self.size):
            for c in range(self.size):
                count += 1
                if self.board[r][c] != player_mark:
                    return False

        if count == self.size:
            return True

        count = 0
        # diagonal -> [row-1][col-1] all the way to [0][0], [row+1][col+1] --> [size-1][size-1]
        # [0][len-1] ... [len-1][0]
        for r in range(self.size):
            for c in range(self.size-1, 0, -1):
                count += 1
                if self.board[r][c] != player_mark:
                    return False

        return True

    def play_game(self):
        player_mark = ""
        coord = [0, 0]
        while not self.win(player_mark, coord):
            # TODO - take input from move and call move function
            player = input("Input player: ")
            row = input("row: ")
            col = input("col: ")
            coord = [int(row), int(col)]
            # coordinates =  input("Input coordinates: ")
            self.move(player, coord)
            player_mark = "X" if player == "player1" else "O"
            # self.win(player_mark, coordinates)

if __name__ == "__main__":
    t = TicTacToe(3)
    t.play_game()