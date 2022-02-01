#install numpy using pip

import numpy as np

#craete numpy array using list or tuple
a = np.array([10,20,31,42,55,67,71,85,91,10,5,6])
# a = np.array((42,55,67,71,85,91,10), dtype = 'int64')

#copy vs view
b = a
# b = a.copy()
# b = a.view()

#update values and indexing
b[0] = 523

#shape of the array
print(a.shape)

#Re shaping an array
b.reshape(6,-1)
c = b.reshape(2,-1).copy()

#iterating array
for i in a:
    print(i)
    
k1 = np.array([10,20,31])
k2 = np.array([60,72,81])

k3 = np.concatenate((k1,k2),axis=0)
k4 = np.concatenate((k3,[55]),axis=0)

print(np.where(k3>40))

a = np.append(a,(10,20))
a = np.insert(a,0,52)

#arange 
k = np.arange(200,50,-20)