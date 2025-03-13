import plotly.express as px
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

#Roll the die 100 times and store results
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# print(results)


#Analyze the results
frequencies = [] 
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)

for value in poss_results: 
    frequency = results.count(value) #count occurences
    frequencies.append(frequency)

#Print the frequency of each number
print(frequencies)

# Visualize the results.
fig = px.bar(x=poss_results, y=frequencies)
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.show()