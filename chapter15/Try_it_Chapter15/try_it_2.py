# 15-2. Colored Cubes: Apply a colormap to your cubes plot

import matplotlib.pyplot as plt

# Generate data for cubes
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Use a colormap for styling
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, s=10)

# Set chart title and label axes
ax.set_title("Colored Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

# Set the range for each axis
ax.ticklabel_format(style='plain')

# Show the plot
plt.show()