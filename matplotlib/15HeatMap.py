import matplotlib.pyplot as plt
import numpy as np

grid = np.array([[0, 0, 1, 1],
                 [0, 1, 1, 0],
                 [0, 0, 0, 0],
                 [1, 1, 0, 0]])

plt.imshow(grid, cmap='hot', interpolation='nearest')
plt.title("Occupancy Probability")
plt.colorbar(label='Occupancy Probability')
plt.show()

