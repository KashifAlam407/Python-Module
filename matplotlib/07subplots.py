import matplotlib.pyplot as plt

## create 2 rows and 1 columns of plots
plt.subplot(2, 1, 1) # 2 rows, 1 column, first plot (here If you want plots next to each other horizontally, you can change rows and columns:)
plt.plot([1, 2, 3], [4, 5, 6])  ## here instead of writing x and y we can directly pass the value of x and y
plt.title('Plot 1')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

plt.subplot(2, 1, 2) # 2 rows, 1 column, second plot
plt.plot([1, 2, 3], [6, 5, 4])
plt.title('Plot 2') 
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

plt.tight_layout() # Adjusts the padding between and around subplots.
plt.show() # Display the plots
# This code creates two subplots in a single figure, each with its own title, x-axis label, y-axis label, and grid lines. The `tight_layout()` function is used to automatically adjust the subplot parameters for better spacing.

