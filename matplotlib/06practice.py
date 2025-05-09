import matplotlib.pyplot as plt

x = [0, 2, 4, 5, 7]
y = [0, 1, 4, 8, 10]

# plt.plot(x,y) # This line connects the dots with lines
plt.scatter(x,y) # This line plots the points without connecting them

plt.title("Path of the robot that moves")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)  # Add background grid to the graph

plt.show()  # Display the graph window