#special methods, abstract methods

names = ['peter','bruce','steve','shyam','ravi']


nm = names.__iter__()

while True:
    try:
        print(nm.__next__())
    except NameError:
        print('Hi, please define your variable')
        break
    except StopIteration:   
        break