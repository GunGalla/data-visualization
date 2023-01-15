"""Module to add graphic vision of dice throwing."""
from dice import Dice

# Create D6 dice
dice = Dice()

# Generating throw rows
results = []
for roll_num in range(100):
    result = dice.roll()
    results.append(result)

print(results)