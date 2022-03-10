import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-m1', '--a', default=1000, type = int, help="a is integer")
parser.add_argument('-m2', '--b', default=1000, type = int, help="b is integer")
parser.add_argument('-m3', '--c', default=1000, type = int, help="c is integer")

args = parser.parse_args()

print("the value is ",args.a)
print("the value is ",args.b)
print("the value is ",args.c)

# python agrparse_example.py --a 10 -m2 20 -m3 50
