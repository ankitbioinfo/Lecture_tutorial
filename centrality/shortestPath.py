import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes and edges with weights
edges = [
    ('A', 'B', 20),
    ('A', 'C', 10),
    ('B', 'C', 4),
    ('B', 'D', 3),
    ('C', 'D', 10),
    ('D', 'E', 20)
]
G.add_weighted_edges_from(edges)

# Find the shortest path from 'A' to 'E'
shortest_path = nx.shortest_path(G, source='A', target='E', weight='weight')
shortest_path_length = nx.shortest_path_length(G, source='A', target='E', weight='weight')

# Print the results
print("Shortest Path:", shortest_path)
print("Shortest Path Length:", shortest_path_length)

# Highlight the shortest path in the graph
pos = nx.spring_layout(G)
plt.figure(figsize=(4, 3))

# Draw the entire graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')

# Highlight the shortest path
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='orange', node_size=600)

# Add edge labels to show weights
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Shortest Path in the Network", fontsize=14)
plt.savefig("shortestPath.png")
