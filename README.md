# 🤖 Vision-Based Node Localization & Path Planning for AGV Logistics

## 🧠 Overview
This project implements a **vision-based AGV (Automated Guided Vehicle)** navigation system that uses **QR codes for localization** and **graph algorithms for path planning**.

A camera detects physical QR codes representing nodes (A, B, C…), identifies the robot’s current location, and computes the **optimal path** to a destination using **A\***.  
Additional algorithms — **Dijkstra**, **BFS**, and **DFS** — are included for comparison.

The system includes:
- 📸 QR-based localization  
- 🧭 Weighted graph path planning  
- 🚀 A\* for shortest path computation  
- 📊 Algorithm performance analysis  
- 🎞 Manim city-style visualization  

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
First, download the project and move into the folder:

```bash
git clone https://github.com/SayedGalibRezvi/AGV_Project.git
cd AGV_Project
pip install -r requirements.txt
cd code
python scan_a_city.py
cd code
python compare_algorithms.py
cd code
python shortest_path_demo.py
cd code
manim -pqh -r 1920,1080 --fps 60 ../multi_algorithm_city_animation.py MultiRobotPaths
AGV_Project/
│
├── code/                 # Python scripts (QR scanner, algorithms, animations)
│   ├── scan_a_city.py
│   ├── graph.py
│   ├── multi_algorithm_city_animation.py
│   ├── compare_algorithms.py
│   ├── shortest_path_demo.py
│   └── ...
│
├── flowcharts/           # PlantUML source + PNG diagrams
│   ├── 01_system_workflow.puml
│   ├── 02_qr_localization.puml
│   ├── 03_astar_path_planning.puml
│   └── exported_diagrams/
│
├── media/                # City map, robot icon, QR images
│   ├── city.png
│   ├── robot.png
│   └── QR_xx.png
│
├── results/              # CSV outputs + comparison plots
│   ├── algorithm_metrics.csv
│   ├── execution_time_plot.png
│   └── algorithm_comparison.png
│
└── README.md
⚙️ System Workflow
1️⃣ QR Localization

Live camera feed

QR detection using OpenCV + Pyzbar

QR string converted to node ID

2️⃣ Path Planning

A weighted graph represents all nodes and travel costs.
Algorithms implemented:

⭐ A* (main algorithm — optimal + efficient)

Dijkstra

BFS

DFS

A* uses heuristics to find the best route quickly.

3️⃣ Visualization

NetworkX + Matplotlib for algorithm comparisons

Manim for animated city visualization

4️⃣ Evaluation

System measures:

⏱ Execution Time

💰 Path Cost

🔁 Nodes Explored

🧩 Path Length

📊 Key Evaluation Metrics
Metric	Meaning
Time	Time needed to compute the path
Cost	Sum of edge weights along the chosen route
Explored Nodes	Nodes visited during computation
Path Length	Number of nodes in the final path
📈 Results (1000-Run Average)
Algorithm	Time (s)	Cost	Path Length
A*	0.000022	20	5
Dijkstra	0.000017	23	5
DFS	0.000015	28	5
BFS	0.000025	29	5
✅ Insight

A* consistently produces the lowest-cost optimal path while maintaining competitive runtime — making it the most suitable algorithm for real-time AGV navigation.

🎞 Visualization

The AGV visualization (created with Manim) shows:

A city map

Nodes and connections

A robot icon smoothly moving along the A* path

This provides a clear, intuitive understanding of the robot’s navigation.

📚 Technologies Used

Python

OpenCV + Pyzbar

NetworkX

Matplotlib

Manim

PlantUML

🧩 Future Improvements

Integrating real AGV motor control

Adding obstacle detection (LIDAR / vision)

ROS / Gazebo simulation

Multi-robot traffic coordinat
