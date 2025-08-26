import pandas

# Load this data into a Pandas dataframe:
temp = { "Day of week": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "Max Temp": [47, 44, 33, 34, 30, 29, 45], "Min Temp": [36, 30, 27, 30, 16, 12, 24] }
temperature = pandas.DataFrame(temp)

# Print the statistical data about this frame (mean, standard dev, min, max)
print(temperature.describe())

# Create another dataframe with this data:
precip = {"Day of week": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "Precip": [0.21, 0.01, 0.00, 0.01, 0.01, 0.00, 0.00], "New Snow": [0.0, 0.0, 0.0, 0.1, 0.3, 0.0, 0.0]}
precipetation = pandas.DataFrame(precip)

# Merge the two dataframes on the "Day of week" common identifier
df = pandas.merge(temperature, precipetation, on="Day of week")

# Print the new dataframe to the console
print(df)

# Set the index of the new dataframe to be on the "Day of week" column
df.set_index("Day of week", inplace=True)

# Convert the "Max Temp" and "Min Temp" columns to Celcius ((F -32)*5/9)
df["Max Temp"] = ((df["Max Temp"] - 32) * 5/9)
df["Min Temp"] = ((df["Min Temp"] - 32) * 5/9)

# Add an "Ave Temp" column which is the average of "Max Temp" and "Min Temp"
df["Ave Temp"] = ((df["Max Temp"] + df["Min Temp"]) / 2)

# Reindex the dataframe so the "Ave Temp" column is right after the "Min Temp" column
column = df.columns.tolist()
index = column.index("Min Temp") + 1
column.insert(index, column.pop(column.index("Ave Temp")))
df = df[column]

# Print the dataframe to the screen
print(df)
