import networkx as nx

# Create a directed or undirected graph (choose based on your layout)
G = nx.Graph()

# Add nodes
G.add_node("A")  # You can use QR code content as node names
G.add_node("B")
G.add_node("C")
G.add_node("D")

# Add edges with travel cost (weight)
G.add_edge("A", "B", weight=1.5)
G.add_edge("A", "C", weight=2.0)
G.add_edge("B", "D", weight=2.5)
G.add_edge("C", "D", weight=1.0)

# OPTIONAL: visualize the graph (can skip for now)
import matplotlib.pyplot as plt
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
