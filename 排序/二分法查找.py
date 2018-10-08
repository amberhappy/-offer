#算法复杂度 log（n）
def binary_search(list,key):
    low = 0
    high = len(list)-1
    while low<high:
        # mid = low + int((high - low) * (key - lis[low])/(lis[high] - lis[low]))
        mid = int((low+high)/2)
        if key<list[mid]:
            high = mid-1
        elif key >list[mid]:
            low = mid +1
        else:
            return mid
    return False