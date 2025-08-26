import numpy

# Use this array to complete the assignment:
# Begin by creating a NumPy array with the values shown above
array = numpy.array([
    [1, 2, 5],
    [8, 0, -7],
    [7, 3, 9]
])

# Print it to the console
print(array)

# Transpose it and print it to the console 
array = array.T
print(array)

# Swap the axes and print it to the console (look familiar?)
array = numpy.swapaxes(array, 0, 1)
print(array)

# Flip the array across the horizontal axis (first row should be 5,2,1 afterwards) and print to console
array = numpy.flip(array, axis=1)
print(array)

# A row at the bottom of the array with these values 3,4,5 and print to console
row = numpy.array([[3, 4, 5]])
array = numpy.vstack((array, row))
print(array)

# A column at the right of the array with these values 7,8,9,0 and print to console
column = numpy.array([[7], [8], [9], [0]])
array = numpy.hstack((array, column))
print(array)

# Remove the last column in the array
array = array[:, :-1]
print(array)

# Reshape the array so it is two columns and 6 rows and print to console
array = array.reshape((6, 2))
print(array)

# Split the array into three 2x2 arrays and print the middle array
split = numpy.split(array, 3)
print(split[1])

# Flatten the third array and print to console
print(split[2].flatten())