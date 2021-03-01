# NumPy Getting Started
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(np.__version__)
print()

# Create a NumPy ndarray Object
arr = np.array([61, 62, 63, 64, 65])
print(arr)
print(type(arr))
print()

# Use a tuple to create a NumPy array
arr = np.array((11, 12, 13, 14, 15))
print(arr)
print()

# Dimensions in Arrays
# 0-D Arrays
arr = np.array(42)
print(arr)
print()

# 1-D Arrays
arr = np.array([21, 22, 23, 24, 25])
print(arr)
print()

# 2-D Arrays
arr = np.array([[31,32, 33], [34, 35, 36]])
print(arr)
print()

# 3-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print()

# Check Number of Dimensions?
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print()

# Higher Dimensional Arrays
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
print()