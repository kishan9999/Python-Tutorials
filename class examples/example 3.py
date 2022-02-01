#create instance attributes

class student:
    #variables
    college = "ZCTW"
    def parameters(self, n, a):
        self.name = n
        self.age = a

#create class intances or objects
s1 = student()
s2 = student()

#create instanec parameters
s1.parameters('peter',20)
s2.parameters('steve',31)

#accessing instance attributes using object
print(s1.name)
print(s1.age)
print(s1.college)

print(s2.name)
print(s2.age)
print(s2.college)