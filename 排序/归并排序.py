def merge(left, right):
    i, j = 0 , 0
    result = []
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

def merge_sort(list):
    if len(list)<=1:
        return list
    num = len(list)/2
    left = merge_sort(list[:num])
    right = merge_sort(list[num:])
    return merge(left,right)