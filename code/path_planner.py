import heapq

# Define the same graph
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'D': 5, 'E': 10},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 5, 'G': 2},
    'E': {'B': 10, 'G': 6},
    'F': {'C': 3, 'G': 7},
    'G': {'D': 2, 'E': 6, 'F': 7}
}

# Dummy heuristic: use 0 for all (no prediction)
heuristic = {
    'A': 0, 'B': 0, 'C': 0,
    'D': 0, 'E': 0, 'F': 0,
    'G': 0
}

def a_star(start, goal):
    queue = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while queue:
        _, current = heapq.heappop(queue)

        if current == goal:
            break

        for neighbor, cost in graph[current].items():
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(queue, (priority, neighbor))
                came_from[neighbor] = current

    # Reconstruct path
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path, cost_so_far[goal]

# Ask for input
start_node = input("Enter START node (e.g. A): ").strip().upper()
end_node = input("Enter END node (e.g. G): ").strip().upper()

if start_node in graph and end_node in graph:
    path, cost = a_star(start_node, end_node)
    print("✅ Shortest path:", ' ➝ '.join(path))
    print("🧮 Total cost:", cost)
else:
    print("❌ Invalid nodes. Please use A to G.")
