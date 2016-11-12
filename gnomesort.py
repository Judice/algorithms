# coding=utf-8
def gnome_sort(seq):      #侏儒排序法
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] < seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
    return seq

nums = [1,2,3,6,7,9,12,31,24,56,32,11,58,99]
print 'finnal:', gnome_sort(nums)