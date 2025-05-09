import matplotlib.pyplot as plt

# One arrow at (0, 0) pointing right (1, 0)
plt.quiver(0, 0, 1, 1, angles='xy', scale_units='xy', scale=1, color='r')

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.grid(True)
plt.title("Arrow pointing right")
plt.gca().set_aspect('equal')
plt.show()
