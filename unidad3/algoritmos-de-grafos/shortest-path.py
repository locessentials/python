# Ruta más corta

import heapq

# Organize the inputs

nodes, edges = map(int, input().split())

graph = {}                          # dictionary for the graph
for node in range(1, nodes + 1):    # each node is initialized as a key
    graph[node] = []

for node in range(edges):           # each edge is added to the dictionary
    node_a, node_b, weight = map(int, input().split())
    graph[node_a].append((node_b, weight))
    graph[node_b].append((node_a, weight))

start = int(input())                # the starting point

# Calculate the costs

costs = {}                      # dictionary for costs
for node in range(1, nodes + 1):  # the cost from the starting point to each node
    costs[node] = float("inf")    # starts at infinity
costs[start] = 0                # the start has a cost of 0 to itself
heap = [(0, start)]             # the heap starts with the pair
                                # (cost 0, starting node)

previous = {}                   # dictionary for which node we traveled from
                                # in the shortest path

while len(heap) != 0:           # while the heap isn't empty
    current_cost, current_node = heapq.heappop(heap) # remove the smallest cost and its node
                                                     # (i.e., the first item in the list)
    if current_cost > costs[current_node]:          # if it's cost > what's in the dict
        continue                                    # the pair is old
                                                    # continue to the next smallest cost
                                                    # in the heap

    for neighbor, weight in graph[current_node]:    # for each neighbor of the current node
                                                    # in the graph dict
        new_cost = current_cost + weight            # calculate the new costs

        if new_cost < costs[neighbor]:              # if this new cost is < what's in the dict
            costs[neighbor] = new_cost              # update to the new cost
            previous[neighbor] = current_node       # add the destination node
                                                    # and its intermediary node to the dict
            heapq.heappush(heap, (new_cost, neighbor))  # add the cost and the destination node
                                                        # to the heap for checking

# Print the shortest path

print("Starting point:", start)

for node in range(1, nodes + 1):
    if costs[node] == float("inf"):
        print("Destination:", node, "No path")
    else:
        path = [node]
        current_node = node

        # ir hacia atrás hasta llegar al inicio
        while current_node != start:
            current_node = previous[current_node]
            path.append(current_node)

        path.reverse()      # estaba de atrás hacia adelante
        print("Destination:", node, "Cost:", costs[node], "Path:", path)

# Get-Content caminos-más-cortos-prueba.txt | python caminos-más-cortos.py