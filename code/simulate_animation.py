import matplotlib.pyplot as plt
import networkx as nx
import time

# Define the graph again (same as in graph.py)
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'D': 5, 'E': 10},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 5, 'G': 2},
    'E': {'B': 10, 'G': 6},
    'F': {'C': 3, 'G': 7},
    'G': {'D': 2, 'E': 6, 'F': 7}
}

# Coordinates for plotting
positions = {
    'A': (0, 2),
    'B': (2, 2),
    'C': (0, 0),
    'D': (2, 0),
    'E': (4, 2),
    'F': (1, -1.5),
    'G': (4, 0)
}

# The shortest path (output of your A* code)
path = ['A', 'B', 'D', 'G']

# Build the networkx graph
G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor, cost in neighbors.items():
        G.add_edge(node, neighbor, weight=cost)

# Function to draw the graph
def draw_graph(current_node=None):
    plt.clf()
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, positions, with_labels=True, node_color='skyblue', node_size=1000, font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, positions, edge_labels=edge_labels)
    if current_node:
        nx.draw_networkx_nodes(G, positions, nodelist=[current_node], node_color='orange', node_size=1200)
    plt.pause(1.2)

# Animate the path
plt.figure()
print("🔁 Simulating robot movement...")

for node in path:
    print(f"🤖 Robot at node: {node}")
    draw_graph(current_node=node)

print("✅ Reached Destination!")
plt.show()
