#  15-3. Molecular Motion: Modify rw_visual.py by replacing ax.scatter() with 
# ax.plot(). To simulate the path of a pollen grain on the surface of a drop of 
# water, pass in the rw.x_values and rw.y_values, and include a linewidth argu
# ment. Use 5,000 instead of 50,000 points to keep the plot from being too busy.

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Generate a random walk with 5000 points (instead of 50,000)
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the walk path with a line instead of scatter points
    ax.plot(rw.x_values, rw.y_values, linewidth=1, color='blue')

    # Emphasize the starting and ending points
    ax.scatter(0, 0, c='green', edgecolors='black', s=100, label="Start")
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='black', s=100, label="End")

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Show the plot
    plt.legend()
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break