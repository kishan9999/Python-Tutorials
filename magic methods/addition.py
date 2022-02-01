
class magic:
    def __init__(self):
        self.name = 'peter'
        
    def __getitem__(self, idx):
        print("the value is", idx)
    
    def __add__(self,beta):
        return beta*5
        
        
        

k = magic()
k['peter']

#custom addition in the class
print(k+10)