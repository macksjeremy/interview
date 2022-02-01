def sum(x):
    sum = 0
    for i in x:
        sum += i
    return sum



def sumswap(A, B):
    suma = sum(A)
    sumb = sum(B)
    diff = sumb-suma
    print("Diff:", diff)
    targetsB = set()
    for i in B:
        targetsB.add(i)
    for i in A:
        if(diff-i in targetsB):
            return(i, diff-i)


print(sumswap([4, 1, 2, 1, 1, 2],[3, 6, 3, 3]))