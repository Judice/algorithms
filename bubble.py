# coding=utf-8
def bubble(List):                       #冒泡排序法
    for j in range(len(List)-1,0,-1):
        for i in range(0, j):
            if List[i] > List[i+1]:
                List[i], List[i+1] = List[i+1], List[i]
    return List

nums = [1,2,4,5,7,8,9,12,11,24,17,46,33,59,37,44,99,72,42]
print 'final:', bubble(nums)