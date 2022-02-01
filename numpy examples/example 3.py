# Reshap tutorial

import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], dtype='int32')
print(a.shape)

#rows, columns

#accessing all data
print(a)

#accessing 2nd row
print(a[1,:])


#accessing 2nd column
print(a[:,1])
