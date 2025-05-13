import numpy as np
import matplotlib.pyplot as plt

cost_map = np.zeros((10, 10))
cost_map[3:6, 3:6] = 1  # Obstacle area
cost_map[7, :] = 0.5 # High cost area

plt.imshow(cost_map)
plt.title("Navigation Cost Map")
plt.colorbar(label='Cost')
plt.grid(False)
plt.show()