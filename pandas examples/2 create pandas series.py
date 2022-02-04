import pandas as pd

#create list
a = [100, 200, 300, 400]

#create pandas series
ds = pd.Series(a, dtype ='float64')

#add new element with index 
ds[30]=45

#print value
print(ds)

#print type
print(type(ds))

#create series with different indexing style
ds2 = pd.Series(data = a, index = ['a','b','c','d'])

print(ds2)
print(ds2['b'])
