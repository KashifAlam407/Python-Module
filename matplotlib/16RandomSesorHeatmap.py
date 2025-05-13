import matplotlib.pyplot as plt
import numpy as np

# Simulate random sensor readings
sensor_data = np.random.rand(10, 10)

plt.imshow(sensor_data, cmap='hot', interpolation='nearest')

plt.title("Sensor Heatmap")
plt.colorbar(label='Sensor Intensity')
plt.show()
