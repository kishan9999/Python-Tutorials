#create instance and use class attributes and function

class sigma:
    #variables
    a = 10
    b = 20
    c = 30
    
    #functions
    def greetings():
        print("hello world")
    def greetings2(self):
        print("hello world")
    def avg(self,m, n):
        print((m+n)/2)

#create class intances or objects
s1 = sigma()

#accessing class attributes using class instance
print(s1.a)
print(s1.b)
print(s1.c)

#accessing function
print(s1.greetings2())
s1.avg(10,20)

#use class function using class
sigma.avg(0,10,20)
sigma.greetings2(1)
sigma.greetings()

#Error 
# s1.greetings()


