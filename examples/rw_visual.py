"""Graphic view of random walk."""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Creating of random walk object
rw = RandomWalk()
rw.fill_walk()

# Set points on diagram
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=10)
plt.show()
