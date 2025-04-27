import matplotlib.pyplot as plt

# Robot 1 path
x1 = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 2, 3, 4, 5]     

# Robot 2 path
x2 = [0, 1, 2, 3, 4, 5]
y2 = [0, 1.5, 2.5, 2.5, 1.5, 0]

plt.plot(x1, y1, label='Robot 1', color='blue', linestyle='-', marker='o')
plt.plot(x2, y2, label='Robot 2', color='red', linestyle='--', marker='x')  

plt.title("Comparison of Robot Paths")
plt.xlabel("X-position")    
plt.ylabel("Y-position")
plt.legend()  # Show the names of the line in the plot
plt.grid(True)  # Add background grid to the graph 

plt.show()  # Display the graph window
