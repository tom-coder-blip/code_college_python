# # 15-7. Three Dice: When you roll three D6 dice, the smallest number you can roll 
# is 3 and the largest number is 18. Create a visualization that shows what hap
# pens when you roll three D6 dice.

import plotly.express as px
from die import Die

# Create three D6 dice
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Roll the three dice 1,000 times and store the sums
results = []
for roll_num in range(1000):
    sum_of_dice = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(sum_of_dice) 

# Analyze the results
frequencies = [] 
poss_results = range(3, 19) 

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Print the frequency of each sum
print(frequencies)

# Visualize the results
title = "Results of Rolling Three D6 Dice 1,000 Times"
labels = {'x': 'Sum of Three D6 Dice', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.show()

