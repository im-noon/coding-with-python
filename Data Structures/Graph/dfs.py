"""
Depth-First-Search
- explores as far as possible along each branch before backtracking.
- memory complexity O(logN)
Applications:
- topological ordering.
- Kosaraju algorithm for finding strongly connected component in a graph
which can be proved to be very important in recommendation system.
- detecting cycles (checking weather a graph is a DAG or not).
- generating mazes Or finding way out of a maze.

Pseudo code:
- Recursion
dfs(vertex)
    vertex set visited true
    for v vertex neighbours:
        if v not in visited:
            dfs(v)

- Iteration
dfs(vertex)
    Stack stack
    vertex set visited true
    stack.pop(vertex)

    while stack not empty:
        neighbours = stack.pop()
        for v in neighbours:
            if v not in visited:
                v set visited true
                stack.push(v)
"""


from collections import defaultdict
import time


class Graph:

    def __init__(self, edges):
        self._visited = set()
        self._graph =  defaultdict(list)
        self.add_edge(edges)

    def add_edge(self, edges):
        for u, v in edges:
            self._graph[u].append(v)
            self._graph[v].append(u)

    def dfs_recursive(self, s):
        self._visited.add(s)
        yield s
        for v in self._graph[s]:
            if v not in self._visited:
                yield from self.dfs_recursive(v)

    def dfs_iteration(self, s):
        stack = [s]
        self._visited.add(s)

        while stack:
            vertex = stack.pop()
            yield vertex
            for v in self._graph[vertex]:
                if v not in self._visited:
                    self._visited.add(v)
                    stack.append(v)


if __name__ == "__main__":
    edges = [['A', 'B'],
             ['B', 'C'],
             ['B', 'D'],
             ['D', 'E'],
             ['A', 'F'],
             ['A', 'G'],
             ['G', 'H']]

    print("-----dfs recursion")
    start = time.time()
    g = Graph(edges)
    for v in g.dfs_recursive('A'):
        print(v)
    end = time.time()
    print(end - start)

    print("\n+++++dfs iteration")
    start = time.time()
    g = Graph(edges)
    for v in g.dfs_iteration('A'):
        print(v)
    end = time.time()
    print(end - start)
