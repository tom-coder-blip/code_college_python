# 2. Import Matplotlib and Create a Simple Line Plot
import matplotlib.pyplot as plt

# Define square numbers as data
# Define input values and corresponding square numbers
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Create a figure and axis
fig, ax = plt.subplots()
ax.plot(squares)

# Set chart title and label axes
ax.set_title("Corrected Square Numbers Plot", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

# Display the plot
plt.show()