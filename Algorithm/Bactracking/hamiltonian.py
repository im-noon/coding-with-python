"""
With graph
    G(V,E):
        V: vertices in the graph
        E: edges in the graph
        adjacent ,matrix
Hamiltonian path: is a path in undirected graph that visit every node
exactly one.

Hamiltonian cycle: is the first node and the last node of the path are the
vertexes; starting point = ending point.

Hamiltonian problem:
- determining whether such paths and cycles exist in graphs is the
  Hamiltonian path problem.
- This is an np-complete complete problem.
- Dirac-principle: a simple graph with N vertices is hamiltonian if every
vertex has degree N/2 or greater(degree is the number of edges of a vertex)
- Important fact: finding hamiltonian path is NP-complete, but we can decide
whether such path exists in linear time complexity with topological ordering.

Solution:
    >> backtracking
        - We use the recursion to solve the problem.
        - Create an empty path array and add vertex 0 to it as a starting
          vertex.
        - Add other vertices, starting from vertex 1
        - Before adding a vertex
            > check whether it is adjacent to the previous added vertex.
            > make sure it is not already added.
        - If we find such a vertex
            > we added the vertex as part of the solution
        - If we do not find a vertex
            > backtrack
"""


class HamiltonianProblem(object):

    def __init__(self, adjacent_matrix):
        self.vertexes_num = len(adjacent_matrix)
        self.hamiltonian_path = [None] * self.vertexes_num
        self.adjacent_matrix = adjacent_matrix

    def hamiltonian_cycle(self):
        self.hamiltonian_path[0] = 0

        if not  self.find_feasible_solution(1):
            print("No feasible solution found...")
        else:
            self.show_hanmiltonian_path()

    def find_feasible_solution(self, position):

        # check whether if we are done, ending is the same starting in order
        # to form a cycle
        if position == self.vertexes_num:
            x = self.hamiltonian_path[position - 1]
            y = self.hamiltonian_path[0]

            if self.adjacent_matrix[x][y] == 1:
                return True
            else:
                return False

        for vertext_index in range(1, self.vertexes_num):
            if self.is_feasible(vertext_index, position):
                self.hamiltonian_path[position] = vertext_index

                if self.find_feasible_solution(position + 1):
                    return True
                # backtracking
                # do nothing
        return False

    def is_feasible(self, vertex, position):

        # first criteria: whether the two nodes are connected,
        if self.adjacent_matrix[self.hamiltonian_path[position - 1]][vertex] \
                == 0:
            return False

        # second criteria: whether we have already added this given node?
        for i in range(position):
            if self.hamiltonian_path[i] == vertex:
                return False

        return True

    def show_hanmiltonian_path(self):
        print("Hamiltonian cycle exists: ")
        for i in range(self.vertexes_num):
            print(self.hamiltonian_path[i]),
        print(self.hamiltonian_path[0])

if __name__ == "__main__":
    adjacencyMatrix = [[0, 1, 0],
                       [1, 0, 1],
                       [1, 1, 0]]

    hamiltonian = HamiltonianProblem(adjacencyMatrix)
    hamiltonian.hamiltonian_cycle()

