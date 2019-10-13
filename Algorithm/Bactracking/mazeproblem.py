"""
Maze problem:

"""
import time
class MazeProblem(object):

    def __init__(self, maze_table):
        self.maze_table = maze_table
        self.maze_size = len(maze_table)
        self.solution_table = [[0] * self.maze_size for _ in range(self.maze_size)]

    def solve_maze(self):

        if self.solve(0, 0):
            self.show_result()
        else:
            print("No feasible solution found...")

    def solve(self, x, y):

        if self.is_finished(x, y):
            return True

        if self.valid_move(x, y):

            self.solution_table[x][y] = 1

            # move forward next col
            if self.solve(x + 1, y):
                return True

            # move forward next row
            if self.solve(x, y + 1):
                return True

            # backtrack
            self.solution_table[x][y] = 0

        return False

    def is_finished(self, x, y):
        if x == self.maze_size - 1 and y == self.maze_size - 1:
            self.solution_table[x][y] = 1
            return True

        return False

    def valid_move(self, x, y):

        if x < 0 or x >= self.maze_size:
            return False

        if y < 0 or y >= self.maze_size:
            return False

        if self.maze_table[x][y] == 0:
            return False

        return True

    def show_result(self):
        for i in range(self.maze_size):
            for j in range(self.maze_size):
                if self.solution_table[i][j] == 1:
                    print(' S ', end="")
                else:
                    print(' - ', end="")
            print('\n')

if __name__ == "__main__":

    maze_table = [[1, 1, 1, 1, 1],
                  [1, 0, 0, 1, 0],
                  [0, 0, 0, 1, 0],
                  [1, 1, 1, 1, 1],
                  [1, 1, 1, 0, 1]]


    start = time.time()

    maze_problem = MazeProblem(maze_table)
    maze_problem.solve_maze()

    end = time.time()
    print("execute time :{}".format(end - start))

    maze_table = [[1, 1, 1, 1, 1],
                  [1, 0, 0, 1, 0],
                  [1, 1, 1, 1, 0],
                  [0, 1, 1, 0, 0],
                  [1, 1, 1, 1, 1]]


    start = time.time()

    maze_problem = MazeProblem(maze_table)
    maze_problem.solve_maze()

    end = time.time()
    print("execute time :{}".format(end - start))