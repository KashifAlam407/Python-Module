import matplotlib.pyplot as plt
import numpy as np

# Simulating 360-degree LIDAR
# This line creates a NumPy array called angles that contains 360 equally spaced values starting at 0 and ending at 2π radians (which is the same as 360 degrees — a full circle).
angles = np.linspace(0, 2*np.pi, 360)  ##np.linspace(start, stop, num)
# print(angles)
distances = np.random.uniform(1.0, 5.0, 360)   ## np.random.uniform(low, high, size)
# print(distances)

# Converting polar to cartesian coordinates
x = distances * np.cos(angles)
y = distances * np.sin(angles)

# Scatter plot
plt.scatter(x, y, s=5)  # s is the size of dots
plt.plot(x, y, color='gray', alpha=0.5)  # Optional: connect points with lines
plt.title('Simulated LIDAR Point Cloud')
plt.xlabel('X Distance (m)')
plt.ylabel('Y Distance (m)')
plt.axis('equal')   # make X and Y scale equal
plt.grid(True)
plt.show()
