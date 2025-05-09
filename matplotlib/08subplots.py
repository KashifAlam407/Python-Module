import matplotlib.pyplot as plt

fig, axs = plt.subplots(3)  # 3 subplots vertically
### fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 8)) # 2 rows, 2 columns of subplots
### fig, axs = plt.subplots(2, 2, figsize=(10, 8)) # 2 rows, 2 columns of subplots

axs[0].plot([0, 1, 2], [0, 1, 4])
axs[0].set_title('Robot Trajectory')

axs[1].plot([0, 1, 2], [0, -1, -4])
axs[1].set_title('Robot Velocity')

axs[2].plot([0, 1, 2], [0, -1, -4])
axs[2].set_title('Robot Acceleration')


plt.tight_layout()
plt.show()
