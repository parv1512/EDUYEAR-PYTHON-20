import numpy as np

# part-1 [Write a NumPy program to print the NumPy version in your system.]
print(np.__version__)


# part-2 [Write a NumPy program to convert a list of numeric value into a two-dimensional NumPy array.]
x = [[12.23, 13.32, 100, 36.32]]
print("Original List:",x)
y = np.array(x)
print("Two-dimensional NumPy array: ",y)


# part-3 [Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.]
import numpy as np
a =  np.arange(2, 10+1).reshape(3,3)
print(a)