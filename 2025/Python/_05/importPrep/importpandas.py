import pandas
  
# Load the dataset into a Pandas dataframe (please put the file in the same directory as your program when importing for grading simplicity)
dataframe = pandas.read_csv("steam.csv")

# Create a temp frame that is tempframe by publisher and summed
tempframe = dataframe.groupby("publisher")[["positive_ratings"]].sum()

# From this tempframe frame create a list of rows that need to be deleted based on having less than 50 positive ratings
fiftyless = tempframe[tempframe["positive_ratings"] < 50].index.tolist()

# Using your list of publishers to delete and your original dataframe, create a new dataframe that has the publishers with at least 50 ratings
pubfiftyless = dataframe[~dataframe["publisher"].isin(fiftyless)]

# Sort your new dataframe descending on positive ratings. Your top name should be "Counter-Strike: Global Offensive"
pubfiftyless = pubfiftyless.sort_values(by="positive_ratings", ascending=False)

# Do a describe on the frame to see some quick stats on it
print(pubfiftyless.describe(include='all'))

# Remove the appid column using iloc because we don't need it
removeappid = pubfiftyless.columns.get_loc("appid")
pubfiftyless = pubfiftyless.drop(pubfiftyless.columns[removeappid], axis=1)

# Remove any rows for games that have less than 20000 owners
def extract_low_owner(owner):
    try:
        return int(owner.replace(',', '').split(' - ')[0])
    except:
        return 0

pubfiftyless["min_owners"] = pubfiftyless["owners"].apply(extract_low_owner)
pubfiftyless = pubfiftyless[pubfiftyless["min_owners"] >= 20000]

print(pubfiftyless.head())
