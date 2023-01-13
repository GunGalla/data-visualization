"""Graphic view of random walk."""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Creating of random walk object
    rw = RandomWalk()
    rw.fill_walk()

    # Set points on diagram
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Greens, edgecolors='none', s=10)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
