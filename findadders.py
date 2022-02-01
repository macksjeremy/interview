#def twoSum(self, nums: List[int], target: int) -> List[int]:

def twosum(vals, target):
    targets = set()
    for i in vals:
        targets.add(i)
    for i in vals:
        if target - i in targets:
            print(target, target - i)
            return vals.index(i),vals.index(target-i)

first, second = twosum([2,7,11,15], 9)
print(first, second)