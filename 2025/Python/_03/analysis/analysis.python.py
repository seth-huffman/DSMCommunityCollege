def moby():
    # Using the "Moby_Dick_Chapter_1".txt file used in the example
    print("----------------- Moby_Dick_Chapter_1.txt -----------------")
    with open("Moby_Dick_Chapter_1.txt") as file:
        txt = file.read()
    txt = txt.lower()

    # Determine how many times the world "old" appears in the passage
    old = txt.count("old")
    print("How many times the world 'old' appears in the passage - ", old)

    # Determine how many times "water" appear in the passage
    water = txt.count("water")
    print("how many times 'water' appear in the passage - ", water)

    # Determine the average sentence length in the passage (splitting on periods will suffice)
    sentence = txt.count(".")
    words = txt.split()
    word = len(words)
    average = word / sentence
    print("Average sentence length in the passage - ", average)

#############
# REPEAT
#############
def sense():
    # Now do the same things with chapter 1 in Sense_and_Sensibility_Chapter_1.txt
    print("----------------- Sense_and_Sensibility_Chapter_1.txt -----------------")
    with open("Sense_and_Sensibility_Chapter_1.txt") as file:
        txt = file.read()
    txt = txt.lower()

    # Determine how many times the world "old" appears in the passage
    old = txt.count("old")
    print("How many times the world 'old' appears in the passage - ", old)

    # Determine how many times "water" appear in the passage
    water = txt.count("water")
    print("how many times 'water' appear in the passage - ", water)

    # Determine the average sentence length in the passage (splitting on periods will suffice)
    sentence = txt.count(".")
    words = txt.split()
    word = len(words)
    average = word / sentence
    print("Average sentence length in the passage - ", average)

moby()
sense()


#############
# REPEAT
#############

# What does this scraped information tell you about these two passages?
# - Old: Moby Dick has more mentions of old
# - Water: Moby Dick has more mentions of water
# - Average: Both passages have the same (roughly) sentence average length.

# What other interesting things can be done to find out information on these two passages?
# - How long each paragraph is
# - Biggest word in each passage
# - How longeach passage was