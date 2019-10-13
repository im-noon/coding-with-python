## Tree Component

#### Node
A node is fundamental path of tree. It can have a name, which we call the _key._
A node may also have additional information, which call _payload._ While the payload is not central to many tree algorithms.

#### Edge
An edge is anther fundamental part of a tree. An edge connects two nodes to show that tree is a relationship between them. 
Every node (except the root) is connected by exactly one incoming edge from another node.
Each node may have several outgoing edges.

#### Root
The root of the tree is the only node th the tree that has no incoming edges.

#### Path
A path ia an ordered list of nodes that are connected by edges.

#### Children
The set of nodes _c_ that have incoming edges from the same node to are said to be the children of that node.

#### Parent
A node is the parent of all the nodes it connects to with outgoing edges.

#### Sibling
Nodes in the tree that are children of the same parent are said to be sibling.

#### Subtree
A subtree is a set of nodes and edges comprised of a parent and all the descendants of that parent.

#### Leaf Node
A leaf node is a node that has no children

#### Level
The level of a node _n_ is the number of edges on the path from the root to _n_.

#### Height
The height of a tree is equal to the maximum level of nay node.

## Tree Definitions

#### Definition one:
A tree consists of a set of nodes and a set of edges that connect pairs of nodes has the following properties.
* One node of the tree is designated as the root node.
* Every node _n_, except root node, is connected by any edge from exactly on other node _p_, where _p_ is the parent of _n_.
* A unique path traverses from the root to each node,
* If each node in the tree has maximum of two children we say that the tree is a binary _**tree**_.

#### Definition two:
A tree is either empty or consists of a root and zero or more subtrees, is of which also a tree.
The root of each subtree is connected to the root of the parent tree by an edge.