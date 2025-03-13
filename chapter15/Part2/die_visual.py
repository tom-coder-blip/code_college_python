import plotly.express as px
from die import Die

#Create a D6 die
die = Die()

#Roll the die 1000 times and store results
results = []
for roll_num in range(1000):
    results.append(die.roll())

# print(results)


#Analyze the results
frequencies = []
poss_results = range(1, die.num_sides + 1) #possible values (1-6)

for value in poss_results: 
    frequency = results.count(value) #count occurences
    frequencies.append(frequency)

#Print the frequency of each number
print(frequencies)

# Visualize the results.
fig = px.bar(x=poss_results, y=frequencies)
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.show()  