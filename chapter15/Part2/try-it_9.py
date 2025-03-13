#  15-9. Die Comprehensions: For clarity, the listings in this section use the long 
# form of for loops. If you’re comfortable using list comprehensions, try writing a 
# comprehension for one or both of the loops in each of these programs.

import plotly.express as px
from die import Die

# Create two D6 dice
die_1 = Die() 
die_2 = Die()  

# Roll the dice 1,000 times and store the product in list comprehension
results = [die_1.roll() * die_2.roll() for _ in range(1000)]

# Analyze the results
poss_results = range(1, 37)
frequencies = [results.count(value) for value in poss_results]

print(frequencies)

# Visualize the results
title = "Results of Multiplying Two D6 Dice 1,000 Times"
labels = {'x': 'Multiplication of Two D6 Dice', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.show()


