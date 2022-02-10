import os 

path = 'D:\Pythontutorial\myfolder'


i = 0
for root, dirct, files in os.walk(path):
    print(i)
    print(root)
    print(dirct)
    print(files)
    i = i+1
