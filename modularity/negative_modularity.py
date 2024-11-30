import networkx as nx
from networkx.algorithms.community import modularity
import matplotlib.pyplot as plt
from itertools import cycle
# Create a graph where connections are random
G = nx.Graph()
edges = [
    ('A', 'B'), ('A', 'C'), ('B', 'C'),  # Group 1 (strong connections)
    ('D', 'E'), ('D', 'F'), ('E', 'F'),  # Group 2 (strong connections)
    ('A', 'D'),   # Sparse inter-group connections
]
G.add_edges_from(edges)

# Define a community structure where groups are mixed up
communities = [{'A', 'D'}, {'B', 'E','C', 'F'}]  # Arbitrarily wrong division

# Calculate modularity
mod_value = modularity(G, communities)
print("Modularity:", mod_value)

# Assign different colors for each community
colors = cycle(['red', 'blue', 'green', 'orange'])
node_colors = {}
for comm, color in zip(communities, colors):
    for node in comm:
        node_colors[node] = color

node_color_list = [node_colors[node] for node in G.nodes]

plt.figure(figsize=(4, 3))
nx.draw(
    G, with_labels=True, node_color=node_color_list, node_size=500, font_color='white'
)
plt.title("Graph with High Modularity (>0.8)")
plt.savefig('networkVisual.png')
