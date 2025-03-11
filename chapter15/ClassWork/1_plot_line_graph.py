# 1. Install Matplotlib
# Open a terminal and run the following command:
# $ python -m pip install --user matplotlib

# 2. Import Matplotlib and Create a Simple Line Plot
import matplotlib.pyplot as plt

# Define square numbers as data
squares = [1, 4, 9, 16, 25]

# Create a figure and axis
fig, ax = plt.subplots()
ax.plot(squares)

# Display the plot
plt.show()
