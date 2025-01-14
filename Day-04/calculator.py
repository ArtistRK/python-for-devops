import sys

def add(numb1, numb2):
    add = numb1 + numb2
    return add

def sub(numb1, numb2):
    s = numb1 - numb2
    return s

def mul(numb1, numb2):
    m = numb1 * numb2
    return m

numb1 = int(sys.argv[1])
operation = sys.argv[2]
numb2 = int(sys.argv[3])

if operation == "add":
    output = add(numb1, numb2)
    print(output)