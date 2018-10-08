def QuickSort(List,right,left):

    if left <right:
        return  List
    key = List[right]
    low = right
    high = left

    while right <left:
        while right <left and List[left]>key:
            left -=1
        List[right] = List[left]
        while right<left and List[right]<key:
            right +=1
        List[left] = List[right]
    List[right] = key
    QuickSort(List,low,left)
    QuickSort(List,left+1,high)
