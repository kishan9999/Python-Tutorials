#using init function

class student:
    #variables
    def __init__(self, n, a):
        self.name = n
        self.age = a
        self.score = 0
    
    #functions
    def about_me(self):
        print(f"Hello!, my name is {self.name}")
        

#create class intances or objects
s1 = student('peter',20)
s2 = student('steve',31)

#accessing instance attributes using object
print(s1.name)
print(s1.age)
print(s1.about_me())

print(s2.name)
print(s2.age)
print(s2.about_me())

s1.score += 95
print(s1.score)