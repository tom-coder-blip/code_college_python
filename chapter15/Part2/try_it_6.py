# #15-6. Two D8s: Create a simulation showing what happens when you roll two 
# eight-sided dice 1,000 times. Try to picture what you think the visualization will 
# look like before you run the simulation, then see if your intuition was correct. 
# Gradually increase the number of rolls until you start to see the limits of your 
# system’s capabilities.

import plotly.express as px
from die import Die

die_1 = Die(8)
die_2 = Die(8)


results = []
for roll_num in range(1000):
    sum_of_dice = die_1.roll() + die_2.roll()
    results.append(sum_of_dice)

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides  

frequencies = []
poss_results = range(2, max_result + 1) 

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)


title = "Results of Rolling Two D8 Dice 1,000 Times"
labels = {'x': 'Sum of Dice', 'y': 'Frequency'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()