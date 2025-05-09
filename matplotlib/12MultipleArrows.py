import matplotlib.pyplot as plt
import numpy as np

# Robot positions
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 1, 0, -1])

# Robot heading directions (unit vectors)
u = np.cos([0, 0.3, 0.6, 0.9, 1.2])
v = np.sin([0, 0.3, 0.6, 0.9, 1.2])

# Plot arrows
plt.quiver(x, y, u, v, angles='xy', scale_units='xy', scale=1, color='blue')

# Settings
plt.xlim(-1, 5)
plt.ylim(-2, 2)
plt.grid(True)
plt.title("Robot Heading Vectors")
plt.xlabel("X")
plt.ylabel("Y")
plt.gca().set_aspect('equal')
plt.show()
