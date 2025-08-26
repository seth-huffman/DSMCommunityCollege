import numpy

# Begin by creating two NumPy arrays with the values shown above
one = numpy.array([[10, 15, 20], [2, 3, 4], [9, 14.5, 18]])
two = numpy.array([[1, 2, 5], [8, 0, 12], [11, 3, 22]])

# Print it to the console
print(one)

# Print it's shape
print(one.shape)

# Print a 2x2 slice of the array including the values from [0,0] to [1,1]
print(one[0:2, 0:2])

# Output the boolean value of each element in the array on whether the element is even (even = True, odd = False)
is_even = (one % 2 == 0)
print(is_even)

# Print the output of adding the two arrays together elementwise
print(one + two)

# Print the output of multiplying the two arrays together elementwise
print(one * two)

# Print the sum of all the elements in the array
print(numpy.sum(two))

# Print the product of all elements in the array
print(numpy.prod(two))

# Print the maximum and minimum value of the elements in the array
print(numpy.max(two))
print(numpy.min(two))
