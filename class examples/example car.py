
class car:
    
    max_speed = 60
    
    def __init__(self,m,y):
        self.engine = m
        self.year = y
        self.speed = 20
    
    def accelerator(self):
        if self.speed< car.max_speed:
            self.speed+=1 
        print(f"current speed is {self.speed}")
        
    def breaking(self):
        self.speed-=1
        print(f"current speed is {self.speed}")
    
        
        
        
nano = car('v12',2007)

# nano.speed = 58
nano.engine = 'v14'

nano.accelerator()
nano.accelerator()
nano.breaking()