import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Sample data for streaming services popularity (number of subscribers in millions)
streaming_data = {
    'Netflix': 200,
    'Amazon Prime': 200,
    'Disney+': 153.6,
    'HBO Max': 77,
    'Apple TV+': 25,
    'Paramount+': 32,
    'Showmax': 1.7,
    'Crunchyroll': 50,
    'Youtube Premium': 125
}

# Company colors for gradients
company_colors = {
    'Netflix': ['#e50914', '#000000'],  # Red to Black
    'Amazon Prime': ['#000000', '#00a8e1'],  # Black to Blue
    'Disney+': ['#113ccf', '#00a8e1'],  # Dark Blue to Light Blue
    'HBO Max': ['#1f1f1f', '#a6a6a6'],  # Dark Gray to Light Gray
    'Apple TV+': ['#000000', '#a6a6a6'],  # Black to Light Gray
    'Paramount+': ['#0060a9', '#00a8e1'],  # Dark Blue to Light Blue
    'Showmax': ['#ff007f', '#000000'],  # Pink to Black
    'Crunchyroll': ['#f47521', '#ffcc00'],  # Orange to Yellow
    'Youtube Premium': ['#ff0000', '#282828']  # Red to Dark Gray
}

# Create figure and axis with more height and adjusted margins
fig, ax = plt.subplots(figsize=(12, 8))  
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)  
ax.set_facecolor('#3b3b3b')

# Histogram bins
x = np.arange(len(streaming_data))
heights = list(streaming_data.values())

# Plot bars with transparent color
bars = ax.bar(x, heights, color='none', edgecolor='black', linewidth=1)

colors = ['red', 'blue', 'green', 'purple', 'orange', 'yellow', 'cyan', 'magenta', 'pink']
for bar, height, color in zip(bars, heights, colors):
    ax.text(bar.get_x() + bar.get_width()/2, height + 2, f'{height}', 
            ha='center', va='bottom', fontsize=10, fontweight='bold', color=color)  # 🎨 Dynamic color

# Generate a gradient image for each bar
for bar, height, service in zip(bars, heights, streaming_data.keys()):
    left, right = bar.get_x(), bar.get_x() + bar.get_width()
    bottom, top = 0, height

    # Create a 1D vertical gradient
    gradient = np.linspace(0, 1, 256).reshape(-1, 1)
    cmap = cm.colors.LinearSegmentedColormap.from_list(service, company_colors[service])
    gradient = cmap(gradient)
    gradient = gradient[:, :, :3]

    # Overlay the gradient image onto the bar
    ax.imshow(gradient, extent=[left, right, bottom, top], aspect='auto', alpha=0.9, origin='lower')

# Customize the plot
ax.set_title('Streaming Services Popularity', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Streaming Service')
ax.set_ylabel('Subscribers (Millions)')
ax.set_xticks(x)
ax.set_xticklabels(streaming_data.keys(), rotation=45, ha='right')

# Set y-axis limits with some padding
max_height = max(heights)
ax.set_ylim(0, max_height * 1.1)  # Add 10% padding at the top

# Set x-axis limits with some padding
ax.set_xlim(-0.5, len(streaming_data) - 0.5)



# Show the plot
plt.show()