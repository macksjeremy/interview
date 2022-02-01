#Assuming all values in arr are positive.
#To fix that, change 0 to -999
def UNOPTIMALlissubproblem(arr, i, prev):
    if(i == len(arr)):
        return 0
    excluded = UNOPTIMALlissubproblem(arr,i+1,prev)
    included = 0
    if(arr[i] > prev):
        included = 1 + UNOPTIMALlissubproblem(arr, i+1, arr[i])
    return max(included,excluded)

def UNOPTIMALlis(arr):
    length = UNOPTIMALlissubproblem(arr, 0, -1)
    return length

print(UNOPTIMALlis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
assert UNOPTIMALlis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6, "Incorrect logic"