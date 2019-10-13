"""
- It was constructed by computer scientist Edsger Dijkstra in 1956.
- Dijkstra can handle only positive edge weight!!!
- Several variants: it can find the shortest path from A to B, but it is able to
  construct a shortest path three as well -> defines the shortest paths from
  a source to all the nodes.
- This is asymptotically the fastest know single-source shortest-path algorithm
  for arbitrary directed graphs with unbounded non-negative weights.
- The running time complexity : O(VlogN + E).
- Dijkstra's algorithm is a greedy: it tries to find the global optimum with
  the help of local minimum.
- It is greedy
    -> on every iteration we want to find the minimum distance to the next
       vertex possible.
    -> appropriate data structures: heap (binary or fibonacci) or in general
       a priority queue.
Pseudo code:
class Node
    name
    min_distance
    Node predecessor
function DijkstraAlgorithm(Graph, source)
    // initialize phase
    distance[source] = 0
    create vertex queue Q  // priority queue

    for v in Graph:
        distance[v] = inf
        predecessor[v] = undefined // previous node in the shortest path

    while Q is not empty:
    u = vertex in Q with minimum distance: // use minimum heap
    remove u from Q

    for each neighbours v of u:
        tempDist = distance[u] = dustBetween(u, v)
        if tempDist < distance[v]
            distance[v] = tempDist
            predecessor[v] - u
"""


import sys
import time
import heapq


class Edge(object):

    def __init__(self, weight, source, destination):
        self.weight = weight
        self.source = source
        self.destination = destination

class Node(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.min_distance = sys.maxsize
        self.adjacencies_list = []

    def __cmp__(self, other):
        return self.cmp(self.min_distance, other.min_distance)

    def __lt__(self, other):
        return self.min_distance < other.min_distance

class Algorithm(object):

    def calculate_shortest_path(self, source):
        self.source = source
        q = []
        source.min_distance = 0
        heapq.heappush(q, source)

        while q:
            neighbours = heapq.heappop(q)
            for edge in neighbours.adjacencies_list:
                u = edge.source
                v = edge.destination

                distance = u.min_distance + edge.weight
                if distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = distance
                    heapq.heappush(q, v)

    def get_shortest_path(self, vertex):

        print("shortest path to vertex [{}] is {}".format(vertex.name,
                                                          vertex.min_distance))
        node = vertex
        while node is not None:
            print("{}".format(node.name))
            node = node.predecessor


if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    edge1 = Edge(5, node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(5, node5, node8)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    node1.adjacencies_list.append(edge1)
    node1.adjacencies_list.append(edge2)
    node1.adjacencies_list.append(edge3)
    node2.adjacencies_list.append(edge4)
    node2.adjacencies_list.append(edge5)
    node2.adjacencies_list.append(edge6)
    node8.adjacencies_list.append(edge7)
    node8.adjacencies_list.append(edge8)
    node5.adjacencies_list.append(edge9)
    node5.adjacencies_list.append(edge10)
    node5.adjacencies_list.append(edge11)
    node6.adjacencies_list.append(edge12)
    node6.adjacencies_list.append(edge13)
    node3.adjacencies_list.append(edge14)
    node3.adjacencies_list.append(edge15)
    node4.adjacencies_list.append(edge16)

    vertexList = (node1, node2, node3, node4, node5, node6, node7, node8)

    algorithm = Algorithm()
    algorithm.calculate_shortest_path(node1)
    algorithm.get_shortest_path(node7)
