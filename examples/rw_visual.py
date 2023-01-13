"""Graphic view of random walk."""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Creating of random walk object
    rw = RandomWalk()
    rw.fill_walk()

    # Set points on diagram
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Greens, edgecolors='none', s=1)

    # Enlight first and final point
    ax.scatter(0, 0, c='red', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='orange',
               edgecolors='none', s=100)

    # Remove axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
