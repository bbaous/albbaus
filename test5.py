import numpy as pd
from numpy.core.fromnumeric import sort
#Read the content of the file
ages = pd.loadtxt('ages.txt')
#Print the content of the file
print(ages)
#Print the number of the number of items
print(ages.shape)
#Print the shorted list
print(sort(ages))