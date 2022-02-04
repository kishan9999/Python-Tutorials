# nasted for loop in list comprehensions 

a = [1,2,3]
b = [2,2,2]

# example 1 a major b minor
c = [i*j for i in a for j in b]

# example 2 b major a minor
d = [i*j for i in b for j in a]

#nasted if else
z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
z1 = ['low' if i == 1 else 'high' if i == 10 else 'middle' if i==5 else 'between' for i in z]