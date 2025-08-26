import numpy

# Create a 1-dimensional NumPy array with the numbers 1-36 in it (use np.arange for an easy way to do this)
array = numpy.arange(1, 37)

# Shuffle the array (use np.random.shuffle)
numpy.random.shuffle(array)

# Reshape the array to 6x6
reshaped = array.reshape(6, 6)

# You now need to get the positive diagonal numbers into a new array by multiplying your dealt cards array by an identity matrix
identity = numpy.eye(6, dtype=int)
positiveNum = reshaped * identity

# You now have to flip the numbers that are not on the diagonal to negative:
    # You need to create a 6x6 identity matrix and subtract a 6x6 array of all 1s from it.  You should end up with an array that is zeros on the diagonal and -1s everywhere else
    # Create a new array by multiplying your array of negative 1s and your array of dealt cards.  You should end up with an array that is 0s on the diagonal and negative numbers elsewhere.
negMatrix = numpy.ones((6, 6), dtype=int) - identity
negMatrix *= -1
negativeNum = reshaped * negMatrix

# Using your array of positive numbers and your array of negative numbers, combine them into a new array of all the dealt cards.  It should now have the correct sign on all dealt cards
dealtCards = positiveNum + negativeNum

# create a 6x1 array by summing all the rows of this array.  This new array is your player score
score = numpy.sum(dealtCards, axis=1)

# Determine the maximum score and which player got that score(np.max and np.argmax)
winner = numpy.argmax(score)
maxSocre = score[winner]

# Print the winner and their score (don't forget that the array position is zero indexed.  I don't want player 0 to win)
print(f"Player - {winner + 1}")
print(f"Score - {maxSocre}!")
