"""
Coloring problem:
- NP-complete problem ~ exponential running time
- Vertex coloring: coloring the vertices of a graph such that no two adjacent
  vertices share the same color
- Reach popularity with general public in the form of the popular number of
  puzzle Sudoku.
- The smallest number of colors needed to color the graph G is called its
  chromatic number.
- There may be more that on solution: for example we can color a graph
  with 4 vertices in 12 ways with 3 colors.

Solution:
- We assign colors one by one to different vertices starting from the first
  vertex(optional)
- Before assign a color -> we check for safety by considering already
assigned colors to the adjacent vertices.
- If we find a color assignment which is feasible -> we mark the color
assignment as part of solution.
- If we do not find a color due to clashes -> we backtrack!!!
"""

class ColoringProblem(object):

    def __init__(self, num_of_vertices, num_of_colors, adjacent_matrix):
        self.num_of_vertices = num_of_vertices
        self.num_of_colors = num_of_colors
        self.adjacent_matrix = adjacent_matrix
        self.colors = [0] * num_of_vertices

    def solve_coloring(self):

        if self.solve(0):
            self.show_coloring()
        else:
            print("No feasible solution with the given parameters...")

    def solve(self, node_index):

        if node_index == self.num_of_vertices:
            return True

        # retry rest of colors
        for color_index in range(1, self.num_of_colors + 1):

            if self.valid_color(node_index, color_index):

                # assign and proceed next vertex
                self.colors[node_index] = color_index

                if self.solve(node_index + 1):
                    return True

                # backtracking
                # do nothing
        return False

    def valid_color(self, node_index, color_index):

        for i in range(self.num_of_vertices):
            if self.adjacent_matrix[node_index][i] == 1 and color_index == \
                    self.colors[i]:
                return False
        return True

    def show_coloring(self):

        for i in range(self.num_of_vertices):
            print("Node {} has color index :{}".format(i, self.colors[i]))


if __name__ == "__main__":
    """
        A ------- B
        | \     / | \ 
        |  \   /  |  \
        |   \ /   |   \
        |    C    |    E  
        |   / \   |   /
        |  /   \  |  /
        | /     \ | /
        D ------- F 
    """
                  # A, B, C, D, E, F
    graphMatrix = [[0, 1, 1, 1, 0, 0], # A
                   [1, 0, 1, 0, 1, 1], # B
                   [1, 1, 0, 1, 0, 1], # C
                   [1, 0, 1, 0, 0, 1], # D
                   [0, 1, 0, 0, 0, 1], # E
                   [0, 1, 1, 1, 1, 0]  # F
                   ]

    numOfColors = 3
    numOfVertices = 6

    coloringProblem = ColoringProblem(numOfVertices, numOfColors, graphMatrix)
    coloringProblem.solve_coloring()




