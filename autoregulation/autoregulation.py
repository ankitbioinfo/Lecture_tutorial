import networkx as nx
import matplotlib.pyplot as plt
import random


# Create a directed graph for a small regulatory network
real_network = nx.DiGraph()
real_edges = [
    ("GeneA", "GeneB"),
    ("GeneB", "GeneC"),
    ("GeneC", "GeneA"),  # Feedback loop
    ("GeneA", "GeneA"),  # Autoregulation
]
real_network.add_edges_from(real_edges)

# Create a random directed graph
nodes = list(real_network.nodes())
random_network = nx.DiGraph()
random_edges = random.sample([(u, v) for u in nodes for v in nodes if u != v], len(real_edges))
random_network.add_edges_from(random_edges)


# Plot real and random networks
plt.figure(figsize=(6, 3))

# Real network
plt.subplot(1, 2, 1)
nx.draw(real_network, with_labels=True, node_size=800,alpha=0.6,node_color="skyblue", arrows=True)
plt.title("Real Network with Autoregulation")

# Random network
plt.subplot(1, 2, 2)
nx.draw(random_network, with_labels=True, node_size=800,alpha=0.6,node_color="lightgreen", arrows=True)
plt.title("Random Network")

plt.tight_layout()
plt.savefig('autoregulation.png',bbox_inches='tight',dpi=300)


# Clustering coefficients
real_clustering = nx.average_clustering(real_network.to_undirected())
random_clustering = nx.average_clustering(random_network.to_undirected())

# Shortest path lengths
real_path_lengths = dict(nx.shortest_path_length(real_network))
random_path_lengths = dict(nx.shortest_path_length(random_network))

print("Real Network Clustering Coefficient:", real_clustering)
print("Random Network Clustering Coefficient:", random_clustering)

print("\nReal Network Path Lengths:", real_path_lengths)
print("\nRandom Network Path Lengths:", random_path_lengths)
