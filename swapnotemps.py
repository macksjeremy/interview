#Swap two numbers in place no temporary variables.
def swap(x,y):
    y = x + y
    x = y - x
    y = y - x
    return x,y

print(swap(15,12))
print(swap(23,12))
print(swap(15,17))