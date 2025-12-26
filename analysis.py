

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Create Sample Dataset
# -----------------------------
np.random.seed(42)

signals = ["Signal_A", "Signal_B", "Signal_C", "Signal_D", "Signal_E"]
hours = list(range(24))

data = []

for signal in signals:
    for hour in hours:
        # Simulate higher waiting times during peak hours
        if 8 <= hour <= 10 or 17 <= hour <= 19:
            waiting_time = np.random.randint(60, 180)
        else:
            waiting_time = np.random.randint(20, 90)

        data.append([signal, hour, waiting_time])

df = pd.DataFrame(data, columns=["Signal", "Hour", "Waiting_Time_Seconds"])

# -----------------------------
# 2. Descriptive Statistics
# -----------------------------
print("\n===== Descriptive Statistics =====")
print(df["Waiting_Time_Seconds"].describe())

print("\n===== Average Waiting Time per Signal =====")
print(df.groupby("Signal")["Waiting_Time_Seconds"].mean())

print("\n===== Average Waiting Time per Hour =====")
print(df.groupby("Hour")["Waiting_Time_Seconds"].mean())

# -----------------------------
# 3. Line Plot – Congestion Trend Over Time
# -----------------------------
plt.figure()
for signal in signals:
    signal_data = df[df["Signal"] == signal]
    plt.plot(signal_data["Hour"], signal_data["Waiting_Time_Seconds"], label=signal)

plt.xlabel("Hour of Day")
plt.ylabel("Waiting Time (seconds)")
plt.title("Traffic Signal Waiting Time Trend by Hour")
plt.legend()
plt.show()

# -----------------------------
# 4. Heatmap – Congestion Intensity
# -----------------------------
pivot_table = df.pivot(index="Signal", columns="Hour", values="Waiting_Time_Seconds")

plt.figure()
sns.heatmap(pivot_table, annot=False)
plt.title("Heatmap of Traffic Signal Waiting Times")
plt.xlabel("Hour of Day")
plt.ylabel("Traffic Signal")
plt.show()

# -----------------------------
# 5. Congestion Insights
# -----------------------------
peak_hours = df.groupby("Hour")["Waiting_Time_Seconds"].mean().idxmax()
most_congested_signal = df.groupby("Signal")["Waiting_Time_Seconds"].mean().idxmax()

print("\n===== Congestion Insights =====")
print(f"Peak congestion hour: {peak_hours}:00")
print(f"Most congested signal overall: {most_congested_signal}")
