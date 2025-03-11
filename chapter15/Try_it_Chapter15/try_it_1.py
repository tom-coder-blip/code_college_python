# #15-1. Cubes: A number raised to the third power is a cube. Plot the first five 
# cubic numbers, and then plot the first 5,000 cubic numbers.

import matplotlib.pyplot as plt

# # First 5 cubic numbers
# x_values_small = [1, 2, 3, 4, 5]
# y_values_small = [x**3 for x in x_values_small]

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values_small, y_values_small, c='red', s=100)

# # Set chart title and label axes.
# ax.set_title("First 5 Cubic Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Cube of Value", fontsize=14)

# # Set size of tick labels.
# ax.tick_params(labelsize=14)

# plt.show()


# First 5,000 cubic numbers
x_values_large = range(1, 5001)
y_values_large = [x**3 for x in x_values_large]

fig, ax = plt.subplots()
ax.scatter(x_values_large, y_values_large, c='red', s=10)

# Set chart title and label axes.
ax.set_title("First 5,000 Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.ticklabel_format(style='plain')

plt.show()