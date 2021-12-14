def subproblem(int, lis, max):
    if(int == 0):
        lis[int] = 0
        subproblem(int + 1, lis, max)
    elif(int == 1):
        lis[int] = lis[int - 1] + 1
        subproblem(int + 1, lis, max)
    elif (int != max):
        lis[int] = lis[int - 1] + lis[int - 2]
        subproblem(int + 1, lis, max)
    print(int, max)
    print(lis)
    return lis[max-1]


def fib(x):
    lis = [0] * x
    output = subproblem(0, lis, x)
    return output

print(fib(8))