from graphs import Graph

# Recreating the test block from the screenshot
g: Graph = Graph(5, undirected=False)
g.insert_edge(0, 1, 1.0)
g.insert_edge(0, 3, 1.0)
g.insert_edge(0, 4, 3.0)
g.insert_edge(1, 2, 2.0)
g.insert_edge(1, 4, 1.0)
g.insert_edge(3, 4, 3.0)
g.insert_edge(4, 2, 3.0)
g.insert_edge(4, 3, 3.0)

# --- Additional code to test and verify the output ---

print("--- Edges for Node 0 ---")
for edge in g.nodes[0].get_edge_list():
    print(f"From {edge.from_node} to {edge.to_node}, weight: {edge.weight}")

print("\n--- Is there an edge from 0 to 4? ---")
print(g.is_edge(0, 4))

print("\n--- Is there an edge from 2 to 0? ---")
print(g.is_edge(2, 0))

print("\n--- All edges in the graph ---")
all_edges = g.make_edge_list()
for edge in all_edges:
    print(f"({edge.from_node} -> {edge.to_node}, w={edge.weight})")