# coding=utf-8
def merge_sort(seq):
    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft)>1:
        lft = merge_sort(lft)
    if len(rgt)>1:
        rgt = merge_sort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return  (lft or rgt) + res

nums = [78,4,2,6,3,5,9,7,8,13,11,42,26,78,58,49,99,37,44,66,61,88]
print 'final:', merge_sort(nums)
