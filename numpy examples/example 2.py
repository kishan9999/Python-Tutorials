# Reshap tutorial

import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9], dtype='int32')
print(a.shape)


# transform to 2d array
a1 = a.reshape(3,3)
print(a1.shape)

# rows x columns
a2 = a.reshape(1,9)
print(a2.shape)
print(a2)

a3 = a.reshape(9,1)
print(a3.shape)
print(a3)


