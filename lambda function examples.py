
#average of two values using lambda function
avg = lambda a,b: (a+b)/2

print("average of 5 and 10",avg(5,10))


#square root of the number 
sqrt = lambda a:a**0.5

print("square root of 16 = ",sqrt(16))


#print personalised message
tag = lambda name: print(f"hello, {name}")

tag('peter')

#multiple returns 

combo = lambda a,b: ((a+b)/2 ,a**2, a**3)
a1, a2, a3 = combo(10,12)

print(a1, a2, a3)
