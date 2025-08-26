# Create a list of strings that is at least ten strings long
#   List -> ["word1", "word2", ..., "word10"]
man = [ "spider", "aqua", "iron", "ant", "super", "catwo", "superwo", "batwo", "bat", "wonderwo" ]

# Use the map function to map the list of strings to the function and convert it to a list of lists
#    Output -> [["myword",6], ["word2",5] ...]
def length(s):
    return [s, len(s)]

count = list(map(length, man))

# Create a function that accepts a string parameter and returns a list including the string parameter and the length of that string
#    Output -> ["myword", 6]
print(f"Output -> {count}")

# Output the length of each string
#    Output -> 6, 5, ...
print(f"Output -> {count[0][1]}, {count[1][1]}, {count[2][1]}, {count[3][1]}, {count[4][1]}, {count[5][1]}, {count[6][1]}, {count[7][1]}, {count[8][1]}, {count[9][1]}")




