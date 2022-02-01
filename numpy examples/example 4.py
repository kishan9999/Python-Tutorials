
import numpy as np


a = np.array(['a','b','c'])

print(type(a))
print(a.dtype)


b = np.array([10,'b','c'])

print(type(b))
print(b.dtype)


c = np.array([10,20,50])

print(type(c))
print(c.dtype)

d = np.array([10,20,50], dtype='float64')

print(type(d))
print(d.dtype)