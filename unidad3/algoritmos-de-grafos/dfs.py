from graphs import Graph

# Test block from *Graph Algorithms the Fun Way*
g: Graph = Graph(5, undirected=True)
g.insert_edge(0, 1, 1.0)
g.insert_edge(0, 3, 1.0)
g.insert_edge(0, 4, 3.0)
g.insert_edge(1, 2, 2.0)
g.insert_edge(1, 4, 1.0)
g.insert_edge(3, 4, 3.0)
g.insert_edge(4, 2, 3.0)
g.insert_edge(4, 3, 3.0)

# Recursive DFS function
def dfs(graph, node, visited, order, depth=0):
    print("  " * depth + f"visit {node}")
    visited.add(node)              # mutate: mark visited
    order.append(node)             # mutate: record order
    for edge in graph.nodes[node].get_sorted_edge_list():
        if edge.to_node not in visited:
            dfs(graph, edge.to_node, visited, order, depth + 1)
    print("  " * depth + f"back from {node}") 

# Driver
start = 0
visited = set()                    # empty set
order = []                         # empty list
dfs(g, start, visited, order)
print("Orden de visita:", order)