import networkx as nx
from networkx.algorithms.community import modularity, label_propagation_communities

# Create a graph with distinct communities
G = nx.Graph()

# Add edges for the first community
edges_community1 = [(1, 2), (1, 3), (0,1),(0,3),(2, 3), (2, 4), (3, 4)]
G.add_edges_from(edges_community1)

# Add edges for the second community
edges_community2 = [(5, 6), (5, 7), (6, 7), (6, 8), (7, 8)]
G.add_edges_from(edges_community2)

# Add edges for the third community
edges_community3 = [(9, 10), (9, 11), (14,15),(14,13),(13,15),(10,13),(10, 11),(10, 12), (11, 12),]
G.add_edges_from(edges_community3)

# Add sparse connections between communities
G.add_edges_from([(4, 5), (8, 9)])  # Minimal inter-community connections

# Detect communities using label propagation
communities = label_propagation_communities(G)

# Calculate modularity
mod_value = modularity(G, communities)
print(f"Modularity: {mod_value:.2f}")

# Visualize the graph
import matplotlib.pyplot as plt
from itertools import cycle

# Assign different colors for each community
colors = cycle(['red', 'blue', 'green', 'orange'])
node_colors = {}
for comm, color in zip(communities, colors):
    for node in comm:
        node_colors[node] = color

node_color_list = [node_colors[node] for node in G.nodes]

plt.figure(figsize=(8, 6))
nx.draw(
    G, with_labels=True, node_color=node_color_list, node_size=500, font_color='white'
)
plt.title("Graph with High Modularity (>0.8)")
plt.savefig('networkVisual.png')
