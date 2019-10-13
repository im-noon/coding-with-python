"""
Spanning trees:
- A spanning tree od an undirected G graph is a sub graph tha includes all
the vertices of G
- In general, a tree may have several spanning tree.
- We can assign a weight to each edge,
- A minimum spanning tree is then a spanning tree with weight less than or
equal to the weight of every other spanning tree.
- Standard algorithms: Prim's Jarnik, Kruskal.
Kruskal algorithm:
- We sort the edges according ti their weights.
- It can be done in O(N*logN) with merge sort or quick sort.
- Union find data structure: disjoint set
    ** We start adding edges to the MSR and we want to make sure there will
    be no cycles in the spanning tree.
    ** It can be done in O(logV) the the help of union find data structure.
    // we can use a heap instead sorting the edges in the beginning but the
    running time would be the same. So some times Kruskal's algorithm
    is implemented with the priority queue.
- Worst case running time: O(E*logE), so we can use it for huge graphs too.
- If edges are sorted: the algorithm will be quasi-linear.
"""


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.node = None


class Node(object):
    def __init__(self, height, node_id, parent_node):
        self.height = height
        self.node_id = node_id
        self.parent_node = parent_node


class Edge(object):
    def __init__(self, weight, source, destination):
        self.weight = weight
        self.source = source
        self.destination = destination

    def __cmp__(self, other):
        return self.cmp(self.weight, other.weight)

    def __lt__(self, other):
        return self.weight < other.weight


class DisjointSet(object):
    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        self.root_node = []
        self.node_count = 0
        self.set_count = 0
        self.make_sets(self.vertex_list)

    def find(self, node):

        current_node = node
        while current_node.parent_node:
            current_node = current_node.parent_node

        root = current_node
        current_node = node

        while current_node is not root:
            temp = current_node.parent_node
            current_node.parent_node = root
            current_node = temp

        return root.node_id

    def merge(self, node1, node2):
        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:
            return  # the same set

        root1 = self.root_node[index1]
        root2 = self.root_node[index2]

        if root1.height < root2.height:
            root1.parent_node = root2
        elif root1.height > root2.height:
            root2.parent_node = root1
        else:
            root2.parent_node = root1
            root1.height += 1

    def make_sets(self, vertex_list):

        for v in vertex_list:
            self.make_set(v)

    def make_set(self, vertex):

        node = Node(0, len(self.root_node), None)
        vertex.node = node
        self.root_node.append(node)
        self.set_count += 1
        self.node_count += 1


class KruskalAlgorihtnm(object):

    def get_minimum_spanning_tree(self, vertex_list, edges_list):
        disjoint_set = DisjointSet(vertex_list)
        spanning_tree = []

        edges_list.sort()

        for edge in edges_list:
            u = edge.source
            v = edge.destination

            if disjoint_set.find(u.node) is not disjoint_set.find(v.node):
                spanning_tree.append(edge)
                disjoint_set.merge(u.node, v.node)

        for edge in spanning_tree:
            print("{} - {}".format(edge.source.name, edge.destination.name))


if __name__ == "__main__":
    """vertex1 = Vertex("a")
    vertex2 = Vertex("b")
    vertex3 = Vertex("c")
    vertex4 = Vertex("d")
    vertex5 = Vertex("e")
    vertex6 = Vertex("f")
    vertex7 = Vertex("g")
    """

    vertex1 = Vertex(1)
    vertex2 = Vertex(2)
    vertex3 = Vertex(3)
    vertex4 = Vertex(4)
    vertex5 = Vertex(5)
    vertex6 = Vertex(6)
    vertex7 = Vertex(7)

    edge1  = Edge(2, vertex1, vertex2)
    edge2  = Edge(6, vertex1, vertex3)
    edge3  = Edge(5, vertex1, vertex5)
    edge4  = Edge(10, vertex1, vertex6)
    edge5  = Edge(3, vertex2, vertex4)
    edge6  = Edge(3, vertex2, vertex5)
    edge7  = Edge(1, vertex3, vertex4)
    edge8  = Edge(2, vertex3, vertex6)
    edge9  = Edge(4, vertex4, vertex5)
    edge10 = Edge(5, vertex4, vertex7)
    edge11 = Edge(5, vertex6, vertex7)

    vertices = []
    vertices.append(vertex1)
    vertices.append(vertex2)
    vertices.append(vertex3)
    vertices.append(vertex4)
    vertices.append(vertex5)
    vertices.append(vertex6)
    vertices.append(vertex7)

    edges = []
    edges.append(edge1)
    edges.append(edge2)
    edges.append(edge3)
    edges.append(edge4)
    edges.append(edge5)
    edges.append(edge6)
    edges.append(edge7)
    edges.append(edge8)
    edges.append(edge9)
    edges.append(edge10)
    edges.append(edge11)

    algorithm = KruskalAlgorihtnm()

    algorithm.get_minimum_spanning_tree(vertices, edges)


    x = [1, 2, 3]
    y = [4, 5, 6]
    z = [7, 8, 9]

    gg = [(x[i], y[i], z[i]) for i in range(len(x))]
    print(gg)


    v = 2
    xxx = [i for i in range(1, v)]
    print(xxx)