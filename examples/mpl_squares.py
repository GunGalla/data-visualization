#!/usr/bin/env python3
"""Square visualization."""
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares)


def main():
    """Start the visualization"""
    plt.show()


if __name__ == '__main__':
    main()
