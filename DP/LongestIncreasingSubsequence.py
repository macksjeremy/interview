#Assuming all values in arr are positive.
#To fix that, change 0 to -999
def lissubproblem(arr, i, prev):
    if(i == len(arr)):
        return 0
    excluded = lissubproblem(arr,i+1,prev)
    included = 0
    if(arr[i] > prev):
        included = 1 + lissubproblem(arr, i+1, arr[i])
    return max(included,excluded)

def lis(arr):
    length = lissubproblem(arr, 0, -1)
    return length

print(lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
assert lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6, "Incorrect logic"