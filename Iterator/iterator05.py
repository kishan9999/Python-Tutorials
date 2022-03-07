

class two2:
    def __init__(self):
        self.a = 1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        self.a *= 2
        if self.a<=1000:   
            return self.a
        else:
            raise StopIteration
       
        
t2 = two2()


for i in t2:
    print(i)