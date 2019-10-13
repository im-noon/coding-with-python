"""
Bellman-Ford algorithm:
- Invented in 1958 by Bellman and Ford independently.
- Slower than Dijkstra's but more robust: it can handle negative edge weights.
- Dijkstra algorithm choose the edge greedy, with the lowest cost:
  Bellman-Ford relaxes all edges at the same time for V-1 iteration.
- running time is O(V*E)

Pseudo code:
function BellmanFordAlgorithm(vertices, edges, source)

    distance[source] = 0

    for v in Graph
        distance[v] = inf
        predecessor[v] = undefined

    // relaxes all the edge at the same time
    for i = num_vertexes-1
        for each edge(u, v) with weight w in edges
            tempDist = distance[u] + w

            if tempDist < distance[v]
                distance[v] = tempDist
                predecessor[v] = u

    // A final scan of all the edges is performed and if any distance is updated
    // that means there is a negative cycle
    for each edge(u, v) with weight w in edges
        if distance[u] + w < distance[v]
            error: // negative cycle detected
"""


import sys
import time


class Node(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacent_list = []
        self.min_distance = sys.maxsize


class Edge(object):

    def __init__(self, weight, source, destination):
        self.weight = weight
        self.source = source
        self.destination = destination


class BellmanFord(object):

    def __init__(self):
        self.has_cycle = False

    def calculate_shortest_path(self, vertex_list, edge_list, source):
        source.min_distance = 0

        for i in range(0, len(vertex_list) - 1):
            for edge in edge_list:
                u = edge.source
                v = edge.destination

                new_distance = u.min_distance + edge.weight
                if new_distance < v.min_distance:
                    v.min_distance = new_distance
                    v.predecessor = u

        for edge in edge_list:
            if self.detected_cycle(edge):
                print("Negative cycle detected...")
                self.has_cycle = True
                return

    def detected_cycle(self, edge):
        if (edge.source.min_distance + edge.weight) < \
                edge.destination.min_distance:
            return True
        else:
            return False

    def get_shortest_path(self, source):
        if self.has_cycle:
            print("Negative cycle detected...")
        else:
            print("Shortest path exists with :{}".format(source.min_distance))
            node = source
            while node:
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

    edge17 = Edge(1, node1, node2)
    edge18 = Edge(1, node2, node3)
    edge19 = Edge(-3, node3, node1)

    node1.adjacent_list.append(edge1)
    node1.adjacent_list.append(edge2)
    node1.adjacent_list.append(edge3)
    node2.adjacent_list.append(edge4)
    node2.adjacent_list.append(edge5)
    node2.adjacent_list.append(edge6)
    node8.adjacent_list.append(edge7)
    node8.adjacent_list.append(edge8)
    node5.adjacent_list.append(edge9)
    node5.adjacent_list.append(edge10)
    node5.adjacent_list.append(edge11)
    node6.adjacent_list.append(edge12)
    node6.adjacent_list.append(edge13)
    node3.adjacent_list.append(edge14)
    node3.adjacent_list.append(edge15)
    node4.adjacent_list.append(edge16)

    vertices = (node1, node2, node3, node4, node5, node6, node7, node8)

    edges = (edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9,
             edge10, edge11, edge12, edge13, edge14, edge15, edge16)
    #edges = (edge17, edge18, edge19)
    algorithm = BellmanFord()
    algorithm.calculate_shortest_path(vertices, edges, node1)
    algorithm.get_shortest_path(node3)
