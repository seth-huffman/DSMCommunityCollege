import pandas
import matplotlib.pyplot

# Find a weather dataset for two different climates (Alaska vs. Cancun for instance) for a time frame of at least 30 days
sanDeigo = pandas.read_csv('sanDeigo.csv')
amsterdam = pandas.read_csv('amsterdam.csv')


# Create a simple visual from each of your datasets using PyPlot plots
matplotlib.pyplot.plot(sanDeigo['Date'], sanDeigo['Temperature'])
matplotlib.pyplot.title('San Deigo')
matplotlib.pyplot.xlabel('Date')
matplotlib.pyplot.ylabel('Temp')
matplotlib.pyplot.show()

matplotlib.pyplot.plot(amsterdam['Date'], amsterdam['Temperature'])
matplotlib.pyplot.title('Amsterdam')
matplotlib.pyplot.xlabel('Date')
matplotlib.pyplot.ylabel('Temp')
matplotlib.pyplot.show()

# Explain what your visuals demonstrate.
# This will display on the first plot a visual of san deigos weather that day.
# The second plot will be amsterdam on its weather/day 

# Create a more complex visual from your dataset (like showing rainfall, variance over time frame, etc.) using PyPlot plots. 
#   You must utilize subplots (or have two or more plots on the same figure if you prefer) so you can compare the two climates
fig, grid = matplotlib.pyplot.subplots(2, 1, figsize=(10, 5))

# This needs to include multiple options like color, line weight
grid[0].plot(sanDeigo['Date'], sanDeigo['Temperature'], color='red', linewidth=2)
grid[0].bar(sanDeigo['Date'], sanDeigo['Rainfall'], color='tomato')
grid[0].set_title('San Deigo')
grid[1].set_ylabel('Temp - Rain')

grid[1].plot(amsterdam['Date'], amsterdam['Temperature'], color='green', linewidth=2)
grid[1].bar(amsterdam['Date'], amsterdam['Rainfall'], color='DarkGreen')
grid[1].set_title('Amsterdam')
grid[1].set_xlabel('Date')
grid[1].set_ylabel('Temp - Rain')
matplotlib.pyplot.show()

# Explain what your more complex visual demonstrates and why it required a more complex visual
# I've created two plots on one popup showing the rainfall, temp and date of each place
