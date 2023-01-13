"""Random walk model."""
from random import choice


class RandomWalk:
    """Random walk generator."""

    def __init__(self, num_points=5000):
        """Initialize walking attributes."""
        self.num_points = num_points

        # Start point is (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculating all walking points."""

        # Steps generating until reach max length
        while len(self.x_values) < self.num_points:
            # Choice of direction and distance of a step
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # No movement both params is 0
            if x_step == 0 and y_step == 0:
                continue

            # Calculating new values of x and y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
