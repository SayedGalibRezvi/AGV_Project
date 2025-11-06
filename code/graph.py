# graph.py

graph = {
    'A': {'B': 3, 'C': 8, 'D': 6},
    'B': {'A': 3, 'E': 4, 'F': 9},
    'C': {'A': 8, 'F': 6, 'G': 10},
    'D': {'A': 6, 'H': 7, 'E': 9},
    'E': {'B': 4, 'D': 9, 'I': 8},
    'F': {'B': 9, 'C': 6, 'G': 3, 'J': 9},
    'G': {'C': 10, 'F': 3, 'K': 7},
    'H': {'D': 7, 'I': 5, 'K': 9},
    'I': {'E': 8, 'H': 5, 'J': 6, 'L': 5},
    'J': {'F': 9, 'I': 6, 'K': 5, 'L': 8},
    'K': {'G': 7, 'H': 9, 'J': 5, 'L': 6},
    'L': {'I': 5, 'J': 8, 'K': 6}
}

if __name__ == "__main__":
    for node, neighbors in graph.items():
        print(f"{node} connects to {neighbors}")
