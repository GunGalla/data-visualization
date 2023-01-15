"""Module to add graphic vision of double dice throwing."""
from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice

# Create D6 dice
dice_1 = Dice()
dice_2 = Dice()

# Generating throw rows
results = []
for roll_num in range(5000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualization result
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dices 5000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='double_d6.html')
