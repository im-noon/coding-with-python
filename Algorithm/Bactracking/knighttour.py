"""
Knight's tour problem:
- A sequence of moves of a knight on a chessboard such that knight visited
every square exactly once.
- Closed tour: when the knight end point is the same as the staring point.
- The knight's tour problem is an instance of the more general hamiltonian-path
problem.
- Close knight's tour ~hamiltonian-cycle problem.

Schwenk theorem:
        - For and m x n chessboard, the closed knight tour problem is always
        feasible unless:
            > m and n are both odds
            > m = 1, 2, or 4
            > m = 3 and n = 4, 6, 8
Solution:
- Start with an empty solution matrix or 2D array
- When adding a new item, we check whether adding the current item violates
the problem constraint or not
    > Yes, backtrack
    > NO, we add the item into the solution set and go to the next item
- If we have considered all the items we are ready.
"""

import time
class KnightTour2(object):

    def __init__(self, board_size):
        self.board_size = board_size
        self.x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
        self.solution_matrix = [[-1 for x in range(board_size)] for x in
                               range(board_size)]

    def solve_knight_tour_problem(self):

        self.solution_matrix[0][0] = 0

        if self.solve(1, 0, 0):
            self.show_knight_tour()
        else:
            print("No feasible solution found...")

    def solve(self, step_count, x, y):

        if step_count == (self.board_size * self.board_size):
            return True

        for i in range(8):

            next_x = x + self.x_moves[i]
            next_y = y + self.y_moves[i]

            if self.validate_move(next_x, next_y):
                self.solution_matrix[next_x][next_y] = step_count

                if self.solve(step_count + 1, next_x, next_y):
                    return True

                # backtrack
                self.solution_matrix[next_x][next_y] = -1

        return False

    def validate_move(self, x, y):
        if x < 0 or x >= self.board_size:
            return False

        if y < 0 or y >= self.board_size:
            return False

        # if visited it self
        if self.solution_matrix[x][y] > -1:
            return False

        return True


    def show_knight_tour(self):

        for i in range(self.board_size):
            for j in range(self.board_size):
                print(self.solution_matrix[i][j], end=" "),
            print("\n")

if __name__ == "__main__":
    start = time.time()

    knightTour2 = KnightTour2(8)
    knightTour2.solve_knight_tour_problem()

    end = time.time()
    print(end - start)