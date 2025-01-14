import sys

def add(numb1, numb2):
    result = numb1 + numb2
    return result

def sub(numb1, numb2):
    result = numb1 - numb2
    return result

def mul(numb1, numb2):
    result = numb1 * numb2
    return result

    
numb1 = int(sys.argv[1])
operation = sys.argv[2]  # Normalize the operation to lowercase
numb2 = int(sys.argv[3])

if operation == "add":
    output = add(numb1, numb2)
    
    print(output)
