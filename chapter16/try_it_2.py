from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

plt.style.use('seaborn-v0_8') # Use the seaborn style for better visuals

path = Path('weather_data/sitka_weather_2021_full.csv') # Locate the file
lines = path.read_text().splitlines() # Reads the file and stores each line as an item in a list.

reader = csv.reader(lines)
header_row = next(reader) # Retrieve the first row of data from the CSV file.

dates, highs, lows = [], [], []
fig, ax = plt.subplots() # Create a figure and axis

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d') # Convert to datetime
    try:
        single_high = int(row[3])  
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)  
        highs.append(single_high)
        lows.append(low)

ax.plot(dates, highs, color='red', alpha=0.5)  
ax.plot(dates, lows, color='blue', alpha=0.5)

# Set titles and labels
title = "Daily High and Low Temperatures, 2021\nSitka, AK"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16) 
ax.tick_params(labelsize=16)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Set a common y-axis scale for comparison with Death Valley
ax.set_ylim(0, 130)  # Adjust the range based on Death Valley's extremes

plt.show()
