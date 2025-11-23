# 🤖 Vision-Based Node Localization & Path Planning for AGV Logistics

## 🧠 Overview
This project implements a vision-based AGV (Automated Guided Vehicle) navigation system that uses QR codes for localization and graph algorithms for path planning.

A camera detects physical QR codes representing nodes (A, B, C…), identifies the robot’s current location, and computes the optimal path to a destination using A*. Additional algorithms — Dijkstra, BFS, and DFS — are included for comparison.

The system includes:
- QR-based localization
- Weighted graph path planning
- A* for shortest path computation
- Algorithm performance analysis
- Manim city-style visualization

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
First, download the project and move into the folder:

git clone https://github.com/SayedGalibRezvi/AGV_Project.git
cd AGV_Project

### 2️⃣ Install Required Libraries

pip install -r requirements.txt

---

### 3️⃣ QR Scanner → City Animation Demo
Opens the webcam, waits for QR "A", then launches the Manim animation:

cd code
python scan_a_city.py

---

### 4️⃣ Compare Algorithms (A*, Dijkstra, BFS, DFS)
Runs 1000 trials and generates CSV files + comparison plots:

cd code
python compare_algorithms.py

---

### 5️⃣ Manual Path Planning Demo (Without QR)

cd code
python shortest_path_demo.py

---

### 6️⃣ Run Manim Animation Directly

cd code
manim -pqh -r 1920,1080 --fps 60 ../multi_algorithm_city_animation.py MultiRobotPaths

---

## 📁 Repository Structure

AGV_Project/
│
├── code/
│   ├── scan_a_city.py
│   ├── graph.py
│   ├── multi_algorithm_city_animation.py
│   ├── compare_algorithms.py
│   ├── shortest_path_demo.py
│   └── ...
│
├── flowcharts/
│   ├── 01_system_workflow.puml
│   ├── 02_qr_localization.puml
│   ├── 03_astar_path_planning.puml
│   └── exported_diagrams/
│
├── media/
│   ├── city.png
│   ├── robot.png
│   └── QR_xx.png
│
├── results/
│   ├── algorithm_metrics.csv
│   ├── execution_time_plot.png
│   └── algorithm_comparison.png
│
└── README.md

---

## ⚙️ System Workflow

1️⃣ QR Localization
- Live camera feed
- QR detection using OpenCV + Pyzbar
- QR string converted to a node ID

2️⃣ Path Planning
Weighted graph algorithms implemented:
- A* (main — optimal & efficient)
- Dijkstra
- BFS
- DFS

A* uses heuristics to find the best route quickly.

3️⃣ Visualization
- NetworkX + Matplotlib for algorithm comparisons
- Manim for animated city visualization

4️⃣ Evaluation Metrics
- Execution Time
- Path Cost
- Explored Nodes
- Path Length

---

## 📊 Key Evaluation Metrics

Metric | Meaning
------ | -------
Time | Time to compute the path
Cost | Sum of edge weights
Explored Nodes | Total visited nodes
Path Length | Number of nodes in the final path

---

## 📈 Results (1000-Run Average)

Algorithm | Time (s) | Cost | Path Length
--------- | -------- | ----- | -----------
A*        | 0.000022 | 20    | 5
Dijkstra  | 0.000017 | 23    | 5
DFS       | 0.000015 | 28    | 5
BFS       | 0.000025 | 29    | 5

Insight:
A* consistently produces the lowest-cost optimal path with strong runtime performance, making it ideal for real-time AGV navigation.

---

## 🎞 Visualization
The AGV visualization (created with Manim) shows:
- A city map
- Nodes and roads
- A robot icon moving along the A* path

---

## 📚 Technologies Used
- Python
- OpenCV + Pyzbar
- NetworkX
- Matplotlib
- Manim
- PlantUML

---

## 🧩 Future Improvements
- Real AGV motor integration
- Obstacle detection (LIDAR / vision)
- ROS / Gazebo simulation
- Multi-robot coordination
