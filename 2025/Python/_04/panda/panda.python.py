import pandas

# Load data into Pandas dataframe using read_csv 
dataframe = pandas.read_csv("ign.csv")

# Print the shape of the DataFrame
print("Shape of the DataFrame - ", dataframe.shape)

# Remove the "Unnamed" column using iloc
dataframe = dataframe.drop(columns=[col for col in dataframe.columns if 'Unnamed' in col])

# Print the title, genre and release year columns using .loc
print(dataframe.loc[:, ['title', 'genre', 'release_year']])

# Print the mean, max, and standard deviation for the scores of the dataframe
print("Mean - ", dataframe['score'].mean())
print("Max - ", dataframe['score'].max())
print("Standard Deviation - ", dataframe['score'].std())

# Convert the scores column to 100 base by multiplying it by 10
dataframe['score'] = dataframe['score'] * 10

# Create a new dataframe that only includes the rows with a score above the mean score of the main dataframe (your new dataframe should have 11,373 rows)
mean = dataframe['score'].mean()
upper = dataframe[dataframe['score'] > mean]
print("Above-mean DataFrame shape:", upper.shape)

# Print a series that lists the count of scores by platform from the above mean dataframe sorted decending (PC should have 2191 for a count)
count = upper['platform'].value_counts()
print(count)