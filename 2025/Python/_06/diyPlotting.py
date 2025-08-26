import matplotlib.pyplot
import numpy

# Global Setup
months = numpy.arange(1, 12)
sales = numpy.array([5, 10, 15, 20, 25, 30, 35, 30, 25, 20, 15])

# Create a simple visual from your dataset using matplotlib
matplotlib.pyplot.plot(months, sales)
matplotlib.pyplot.show()

# Explain what your visual demonstrates:
#   This is a simple plot showing the monthly sales of a product for a year

# Create a more complex visual from your dataset using matplotlib. 
#   This needs to include multiple options like color, line weight, 
matplotlib.pyplot.plot(months, sales, color='tomato', linewidth=2.5)
matplotlib.pyplot.xlabel("Month")
matplotlib.pyplot.ylabel("Sales")
matplotlib.pyplot.show()

# Explain what your visual demonstrates and why it required a more complex visual
# This is a complex plot showing monthly sales of a product for a year that is doing negative sales