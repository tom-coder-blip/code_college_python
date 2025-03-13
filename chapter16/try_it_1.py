from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

plt.style.use('seaborn-v0_8') # Use the seaborn style for better visuals

path = Path('weather_data/sitka_weather_2021_full.csv') #locating the file
lines = path.read_text().splitlines() #reads the file and stores each line as an item in a list.


reader = csv.reader(lines) #read data from a CSV (Comma-Separated Values) file and convert it into a format that can be processed by Python
header_row = next(reader) # retrieve the first row of data from the CSV file.
dates, rainfall_amount = [], []
fig, ax = plt.subplots() # Create a figure and axis


for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d') #convert a string representing a date or time into a datetime object
    prcp = float(row[5]) 
    dates.append(current_date)  
    rainfall_amount.append(prcp)

print(rainfall_amount)

ax.plot(dates, rainfall_amount, color='red')

#setting titles an labels
ax.set_title("Rainfall amounts for 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() #automatically formats the x-axis date labels so that its more readable and understandable
ax.set_ylabel("Rainfall", fontsize=16) 
ax.tick_params(labelsize=16)

plt.show()
