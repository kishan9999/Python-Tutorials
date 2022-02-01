
import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,11,12,13])
print(a)

a = np.delete(a,(0,2), axis=0)
print(a)

a = np.delete(a,np.where(a == 6), axis=0)
print(a)

b = np.zeros((5,2))
print(b)

c = np.ones(4)
print(c)

d = np.sin(-np.pi/2)
print(d)

e = np.sin(90)
print(e)