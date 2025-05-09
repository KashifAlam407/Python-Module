import matplotlib.pyplot as plt

# Arrow from (0,0) pointing right 3 units and up 2 units
plt.quiver(0, 0, 3, 2, angles='xy', scale_units='xy', scale=1)

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.grid(True)
plt.title("Velocity Vector")
plt.xlabel("X")
plt.ylabel("Y")
plt.gca().set_aspect('equal')
plt.show()
