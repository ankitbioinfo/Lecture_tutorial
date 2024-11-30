import networkx as nx
import matplotlib.pyplot as plt

n=10000
avg=0
for i in range(n):
    # Parameters
    num_nodes = 6  # Number of nodes
    probability = 0.9  # Probability of edge creation

    # Create random graph
    G = nx.erdos_renyi_graph(n=num_nodes, p=probability)

    avg+=len(G.edges())

print(avg/n)

'''
# Draw the graph
plt.figure(figsize=(4, 3))  # Set figure size
nx.draw(G, with_labels=True, node_size=500, node_color="skyblue", font_size=18, font_color="black")
plt.title(f"Random Graph (n={num_nodes}, p={probability})", fontsize=16)
plt.savefig('random.png',dpi=300)
'''
