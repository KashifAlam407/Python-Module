import matplotlib.pyplot as plt
import numpy as np

# Simulated robot trajectory
t = np.linspace(0, 2*np.pi, 20)
x = np.cos(t)
y = np.sin(t)

# Compute velocities (dx/dt and dy/dt)
u = -np.sin(t)  # derivative of cos
v = np.cos(t)   # derivative of sin

plt.plot(x, y, label="Trajectory")
plt.quiver(x, y, u, v, color='red', scale=20, label="Velocity Vectors")

plt.title("Robot Trajectory with Velocity Vectors")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
