"""Scatter squares visualization module."""
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-bright')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Diagram and axis titles
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set axis font
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()