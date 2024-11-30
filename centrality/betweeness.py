import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add edges

edges = [
    ('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'E'),  # Dense cluster
    ('E', 'F'),                                                  # Bridge
    ('F', 'G'), ('F', 'H'), ('G', 'H')                           # Another cluster
]

#
#edges = [
#    ('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'E'),  # Dense cluster
#    ('E', 'F'),                                                  # Bridge
#]
#'''
G.add_edges_from(edges)

# Calculate betweenness centrality
betweenness = nx.betweenness_centrality(G,normalized=False)

# Print betweenness centrality
for node, value in betweenness.items():
    print(f"Node {node}: Betweenness Centrality = {value:.3f}")
#'''
# Visualize the network
pos = nx.spring_layout(G)

# Color nodes based on betweenness centrality
node_colors = [betweenness[node] for node in G.nodes()]
node_sizes = [1000 * betweenness[node] for node in G.nodes()]  # Scale node size for visualization

input_colormap='viridis'

fig,ax=plt.subplots(figsize=(4, 3))
nx.draw(
    G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes,
    cmap=plt.colormaps.get_cmap(input_colormap), edge_color='gray', alpha=0.8,
)

# Add a color bar
sm = plt.cm.ScalarMappable(cmap=plt.colormaps.get_cmap(input_colormap), norm=plt.Normalize(vmin=min(node_colors), vmax=max(node_colors)))
sm.set_array([])
fig.colorbar(sm,ax=ax, label="Betweenness Centrality")

#plt.title("Network with Low and High Betweenness Centrality", fontsize=14)
plt.savefig('betweeness.png',bbox_inches='tight',dpi=300)
'''

nodes=G.nodes()
print(nodes)

for i in range(len(nodes)):
    for j in range(len(nodes)):
        path=nx.all_shortest_paths(G, source=nodes[i], target=nodes[j])
        print(nodes[i],nodes[j],path)
    print()
'''
