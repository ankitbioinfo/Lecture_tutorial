

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




#G = nx.Graph([('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'),('D','E')])
#print(nx.degree_centrality(G))
#{0: 1.0, 1: 1.0, 2: 0.6666666666666666, 3: 0.6666666666666666}
G = nx.Graph([('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'),('B','D')])
print("closeness",nx.closeness_centrality(G))

plt.figure(figsize=(4, 3))
nx.draw(
    G, with_labels=True,node_size=500, font_color='white'
)
#plt.title("Graph with High Modularity (>0.8)")
plt.savefig('networkCentrality.png')
