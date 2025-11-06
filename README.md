# 🤖 Vision-Based Node Localization and Path Planning for Abstract AGV Logistics

## 🧠 Overview
This project presents a **vision-based AGV (Automated Guided Vehicle)** system designed to autonomously navigate through predefined nodes using **QR-code-based localization** and **graph-based path planning**.

The AGV identifies its current node using camera-detected QR codes and computes the **shortest and most efficient route** to its destination using advanced pathfinding algorithms.

While the project includes a comparative evaluation between multiple algorithms —  
- 🟥 **A\*** (Heuristic-based optimal pathfinding)  
- 🟦 **Dijkstra’s Algorithm** (Uniform-cost search)  
- 🟩 **Depth-First Search (DFS)**  
- 🟧 **Breadth-First Search (BFS)**  

👉 The **primary algorithm used in this AGV system is A\***, as it combines **optimal path accuracy** (like Dijkstra) with **heuristic-driven efficiency**, making it highly suitable for **real-time navigation**.

The other algorithms were implemented only for **comparison and performance benchmarking**, providing insight into how A\* consistently outperforms them in:
- ⏱️ **Execution time**
- 💰 **Path cost**
- 🧩 **Route accuracy**

A\* uses a heuristic function to estimate the remaining distance between nodes, allowing the AGV to intelligently predict the most promising next step and minimize unnecessary traversal — ideal for environments with dynamic or weighted paths.

---

## ⚙️ System Workflow

### 1️⃣ QR Code Detection
- The AGV camera scans physical QR codes to detect nodes.  
- Each QR code corresponds to a **graph node** (e.g., A, B, C...).  
- Detected coordinates are sent to the control system for localization.

### 2️⃣ Path Planning
- The system builds a **weighted graph** where each edge represents a route and its travel cost.  
- Different algorithms (A*, Dijkstra, BFS, DFS) compute possible paths between a start and goal node.  
- Each algorithm’s route,

### 3️⃣ Route Visualization
- The computed paths are visualized using **NetworkX** and **Matplotlib**.  
- Each algorithm is displayed in its own color and style:
  - A*: 🔴 Red (Dashed)
  - Dijkstra: 🔵 Blue (Solid)
  - DFS: 🟢 Green (Dash-dot)
  - BFS: 🟠 Orange (Dotted)

### 4️⃣ Evaluation and Comparison
- Each algorithm is evaluated on:
  - ⏱️ **Execution Time**
  - 💰 **Total Path Cost**
  - 🧩 **Path Length**
  - 🔁 **Nodes Explored**

- Metrics are automatically saved into CSV files for visualization.
