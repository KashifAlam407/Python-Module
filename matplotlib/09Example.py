import matplotlib.pyplot as plt
import numpy as np

# ----- Part 1: Simulate Robot Trajectory -----
t = np.linspace(0, 10, 100)
x = np.cos(t)        # X position over time
y = np.sin(t)        # Y position over time

# ----- Part 2: Simulate LIDAR around robot -----
angles = np.linspace(0, 2*np.pi, 360)
distances = np.random.uniform(1.0, 3.0, 360)
lidar_x = distances * np.cos(angles)
lidar_y = distances * np.sin(angles)

# ----- Plotting -----
fig, axs = plt.subplots(1, 2, figsize=(12, 5))  # 1 row, 2 columns

# Left plot: Robot Trajectory
axs[0].plot(x, y, color='blue')
axs[0].set_title("Robot Trajectory")
axs[0].set_xlabel("X (m)")
axs[0].set_ylabel("Y (m)")
axs[0].grid(True)
axs[0].axis('equal')

# Right plot: LIDAR Scan
axs[1].scatter(lidar_x, lidar_y, s=3, color='red', alpha=0.5)
axs[1].set_title("Simulated LIDAR Scan")
axs[1].set_xlabel("X (m)")
axs[1].set_ylabel("Y (m)")
axs[1].grid(True)
axs[1].axis('equal')

plt.tight_layout()
plt.show()
# This code simulates a robot's trajectory and a LIDAR scan around it, displaying both in a single figure with two subplots.
# The left subplot shows the robot's trajectory in blue, while the right subplot displays the simulated LIDAR scan in red.