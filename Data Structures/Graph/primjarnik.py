"""
Prim-Jarrnik:
- IN Kruskal implementation we build the spanning tree separately, adding the
  smallest edges to the spanning tree if there is no cycle.
- In Primes algorithm we build a spanning tree from a given vertex, adding a
  smallest to the MST.
- Kruskal -> edge base.
- Prims -> vertex base.
- There are two implementations: lazy and eager.
- Lazy implementation: add the new neighbour edges to the heap without deleting
  its content.
- Eager implementation: keep updating the heap if the distance from a vertex
  to the MST has changed.
- Average running time: O(E*logE), but we need additional memory space O(E)
 for worst case scenario running time O(E*logV).
"""


import heapq


class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacent_list = list()

    def __str__(self):
        return self.name


class Edge(object):

    def __init__(self, weight, source, destination):
        self.weight = weight
        self.source = source
        self.destination = destination

    def __cmp__(self, other):
        return self.cmp(self.weight, other.weight)

    def __lt__(self, other):
        return self.weight < other.weight


class PrimsJarnik(object):

    def __init__(self, unvisited):
        self.unvisited = unvisited
        self.spanning_tree = list()
        self.edge_heap = []
        self.full_cost = 0

    def get_minimum_spanning_tree(self, source):

        self.unvisited.remove(source)

        while self.unvisited:
            for edge in source.adjacent_list:
                if edge.destination in self.unvisited:
                    heapq.heappush(self.edge_heap, edge)

            min_edge = heapq.heappop(self.edge_heap)

            self.spanning_tree.append(min_edge)
            print("Edge added to spanning tree {} : {}".format(
                min_edge.source.name, min_edge.destination.name))
            self.full_cost += min_edge.weight

            source = min_edge.destination
            self.unvisited.remove(source)

        return self.full_cost#self.spanning_tree



if __name__ == "__main__":
    """
    node1 = Vertex("A")
    node2 = Vertex("B")
    node3 = Vertex("C")

    edge1 = Edge(100, node1, node2)
    edge2 = Edge(100, node2, node1)
    edge3 = Edge(1000, node1, node3)
    edge4 = Edge(1000, node3, node1)
    edge5 = Edge(0.01, node3, node2)
    edge6 = Edge(0.01, node2, node3)

    node1.adjacent_list.append(edge1)
    node1.adjacent_list.append(edge3)
    node2.adjacent_list.append(edge2)
    node2.adjacent_list.append(edge6)
    node3.adjacent_list.append(edge4)
    node3.adjacent_list.append(edge5)

    unvisitedList = []
    unvisitedList.append(node1)
    unvisitedList.append(node2)
    unvisitedList.append(node3)

    algorithm = PrimsJarnik(unvisitedList)
    cost = algorithm.get_minimum_spanning_tree(node2)
    print(cost)
    """

    node1 = Vertex(1)
    node2 = Vertex(2)
    node3 = Vertex(3)
    node4 = Vertex(4)
    node5 = Vertex(5)

    edge1 = Edge(3, node1, node2)
    edge2 = Edge(4, node1, node3)
    edge3 = Edge(6, node4, node2)
    edge4 = Edge(2, node5, node2)
    edge5 = Edge(5, node2, node3)
    #edge6 = Edge(7, node3, node5)

    node1.adjacent_list.append(edge1)
    node1.adjacent_list.append(edge2)
    node2.adjacent_list.append(edge1)
    node2.adjacent_list.append(edge3)
    node2.adjacent_list.append(edge4)
    node2.adjacent_list.append(edge5)

    node3.adjacent_list.append(edge1)
    node3.adjacent_list.append(edge5)
    node4.adjacent_list.append(edge3)
    node5.adjacent_list.append(edge4)

    unvisitedList = []
    unvisitedList.append(node1)
    unvisitedList.append(node2)
    unvisitedList.append(node3)
    unvisitedList.append(node4)
    unvisitedList.append(node5)

    algorithm = PrimsJarnik(unvisitedList)
    cost = algorithm.get_minimum_spanning_tree(node2)
    print(cost)