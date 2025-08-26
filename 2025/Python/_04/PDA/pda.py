import pandas as pd

# Load dataset
df = pd.read_csv("ign.csv")

# Step 1: Create a frame with owners, positive_ratings, negative_ratings
ratings_by_owners = df[['owners', 'positive_ratings', 'negative_ratings']].copy()

# Group by owners and sum
grouped_by_owners = ratings_by_owners.groupby('owners').sum()

# Add percentage columns
grouped_by_owners['%_positive'] = grouped_by_owners['positive_ratings'] / (grouped_by_owners['positive_ratings'] + grouped_by_owners['negative_ratings'])
grouped_by_owners['%_negative'] = grouped_by_owners['negative_ratings'] / (grouped_by_owners['positive_ratings'] + grouped_by_owners['negative_ratings'])

# Sort by % positive reviews
grouped_by_owners_sorted = grouped_by_owners.sort_values(by='%_positive', ascending=False)

# Print the result
print("Grouped by owners:")
print(grouped_by_owners_sorted.head(10))


# Step 2: Find which publishers have the highest ratings
# Create a frame with publisher, positive, negative
ratings_by_publisher = df[['publisher', 'positive_ratings', 'negative_ratings']].copy()

# Group by publisher and sum
grouped_by_publisher = ratings_by_publisher.groupby('publisher').sum()

# Add % positive and % negative columns
grouped_by_publisher['%_positive'] = grouped_by_publisher['positive_ratings'] / (grouped_by_publisher['positive_ratings'] + grouped_by_publisher['negative_ratings'])
grouped_by_publisher['%_negative'] = grouped_by_publisher['negative_ratings'] / (grouped_by_publisher['positive_ratings'] + grouped_by_publisher['negative_ratings'])

# Sort by % positive
grouped_by_publisher_sorted = grouped_by_publisher.sort_values(by='%_positive', ascending=False)

# Print to show strange result (e.g., Dexion Games with only 1 rating)
print("\nGrouped by publisher (pre-filter):")
print(grouped_by_publisher_sorted.head(10))

# Dexion Games appears because we haven’t filtered for *total* ratings; the previous step only filtered out rows in the original df, not grouped sums.
# We now drop those publishers with fewer than 1000 positive ratings
filtered_publishers = grouped_by_publisher[grouped_by_publisher['positive_ratings'] >= 1000]

# Now filter out publishers with fewer than 5 games
games_per_publisher = df['publisher'].value_counts()
eligible_publishers = games_per_publisher[games_per_publisher >= 5].index
filtered_publishers = filtered_publishers[filtered_publishers.index.isin(eligible_publishers)]

# Sort again
filtered_sorted = filtered_publishers.sort_values(by='%_positive', ascending=False)

# Final result
print("\nFiltered publishers (at least 1000 positive ratings and 5+ games):")
print(filtered_sorted.head(10))
