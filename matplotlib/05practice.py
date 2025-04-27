import matplotlib.pyplot as plt
import numpy as np

# Generate 20 random X and Y coordinates between -10 and +10
# It generates an array of 20 random floating-point numbers, where each number is between -10 and +10.
x = np.random.uniform(-10, 10, 20)
y = np.random.uniform(-10, 10, 20)

# Plot the points
plt.scatter(x, y, color='blue', alpha=0.5)
plt.plot(x, y, color='gray', alpha=0.5)  # Optional: connect points with lines

# Add title and grid
plt.title('20 Random Points in 2D Space')
plt.grid(True)

# Label axes (optional, but helpful)
plt.xlabel('X')
plt.ylabel('Y')

# Equal aspect ratio
plt.axis('equal')

# Show plot
plt.show()
