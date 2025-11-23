# 🤖 Vision-Based Node Localization & Path Planning for AGV Logistics

## 🧠 Overview
This project implements a **vision-based AGV (Automated Guided Vehicle)** navigation system that uses **QR codes for localization** and **graph algorithms for path planning**.

A camera detects physical QR codes representing nodes (A, B, C…), identifies the robot’s current location, and computes the **optimal path** to a destination using **A\***.  
Additional algorithms — **Dijkstra**, **BFS**, and **DFS** — are included to compare performance.

The system includes:
- 📸 QR-based localization  
- 🧭 Weighted graph path planning  
- 🚀 A\* for shortest path computation  
- 📊 Algorithm performance analysis  
- 🎞 Manim city-style visualization  

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SayedGalibRezvi/AGV_Project.git
cd AGV_Project
