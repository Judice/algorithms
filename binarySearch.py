# coding=utf-8
def Solution(nums,target):   #二分查找法
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left)/2
        if target == nums[mid]:
            return mid
        elif nums[left] <= target < nums[mid]:
            right = mid
        else:
            left = mid + 1
    return -1
nums=[1,2,3,14,33,36,47,58,99]
print 'final:', Solution(nums,target=1)