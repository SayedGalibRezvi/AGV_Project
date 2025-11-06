import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("algorithm_average_metrics.csv")
print("\n📈 Loaded Evaluation Metrics:\n")
print(df)

# ------------------------------------------------------------
# Plot 1: Execution Time Comparison
# ------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.bar(df["Algorithm"], df["Average Time (s)"], color=["red", "blue", "green", "orange"])
plt.title("Execution Time Comparison", fontsize=14, fontweight="bold")
plt.xlabel("Algorithm")
plt.ylabel("Average Time (seconds)")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("execution_time_comparison_avg.png", dpi=300)
plt.show()

# ------------------------------------------------------------
# Plot 2: Path Length vs Total Cost
# ------------------------------------------------------------
plt.figure(figsize=(8, 5))
bar_width = 0.35
x = np.arange(len(df["Algorithm"]))
plt.bar(x - bar_width/2, df["Path Length"], bar_width, label="Path Length", color="cyan")
plt.bar(x + bar_width/2, df["Total Cost"], bar_width, label="Total Cost", color="magenta")
plt.xticks(x, df["Algorithm"])
plt.title("Path Length vs Total Cost", fontsize=14, fontweight="bold")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("path_vs_cost_avg.png", dpi=300)
plt.show()


# ------------------------------------------------------------
# Plot 3: Radar Chart for Multi-Metric Comparison
# ------------------------------------------------------------
from math import pi

# Normalize metrics for better visual comparison
metrics = ["Execution Time (s)", "Path Length", "Total Cost", "Explored Nodes"]
values = df[metrics].copy()
values = (values - values.min()) / (values.max() - values.min())

angles = np.linspace(0, 2*np.pi, len(metrics), endpoint=False).tolist()
angles += angles[:1]  # close loop

plt.figure(figsize=(7, 7))
for i, row in df.iterrows():
    stats = values.iloc[i].tolist()
    stats += stats[:1]
    plt.polar(angles, stats, label=row["Algorithm"], linewidth=2)
plt.xticks(angles[:-1], metrics)
plt.title("Algorithm Performance Radar", fontsize=14, fontweight="bold")
plt.legend(loc="upper right", bbox_to_anchor=(1.2, 1))
plt.tight_layout()
plt.savefig("radar_comparison.png", dpi=300)
plt.show()
