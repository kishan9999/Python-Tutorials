#square index in object
# https://www.geeksforgeeks.org/__getitem__-in-python/
# https://www.tensorflow.org/api_docs/python/tf/keras/utils/Sequence

class dataloader:
    
    def __init__(self,a,b):
        self.data = a
        self.batch_size = b

    def __len__(self):
        return len(self.data)//self.batch_size
    
    def __getitem__(self, idx):
        i = idx*self.batch_size
        datax = self.data[i:i+self.batch_size]     
        return datax
        
        
dt = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]        


datagen = dataloader(dt, 4)


print(datagen[2])
print(datagen[3])

print(len(datagen))

# del datagen