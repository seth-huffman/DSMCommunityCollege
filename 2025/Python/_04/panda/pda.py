import pandas

database = pandas.read_csv("ign.csv")

# Create a frame from your original dataset that includes owners positive ratings and negative ratings
ratings_frame = database[['platform', 'score']]

# Group the frame by owners
owners = ratings_frame.groupby('platform')

# Sum the owners frame
sum = owners.agg(['mean', 'count'])

# print the owners summed frame
print(sum)

# add a column to your owners summed frame showing the % of positive reviews (pos reviews/(neg reviews+pos reviews))
database['is_positive'] = database['score'] >= 75
database['is_negative'] = database['score'] < 75

# Recreate owners sums
owners_pos_neg = database.groupby('platform')[['is_positive', 'is_negative']].sum()#####

# add a column that does the same for % of negative reviews
owners_pos_neg['% positive'] = owners_pos_neg['is_positive'] / (owners_pos_neg['is_positive'] + owners_pos_neg['is_negative']) * 100
owners_pos_neg['% negative'] = owners_pos_neg['is_negative'] / (owners_pos_neg['is_positive'] + owners_pos_neg['is_negative']) * 100

# print the output
print(owners_pos_neg.sort_values('% positive', ascending=False))

# Sort the frame descending by % positive ratings
sorted_by_positive = owners_pos_neg.sort_values('% positive', ascending=False)
print(sorted_by_positive)

# Create a frame that has publisher positive_ratings negative ratings
genre_frame = database[['genre', 'is_positive', 'is_negative']]

# Group by publisher
owners_genre = genre_frame.groupby('genre').sum()


# add in the % positive and % negative reviews
owners_genre['% positive'] = owners_genre['is_positive'] / (owners_genre['is_positive'] + owners_genre['is_negative']) * 100
owners_genre['% negative'] = owners_genre['is_negative'] / (owners_genre['is_positive'] + owners_genre['is_negative']) * 100

# Sort the frame decending by % positive reviews
sorted_genre = owners_genre.sort_values('% positive', ascending=False)

# print the owners summed frame
print(sorted_genre)

# Add total ratings column
# owners_genre['total'] = owners_genre['is_positive'] + owners_genre['is_negative']

# Let's drop any rows that don't have at least 1000 positive ratings
filtered_genre = owners_genre[owners_genre['is_positive'] >= 1000]

# Now Wube Software is the winner...but they only have 1 game (and everyone loves it).  I want to see how publishers do overall so let's drop any publisher that doesn't have at least 5 games listed
genre_counts = database['genre'].value_counts()
valid_genres = genre_counts[genre_counts >= 5].index
final_genre_database = filtered_genre[filtered_genre.index.isin(valid_genres)]

# print your final dataframe with Nicalis Inc. as the highest rated publisher
print(final_genre_database.sort_values('% positive', ascending=False).head())
