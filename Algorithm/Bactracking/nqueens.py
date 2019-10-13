"""
N-queens problem:
- The problem of placing N chess queens on an NxN chessboard so that no two
  queens threaten each other (they are not be able to attack each other)
- We have to consider: queens can move diagonal directions too.
- The original problem was designed for 8 queens...
  the general form is about N queens.
- Guess worked on this problem
- Dijkstra used this problem to illustrate the power of call structured
  programming.
"""

class QueensProblem(object):

    def __init__(self, num_of_queens):
        self.num_of_queen = num_of_queens
        self.chessboard = [[None for i in range(num_of_queens)] for j in
                           range(num_of_queens)]

    def solve_queens_problen(self):
        if self.solve(0):
            self.print_queen()
        else:
            print("There is no solution...")

    def solve(self, col_index):
        if col_index == self.num_of_queen:
            return True

        for row_index in range(self.num_of_queen):

            if self.valid_place(row_index, col_index):
                self.chessboard[row_index][col_index] = 1

                if self.solve(col_index + 1):
                    return True

                # backtracking
                self.chessboard[row_index][col_index] = None
        return False

    def valid_place(self, row_index, col_index):

        # same row
        for i in range(col_index):
            if self.chessboard[row_index][i] == 1:
                return False

        # top left to bottom right
        j = col_index
        for i in range(row_index, -1, -1):
            if j < 0:
                break

            if self.chessboard[i][j] == 1:
                return False

            j -= 1

        # bottom left to top right
        j = col_index
        for i in range(row_index, len(self.chessboard)):
            if j < 0:
                break

            if self.chessboard[i][i] == 1:
                return False

            j -= 1

        return True

    def print_queen(self):

        for i in range(self.num_of_queen):
            for j in range(self.num_of_queen):
                if self.chessboard[i][j] == 1:
                    print(" * ", end="")
                else:
                    print(" - ", end="")
            print("\n")

if __name__ == "__main__":
    nqueens_problem = QueensProblem(20)
    nqueens_problem.solve_queens_problen()
