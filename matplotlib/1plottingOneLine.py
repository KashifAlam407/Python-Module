import matplotlib.pyplot as plt

# Data: x and y positions
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 3, 4, 5]

# Create a line plot with x and y points.
plt.plot(x,y)

# Adding title to the graph.
plt.title("Line Plot")

# Adding label to the graph.
plt.xlabel("X-position")
plt.ylabel("Y-position")

# Adding grid to the graph.
plt.grid(True)

# Display the graph window.
plt.show()
