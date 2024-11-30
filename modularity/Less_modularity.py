
import os
import pandas as pd
from os import listdir
from os.path import isfile, join
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import k_clique_communities
import scipy.stats
from networkx.algorithms import isomorphism
from networkx.algorithms.community import modularity, label_propagation_communities


df = pd.read_csv('modularity1.dat',sep=',')
edges = df.to_numpy()

print(edges,edges.shape)

G=nx.Graph()
G.add_edges_from(edges)

'''
#mod=nx.community.modularity(G, communities, weight='weight', resolution=1)
mod = nx.community.modularity(G, nx.community.label_propagation_communities(G))

print(mod)

plt.figure(figsize=(8, 6))
nx.draw(
    G,
    with_labels=True,
    node_size=800,  # Customize node size
    font_size=18,   # Customize label size
    node_color="skyblue",  # Color of the nodes
    edge_color="gray"      # Color of the edges
)
plt.title("Biological Network Visualization", fontsize=16)
plt.savefig('networkVisual.png')
'''

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
