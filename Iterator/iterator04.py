class three3:
    def __init__(self):
        self.a = 1
        
    def __next__(self):
        self.a *= 3
        return self.a
       
        
t3 = three3()

print(t3.a)
next(t3)
print(t3.a)
next(t3)
print(t3.a)


#check of integer object
# b = 1
# c = next(b)