# Import Matplotlib and Create a Simple Line Plot
import matplotlib.pyplot as plt

# Define input values and corresponding square numbers
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# Apply a built-in style to the plot
plt.style.use('seaborn-v0_8')

# Create a figure and axis
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)  #use scatter graph

# Set chart title and label axes
ax.set_title("Corrected Square Numbers Plot", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

# Display the plot
plt.show()