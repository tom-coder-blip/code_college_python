# 15-8. Multiplication: When you roll two dice, you usually add the two numbers 
# together to get the result. Create a visualization that shows what happens if you 
# multiply these numbers by each other instead.

import plotly.express as px
from die import Die

# Create two D6 dice
die_1 = Die()
die_2 = Die()

# Roll the dice 1,000 times and store the multiplication results
results = []
for roll_num in range(1000):
    multiply_die = die_1.roll() * die_2.roll()
    results.append(multiply_die)

# Analyze the results
frequencies = []
poss_results = range(1, 37) 

for value in poss_results:
    frequency = results.count(value)  # count() just returns the amount of times each result occurred
    frequencies.append(frequency)

print(frequencies)

# Visualize the results
title = "Results of Multiplying Two D6 Dice 1,000 Times"
labels = {'x': 'Multiplication of Two D6 Dice', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.show()