a = [1,2,3,4,5,6,7,8]
b = [5,5,5,5,5,5,5,5]


#mutliplication of array with scaler
a1 = [i*10 for i in a]

#with condition
a2 = [i*10 for i in a if i<5]

#with conditions
a3 = [i*10 if i<5 else 0 for i in a]


#addition of two array
c = [i+j for i,j in zip(a,b)] 


