import matplotlib.pyplot as plt

# Data for Pie Chart
labels = ['Python', 'JavaScript', 'Html', 'Css']
sizes = [40, 20, 20, 20]  # Values representing the percentage of each category
colors = ['blue', 'red', 'green', 'purple']  # Custom colors for better visualization

# Create Pie Chart
plt.figure(figsize=(6,6))  # Set figure size
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)

# Add Title
plt.title('Favourite Languages')

# Show Pie Chart
plt.show()


