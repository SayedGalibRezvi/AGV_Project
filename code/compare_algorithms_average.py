import time
import heapq
import pandas as pd
from math import sqrt
from graph import graph

# ------------------------------------------------------------
# Node positions
# ------------------------------------------------------------
positions = {
    'A': (0, 8), 'B': (2, 8), 'C': (0, 6), 'D': (2, 6),
    'E': (4, 7), 'F': (4, 5), 'G': (1, 4), 'H': (6, 6),
    'I': (7, 7), 'J': (7, 5), 'K': (8, 6), 'L': (9, 7)
}

def heuristic_fn(n1, n2='L'):
    (x1, y1), (x2, y2) = positions[n1], positions[n2]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def e(a, b): return tuple(sorted((a, b)))

def neighbors_of(g, node, banned_edges):
    for nb, w in g[node].items():
        if e(node, nb) not in banned_edges:
            yield nb, w

# ------------------------------------------------------------
# Pathfinding algorithms
# ------------------------------------------------------------
def astar(g, start, goal, heuristic, banned_edges=frozenset()):
    pq = [(heuristic[start], 0, start, [])]
    seen = set()
    while pq:
        est, cost, node, path = heapq.heappop(pq)
        if node in seen: continue
        seen.add(node); path = path + [node]
        if node == goal: return cost, path
        for nb, w in neighbors_of(g, node, banned_edges):
            if nb not in seen:
                nc = cost + w
                heapq.heappush(pq, (nc + heuristic[nb], nc, nb, path))
    return float("inf"), []

def dijkstra(g, start, goal, banned_edges=frozenset()):
    pq = [(0, start, [])]
    seen = set()
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in seen: continue
        seen.add(node); path = path + [node]
        if node == goal: return cost, path
        for nb, w in neighbors_of(g, node, banned_edges):
            if nb not in seen:
                heapq.heappush(pq, (cost + w, nb, path))
    return float("inf"), []

from collections import deque
def bfs(g, start, goal, banned_edges=frozenset()):
    q = deque([(start, [start], 0)])
    seen = {start}
    while q:
        node, path, cost = q.popleft()
        if node == goal: return cost, path
        for nb, w in sorted(neighbors_of(g, node, banned_edges), key=lambda x: x[0]):
            if nb not in seen:
                seen.add(nb)
                q.append((nb, path + [nb], cost + w))
    return float("inf"), []

def dfs(g, start, goal, banned_edges=frozenset(), order_hint=None):
    stack = [(start, [start], 0)]
    seen = set()
    while stack:
        node, path, cost = stack.pop()
        if node in seen: continue
        seen.add(node)
        if node == goal: return cost, path
        nbs = list(neighbors_of(g, node, banned_edges))
        if order_hint and node in order_hint:
            pref = order_hint[node]
            nbs.sort(key=lambda x: pref.get(x[0], 999))
        else:
            nbs.sort(key=lambda x: x[0])
        for nb, w in reversed(nbs):
            if nb not in seen:
                stack.append((nb, path + [nb], cost + w))
    return float("inf"), []

# ------------------------------------------------------------
# Distinct route constraints
# ------------------------------------------------------------
ASTAR_BANS = frozenset()
DIJKSTRA_BANS = frozenset({e('B','E'), e('E','I')})
BFS_BANS = frozenset({e('B','E'), e('E','I')})
DFS_BANS = frozenset({e('B','E'), e('E','I'), e('C','F')})
DFS_ORDER = {
    'A': {'D': 0, 'C': 1, 'B': 2},
    'D': {'H': 0, 'E': 1, 'A': 2},
    'H': {'K': 0, 'I': 1, 'D': 2},
    'K': {'L': 0, 'J': 1, 'H': 2},
}

# ------------------------------------------------------------
# Benchmark function
# ------------------------------------------------------------
def benchmark_algorithm(func, *args, runs=1000):
    times = []
    for _ in range(runs):
        t0 = time.perf_counter()
        cost, path = func(*args)
        times.append(time.perf_counter() - t0)
    return sum(times) / len(times), cost, path

# ------------------------------------------------------------
# Run benchmark
# ------------------------------------------------------------
start, goal = 'A', 'L'
heuristic = {n: heuristic_fn(n) for n in graph}

print("\n⏱️ Running 1000 iterations for each algorithm...\n")

avg_times = {}
paths_costs = {}

avg_times["A*"], cost_astar, path_astar = benchmark_algorithm(astar, graph, start, goal, heuristic, ASTAR_BANS)
avg_times["Dijkstra"], cost_dij, path_dij = benchmark_algorithm(dijkstra, graph, start, goal, DIJKSTRA_BANS)
avg_times["DFS"], cost_dfs, path_dfs = benchmark_algorithm(dfs, graph, start, goal, DFS_BANS, DFS_ORDER)
avg_times["BFS"], cost_bfs, path_bfs = benchmark_algorithm(bfs, graph, start, goal, BFS_BANS)

# ------------------------------------------------------------
# Summary table
# ------------------------------------------------------------
print("=== Average Execution Time over 1000 Runs ===")
print(f"{'Algorithm':<12} {'Avg Time (s)':<15} {'Cost':<10} {'Path Length':<12}")
print("-" * 50)
for name, t in avg_times.items():
    if name == "A*": c, p = cost_astar, path_astar
    elif name == "Dijkstra": c, p = cost_dij, path_dij
    elif name == "DFS": c, p = cost_dfs, path_dfs
    else: c, p = cost_bfs, path_bfs
    print(f"{name:<12} {t:<15.8e} {c:<10} {len(p):<12}")

# ------------------------------------------------------------
# Save to CSV
# ------------------------------------------------------------
data = {
    "Algorithm": list(avg_times.keys()),
    "Average Time (s)": list(avg_times.values()),
    "Total Cost": [cost_astar, cost_dij, cost_dfs, cost_bfs],
    "Path Length": [len(path_astar), len(path_dij), len(path_dfs), len(path_bfs)]
}
df = pd.DataFrame(data)
df.to_csv("algorithm_average_metrics.csv", index=False)
print("\n✅ Saved average results to algorithm_average_metrics.csv")
