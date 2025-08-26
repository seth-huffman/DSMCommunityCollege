import re

# Using this passage:
passage = ( "I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain.” – Frank Herbert, Dune")

words = re.findall(r'\b\w+\b', passage)
containFCount = 0
startFCount = 0

for word in words:
# How many words contain the letter f (case insensitive)? ... This includes Frank 
    if 'f' in word.lower():
        containFCount += 1
# How many words start with the letter f (case insensitive)? ... This includes Frank
        if word.lower().startswith('f'):
            startFCount += 1

# How many times the word "not" appears (whole word only)?
notCount = len(re.findall(r'\bnot\b', passage))

# Update the passage to change every "I" word to "You", "my" to "your", and "me" to "you".
replacePassage = re.sub(r'\bI\b', 'You', passage)
replacePassage = re.sub(r'\bmy\b', 'your', replacePassage)
replacePassage = re.sub(r'\bme\b', 'you', replacePassage)

# Submit your answers to the first three items in a comment and submit your program file.
print(f"Containing F Count: {containFCount}") # 7
print(f"Starting with F Count: {startFCount}")  # 7
print(f"Not Count {notCount}") # 1
print(f"Updated passage: {replacePassage}")