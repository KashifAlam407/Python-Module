import matplotlib.pyplot as plt

# X and Y coordinates of points
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

# Scatter plot
plt.scatter(x, y) # plot individual dots without connnecting them.

plt.title('Simple Scatter Plot') # Title of the plot
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.show()
