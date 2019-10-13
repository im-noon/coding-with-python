
Shortest path problem:
- finding path between two vertices in a graph such that the sum of the
weights of its edges is minimized.
- Dijkstra algorithm
- Bellman-Ford algorithm
- A* search
- Floyd-Warshall algorithm

DAG shortest path:
- if the graph is a DAG, so there is no directed cycles, it is easy to find
  the shortest path.
- we sort the vertices into topological order: we iterate through the
  topological order relaxing all edges from the actual vertex.
- Topological sort algorithm computes shortest path tree in any edges weights
  (can be negative) DAG in time O(V+E).
- It is much faster than Bellman-Ford or Dijkstra.

Application:
- solving Knapsack problem.
- GPS, vehicle routing and navigation
- Detecting arbitrage in Forex

Longest oath problem:
