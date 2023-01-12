"""Square visualization."""
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares)

if __name__ == '__main__':
    plt.show()