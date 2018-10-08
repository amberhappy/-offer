#输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。

#思路：利用python中的双向队列
from collections import deque
class Solution:
    def reOrderArray(self,array):
        count = len(array)
        result = deque()
        for i in range(count):
            if array[count-i-1]%2 !=0:
                result.appendleft(array[count-i-1])
            if array[i]%2 ==0:
                result.append(array[i])
        return result