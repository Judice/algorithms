# coding=utf-8
def quicksort(nums):
    less = []
    greater = []
    if len(nums) <= 1: # 必须考虑等于0
        return nums
    n = nums.pop()
    for i in nums:
        if i <= n:
            less.append(i)
        else:
            greater.append(i)
    return quicksort(less)+[n]+quicksort(greater)