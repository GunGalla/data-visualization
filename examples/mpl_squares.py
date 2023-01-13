#!/usr/bin/env python3
"""Square visualization."""
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Diagram and axis titles
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set axis font
ax.tick_params(axis='both', labelsize=14)


def main():
    """Start the visualization"""
    plt.show()


if __name__ == '__main__':
    main()
