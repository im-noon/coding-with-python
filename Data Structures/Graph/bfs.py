"""
Breath-First-Search:
    It's good for:
    - when we want to visit every node.
    - visit every vertex exactly once.
    - visit the neighbours of these new vertices and so on.
    - construct a shortest path, e.g. Dijkstra algorithm.
    - construct a maximum flow algorithm.
    Complexity:
    - running time complexity is linear O(V+E).
    - memory complexity is not good, due to sore lots of references.
    Applications:
    - Robot prove to discover surrounding object more easily.
    - Edmonds-Karp algorithm use BFS to finding augmenting paths.
    - Cheyen's algorithm in garbage collection; it help to maintain active
    reference on the heap memory.
    - It use BFS to detect all the references on the heap (Java)
    - Serialization/deserialization of tree like structure (order does matter)
    Pseudo code:
        bfs(vertex)
            Queue queue
            vertex set visited true
            queue.enqueue(vertex)
            while queue not empty:
                neighbours = queue.dequeue()
                for v in neighbours:
                    if v is not visited:
                        v set visited true
                        q.enqueue(v)
"""


from collections import defaultdict
import time


class Graph:

    def __init__(self, edge_list):
        self._visited = set()
        self._graph = defaultdict(list)
        self.add_edge(edge_list)

    def add_edge(self, edge_list):
        for u, v in edge_list:
            self._graph[u].append(v)
            self._graph[v].append(u)

    def bfs(self, s):
        queue = []
        queue.append(s)
        self._visited.add(s)
        while queue:
            s = queue.pop(0)
            print("{}".format(s))
            for v in self._graph[s]:
                if v not in self._visited:
                    self._visited.add(v)
                    queue.append(v)


if __name__ == "__main__":
    edges = [['A', 'B'],
             ['B', 'C'],
             ['B', 'D'],
             ['D', 'E'],
             ['A', 'F'],
             ['A', 'G'],
             ['G', 'H']]

    start = time.time()
    g = Graph(edges)
    g.bfs('A')
    end = time.time()
    print(end - start)
    print("-----------")
