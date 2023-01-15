"""Module to add graphic vision of dice throwing."""
from dice import Dice

# Create D6 dice
dice = Dice()

# Generating throw rows
results = []
for roll_num in range(5000):
    result = dice.roll()
    results.append(result)

frequencies = []
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
